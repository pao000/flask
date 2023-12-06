from app import app
from flask import jsonify, request
from app.northwind import obtener_tabla

@app.route('/')
def index():
    return jsonify({"message": "Bienvenid@s al endpoint de Northwind."}), 200


@app.route('/products', methods=['GET'])
def get_products():
    products_data = obtener_tabla('Products')
    product_id = request.args.get('id', type=int)

    if product_id is not None:
        product = next((product for product in products_data if product['ProductID'] == product_id), None)

        if product is not None:
            return jsonify(product), 200
        else:
            return jsonify({"message": "Producto no encontrado"}), 404

    return jsonify(products_data), 200


@app.route('/categories', methods=['GET'])
def get_categories():
    categories_data = obtener_tabla('Categories')
    return jsonify(categories_data), 200
    

@app.route('/suppliers', methods=['GET'])
def get_suppliers():
    suppliers_data  = obtener_tabla('Suppliers')
    return jsonify(suppliers_data), 200

@app.route('/territories', methods=['GET'])
def territories_country():
    territories_data  = obtener_tabla('territories')
    return jsonify(territories_data), 200

@app.route('/employees', methods=['GET'])
def employees_country():
    employees_data  = obtener_tabla('employees')
    return jsonify(employees_data), 200

@app.errorhandler(404)
def not_found(error):
    return jsonify({"error": "Ruta no disponible"}), 404
