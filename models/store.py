from db import db

class StoreModel(db.Model):

    __tablename__ = 'stores'

    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(30))

    items = db.relationship('ItemModel', lazy = 'dynamic')
    
    def __init__(self, name):
        self.name = name
    
    def json(self):
        return {'name': self.name, 'items': [item.json() for item in self.items.all()]}
    
    
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