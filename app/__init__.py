from flask import Flask


def create_app(**config):
    app = Flask(__name__)
    
    @app.route('/')
    def index():
        return 'This is a sample of SambaTech Media API'

    return app
