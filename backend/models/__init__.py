from flask_sqlalchemy import SQLAlchemy

# Create database instance
db = SQLAlchemy()

# Import models (only 3!)
from .user import User
from .product import Product
from .booking import Booking