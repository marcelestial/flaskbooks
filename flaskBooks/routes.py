from flask import render_template, url_for, flash, redirect, request, abort
from flaskBooks import app, db, bcrypt
from flaskBooks.forms import RegistrationForm, LoginForm, BookForm
from flaskBooks.models import User, Book
from flask_login import login_user, current_user, logout_user, login_required
from sqlalchemy import desc


#The home page route
@app.route("/")
@app.route("/home")
def home():
    books = Book.query.order_by(desc(Book.id)).all()
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

#Route for uesr's account. Not used for anything right now.
@app.route("/account")
@login_required
def account():
    return render_template('account.html', title='Account')

#Route for adding a new book to user's library
@app.route("/book/new", methods=['GET', 'POST'])
@login_required
def new_book():
    form = BookForm()
    if form.validate_on_submit():
        book=Book(title=form.title.data, author=form.author.data, description=form.description.data, isbn=form.isbn.data, imgurl=form.imgurl.data, owner=current_user)
        db.session.add(book)
        db.session.commit()
        flash('New book added to your library!', 'success')
        return redirect(url_for('home'))
    return render_template('create_book.html', title='New Book', 
        form=form, legend='New Book')

#Route for viewing a specific book's details
@app.route("/book/<int:book_id>")
def book(book_id):
    book = Book.query.get_or_404(book_id)
    return render_template('book.html', title=book.title, book=book)

#Route for editing a book's details
@app.route("/book/<int:book_id>/update", methods=['GET', 'POST'])
@login_required
def update_book(book_id):
    book = Book.query.get_or_404(book_id)
    if book.owner != current_user:
        abort(403)
    form = BookForm()
    if form.validate_on_submit():
        book.title = form.title.data
        book.author = form.author.data
        book.description = form.description.data
        book.isbn = form.isbn.data
        book.imgurl = form.imgurl.data
        db.session.commit()
        flash('Your book\'s data has been updated!', 'success')
        return redirect(url_for('book', book_id=book.id))
    elif request.method == 'GET':
        form.title.data = book.title
        form.author.data = book.author
        form.description.data = book.description
        form.isbn.data = book.isbn
        form.imgurl.data = book.imgurl
    return render_template('create_book.html', title='Edit Book', 
        form=form, legend='Edit Book')

@app.route("/book/<int:book_id>/delete", methods=['POST'])
@login_required
def delete_book(book_id):
    book = Book.query.get_or_404(book_id)
    if book.owner != current_user:
        abort(403)
    db.session.delete(book)
    db.session.commit()
    flash('Your book has been deleted.', 'success')
    return redirect(url_for('home'))



