from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///donors.db'
db = SQLAlchemy(app)


from app.controllers import links
app.register_blueprint(links)

db.create_all()