from app import app

# Home Page
@app.route("/")
def index():
    return "This is a test page!"

