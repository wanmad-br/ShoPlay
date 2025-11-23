from flask import Blueprint, render_template, request
from .models import Product

main = Blueprint('main', __name__)

@main.route('/')
def catalog():
    page = request.args.get('page', 1, type=int)
    products_per_page = 5
    
    all_products = Product.get_all_products()
    total_products = len(all_products)
    
    # Calculate pagination
    total_pages = (total_products + products_per_page - 1) // products_per_page
    start_idx = (page - 1) * products_per_page
    end_idx = start_idx + products_per_page
    
    # Validate page number
    if page < 1 or page > total_pages:
        page = 1
        start_idx = 0
        end_idx = products_per_page
    
    paginated_products = all_products[start_idx:end_idx]
    
    return render_template('catalog.html', 
                         products=paginated_products,
                         current_page=page,
                         total_pages=total_pages,
                         total_products=total_products)