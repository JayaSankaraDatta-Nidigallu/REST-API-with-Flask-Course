import imp
from flask_restful import Resource
from models.store import StoreModel

class Store(Resource):
    
    def __init__(self):
        pass

    def get(self, name):
        store = StoreModel.find_by_name(name)
        
        if store:
            return store.json(), 200
        return {"message": "Store not found"},404

    def post(self, name):
        store = StoreModel.find_by_name(name)

        if store:
            return {"message": f"A store with name {store} already exists"}, 400
        else:
            store = StoreModel(name)
            try:
                store.save_to_db()
            except:
                return {"message": "A error occured while creating store"}, 500
            
            return store.json(), 201

    def delete(self, name):
        store = StoreModel.find_by_name(name)
        print("*****",store)
        if store:
            store.delete_from_db()
            
            return {"message": "Store deleted"},200
        else:
            return {"message": f"A store with name {name} does not exists"}, 400
            
    
class StoreList(Resource):
    def get(self):
        return {"Stores": [store.json() for store in StoreModel.query.all()]}
        # we can also use list(map(lambda store : store.json(), StoreModel.query.all()))