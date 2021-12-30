from flask import Flask

app = Flask(__name__)

if __name__ == "__main__":
    app.run()
# Defining the home page of our site
@app.route("/")  # this sets the route to this page
def home():
	return "<h1>Hello World</h1>"  
