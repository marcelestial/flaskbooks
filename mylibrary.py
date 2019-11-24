from flask import Flask, render_template
app = Flask(__name__)

#A hardcoded sample list of books, to be replaced eventually with database access
books = [
    {
        'author': 'Writer Name',
        'title': 'Sample Book',
        'description': 'A book that was definitely written',
        'isbn': 'A long confusing number'
    },
    {
        'author': 'Writer2 Name',
        'title': 'Sample Book2',
        'description': 'Another book that was definitely written',
        'isbn': 'Another long confusing number'
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