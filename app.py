from flask import Flask, jsonify

app = Flask(__name__)

# Static product list data
PRODUCTS = [
    {"id": 1, "name": "Wireless Mouse", "category": "Electronics", "price": 25.99, "in_stock": True},
    {"id": 2, "name": "Mechanical Keyboard", "category": "Electronics", "price": 89.99, "in_stock": True},
    {"id": 3, "name": "Coffee Mug", "category": "Home & Kitchen", "price": 12.50, "in_stock": False},
    {"id": 4, "name": "Notebook", "category": "Stationery", "price": 4.99, "in_stock": True}
]

@app.route('/api/products', methods=['GET'])
def get_products():
    """Returns the full list of products."""
    return jsonify({
        "status": "success",
        "count": len(PRODUCTS),
        "data": PRODUCTS
    }), 200

@app.route('/api/products/<int:product_id>', methods=['GET'])
def get_product(product_id):
    """Returns a single product by ID."""
    product = next((p for p in PRODUCTS if p["id"] == product_id), None)
    if product is None:
        return jsonify({"status": "error", "message": "Product not found"}), 404
    return jsonify({"status": "success", "data": product}), 200

if __name__ == '__main__':
    app.run(debug=True, port=5000)
