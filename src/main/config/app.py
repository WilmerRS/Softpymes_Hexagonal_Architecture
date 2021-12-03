from flask import Flask


def create_app(config):
    """Returns an initialized Flask application."""
    app = Flask(__name__)
    app.config.from_object(config)

    # register_extensions(app)
    # register_blueprints(app)
    # register_commands(app)

    @app.route('/', methods=['GET'])
    def index():
        """Returns the applications index page."""
        return 'Welcome to wilmer'

    return app
