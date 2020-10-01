from flask import Flask, render_template
application = Flask(__name__)

@application.route('/')
def hello_world():
    return render_template('index.html')

if __name__ == "__main__":
    # Setting debug to True enables debug output. This line should be
    # removed before deploying a production application.
    application.debug = True
    application.run()