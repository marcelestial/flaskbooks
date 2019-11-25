from flask import render_template, url_for, flash, redirect, request
from flaskBooks import app, db, bcrypt
from flaskBooks.forms import RegistrationForm, LoginForm
from flaskBooks.models import User, Book
from flask_login import login_user, current_user, logout_user, login_required

#A hardcoded sample list of books, to be replaced eventually with database access
books = [
    {
        'author': 'Jolkien Rolkien Rolkien Tolkien',
        'title': 'The Hobbit',
        'description': 'It\'s the hobbit, man',
        'isbn': '9780582186552',
        'imgurl': 'https://images-na.ssl-images-amazon.com/images/I/61Ng-W9EhBL._SY346_.jpg'
    },
    {
        'author': 'Some Mormon lady',
        'title': 'Twilight',
        'description': 'A book about some things, I didn\'t read it',
        'isbn': '9789610007258',
        'imgurl': 'https://images-na.ssl-images-amazon.com/images/I/31kH-OWxJ-L._SY346_.jpg'
    }
]

#The home page route
@app.route("/")
@app.route("/home")
def home():
	return render_template('home.html', books=books)

#The about page route
@app.route("/about")
def about():
	return render_template('about.html', title='About')

#The registration page route. Only visible if user is not logged in
@app.route("/register", methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username=form.username.data, email=form.email.data, password=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash(f'Your account has been created! You are now able to log in.', 'success')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)

#The login page route. Only visible if user is not logged in
@app.route("/login", methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            next_page = request.args.get('next')
            return redirect (next_page) if next_page else redirect(url_for('home'))
        else:
            flash('Login unsuccessful. Please check email and password', 'danger')
    return render_template('login.html', title='Login', form=form)

#The logout function route. Only visible if user is logged in
@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('home'))

@app.route("/account")
@login_required
def account():
    return render_template('account.html', title='Account')






