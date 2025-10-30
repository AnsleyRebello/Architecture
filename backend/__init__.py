from flask import Flask
from flask_cors import CORS
from backend.models import db

# function that will create an app
def create_app():

    # Flask app object
    app = Flask(__name__)
    
    # Basic configuration
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SECRET_KEY'] = 'your-secret-key'
    
    CORS(app)

    # connection to the database
    db.init_app(app)
    
    # Register routes
    from backend.routes.users import users_bp
    from backend.routes.products import products_bp
    from backend.routes.bookings import bookings_bp

    app.register_blueprint(users_bp, url_prefix="/user")
    app.register_blueprint(products_bp, url_prefix="/product")
    app.register_blueprint(bookings_bp, url_prefix="/bookings")
    
    return app
