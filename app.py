from flask import  Flask

app = Flask(__name__)

@app.route("/getmessage", methods=["GET"])
def say_hello():
    return "Welcome to flask"

if __name__ == "__main__":
    app.run(debug=True)
    