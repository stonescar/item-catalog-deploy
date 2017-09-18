from flask import Flask
from sqlalchemy.orm import sessionmaker
from database import engine


app = Flask('catalog')

DBsession = sessionmaker(bind=engine)
session = DBsession()
