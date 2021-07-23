from flask_wtf.file import FileAllowed, FileField, FileRequired
from wtforms import Form, IntegerField, StringField, BooleanField,TextAreaField, validators,DecimalField

class Addproducts(Form):
    name = StringField('Name',[validators.DataRequired()])
    price = DecimalField('Price',[validators.DataRequired()])
    discount = IntegerField('Discount', default=0)
    stock = IntegerField('Stock',[validators.DataRequired()])
    description = TextAreaField('Description',[validators.DataRequired()])
    color = TextAreaField('Color',[validators.DataRequired()])

    image_1 = FileField('image 1',validators=[FileRequired(), FileAllowed(['jpg','png','gif','jpeg'])])
    image_2 = FileField('image 2',validators=[FileRequired(), FileAllowed(['jpg','png','gif','jpeg'])])
    image_3 = FileField('image 3',validators=[FileRequired(), FileAllowed(['jpg','png','gif','jpeg'])])


    