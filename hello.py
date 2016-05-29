# import Flask
from flask import Flask, render_template, request

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


@app.route('/show_the_login_form/')
def show_the_login_form():
    return "The login page"


@app.route('/do_the_login')
def do_the_login():
    return "The logged in page"


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return "Return login page"
    else:
        return "Logged in page"


@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('hello.html', name=name)

# Run the app
if __name__ == '__main__':
    # app.debug = True
    # app.run(host = '0.0.0.0')
    app.run(debug=True, host='0.0.0.0')
