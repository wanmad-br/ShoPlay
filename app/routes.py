from flask import Blueprint, render_template
from .models import Product

main = Blueprint('main', __name__)

@main.route('/')
def catalog():
    products = Product.get_all_products()  # Assuming a method to get all products
    return render_template('catalog.html', products=products)