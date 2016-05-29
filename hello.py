# import Flask
import requests
from flask import Flask,
app = Flask(__name__)

# Specify the route for the app and define the app view


@app.route('/')
def index():
    return "Hello World"
# add_url_rule function is also available instead of using decorator

# Variable rules in flask


@app.route('/user/<username>')
def user_profile(username):
    return "User: %s" % (username)


@app.route('/post/<int:post_id>')
def show_post(post_id):
    return "Post: %d" % (post_id)


@app.route('/projects/')
def projects():
    return "The projects page"

# url_for('static', filename='style.css')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        do_the_login()
    else:
        show_the_login_form()


@app.route('/about')
def about():
    return "The about page"

# Run the app
if __name__ == '__main__':
    # app.debug = True
    # app.run(host = '0.0.0.0')
    app.run(debug=True, host='0.0.0.0')
