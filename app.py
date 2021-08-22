# -*- coding: utf-8 -*-
"""
Created on Mon Oct  5 16:58:29 2020

@author: Pnk
"""

from flask import Flask
from flask_restful import Api
from flask_bcrypt import Bcrypt
from database.db import initialize_db
from flask_jwt_extended import JWTManager
from resources.errors import errors
from flask_mail import Mail
from flask_cors import CORS

import gc
import torch

#import requiring app and mail
app = Flask(__name__)
CORS(app)

app.config['JWT_SECRET_KEY'] = 'kjsadifh81793rh1u35183fioasfuk32413fdsfsaxcvvb'
app.config['MAIL_SERVER'] = "localhost"
app.config['MAIL_PORT'] = "1025"
app.config['MAIL_USERNAME'] = "support@cArtificial.com"
app.config['MAIL_PASSWORD'] = ""
app.config['MONGODB_SETTINGS'] = {
     'host': 'mongodb://localhost/cArtificial'
}

api = Api(app)
mail = Mail(app)
api = Api(app, errors=errors)
bcrypt = Bcrypt(app)

from resources.routes import initialize_routes

jwt = JWTManager(app)

initialize_db(app)
initialize_routes(api)

torch.cuda.empty_cache()
gc.collect()

