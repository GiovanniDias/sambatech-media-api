from flask import Flask


app = Flask(__name__)

@app.route('/')
def index():
    return 'This is a sample of SambaTech Media API'
