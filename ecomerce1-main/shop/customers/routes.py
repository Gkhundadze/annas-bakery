from flask import render_template,session,request,redirect,url_for,flash,current_app
from flask_login import login_required,current_user,login_user,logout_user
from shop import app,db,photos,search,bcrypt,login_manager
from .forms import CustomerRegistrationForm,CustomerLoginForm,CustomerEditInfo
from .model import Register,CustomerOrder
from ..products.routes import brands,categoryes
import secrets,os,json,sys
try:
    import pdfkit
    print('packige found')
except Exception as e:
    print('packige not found',e)

@app.route('/customer/register',methods=['GET','POST'])
def customer_register():
    title = 'Register Page'
    form = CustomerRegistrationForm()
    if form.validate_on_submit():
        hash_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8') 
        register=Register(
        name=form.name.data,
        username=form.username.data,
        email=form.email.data,
        password=hash_password,
        country=form.country.data,
        # state=form.state.data,
        city=form.city.data,
        contact=form.contact.data,
        address=form.address.data,
        zipcode=form.zipcode.data,
        profile = photos.save(form.profile.data, name = secrets.token_hex(10)+".")
        )
        db.session.add(register)
        flash(f'welcome {form.name.data} thenk you for registring','success')
        db.session.commit()
        return redirect(url_for('login'))
    return render_template('customer/register.html', form=form, title = title)


@app.route('/customer/login',methods=['GET','POST'])
def customerLogin():
    title = 'Login Page'
    form=CustomerLoginForm()
    if form.validate_on_submit():
        user=Register.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user)
            flash(f'You are login now','success')
            next = request.args.get('next')
            return redirect(next or url_for('home'))
        flash(f'Incorect email and password','danger')
        return redirect(url_for("customerLogin"))
    return render_template('customer/login.html',form=form, title = title)


@app.route('/customer/logout')
def customer_logout():
    logout_user()
    flash(f'end session','success')
    return redirect(url_for('home'))

# update customer settings
@app.route('/settings_update/<int:id>', methods=['GET','POST'])
def customer_settings_update(id):
    registers=Register.query.get_or_404(id)
    # print(registers.name)
    form = CustomerEditInfo(request.form)
    if request.method == "POST":
        registers.name=form.name.data
        registers.username=form.username.data
        registers.email=form.email.data
        registers.contact=form.contact.data
        registers.address=form.address.data
        # print(form.name.data)
        registers.password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        if request.files.get('profile'):
            try:
                os.unlink(os.path.join(current_app.root_path,"static/images/" + registers.profile))
                registers.profile = photos.save(request.files.get('profile'), name = secrets.token_hex(10)+".")
            except:
                registers.profile = photos.save(request.files.get('profile'), name = secrets.token_hex(10)+".")
        db.session.commit()
        flash(f'შენი მონაცემები წარმატებით განახლდა','success')
        return redirect(url_for ('customer_settings_update',id=registers.id))
    form.name.data=registers.name
    form.username.data=registers.username
    form.email.data=registers.email
    form.contact.data=registers.contact
    form.address.data=registers.address
    return render_template('customer/profile.html', registers=registers ,title='change your information', form=form)


@app.route('/getorder')
@login_required
def get_order():
    if current_user.is_authenticated:
        Customer_id = current_user.id
        invoice = secrets.token_hex(5)
        try:
            order = CustomerOrder(invoice = invoice, Customer_id = Customer_id, orders = session['shoppcart'])
            db.session.add(order)
            db.session.commit()
            session.pop('shoppcart')
            flash(f'შენი შეკვეთა გაიზავნა წარმატებით','success')
            return redirect(url_for('orders',invoice=invoice))
        except Exception as e:
            print(e)
            flash(f'რაგაც შცდომა შეამოწმეთ თავიდან','danger')
            return redirect(url_for('getcart'))


@app.route('/orders/<invoice>')
@login_required
def orders(invoice):
    if current_user.is_authenticated:
        grandTotal = 0
        subTotal = 0 
        customer_id = current_user.id
        customer = Register.query.filter_by(id=customer_id).first()
        orders = CustomerOrder.query.filter_by(Customer_id=customer_id).order_by(CustomerOrder.id.desc()).first()
        for _key,product in orders.orders.items():
            discount = (int(product['discount'])/100) * float(product['price'])
            subTotal += float(product['price']) * int(product['quantity'])
            subTotal -= discount
            tax = ("%.2f" % (.06 * float(subTotal)))
            grendTotal = float("%.2f" % (1.6 * subTotal))
    else:
        return redirect(url_for('customerLogin'))
    return render_template ('customer/order.html',invoice=invoice,tax=tax,subTotal=subTotal,grendTotal=grendTotal,customer=customer,orders=orders)