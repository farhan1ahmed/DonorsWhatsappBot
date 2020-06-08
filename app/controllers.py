from flask import request
from flask import Blueprint
from app import app
from app import service

links = Blueprint('controllers', __name__)

@app.route('/')
def hello():
    print("HERE")
    return "Hello World"


@app.route('/reply', methods=['POST'])
def reply():
    message = request.form.get('Body')
    return service.reply(message)