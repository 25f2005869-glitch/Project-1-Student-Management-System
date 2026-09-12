from flask import Flask, render_template
from config import Config
from extensions import db

# Import Models
from models.user import User
from models.student import Student

# Import Blueprints
from routes.auth import auth
from routes.student import student

# Create Flask App
app = Flask(__name__)

# Load Configuration
app.config.from_object(Config)

# Initialize Database
db.init_app(app)

# Register Blueprints
app.register_blueprint(auth)
app.register_blueprint(student)

# Create Database Tables
with app.app_context():
    db.create_all()


# ==========================
# Home Page
# ==========================
@app.route("/")
def home():
    return render_template("index.html")


# ==========================
# Dashboard
# ==========================
@app.route("/dashboard")
def dashboard():
    return render_template("dashboard.html")


# ==========================
# Run Flask App
# ==========================
if __name__ == "__main__":
    app.run(debug=True)