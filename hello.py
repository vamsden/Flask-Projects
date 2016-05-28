# import Flask
from flask import Flask
app = Flask(__name__)

# Specify the route for the app and define the app view


@app.route('/')
def index():
    return "Hello World"
# add_url_rule function is also available instead of using decorator

# Run the app
if __name__ == '__main__':
    app.run(debug=True)
