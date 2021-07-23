from flask import render_template, session, request, redirect, url_for, flash,current_app
from shop import db, app
from shop.products.models import Addproduct
from shop.products.routes import brands,categoryes

def MergeDicts(dict1, dict2):
    if isinstance(dict1, list) and isinstance(dict2,list):
        return dict1 + dict2
    elif isinstance(dict1, dict) and isinstance(dict2,dict):
        return dict(list(dict1.items()) + list(dict2.items()))
    return False

@app.route('/addcart', methods = ['POST'])
def Addcart():
    try:
        product_id = request.form.get('product_id')
        quantity = int(request.form.get('quantity'))
        color = request.form.get('colors')
        product = Addproduct.query.filter_by(id=product_id).first()
        if request.method == "POST":
            DictItems = {product_id:{'name':product.name, 'price':float(product.price), 'discount': product.discount,
            'color':color, 'quantity':quantity, 'image':product.image_1, 'colors':product.color } }
            if 'shoppcart' in session:
                print(session['shoppcart'])
                if product_id in session['shoppcart']:
                    for key, item in session['shoppcart'].items():
                        if int(key)==int(product_id):
                            session.modified=True
                            item['quantity']+=1
                    print('this product alredy exist in your cart')
                else:
                    session['shoppcart'] = MergeDicts(session['shoppcart'], DictItems)
                    return redirect(request.referrer)
            else:
                session['shoppcart'] = DictItems
                return redirect(request.referrer) 

    except Exception as e:
        print(e)
    finally:
        return redirect(request.referrer)


@app.route('/carts')
def getcart():
    if 'shoppcart' not in session or len(session['shoppcart'])<=0:
        return redirect(url_for('home'))
    subtotal = 0
    grandtotal = 0
    for key, product in session['shoppcart'].items():
        discount = (float (product['discount'])/100) * float(product['price'])
        subtotal += float(product['price']) * int(product['quantity'])
        subtotal -= discount
        tax = ("%0.2f" % (0.06 * float(subtotal))) 
        grandtotal = float("%0.2f" % (1.06 * subtotal))
    return render_template('products/carts.html', tax=tax, grandtotal=grandtotal,brands=brands(),categoryes=categoryes())


@app.route('/updatecart/<int:code>', methods=['POST'])
def updatecart(code):
    if 'shoppcart' not in session or len(session['shoppcart']) <= 0:
        return redirect(url_for('home'))
    if request.method == 'POST':
        quantity=request.form.get('quantity')
        color= request.form.get('color')
        try:
            session.modified = True
            for key, item in session['shoppcart'].items():
                if int(key) == code:
                    item['quantity'] = quantity
                    item['color'] = color
                    flash(f'Product is updated','success')
                    return redirect(url_for('getcart'))
        except Exception as e:
            print(e)
            return redirect(url_for('getcart'))



@app.route('/deleteitem/<int:id>')
def deleteitem(id):
    if 'shoppcart' not in session or len(session['shoppcart'])<=0:
        return redirect(url_for('home'))
    try:
        session.modified=True
        for key,item in session['shoppcart'].items():
            if int(key)==id:
                session['shoppcart'].pop(key,None)
                return redirect(url_for('getcart'))
    except Exception as e:
        print(e)
        return redirect(url_for('getcart'))



@app.route('/empty')
def empty_cart():
    try:
        session.clear()
        return redirect(url_for('home'))
    except Exception as e:
        print(e)
    
@app.route('/clearcart')
def clearcart():
    try:
        session.pop("shoppcart",None)
        return redirect(url_for('home'))
    except Exception as e:
        print(e)
