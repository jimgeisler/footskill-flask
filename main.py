from flask import Flask

# Create an instance of the Flask class
app = Flask(__name__)

# Define a route and its corresponding handler function
@app.route('/')
def index():
    return 'Hello, World!'

# Run the application if this script is executed directly
if __name__ == '__main__':
    app.run()
