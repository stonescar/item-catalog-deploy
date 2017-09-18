from catalog.modules.setup.app import app, session
from catalog.modules.setup.database import Category
from catalog.modules import helpers
from flask import (render_template, request, flash, redirect,
                   url_for, session as login_session)


@app.route('/category/new/', methods=['POST', 'GET'])
@helpers.login_required
@helpers.csrf_protect
def newCategory():
    if request.method == 'POST':
        category = Category(name=request.form['name'],
                            user_id=login_session['user_id'])
        session.add(category)
        session.commit()
        flash('Category <b>%s</b> added' % category.name)
        return redirect(url_for('viewCategory', category_id=category.id))
    return render_template('newcategory.html')
