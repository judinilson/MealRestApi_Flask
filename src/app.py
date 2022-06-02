
from flask import Flask, app

# default mongodb configuration
default_config = {'MONGODB_SETTINGS': {
    'db': 'meals',
    'host': 'localhost',
    'port': 27017, }}


def get_flask_app(config: dict = None) -> app.Flask:

    # init flask
    flask_app = Flask(__name__)

    # configure app
    config = default_config if config is None else config
    flask_app.config.update(config)

    return flask_app


if __name__ == '__main__':
    # Main entry point when run in stand-alone mode.
    app = get_flask_app()
    app.run(debug=True)
