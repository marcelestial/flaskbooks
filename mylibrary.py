from flask import Flask, render_template, url_for
app = Flask(__name__)

#Secret key to protect against cookie editing etc
app.config['SECRET_KEY'] = '144c3171a3fdeae712ed9bd8dac5994a'

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


if __name__ == '__main__':
	app.run(debug=True)