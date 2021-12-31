from flask import Flask, render_template

app = Flask(__name__)


# Defining the home page of our site
@app.route("/")
def home():
    return render_template("index.html")

if __name__ == "__main__":
    app.run()
