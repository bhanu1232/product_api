from flask import Flask, request, jsonify
from flask_cors import CORS
from database import db, Product, Category
import json
import os
from sqlalchemy import desc, asc
from datetime import datetime

app = Flask(__name__)
CORS(app)

# Database configuration
if os.environ.get('DATABASE_URL'):
    app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL')
else:
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
    # Get product count
    product_count = Product.query.count()
    
    return jsonify({
        "message": "Products Store API with Database",
        "version": "2.1.0",
        "database": "PostgreSQL",
        "product_count": product_count,
        "features": [
            "Advanced search with filters",
            "Full-text search",
            "Category and brand filtering",
            "Price range filtering",
            "Stock availability filtering",
            "Pagination and sorting",
            "CRUD operations",
            "Clean database - no mock data"
        ],
        "endpoints": {
            "get_all_products": "GET /products",
            "get_single_product": "GET /product/{id}",
            "create_product": "POST /products",
            "create_product_alt": "POST /product/create",
            "update_product": "PUT /products/{id}",
            "delete_product": "DELETE /products/{id}",
            "search_products": "GET /products/search",
            "get_categories": "GET /products/categories",
            "get_brands": "GET /products/brands",
            "get_by_category": "GET /products/category/{category}"
        },
        "example_usage": {
            "get_product": "/product/1",
            "search": "/products/search?q=iPhone",
            "filter": "/products?category=smartphones&minPrice=500",
            "create": "POST /products with JSON data"
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

@app.route('/product/<int:product_id>', methods=['GET'])
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
        
        # Validate required fields
        required_fields = ['title', 'description', 'price', 'brand', 'category']
        missing_fields = [field for field in required_fields if not data.get(field)]
        
        if missing_fields:
            return jsonify({
                "error": f"Missing required fields: {', '.join(missing_fields)}"
            }), 400
        
        # Generate SKU if not provided
        sku = data.get('sku')
        if not sku:
            # Generate SKU from brand and title
            brand_code = data['brand'][:3].upper()
            title_code = ''.join(data['title'].split()[:2])[:6].upper()
            import random
            random_num = random.randint(100, 999)
            sku = f"{brand_code}-{title_code}-{random_num}"
        
        # Create new product
        new_product = Product(
            title=data.get("title"),
            description=data.get("description"),
            price=float(data.get("price", 0)),
            discount_percentage=float(data.get("discountPercentage", 0)),
            rating=float(data.get("rating", 0)),
            stock=int(data.get("stock", 0)),
            brand=data.get("brand"),
            category=data.get("category"),
            thumbnail=data.get("thumbnail", ""),
            images=str(data.get("images", [])),
            sku=sku,
            weight=float(data.get("weight", 0)) if data.get("weight") else None,
            dimensions=data.get("dimensions", ""),
            warranty_information=data.get("warrantyInformation", "1 year warranty"),
            shipping_information=data.get("shippingInformation", "Standard shipping"),
            availability_status=data.get("availabilityStatus", "In Stock"),
            return_policy=data.get("returnPolicy", "30-day return policy"),
            minimum_order_quantity=int(data.get("minimumOrderQuantity", 1)),
            meta_title=data.get("metaTitle", data.get("title")),
            meta_description=data.get("metaDescription", data.get("description")[:160]),
            meta_keywords=data.get("metaKeywords", f"{data.get('brand')}, {data.get('category')}")
        )
        
        db.session.add(new_product)
        db.session.commit()
        
        return jsonify({
            "message": "Product created successfully",
            "product": new_product.to_dict()
        }), 201
    
    except ValueError as e:
        return jsonify({"error": f"Invalid data type: {str(e)}"}), 400
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500

@app.route('/product/create', methods=['POST'])
def create_product():
    """Create a new product (alternative endpoint)"""
    try:
        # Handle both JSON and form data
        if request.is_json:
            data = request.get_json()
        else:
            data = request.form.to_dict()
        
        if not data:
            return jsonify({"error": "No data provided"}), 400
        
        # Validate required fields
        required_fields = ['title', 'description', 'price', 'brand', 'category']
        missing_fields = [field for field in required_fields if not data.get(field)]
        
        if missing_fields:
            return jsonify({
                "error": f"Missing required fields: {', '.join(missing_fields)}",
                "required_fields": required_fields,
                "provided_fields": list(data.keys())
            }), 400
        
        # Generate SKU if not provided
        sku = data.get('sku')
        if not sku:
            import random
            brand_code = data['brand'][:3].upper().replace(' ', '')
            title_words = data['title'].split()
            title_code = ''.join(word[:2] for word in title_words[:2]).upper()
            random_num = random.randint(100, 999)
            sku = f"{brand_code}-{title_code}-{random_num}"
        
        # Handle images (convert string to list if needed)
        images = data.get('images', [])
        if isinstance(images, str):
            # If it's a string, try to parse as JSON or split by comma
            try:
                import json
                images = json.loads(images)
            except:
                images = [img.strip() for img in images.split(',') if img.strip()]
        
        # Create new product
        new_product = Product(
            title=data.get("title"),
            description=data.get("description"),
            price=float(data.get("price", 0)),
            discount_percentage=float(data.get("discountPercentage", 0)),
            rating=float(data.get("rating", 0)),
            stock=int(data.get("stock", 0)),
            brand=data.get("brand"),
            category=data.get("category"),
            thumbnail=data.get("thumbnail", ""),
            images=str(images),
            sku=sku,
            weight=float(data.get("weight", 0)) if data.get("weight") else None,
            dimensions=data.get("dimensions", ""),
            warranty_information=data.get("warrantyInformation", "1 year warranty"),
            shipping_information=data.get("shippingInformation", "Standard shipping"),
            availability_status=data.get("availabilityStatus", "In Stock"),
            return_policy=data.get("returnPolicy", "30-day return policy"),
            minimum_order_quantity=int(data.get("minimumOrderQuantity", 1)),
            meta_title=data.get("metaTitle", data.get("title")),
            meta_description=data.get("metaDescription", data.get("description")[:160]),
            meta_keywords=data.get("metaKeywords", f"{data.get('brand')}, {data.get('category')}")
        )
        
        db.session.add(new_product)
        db.session.commit()
        
        return jsonify({
            "success": True,
            "message": "Product created successfully",
            "product_id": new_product.id,
            "product": new_product.to_dict()
        }), 201
    
    except ValueError as e:
        return jsonify({"error": f"Invalid data type: {str(e)}"}), 400
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

# No auto-seeding of mock data on startup
if __name__ == '__main__':
    with app.app_context():
        # Only create tables, don't seed data
        db.create_all()
    app.run(debug=False, host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))
