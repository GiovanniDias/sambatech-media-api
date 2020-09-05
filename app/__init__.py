from flask import Flask
from .extensions import configuration, database


def create_app(**config):
    app = Flask(__name__)
    
    # Apply settings to app (settings.toml)
    configuration.init_app(app, **config)
    # Stablish database connection
    database.init_app(app)

    @app.route('/')
    def index():
        return 'This is a sample of SambaTech Media API'

    return app
