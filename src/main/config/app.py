# python
import os

# Flask
from flask import Flask

# flask restfull
from flask_restful import Api

# Local
from src.app.routes.routes import register_routes
from src.main.database import db, ma
from src.main.config.config import config


def register_extensions(app):
    """Register extensions with the Flask application."""
    db.init_app(app)
    ma.init_app(app)

    # with app.app_context():
        # db.drop_all()
        # db.create_all()


def create_app():
    """Returns an initialized Flask application."""
    app = Flask(__name__)

    env = os.environ.get('FLASK_ENV', 'development')
    app.config.from_object(config[env])

    api = Api(app)

    register_routes(api)
    register_extensions(app)

    @app.route('/', methods=['GET'])
    def index():
        """Returns the applications index page."""
        return 'Server up!'

    return app
