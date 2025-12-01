from flask import Flask, jsonify, request

app = Flask(__name__)

products = [
    {"id": 1, "name": "iPhone 15", "price": 1200},
    {"id": 2, "name": "Samsung TV", "price": 900},
    {"id": 3, "name": "Sony Headphones", "price": 199}
]

@app.route("/")
def home():
    return "Ecommerce API running on Elastic Beanstalk!"

@app.route("/products")
def list_products():
    return jsonify(products)

@app.route("/order", methods=["POST"])
def create_order():
    data = request.json
    return jsonify({"message": "Order created", "order": data})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
