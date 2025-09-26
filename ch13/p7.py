from flask import Flask

# Create a Flask app instance
app = Flask(__name__)

# Define a route (homepage)
@app.route("/")
def home():
    return "Hello, Flask! 🚀 Your server is running!"

# Another route (about page)
@app.route("/about")
def about():
    return "This is the About Page."

# Run the server
if __name__ == "__main__":
    app.run(debug=True)
