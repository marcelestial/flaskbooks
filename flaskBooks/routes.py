from flask import render_template, url_for, flash, redirect
from flaskBooks import app
from flaskBooks.forms import RegistrationForm, LoginForm
from flaskBooks.models import User, Book

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

#The registration page route
@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title='Register', form=form)

#The login page route
@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@book.com' and form.password.data == 'password':
            flash('You have been logged in!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Login unsuccessful. Please check email and password', 'danger')
    return render_template('login.html', title='Login', form=form)