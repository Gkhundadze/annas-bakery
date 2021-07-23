from flask import redirect, render_template, url_for, flash, request,session,current_app
from wtforms.validators import DataRequired
from shop import db, app, photos,search
from .models import Brand, Category, Addproduct
from .forms import Addproducts
import secrets,os

def brands():
    brands=Brand.query.join(Addproduct, (Brand.id==Addproduct.brand_id)).all()
    return brands
 
def categoryes():
    categoryes=Category.query.join(Addproduct, (Category.id==Addproduct.category_id)).all()
    return categoryes

@app.route('/')
def home():
    page=request.args.get('page',1, type=int)
    products=Addproduct.query.filter(Addproduct.stock > 0).order_by(Addproduct.id.desc()).paginate(page=page,per_page=8)
    return render_template('products/index.html', products=products,brands=brands(),categoryes=categoryes())
    
    
# serch query
@app.route('/result')
def result():
    searchword =request.args.get('q')
    products = Addproduct.query.msearch(searchword, fields=['name','desc'], limit=20)
    return render_template('products/result.html',products=products,
    brands=brands(),categoryes=categoryes())

@app.route('/product/<int:id>')
def single_page(id):
    product=Addproduct.query.get_or_404(id)
    return render_template('products/single_page.html', product=product,brands=brands(),categoryes=categoryes())


@app.route('/brand/<int:id>')
def get_brand(id):
    get_br=Brand.query.filter_by(id=id).first_or_404()
    page=request.args.get('page',1, type=int)
    brand=Addproduct.query.filter_by(brand=get_br).paginate(page=page,per_page=8)
    return render_template('products/index.html',brand=brand, brands=brands(),categoryes=categoryes(),get_br=get_br)

@app.route('/categoryes/<int:id>')
def get_category(id):
    page=request.args.get('page',1, type=int)
    get_cat=Category.query.filter_by(id=id).first_or_404()
    get_cat_prod=Addproduct.query.filter_by(category=get_cat).paginate(page=page,per_page=8)
    return render_template('products/index.html',get_cat_prod=get_cat_prod, categoryes=categoryes(),brands=brands(),get_cat=get_cat)


@app.route('/addbrand', methods=['GET','POST'])
def addbrand():
    if 'email' not in session:
        flash(f'flease login first','danger')
        return redirect(url_for('login'))
    if request.method == 'POST':
        getbrand=request.form.get('brand')
        if getbrand !='':
            brand = Brand(name=getbrand)
            db.session.add(brand)
            flash(f'the brand {getbrand} was added to your database','success')
            db.session.commit()
            return redirect(url_for('addbrand'))
        flash(f'ცარიელი მონაცემის დამატება შეუძლებელია','danger')
    return render_template('products/addbrand.html', brands='brands')


@app.route('/updatebrand/<int:id>', methods=['GET','POST'])
def updatebrand(id):
    if 'email' not in session:
        flash(f'flease login first','danger')
    updatebrand=Brand.query.get_or_404(id)
    brand=request.form.get('brand')
    if request.method == "POST":
        updatebrand.name = brand
        flash(f'Your brand has been updated','success')
        db.session.commit()
        return redirect(url_for('brands'))
    return render_template('products/updatebrand.html',title='Update Brand Page',updatebrand=updatebrand)



@app.route('/deletebrand/<int:id>', methods=['POST'])
def deletebrand(id):
    brand=Brand.query.get_or_404(id)
    if request.method=='POST':
        db.session.delete(brand)
        db.session.commit()
        flash(f'the brand {brand.name} was deleted from your database','success')
        return redirect(url_for('admin'))
    flash(f'the brand {brand.name} cant be deleted','warning')
    return redirect(url_for('admin'))


@app.route('/updatecat/<int:id>', methods=['GET','POST'])
def updatecat(id):
    if 'email' not in session:
        flash(f'flease login first','danger')
    updatecat=Category.query.get_or_404(id)
    category=request.form.get('category')
    if request.method == "POST":
        updatecat.name = category
        try:
            flash(f'Your category has been updated','success')
            db.session.commit()
        except IntegrityError as e:
             flash(f'the record {updatecat.name} alredy exist to your database','danger')
             return redirect(url_for('category'))
    return render_template('products/updatebrand.html',title='Update Category Page',updatecat=updatecat)



@app.route('/addcat', methods=['GET','POST'])
def addcat():
    if 'email' not in session:
        flash(f'flease login first','danger')
        return redirect(url_for('login'))
    if request.method == 'POST':
        getbrand=request.form.get('category')
        if getbrand != '':
            cat = Category(name=getbrand)
            db.session.add(cat)
            try:
                flash(f'the category {getbrand} was added to your database','success')
                db.session.commit()
                return redirect(url_for('addcat'))
            except IntegrityError as e:
                flash(f'the category {getbrand} alredy exist to your database','danger')
        flash(f'ცარიელი მონაცემების დამატება შეუძლებელია','danger')
    return render_template('products/addbrand.html')

@app.route('/deletecat/<int:id>', methods=['POST'])
def deletecat(id):
    cat=Category.query.get_or_404(id)
    if request.method=='POST':
        db.session.delete(cat)
        db.session.commit()
        flash(f'the brand {cat.name} was deleted from your database','success')
        return redirect(url_for('admin'))
    flash(f'the brand {cat.name} cant be deleted','warning')
    return redirect(url_for('admin'))


@app.route('/addproduct', methods=['POST','GET'])
def addproduct():
    if 'email' not in session:
        flash(f'flease login first','danger')
        return redirect(url_for('login'))
    brands = Brand.query.all()
    categoryes = Category.query.all()
    form = Addproducts(request.form)
    if request.method == 'POST':
        name=form.name.data
        price=form.price.data
        discount=form.discount.data
        stock=form.stock.data
        color=form.color.data
        desc=form.description.data
        brand=request.form.get('brand')
        category=request.form.get('category') 
        image_1 = photos.save(request.files.get('image_1'),name = secrets.token_hex(10)+".")
        image_2 = photos.save(request.files.get('image_2'),name = secrets.token_hex(10)+".")
        image_3 = photos.save(request.files.get('image_3'),name = secrets.token_hex(10)+".")
        addpro = Addproduct(name=name,price=price,discount=discount,stock=stock,color=color,
        desc=desc,brand_id=brand,category_id=category, image_1=image_1, image_2=image_2,image_3=image_3)
        db.session.add(addpro)
        flash(f'the product {name} has bin adedd to your database','success')
        db.session.commit()
        return redirect(url_for('admin'))
    return render_template ('products/addproducts.html', form=form , title='add products page', categoryes=categoryes, brands=brands)


@app.route('/updateproduct/<int:id>', methods=['GET', 'POST'])
def updateproduct(id):
    brands=Brand.query.all()
    categoryes=Category.query.all()
    product=Addproduct.query.get_or_404(id)
    brand=request.form.get('brand')
    category=request.form.get('category')
    form=Addproducts(request.form)
    if request.method=="POST":
        product.name=form.name.data
        product.price=form.price.data
        product.discount=form.discount.data
        product.brand_id=brand
        product.category_id=category
        product.color=form.color.data
        product.desc=form.description.data

        if request.files.get('image_1'):
            try:
                os.unlink(os.path.join(current_app.root_path,"static/images/" + product.image_1))
                product.image_1 = photos.save(request.files.get('image_1'), name = secrets.token_hex(10)+".")
            except:
                product.image_1 = photos.save(request.files.get('image_1'), name = secrets.token_hex(10)+".")

        if request.files.get('image_2'):
            try:
                os.unlink(os.path.join(current_app.root_path,"static/images/" + product.image_2))
                product.image_2 = photos.save(request.files.get('image_2'), name = secrets.token_hex(10)+".")
            except:
                product.image_2 = photos.save(request.files.get('image_2'), name = secrets.token_hex(10)+".")

        if request.files.get('image_3'):
            try:
                os.unlink(os.path.join(current_app.root_path,"static/images/" + product.image_3))
                product.image_3 = photos.save(request.files.get('image_3'), name = secrets.token_hex(10)+".")
            except:
                product.image_3 = photos.save(request.files.get('image_3'), name = secrets.token_hex(10)+".")

        db.session.commit()
        flash(f'your product has been updated','success')
        return redirect(url_for('admin'))
    form.name.data=product.name
    form.price.data=product.price
    form.discount.data=product.discount
    form.description.data=product.desc
    form.stock.data=product.stock
    form.color.data=product.color
    return render_template('products/updateproduct.html',form=form,brands=brands,categoryes=categoryes,product=product)



@app.route('/deleteproduct/<int:id>', methods=['POST'])
def deleteproduct (id):
    product = Addproduct.query.get_or_404(id)
    if request.method=="POST":
        try:
            os.unlink(os.path.join(current_app.root_path,"static/images/" + product.image_1))
            os.unlink(os.path.join(current_app.root_path,"static/images/" + product.image_2))
            os.unlink(os.path.join(current_app.root_path,"static/images/" + product.image_3))
        except Exception as e:
            print(e)
        db.session.delete(product)
        db.session.commit()
        flash(f'the product {product.name} was deleted in your record','success')
        return redirect(url_for('admin'))
    flash(f'cant delete the product','danger')
    return redirect(url_for('admin'))

@app.route('/contact')
def contact ():
    return render_template('products/contact.html')

@app.route('/about')
def about ():
    return render_template('products/about.html')

@app.route('/gallery')
def gallery ():
    return render_template('products/gallery.html')

@app.route('/accessories')
def accessories ():
    return render_template('products/accessories.html')

@app.route('/clothes')
def clothes ():
    return render_template('products/clothes.html')

@app.route('/toys')
def toys ():
    return render_template('products/toys.html')

@app.route('/cookbook')
def cookbook ():
    return render_template('products/cookbook.html')

@app.route('/new-receipts')
def newReceipts ():
    return render_template('products/new-receipts.html')

@app.route('/healthy-eat')
def healthyEat ():
    return render_template('products/healthy-eat.html')

@app.route('/breakfast')
def breakFast ():
    return render_template('products/breakfast.html')

@app.route('/salads')
def salads ():
    return render_template('products/salads.html')

@app.route('/baked')
def baked ():
    return render_template('products/baked.html')

@app.route('/dessert')
def dessert ():
    return render_template('products/dessert.html')

@app.route('/baby-receipts')
def babyReceipts ():
    return render_template('products/baby-receipts.html')