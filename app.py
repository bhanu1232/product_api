from flask import Flask, request, jsonify
from flask_cors import CORS
from database import db, Product, Category
import json
import os
from sqlalchemy import desc, asc

app = Flask(__name__)
CORS(app)

# Database configuration
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://products_qnmx_user:PYbv6akp0SOprUqCqgMVU27wpcf9L2sF@dpg-d1191sidbo4c739pelk0-a.oregon-postgres.render.com/products_qnmx'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ENGINE_OPTIONS'] = {
    'pool_pre_ping': True,
    'pool_recycle': 300,
    'connect_args': {
        'sslmode': 'require'
    }
}

# Initialize database
db.init_app(app)

@app.route('/')
def home():
    return jsonify({
        "message": "Products Store API with Database",
        "version": "2.0.0",
        "database": "SQLite/PostgreSQL",
        "features": [
            "Advanced search with filters",
            "Full-text search",
            "Category and brand filtering",
            "Price range filtering",
            "Stock availability filtering",
            "Pagination and sorting",
            "100+ mock products"
        ],
        "endpoints": {
            "products": "/products",
            "single_product": "/products/{id}",
            "search": "/products/search",
            "categories": "/products/categories",
            "brands": "/products/brands",
            "category_products": "/products/category/{category}"
        }
    })

@app.route('/products', methods=['GET'])
def get_all_products():
    """Get all products with advanced filtering and pagination"""
    try:
        # Get query parameters
        limit = min(int(request.args.get('limit', 30)), 100)  # Max 100 items per request
        skip = int(request.args.get('skip', 0))
        select = request.args.get('select', '')
        sort_by = request.args.get('sortBy', 'id')
        order = request.args.get('order', 'asc')
        
        # Filter parameters
        category = request.args.get('category')
        brand = request.args.get('brand')
        min_price = request.args.get('minPrice', type=float)
        max_price = request.args.get('maxPrice', type=float)
        in_stock = request.args.get('inStock', type=bool)
        
        # Build query
        query = Product.query
        
        # Apply filters
        if category:
            query = query.filter(Product.category.ilike(f'%{category}%'))
        if brand:
            query = query.filter(Product.brand.ilike(f'%{brand}%'))
        if min_price is not None:
            query = query.filter(Product.price >= min_price)
        if max_price is not None:
            query = query.filter(Product.price <= max_price)
        if in_stock:
            query = query.filter(Product.stock > 0)
        
        # Apply sorting
        if hasattr(Product, sort_by):
            if order.lower() == 'desc':
                query = query.order_by(desc(getattr(Product, sort_by)))
            else:
                query = query.order_by(asc(getattr(Product, sort_by)))
        
        # Get total count before pagination
        total = query.count()
        
        # Apply pagination
        products = query.offset(skip).limit(limit).all()
        
        # Apply field selection if specified
        if select:
            selected_fields = [field.strip() for field in select.split(',')]
            result_products = []
            for product in products:
                product_dict = product.to_dict()
                selected_product = {field: product_dict.get(field) for field in selected_fields if field in product_dict}
                result_products.append(selected_product)
        else:
            result_products = [product.to_dict() for product in products]
        
        return jsonify({
            "products": result_products,
            "total": total,
            "skip": skip,
            "limit": limit
        })
    
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/products/<int:product_id>', methods=['GET'])
def get_single_product(product_id):
    """Get a single product by ID"""
    try:
        product = Product.query.get(product_id)
        if not product:
            return jsonify({"error": "Product not found"}), 404
        
        return jsonify(product.to_dict())
    
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/products/search', methods=['GET'])
def search_products():
    """Advanced search products with multiple filters"""
    try:
        # Get search parameters
        query = request.args.get('q', '')
        limit = min(int(request.args.get('limit', 30)), 100)
        skip = int(request.args.get('skip', 0))
        
        # Filter parameters
        category = request.args.get('category')
        brand = request.args.get('brand')
        min_price = request.args.get('minPrice', type=float)
        max_price = request.args.get('maxPrice', type=float)
        in_stock = request.args.get('inStock', type=bool)
        sort_by = request.args.get('sortBy', 'id')
        order = request.args.get('order', 'asc')
        
        if not query and not any([category, brand, min_price, max_price, in_stock]):
            return jsonify({"error": "At least one search parameter is required"}), 400
        
        # Perform search
        search_query = Product.search(
            query=query,
            category=category,
            min_price=min_price,
            max_price=max_price,
            brand=brand,
            in_stock=in_stock
        )
        
        # Apply sorting
        if hasattr(Product, sort_by):
            if order.lower() == 'desc':
                search_query = search_query.order_by(desc(getattr(Product, sort_by)))
            else:
                search_query = search_query.order_by(asc(getattr(Product, sort_by)))
        
        # Get total count
        total = search_query.count()
        
        # Apply pagination
        results = search_query.offset(skip).limit(limit).all()
        
        return jsonify({
            "products": [product.to_dict() for product in results],
            "total": total,
            "skip": skip,
            "limit": limit,
            "query": query,
            "filters": {
                "category": category,
                "brand": brand,
                "minPrice": min_price,
                "maxPrice": max_price,
                "inStock": in_stock
            }
        })
    
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/products/categories', methods=['GET'])
def get_categories():
    """Get all product categories"""
    try:
        categories = Product.get_categories()
        return jsonify(categories)
    
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/products/brands', methods=['GET'])
def get_brands():
    """Get all product brands"""
    try:
        brands = Product.get_brands()
        return jsonify(brands)
    
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/products/category/<category>', methods=['GET'])
def get_products_by_category(category):
    """Get products by category"""
    try:
        limit = min(int(request.args.get('limit', 30)), 100)
        skip = int(request.args.get('skip', 0))
        
        # Filter products by category
        query = Product.query.filter(Product.category.ilike(f'%{category}%'))
        
        total = query.count()
        if total == 0:
            return jsonify({"error": "Category not found"}), 404
        
        products = query.offset(skip).limit(limit).all()
        
        return jsonify({
            "products": [product.to_dict() for product in products],
            "total": total,
            "skip": skip,
            "limit": limit,
            "category": category
        })
    
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/products', methods=['POST'])
def add_product():
    """Add a new product"""
    try:
        data = request.get_json()
        
        if not data:
            return jsonify({"error": "No data provided"}), 400
        
        # Create new product
        new_product = Product(
            title=data.get("title", ""),
            description=data.get("description", ""),
            price=data.get("price", 0),
            discount_percentage=data.get("discountPercentage", 0),
            rating=data.get("rating", 0),
            stock=data.get("stock", 0),
            brand=data.get("brand", ""),
            category=data.get("category", ""),
            thumbnail=data.get("thumbnail", ""),
            images=str(data.get("images", [])),
            sku=data.get("sku", ""),
            weight=data.get("weight"),
            dimensions=data.get("dimensions", ""),
            warranty_information=data.get("warrantyInformation", ""),
            shipping_information=data.get("shippingInformation", ""),
            availability_status=data.get("availabilityStatus", "In Stock"),
            return_policy=data.get("returnPolicy", ""),
            minimum_order_quantity=data.get("minimumOrderQuantity", 1)
        )
        
        db.session.add(new_product)
        db.session.commit()
        
        return jsonify(new_product.to_dict()), 201
    
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500

@app.route('/products/<int:product_id>', methods=['PUT'])
def update_product(product_id):
    """Update a product"""
    try:
        data = request.get_json()
        
        if not data:
            return jsonify({"error": "No data provided"}), 400
        
        product = Product.query.get(product_id)
        if not product:
            return jsonify({"error": "Product not found"}), 404
        
        # Update product fields
        for key, value in data.items():
            if key == 'discountPercentage':
                product.discount_percentage = value
            elif key == 'images':
                product.images = str(value)
            elif hasattr(product, key) and key != 'id':
                setattr(product, key, value)
        
        db.session.commit()
        
        return jsonify(product.to_dict())
    
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500

@app.route('/products/<int:product_id>', methods=['DELETE'])
def delete_product(product_id):
    """Delete a product"""
    try:
        product = Product.query.get(product_id)
        if not product:
            return jsonify({"error": "Product not found"}), 404
        
        product_data = product.to_dict()
        db.session.delete(product)
        db.session.commit()
        
        return jsonify({
            **product_data,
            "isDeleted": True,
            "deletedOn": datetime.now().isoformat()
        })
    
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True, host='0.0.0.0', port=5000)
