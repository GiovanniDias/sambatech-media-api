from flask import Flask
from .extensions import configuration, database, commands
from .blueprints import api


def create_app(**config):
    app = Flask(__name__)
    
    # Apply settings to app (settings.toml)
    configuration.init_app(app, **config)
    # Stablish database connection
    database.init_app(app)
    # Set api routes
    api.init_app(app)
    # Set custom app commands
    commands.init_app(app)

    return app
