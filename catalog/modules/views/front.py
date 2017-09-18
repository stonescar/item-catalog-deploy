from catalog.modules.setup.app import app, session
from catalog.modules.setup.database import Item
from flask import render_template
from sqlalchemy import desc


@app.route('/')
def front():
    recent = session.query(Item).order_by(desc(Item.time)).limit(10).all()
    return render_template('front.html', recent=recent)
