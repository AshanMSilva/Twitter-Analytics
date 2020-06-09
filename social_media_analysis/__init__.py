from flask import Flask
from social_media_analysis.config import Config
from flask import flash



def create_app(config_class=None):
    app = Flask(__name__)
    app.config.from_object(Config)

    from social_media_analysis.main.routes import main
    from social_media_analysis.errors.handlers import errors
    from social_media_analysis.twitter.routes import twitter
    app.register_blueprint(main)
    app.register_blueprint(errors)
    app.register_blueprint(twitter)

    return app
