from flask import Flask
from sqlalchemy.orm import sessionmaker
from database import engine


app = Flask(__name__)

DBsession = sessionmaker(bind=engine)
session = DBsession()
