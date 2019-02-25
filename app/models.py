from app import db
from datetime import datetime

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    self_introduction = db.Column(db.Text)
    rating = db.Column(db.Integer)
    head_portrait = db.Column(db.String(200))
    sales_history=db.relationship('Dish', backref='seller', lazy='dynamic')
    purchasing_history=db.relationship('Order', backref='buyer', lazy='dynamic')
    
    def __repr__(self):
        return '<User {}>'.format(self.username)

class Dish(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    dish_name = db.Column(db.String(50))
    price = db.Column(db.Float)
    photo = db.Column(db.String(200))
    deliveryTime = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    expected_order_number = db.Column(db.Integer)
    current_order_number = db.Column(db.Integer)
    rating = db.Column(db.Integer)
    flavour = db.Column(db.String(140))
    potential_taboo=db.Column(db.String(500))
    description = db.Column(db.Text)
    pick_up_location=db.Column(db.String(500))
    chef_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    order_lists=db.relationship('Order', backref='dish', lazy='dynamic')
    
    def __repr__(self):
        return '<Dish {}>'.format(self.dish_name)  
    
class Order(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    quantity=db.Column(db.Integer)
    order_time=db.Column(db.DateTime, index=True, default=datetime.utcnow)
    status=db.Column(db.Integer)
    comment=db.Column(db.Text)
    customer_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    dish_id = db.Column(db.Integer, db.ForeignKey('dish.id'))
    def __repr__(self):
        return '<Order {}>'.format(self.id)