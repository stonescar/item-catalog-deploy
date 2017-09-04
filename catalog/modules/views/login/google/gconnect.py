from modules.setup.app import app
from modules import helpers
from flask import request, make_response, flash, session as login_session
from oauth2client.client import flow_from_clientsecrets, FlowExchangeError
import json
import httplib2
import requests
import os
import sys

ROOT_DIR = os.path.dirname(sys.modules['__main__'].__file__)
client_secret_path = os.path.join(
    ROOT_DIR, 'client_secrets/g_client_secrets.json')


@app.route('/gconnect', methods=['POST'])
def gconnect():
    if request.args.get('state') != login_session['state']:
        response = make_response(json.dumps('Invalid state parameter'), 401)
        response.headers['Content-type'] = 'application/json'
        return response
    code = request.data
    try:
        # Upgrade the authorization code to a credentials object
        oauth_flow = flow_from_clientsecrets(client_secret_path, scope='')
        oauth_flow.redirect_uri = 'postmessage'
        credentials = oauth_flow.step2_exchange(code)
    except FlowExchangeError:
        response = make_response(json.dumps(
            'Failed to upgrade the authorization code'), 401)
        response.headers['Content-type'] = 'application/json'
        return response
    # Check that the access token is valid
    access_token = credentials.access_token
    url = ('https://www.googleapis.com/oauth2/v1/tokeninfo?access_token=%s'
           % access_token)
    h = httplib2.Http()
    result = json.loads(h.request(url, 'GET')[1])
    # If there was an error in the access token info, abort
    if result.get('error') is not None:
        response = make_response(json.dumps(result.get('error')), 500)
        response.headers['Content-type'] = 'application/json'
        return response
    # Verify that the access token is used for the intended user
    gplus_id = credentials.id_token['sub']
    if result['user_id'] != gplus_id:
        response = make_response(json.dumps(
            "Token's user ID does not match given user ID"), 401)
        response.headers['Content-type'] = 'application/json'
        return response
    # Verify that the access token is valid for this app
    CLIENT_ID = json.loads(open(
        client_secret_path, 'r').read())['web']['client_id']
    if result['issued_to'] != CLIENT_ID:
        response = make_response(json.dumps(
            "Token's client ID does not match app's ID"), 401)
        response.headers['Content-type'] = 'application/json'
        return response
    # Check to see if user is already logged in
    stored_credentials = login_session.get('credentials')
    stored_gplus_id = login_session.get('gplus_id')
    if stored_credentials is not None and gplus_id == stored_gplus_id:
        response = make_response(json.dumps(
            'Current user is already connected'), 200)
        response.headers['Content-type'] = 'application/json'

    # Store the access token in the session for later use
    login_session['provider'] = 'google'
    login_session['credentials'] = credentials
    login_session['gplus_id'] = gplus_id

    # Get user info
    userinfo_url = 'https://www.googleapis.com/oauth2/v1/userinfo'
    params = {'access_token': credentials.access_token, 'alt': 'json'}
    answer = requests.get(userinfo_url, params=params)
    data = json.loads(answer.text)

    login_session['username'] = data['name']
    login_session['picture'] = data['picture']
    login_session['email'] = data['email']

    # Create user, if it doesn't already exist
    user_id = helpers.getUserID(login_session['email'])
    if not user_id:
        user_id = helpers.createUser(login_session)
    login_session['user_id'] = user_id

    flash('You are now logged in as %s (%s)' % (
        login_session['username'], login_session['email']))
    return 'success'
