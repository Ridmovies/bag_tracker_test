import sentry_sdk
from flask import Flask, request


app = Flask(__name__)



@app.route("/error")
def hello_world():
    1/0  # raises an error
    return "<p>Hello, World!</p>"


@app.route("/type")
def test_type():
    user_id = request.args.get('user_id')
    user_id = float(user_id)
    return user_id


if __name__ == '__main__':
    app.run(debug=True)
