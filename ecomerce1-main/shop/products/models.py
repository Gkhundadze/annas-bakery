from shop import db
from datetime import datetime

class Addproduct(db.Model):
    _searchable_=['name','desc']
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    price = db.Column(db.Numeric(10,2), nullable=False)
    discount = db.Column(db.String(80), nullable=False)
    stock = db.Column(db.Integer, nullable=False)
    color = db.Column(db.Text, nullable=False)
    desc= db.Column(db.Text, nullable=False)
    date = db.Column(db.DateTime, nullable=False,default=datetime.utcnow)
  
    brand_id = db.Column(db.Integer, db.ForeignKey('brand.id'),nullable=False)
    brand = db.relationship('Brand', backref=db.backref('Addproduct', lazy=True))
    
    category_id = db.Column(db.Integer, db.ForeignKey('category.id'),nullable=False)
    category = db.relationship('Category', backref=db.backref('Addproduct', lazy=True))
 
    image_1 = db.Column(db.String(150),nullable=False,default='image.jpg')
    image_2 = db.Column(db.String(150),nullable=False,default='image.jpg')
    image_3 = db.Column(db.String(150),nullable=False,default='image.jpg')

  
    def __repr__(self):
        return '<Addproduct %r>' % self.name

class Brand(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String(30), nullable=False, unique=True)


class Category(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String(30), nullable=False, unique=True)


# class Images(db.Model):
#     id=db.Column(db.Integer,primary_key=True)
#     image=db.Column(db.String(150),nullable=False,default='image.jpg')


# class Galey(db.Model):
#     id=db.Column(db.Integer,primary_key=True)
#     title = db.Column(db.String(150),nullable=False)
#     image=db.Column(db.String(150),nullable=False,default='image.jpg')
#     image_id = db.Column(db.Integer, db.ForeignKey('image.id'),nullable=False)
#     category = db.relationship('Image', backref=db.backref('Galey', lazy=True))


