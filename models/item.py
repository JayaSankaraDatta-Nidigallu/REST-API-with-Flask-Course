from db import db

class ItemModel(db.Model):

    __tablename__ = 'items'

    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(30))
    price = db.Column(db.Float(precision=2))

    store_id = db.Column(db.Integer, db.ForeignKey('stores.id')) #creating the store table
    store = db.relationship('StoreModel')

    def __init__(self, name, price, store_id):
        self.name = name
        self.price = price
        self.store_id = store_id
    
    def json(self):
        return {'name': self.name, 'price': self.price}
    
    
    @classmethod
    def find_by_name(cls, name):
        return cls.query.filter_by(name=name).first() #.first() return first row only 
        #SQLAlchemy makes easy for retriving data
        # the above code is similar to SELECT * FROM items WHERE name=name
        #and the conncetion, cursor are not required for SQLAlchemy

    def save_to_db(self):
        '''This function insert and update the data'''
        db.session.add(self)
        db.session.commit()


    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()