import os
from flask import Flask
from flask.ext.mongoengine import MongoEngine
from flask.ext.heroku import Heroku

app = Flask(__name__)
app.config["MONGODB_SETTINGS"] = {"DB": "pyladies_blog"}
app.config["SECRET_KEY"] = "KeepThisS3cr3t"

db = MongoEngine(app)

def register_blueprints(app):
    # Prevents circular imports
    from pyladiesblog.views import posts
    app.register_blueprint(posts)

register_blueprints(app)

if __name__ == '__main__':
	app.run()