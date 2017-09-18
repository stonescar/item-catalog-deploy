from catalog.modules.setup.app import app, session
from catalog.modules.setup.database import Item
from catalog.modules import helpers
from flask import render_template


@app.route('/category/<int:category_id>/')
@helpers.category_exists
def viewCategory(category_id, category):
    items = session.query(Item).filter_by(category=category).all()
    return render_template('viewcategory.html', category=category, items=items)
