from importlib import resources
from flask import Flask
from flask_restful import Api
#from flask_jwt import JWT

from db import db 
from security import authenticate, identity
from resources.user import UserRegister
from resources.item import Item, ItemList
from resources.store import Store, StoreList

import warnings
warnings.filterwarnings('ignore')

app = Flask(__name__)
app.config['PROPAGATE_EXCEPTIONS'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///data.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = 'jose'
api = Api(app)


#jwt = JWT(app, authenticate, identity)
#when JWT is initialised it will use app, authenticate, identity for autheticating
#JWT creates an new endpoint i.e /auth
#when /auth is called we send username,id,password to auticate function
# JWT - Json web Token --> encoding a messeage so with out JWT we can't decrypt

#@app.route is not required instead passing the route as parameter to ad_resource
api.add_resource(Item, '/item/<string:name>')# http://127.0.0.1:5000/item/<string:name>
api.add_resource(ItemList, '/items')
api.add_resource(UserRegister, '/register')
api.add_resource(Store, "/store/<name>")
api.add_resource(StoreList, "/stores")

if __name__ == '__main__':
    db.init_app(app)
    app.run(port=5000, debug=True)  # important to mention debug=True
