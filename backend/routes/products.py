from flask import Blueprint, request, jsonify
from backend.models import db, Product

# mini app
products_bp = Blueprint("products", __name__)

# Create Product
@products_bp.route("/", methods=["POST"])
def create_product():
    data = request.get_json()
    product = Product(
        name=data["name"],
        description=data["description"],
        price=data["price"]
    )
    db.session.add(product)
    db.session.commit()
    return {"response": "Product created successfully"}, 201

# Get All Products
@products_bp.route("/", methods=["GET"])
def get_products():
    products = Product.query.all()
    result = [{"name": p.name, "description": p.description, "price": p.price} for p in products]
    return jsonify(result)
