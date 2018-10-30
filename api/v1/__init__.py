from flask import Flask

app = Flask(__name__)

from api.v1.views import views


# from flask import Flask
# from config import DevelopmentConfig

# def create_app(DevelopmentConfig):
#     app = Flask(__name__)
#     app.config.from_object(DevelopmentConfig)
#     return app

