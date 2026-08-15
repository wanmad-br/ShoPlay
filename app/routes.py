from flask import Blueprint, jsonify, render_template, request
from .models import Product

main = Blueprint('main', __name__)


@main.route('/')
def catalog():
    products = Product.get_all_products()
    return render_template('catalog.html', products=products)


@main.route('/api/products')
def api_products():
    return jsonify([product.to_dict() for product in Product.get_all_products()])


@main.route('/api/purchase', methods=['POST'])
def purchase():
    payload = request.get_json(silent=True) or {}
    item_id = int(payload.get('item_id', 0) or 0)
    quantity = int(payload.get('quantity', 1) or 1)

    if quantity < 1:
        return jsonify({'status': 'error', 'message': 'Quantity must be at least 1.'}), 400

    products = Product.get_all_products()
    item = next((product for product in products if product.id == item_id), None)

    if item is None:
        return jsonify({'status': 'error', 'message': 'Item not found.'}), 404

    if quantity > item.stock:
        return jsonify({'status': 'error', 'message': 'Not enough stock available.'}), 400

    item.stock -= quantity
    total = round(item.price * quantity, 2)

    return jsonify({
        'status': 'success',
        'item': item.to_dict(),
        'quantity': quantity,
        'total': total,
        'receipt': {
            'item_id': item.id,
            'item_name': item.name,
            'quantity': quantity,
            'unit_price': item.price,
            'total': total,
            'currency': 'gold',
        },
    })