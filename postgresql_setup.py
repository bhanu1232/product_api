import os
import subprocess
import sys
import psycopg2
from psycopg2 import sql

# Database connection details
DB_CONFIG = {
    'host': 'dpg-d1191sidbo4c739pelk0-a.oregon-postgres.render.com',
    'database': 'products_qnmx',
    'user': 'products_qnmx_user',
    'password': 'PYbv6akp0SOprUqCqgMVU27wpcf9L2sF',
    'port': 5432
}

DATABASE_URL = f"postgresql://{DB_CONFIG['user']}:{DB_CONFIG['password']}@{DB_CONFIG['host']}:{DB_CONFIG['port']}/{DB_CONFIG['database']}"

def install_requirements():
    """Install required packages including PostgreSQL adapter"""
    print("📦 Installing requirements (including PostgreSQL support)...")
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"])
        print("✅ Requirements installed successfully!")
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ Error installing requirements: {e}")
        return False

def test_connection():
    """Test connection to PostgreSQL database"""
    print("🔌 Testing PostgreSQL connection...")
    try:
        conn = psycopg2.connect(
            host=DB_CONFIG['host'],
            database=DB_CONFIG['database'],
            user=DB_CONFIG['user'],
            password=DB_CONFIG['password'],
            port=DB_CONFIG['port'],
            sslmode='require'
        )
        
        cursor = conn.cursor()
        cursor.execute("SELECT version();")
        version = cursor.fetchone()
        print(f"✅ Connected to PostgreSQL: {version[0]}")
        
        cursor.close()
        conn.close()
        return True
        
    except Exception as e:
        print(f"❌ Connection failed: {e}")
        return False

def setup_database():
    """Setup and initialize the PostgreSQL database"""
    print("🗄️ Setting up PostgreSQL database...")
    
    try:
        # Set environment variable for the app
        os.environ['DATABASE_URL'] = DATABASE_URL
        
        from app import app, db
        
        with app.app_context():
            print("📋 Creating database tables...")
            # Drop all tables first (clean slate)
            db.drop_all()
            print("🗑️ Dropped existing tables")
            
            # Create all tables
            db.create_all()
            print("✅ Database tables created successfully!")
            
            # Check if we need to seed data
            from database import Product
            product_count = Product.query.count()
            
            if product_count == 0:
                print("📊 Database is empty, seeding with mock data...")
                seed_postgresql_database()
            else:
                print(f"📊 Database already contains {product_count} products")
                
        return True
        
    except Exception as e:
        print(f"❌ Error setting up database: {e}")
        return False

def seed_postgresql_database():
    """Seed PostgreSQL database with mock products"""
    print("🌱 Seeding PostgreSQL database...")
    
    try:
        os.environ['DATABASE_URL'] = DATABASE_URL
        from app import app, db
        from database import Product
        
        with app.app_context():
            # Clear existing data
            db.session.query(Product).delete()
            db.session.commit()
            print("✅ Cleared existing products")
            
            # Create comprehensive mock products
            mock_products = create_comprehensive_products()
            print(f"📦 Created {len(mock_products)} mock products")
            
            # Add products to database in batches
            batch_size = 50
            for i in range(0, len(mock_products), batch_size):
                batch = mock_products[i:i + batch_size]
                for product_data in batch:
                    product = Product(**product_data)
                    db.session.add(product)
                
                db.session.commit()
                print(f"✅ Inserted batch {i//batch_size + 1}/{(len(mock_products) + batch_size - 1)//batch_size}")
            
            # Print statistics
            total_products = Product.query.count()
            categories = Product.get_categories()
            brands = Product.get_brands()
            
            print(f"\n📊 PostgreSQL Database Statistics:")
            print(f"   Total Products: {total_products}")
            print(f"   Categories: {len(categories)}")
            print(f"   Brands: {len(brands)}")
            print(f"   Average Price: ${db.session.query(db.func.avg(Product.price)).scalar():.2f}")
            
            # Show sample products
            sample_products = Product.query.limit(5).all()
            print(f"\n📦 Sample Products:")
            for product in sample_products:
                print(f"   - {product.title} (${product.price}) - {product.category}")
            
    except Exception as e:
        print(f"❌ Error seeding database: {e}")
        if 'db' in locals():
            db.session.rollback()

def create_comprehensive_products():
    """Create comprehensive mock product data"""
    
    products = []
    
    # Technology Products
    tech_products = [
        {
            "title": "iPhone 15 Pro Max",
            "description": "Latest iPhone with titanium design, A17 Pro chip, and advanced camera system",
            "price": 1199.99,
            "discount_percentage": 5.0,
            "rating": 4.9,
            "stock": 45,
            "brand": "Apple",
            "category": "smartphones",
            "thumbnail": "https://cdn.dummyjson.com/product-images/1/thumbnail.jpg",
            "images": str(["https://cdn.dummyjson.com/product-images/1/1.jpg", "https://cdn.dummyjson.com/product-images/1/2.jpg"]),
            "sku": "APL-IP15PM-256",
            "weight": 221.0,
            "dimensions": "159.9 x 76.7 x 8.25 mm",
            "warranty_information": "1 year limited warranty",
            "shipping_information": "Ships within 2-3 business days",
            "availability_status": "In Stock",
            "return_policy": "30-day return policy",
            "minimum_order_quantity": 1,
            "meta_title": "iPhone 15 Pro Max - Latest Apple Smartphone",
            "meta_description": "Get the newest iPhone 15 Pro Max with titanium design and A17 Pro chip",
            "meta_keywords": "iPhone, Apple, smartphone, titanium, A17 Pro"
        },
        {
            "title": "Samsung Galaxy S24 Ultra",
            "description": "Premium Android flagship with S Pen, 200MP camera, and AI features",
            "price": 1299.99,
            "discount_percentage": 8.0,
            "rating": 4.8,
            "stock": 32,
            "brand": "Samsung",
            "category": "smartphones",
            "thumbnail": "https://cdn.dummyjson.com/product-images/2/thumbnail.jpg",
            "images": str(["https://cdn.dummyjson.com/product-images/2/1.jpg"]),
            "sku": "SAM-GS24U-512",
            "weight": 232.0,
            "dimensions": "162.3 x 79.0 x 8.6 mm",
            "warranty_information": "2 year manufacturer warranty",
            "shipping_information": "Free shipping on orders over $500",
            "availability_status": "In Stock",
            "return_policy": "15-day return policy",
            "minimum_order_quantity": 1,
            "meta_title": "Samsung Galaxy S24 Ultra - Premium Android Phone",
            "meta_description": "Experience the Samsung Galaxy S24 Ultra with S Pen and 200MP camera",
            "meta_keywords": "Samsung, Galaxy, S24, Ultra, Android, S Pen"
        },
        {
            "title": "MacBook Pro 16-inch M3 Max",
            "description": "Most powerful MacBook Pro with M3 Max chip, 36GB RAM, and Liquid Retina XDR display",
            "price": 3499.99,
            "discount_percentage": 3.0,
            "rating": 4.9,
            "stock": 12,
            "brand": "Apple",
            "category": "laptops",
            "thumbnail": "https://cdn.dummyjson.com/product-images/6/thumbnail.png",
            "images": str(["https://cdn.dummyjson.com/product-images/6/1.png"]),
            "sku": "APL-MBP16-M3MAX",
            "weight": 2140.0,
            "dimensions": "35.57 x 24.81 x 1.68 cm",
            "warranty_information": "1 year limited warranty + AppleCare eligible",
            "shipping_information": "Free shipping, ships within 2-4 weeks",
            "availability_status": "In Stock",
            "return_policy": "14-day return policy",
            "minimum_order_quantity": 1,
            "meta_title": "MacBook Pro 16-inch M3 Max - Professional Laptop",
            "meta_description": "Ultimate MacBook Pro with M3 Max chip for professional workflows",
            "meta_keywords": "MacBook Pro, Apple, M3 Max, laptop, professional"
        },
        {
            "title": "Dell XPS 15 OLED",
            "description": "Premium Windows laptop with 4K OLED display, Intel Core i9, and RTX 4070",
            "price": 2299.99,
            "discount_percentage": 10.0,
            "rating": 4.7,
            "stock": 18,
            "brand": "Dell",
            "category": "laptops",
            "thumbnail": "https://cdn.dummyjson.com/product-images/7/thumbnail.jpg",
            "images": str(["https://cdn.dummyjson.com/product-images/7/1.jpg"]),
            "sku": "DEL-XPS15-OLED",
            "weight": 1860.0,
            "dimensions": "34.4 x 23.0 x 1.8 cm",
            "warranty_information": "1 year premium support",
            "shipping_information": "Ships within 3-5 business days",
            "availability_status": "In Stock",
            "return_policy": "30-day return policy",
            "minimum_order_quantity": 1,
            "meta_title": "Dell XPS 15 OLED - Premium Windows Laptop",
            "meta_description": "Dell XPS 15 with stunning 4K OLED display and powerful performance",
            "meta_keywords": "Dell, XPS 15, OLED, Windows, laptop, Intel"
        },
        {
            "title": "Sony WH-1000XM5",
            "description": "Industry-leading noise canceling wireless headphones with 30-hour battery",
            "price": 399.99,
            "discount_percentage": 15.0,
            "rating": 4.8,
            "stock": 67,
            "brand": "Sony",
            "category": "headphones",
            "thumbnail": "https://cdn.dummyjson.com/product-images/11/thumbnail.jpg",
            "images": str(["https://cdn.dummyjson.com/product-images/11/1.jpg"]),
            "sku": "SON-WH1000XM5",
            "weight": 250.0,
            "dimensions": "26.4 x 19.3 x 7.3 cm",
            "warranty_information": "1 year manufacturer warranty",
            "shipping_information": "Ships within 24 hours",
            "availability_status": "In Stock",
            "return_policy": "30-day return policy",
            "minimum_order_quantity": 1,
            "meta_title": "Sony WH-1000XM5 - Premium Noise Canceling Headphones",
            "meta_description": "Experience superior sound with Sony's flagship noise canceling headphones",
            "meta_keywords": "Sony, headphones, noise canceling, wireless, WH-1000XM5"
        }
    ]
    
    products.extend(tech_products)
    
    # Generate products for different categories
    categories_data = [
        ("gaming", "Gaming", ["PlayStation", "Xbox", "Nintendo", "Razer", "Logitech"], 50, 800),
        ("home-appliances", "Home Appliances", ["Dyson", "KitchenAid", "Breville", "Ninja", "Instant Pot"], 30, 500),
        ("fitness", "Fitness", ["Nike", "Adidas", "Fitbit", "Garmin", "Under Armour"], 25, 300),
        ("beauty", "Beauty", ["L'Oreal", "Maybelline", "MAC", "Sephora", "Urban Decay"], 15, 150),
        ("books", "Books", ["Penguin", "HarperCollins", "Random House", "Scholastic", "O'Reilly"], 10, 50),
        ("clothing", "Clothing", ["Nike", "Adidas", "Zara", "H&M", "Uniqlo"], 20, 200),
        ("jewelry", "Jewelry", ["Tiffany", "Pandora", "Swarovski", "Kay", "Zales"], 100, 2000),
        ("automotive", "Automotive", ["Bosch", "Michelin", "Castrol", "3M", "Chemical Guys"], 25, 300),
        ("garden", "Garden", ["Black+Decker", "Scotts", "Miracle-Gro", "Husqvarna", "WORX"], 30, 400),
        ("toys", "Toys", ["LEGO", "Mattel", "Hasbro", "Fisher-Price", "Nerf"], 15, 100),
        ("office", "Office", ["HP", "Canon", "Staples", "3M", "Logitech"], 20, 300),
        ("health", "Health", ["Johnson & Johnson", "Pfizer", "CVS", "Walgreens", "Nature Made"], 10, 100)
    ]
    
    product_id = len(tech_products) + 1
    
    for category, category_name, brands, min_price, max_price in categories_data:
        for i in range(15):  # 15 products per category
            brand = brands[i % len(brands)]
            price = round(min_price + (i * (max_price - min_price) / 15) + (hash(f"{category}{i}") % 100), 2)
            
            product = {
                "title": f"{brand} {category_name} Product {i+1}",
                "description": f"High-quality {category} product from {brand} with premium features and excellent performance. Perfect for {category} enthusiasts.",
                "price": price,
                "discount_percentage": round(5 + (i % 20), 1),
                "rating": round(3.5 + (i % 20) / 10, 1),
                "stock": 10 + (i * 3) + (hash(f"{category}{i}") % 50),
                "brand": brand,
                "category": category,
                "thumbnail": f"https://cdn.dummyjson.com/product-images/{(i % 20) + 1}/thumbnail.jpg",
                "images": str([f"https://cdn.dummyjson.com/product-images/{(i % 20) + 1}/1.jpg"]),
                "sku": f"{brand.upper().replace(' ', '')}-{category.upper()}-{i+1:03d}",
                "weight": round(50 + (i * 25) + (hash(f"{category}{i}") % 200), 1),
                "dimensions": f"{8 + i} x {6 + i} x {2 + (i % 4)} cm",
                "warranty_information": f"{(i % 3) + 1} year warranty",
                "shipping_information": "Standard shipping available" if i % 3 != 0 else "Free shipping",
                "availability_status": "In Stock" if i % 15 != 0 else "Low Stock",
                "return_policy": "30-day return policy",
                "minimum_order_quantity": 1,
                "meta_title": f"{brand} {category_name} Product {i+1} - Premium Quality",
                "meta_description": f"Shop {brand} {category} products with excellent quality and performance",
                "meta_keywords": f"{brand}, {category}, {category_name}, premium, quality"
            }
            
            products.append(product)
            product_id += 1
    
    return products

def main():
    """Main setup function for PostgreSQL"""
    print("🐘 PostgreSQL Flask Products API Setup")
    print("=" * 60)
    print(f"🔗 Database: {DB_CONFIG['database']}")
    print(f"🏠 Host: {DB_CONFIG['host']}")
    print(f"👤 User: {DB_CONFIG['user']}")
    print("=" * 60)
    
    # Step 1: Install requirements
    if not install_requirements():
        return
    
    # Step 2: Test connection
    if not test_connection():
        return
    
    # Step 3: Setup database
    if not setup_database():
        return
    
    print("\n🎉 PostgreSQL setup completed successfully!")
    print("\n📋 Next steps:")
    print("1. Run the Flask app: python app.py")
    print("2. Test the API: python test_advanced_api.py")
    print("3. Access API at: http://localhost:5000")
    print(f"\n🐘 Database: PostgreSQL on Render")
    print(f"📊 Products: 180+ mock products across 13 categories")
    print(f"🔎 Advanced search capabilities enabled")
    print(f"🌐 External database URL configured")

if __name__ == "__main__":
    main()
