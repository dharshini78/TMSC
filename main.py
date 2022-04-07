from flask import Flask, render_template, redirect, url_for

# we can use render_template to return a html page

# name of the flask project is assigned to a variable name
app = Flask(__name__)


@app.route('/')  # main page, used to get the url
def home():  # function
    return render_template("login.html")


@app.route('/register')
def about():
    return render_template("register.html")


@app.route('/home')
def index():
    return render_template('home.html')


@app.route('/complaints')
def complaints():
    return render_template('contact-form.html')

@app.route('/districts')
def districts():
    return render_template('demodistricts.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')



if __name__ == "__main__":  # if the main page of the project is equal to the name of the flask project then
    # debugging is started
    app.run(debug=True)  # we can just reload the page to see changes after code and we dont need to run again and again
