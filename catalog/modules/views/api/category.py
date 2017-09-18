from catalog.modules.setup.app import app, session
from catalog.modules.setup.database import Item
from catalog.modules import helpers
from flask import jsonify


@app.route('/category/<int:category_id>/JSON/')
@helpers.category_exists
def categoryJSON(category_id, category):
    items = session.query(Item).filter_by(category_id=category_id).all()
    return jsonify(Category=category.serialize(items))
