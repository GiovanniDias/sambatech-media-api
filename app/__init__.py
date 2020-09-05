from flask import Flask
from .extensions import configuration, database
from .blueprints import api


def create_app(**config):
    app = Flask(__name__)
    
    # Apply settings to app (settings.toml)
    configuration.init_app(app, **config)
    # Stablish database connection
    database.init_app(app)
    # Set api routes
    api.init_app(app)

    return app
