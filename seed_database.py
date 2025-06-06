from app import app, db
from database import Product, Category
import json

def create_mock_products():
    """Create 100+ mock e-commerce products"""
    
    mock_products = [
        # Smartphones (20 products)
        {
            "title": "iPhone 14 Pro Max",
            "description": "The most advanced iPhone with A16 Bionic chip, Pro camera system, and Dynamic Island",
            "price": 1099.99,
            "discount_percentage": 5.0,
            "rating": 4.8,
            "stock": 45,
            "brand": "Apple",
            "category": "smartphones",
            "thumbnail": "https://cdn.dummyjson.com/product-images/1/thumbnail.jpg",
            "images": str(["https://cdn.dummyjson.com/product-images/1/1.jpg", "https://cdn.dummyjson.com/product-images/1/2.jpg"]),
            "sku": "APL-IP14PM-128",
            "weight": 240.0,
            "dimensions": "160.7 x 77.6 x 7.85 mm",
            "warranty_information": "1 year limited warranty",
            "shipping_information": "Ships within 2-3 business days",
            "availability_status": "In Stock",
            "return_policy": "30-day return policy",
            "minimum_order_quantity": 1
        },
        {
            "title": "Samsung Galaxy S23 Ultra",
            "description": "Premium Android smartphone with S Pen, 200MP camera, and 5000mAh battery",
            "price": 999.99,
            "discount_percentage": 8.0,
            "rating": 4.7,
            "stock": 32,
            "brand": "Samsung",
            "category": "smartphones",
            "thumbnail": "https://cdn.dummyjson.com/product-images/2/thumbnail.jpg",
            "images": str(["https://cdn.dummyjson.com/product-images/2/1.jpg"]),
            "sku": "SAM-GS23U-256",
            "weight": 234.0,
            "dimensions": "163.4 x 78.1 x 8.9 mm",
            "warranty_information": "2 year manufacturer warranty",
            "shipping_information": "Free shipping on orders over $500",
            "availability_status": "In Stock",
            "return_policy": "15-day return policy",
            "minimum_order_quantity": 1
        },
        {
            "title": "Google Pixel 7 Pro",
            "description": "Google's flagship phone with advanced AI photography and pure Android experience",
            "price": 799.99,
            "discount_percentage": 12.0,
            "rating": 4.6,
            "stock": 28,
            "brand": "Google",
            "category": "smartphones",
            "thumbnail": "https://cdn.dummyjson.com/product-images/3/thumbnail.jpg",
            "images": str(["https://cdn.dummyjson.com/product-images/3/1.jpg"]),
            "sku": "GOO-PX7P-128",
            "weight": 210.0,
            "dimensions": "162.9 x 76.6 x 8.9 mm",
            "warranty_information": "1 year limited warranty",
            "shipping_information": "Ships within 1-2 business days",
            "availability_status": "In Stock",
            "return_policy": "30-day return policy",
            "minimum_order_quantity": 1
        },
        {
            "title": "OnePlus 11",
            "description": "Flagship killer with Snapdragon 8 Gen 2, 100W fast charging, and Hasselblad cameras",
            "price": 699.99,
            "discount_percentage": 10.0,
            "rating": 4.5,
            "stock": 41,
            "brand": "OnePlus",
            "category": "smartphones",
            "thumbnail": "https://cdn.dummyjson.com/product-images/4/thumbnail.jpg",
            "images": str(["https://cdn.dummyjson.com/product-images/4/1.jpg"]),
            "sku": "ONE-OP11-256",
            "weight": 205.0,
            "dimensions": "163.1 x 74.1 x 8.5 mm",
            "warranty_information": "1 year manufacturer warranty",
            "shipping_information": "Free express shipping",
            "availability_status": "In Stock",
            "return_policy": "14-day return policy",
            "minimum_order_quantity": 1
        },
        {
            "title": "Xiaomi 13 Pro",
            "description": "Premium smartphone with Leica cameras, Snapdragon 8 Gen 2, and 120W charging",
            "price": 649.99,
            "discount_percentage": 15.0,
            "rating": 4.4,
            "stock": 37,
            "brand": "Xiaomi",
            "category": "smartphones",
            "thumbnail": "https://cdn.dummyjson.com/product-images/5/thumbnail.jpg",
            "images": str(["https://cdn.dummyjson.com/product-images/5/1.jpg"]),
            "sku": "XIA-MI13P-256",
            "weight": 229.0,
            "dimensions": "162.9 x 74.6 x 8.4 mm",
            "warranty_information": "2 year international warranty",
            "shipping_information": "Ships within 3-5 business days",
            "availability_status": "In Stock",
            "return_policy": "30-day return policy",
            "minimum_order_quantity": 1
        },
        
        # Laptops (20 products)
        {
            "title": "MacBook Pro 16-inch M2 Max",
            "description": "Professional laptop with M2 Max chip, 32GB RAM, and stunning Liquid Retina XDR display",
            "price": 2499.99,
            "discount_percentage": 3.0,
            "rating": 4.9,
            "stock": 15,
            "brand": "Apple",
            "category": "laptops",
            "thumbnail": "https://cdn.dummyjson.com/product-images/6/thumbnail.png",
            "images": str(["https://cdn.dummyjson.com/product-images/6/1.png"]),
            "sku": "APL-MBP16-M2MAX",
            "weight": 2100.0,
            "dimensions": "35.57 x 24.81 x 1.68 cm",
            "warranty_information": "1 year limited warranty + AppleCare eligible",
            "shipping_information": "Free shipping, ships within 1-2 weeks",
            "availability_status": "In Stock",
            "return_policy": "14-day return policy",
            "minimum_order_quantity": 1
        },
        {
            "title": "Dell XPS 13 Plus",
            "description": "Ultra-portable laptop with 12th Gen Intel Core i7, 16GB RAM, and InfinityEdge display",
            "price": 1299.99,
            "discount_percentage": 8.0,
            "rating": 4.6,
            "stock": 22,
            "brand": "Dell",
            "category": "laptops",
            "thumbnail": "https://cdn.dummyjson.com/product-images/7/thumbnail.jpg",
            "images": str(["https://cdn.dummyjson.com/product-images/7/1.jpg"]),
            "sku": "DEL-XPS13P-I7",
            "weight": 1260.0,
            "dimensions": "29.5 x 19.9 x 1.5 cm",
            "warranty_information": "1 year premium support",
            "shipping_information": "Ships within 2-3 business days",
            "availability_status": "In Stock",
            "return_policy": "30-day return policy",
            "minimum_order_quantity": 1
        },
        {
            "title": "HP Spectre x360 14",
            "description": "2-in-1 convertible laptop with OLED display, Intel Evo platform, and premium design",
            "price": 1199.99,
            "discount_percentage": 12.0,
            "rating": 4.5,
            "stock": 18,
            "brand": "HP",
            "category": "laptops",
            "thumbnail": "https://cdn.dummyjson.com/product-images/8/thumbnail.jpg",
            "images": str(["https://cdn.dummyjson.com/product-images/8/1.jpg"]),
            "sku": "HP-SPX360-14",
            "weight": 1340.0,
            "dimensions": "31.2 x 22.0 x 1.7 cm",
            "warranty_information": "1 year limited warranty",
            "shipping_information": "Free shipping on orders over $999",
            "availability_status": "In Stock",
            "return_policy": "30-day return policy",
            "minimum_order_quantity": 1
        },
        {
            "title": "Lenovo ThinkPad X1 Carbon Gen 10",
            "description": "Business ultrabook with 12th Gen Intel Core, military-grade durability, and excellent keyboard",
            "price": 1599.99,
            "discount_percentage": 6.0,
            "rating": 4.7,
            "stock": 25,
            "brand": "Lenovo",
            "category": "laptops",
            "thumbnail": "https://cdn.dummyjson.com/product-images/9/thumbnail.jpg",
            "images": str(["https://cdn.dummyjson.com/product-images/9/1.jpg"]),
            "sku": "LEN-TPX1C-G10",
            "weight": 1120.0,
            "dimensions": "31.5 x 22.1 x 1.5 cm",
            "warranty_information": "3 year on-site warranty",
            "shipping_information": "Ships within 1-2 business days",
            "availability_status": "In Stock",
            "return_policy": "30-day return policy",
            "minimum_order_quantity": 1
        },
        {
            "title": "ASUS ROG Zephyrus G14",
            "description": "Gaming laptop with AMD Ryzen 9, RTX 4060, and AniMe Matrix LED display",
            "price": 1499.99,
            "discount_percentage": 10.0,
            "rating": 4.6,
            "stock": 31,
            "brand": "ASUS",
            "category": "laptops",
            "thumbnail": "https://cdn.dummyjson.com/product-images/10/thumbnail.jpeg",
            "images": str(["https://cdn.dummyjson.com/product-images/10/1.jpg"]),
            "sku": "ASU-ROGZ-G14",
            "weight": 1650.0,
            "dimensions": "31.2 x 22.7 x 1.9 cm",
            "warranty_information": "2 year international warranty",
            "shipping_information": "Free gaming mouse included",
            "availability_status": "In Stock",
            "return_policy": "15-day return policy",
            "minimum_order_quantity": 1
        },
        
        # Headphones & Audio (15 products)
        {
            "title": "Sony WH-1000XM5",
            "description": "Industry-leading noise canceling wireless headphones with 30-hour battery life",
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
            "minimum_order_quantity": 1
        },
        {
            "title": "Apple AirPods Pro 2nd Gen",
            "description": "Active noise cancellation, spatial audio, and up to 6 hours of listening time",
            "price": 249.99,
            "discount_percentage": 8.0,
            "rating": 4.7,
            "stock": 89,
            "brand": "Apple",
            "category": "headphones",
            "thumbnail": "https://cdn.dummyjson.com/product-images/12/thumbnail.jpg",
            "images": str(["https://cdn.dummyjson.com/product-images/12/1.jpg"]),
            "sku": "APL-APP2-GEN2",
            "weight": 56.4,
            "dimensions": "4.5 x 6.1 x 2.1 cm",
            "warranty_information": "1 year limited warranty",
            "shipping_information": "Free shipping",
            "availability_status": "In Stock",
            "return_policy": "14-day return policy",
            "minimum_order_quantity": 1
        },
        {
            "title": "Bose QuietComfort 45",
            "description": "Wireless noise cancelling headphones with exceptional comfort and sound quality",
            "price": 329.99,
            "discount_percentage": 12.0,
            "rating": 4.6,
            "stock": 43,
            "brand": "Bose",
            "category": "headphones",
            "thumbnail": "https://cdn.dummyjson.com/product-images/13/thumbnail.webp",
            "images": str(["https://cdn.dummyjson.com/product-images/13/1.jpg"]),
            "sku": "BOS-QC45-BLK",
            "weight": 238.0,
            "dimensions": "18.4 x 15.2 x 7.6 cm",
            "warranty_information": "1 year limited warranty",
            "shipping_information": "Ships within 2-3 business days",
            "availability_status": "In Stock",
            "return_policy": "30-day return policy",
            "minimum_order_quantity": 1
        },
        
        # Smart Watches (10 products)
        {
            "title": "Apple Watch Series 8",
            "description": "Advanced health monitoring, crash detection, and all-day battery life",
            "price": 399.99,
            "discount_percentage": 7.0,
            "rating": 4.8,
            "stock": 52,
            "brand": "Apple",
            "category": "smartwatches",
            "thumbnail": "https://cdn.dummyjson.com/product-images/14/thumbnail.jpg",
            "images": str(["https://cdn.dummyjson.com/product-images/14/1.jpg"]),
            "sku": "APL-AWS8-45MM",
            "weight": 51.5,
            "dimensions": "4.5 x 3.8 x 1.05 cm",
            "warranty_information": "1 year limited warranty",
            "shipping_information": "Ships within 1-2 business days",
            "availability_status": "In Stock",
            "return_policy": "14-day return policy",
            "minimum_order_quantity": 1
        },
        {
            "title": "Samsung Galaxy Watch 5 Pro",
            "description": "Premium smartwatch with titanium build, GPS tracking, and health monitoring",
            "price": 449.99,
            "discount_percentage": 10.0,
            "rating": 4.5,
            "stock": 38,
            "brand": "Samsung",
            "category": "smartwatches",
            "thumbnail": "https://cdn.dummyjson.com/product-images/15/thumbnail.jpg",
            "images": str(["https://cdn.dummyjson.com/product-images/15/1.jpg"]),
            "sku": "SAM-GW5P-45MM",
            "weight": 46.5,
            "dimensions": "4.5 x 4.5 x 1.1 cm",
            "warranty_information": "1 year manufacturer warranty",
            "shipping_information": "Free shipping",
            "availability_status": "In Stock",
            "return_policy": "15-day return policy",
            "minimum_order_quantity": 1
        },
        
        # Gaming Consoles (8 products)
        {
            "title": "PlayStation 5",
            "description": "Next-gen gaming console with 4K gaming, ray tracing, and ultra-fast SSD",
            "price": 499.99,
            "discount_percentage": 0.0,
            "rating": 4.9,
            "stock": 12,
            "brand": "Sony",
            "category": "gaming",
            "thumbnail": "https://cdn.dummyjson.com/product-images/16/thumbnail.jpg",
            "images": str(["https://cdn.dummyjson.com/product-images/16/1.jpg"]),
            "sku": "SON-PS5-STD",
            "weight": 4200.0,
            "dimensions": "39.0 x 26.0 x 10.4 cm",
            "warranty_information": "1 year manufacturer warranty",
            "shipping_information": "Limited availability - ships when in stock",
            "availability_status": "Low Stock",
            "return_policy": "30-day return policy",
            "minimum_order_quantity": 1
        },
        {
            "title": "Xbox Series X",
            "description": "Most powerful Xbox ever with 4K gaming at 60fps and Quick Resume feature",
            "price": 499.99,
            "discount_percentage": 0.0,
            "rating": 4.8,
            "stock": 18,
            "brand": "Microsoft",
            "category": "gaming",
            "thumbnail": "https://cdn.dummyjson.com/product-images/17/thumbnail.jpg",
            "images": str(["https://cdn.dummyjson.com/product-images/17/1.jpg"]),
            "sku": "MIC-XSX-1TB",
            "weight": 4450.0,
            "dimensions": "30.1 x 15.1 x 15.1 cm",
            "warranty_information": "1 year limited warranty",
            "shipping_information": "Ships within 1-2 weeks",
            "availability_status": "In Stock",
            "return_policy": "30-day return policy",
            "minimum_order_quantity": 1
        },
        
        # Tablets (12 products)
        {
            "title": "iPad Pro 12.9-inch M2",
            "description": "Ultimate iPad experience with M2 chip, Liquid Retina XDR display, and Apple Pencil support",
            "price": 1099.99,
            "discount_percentage": 5.0,
            "rating": 4.8,
            "stock": 29,
            "brand": "Apple",
            "category": "tablets",
            "thumbnail": "https://cdn.dummyjson.com/product-images/18/thumbnail.jpg",
            "images": str(["https://cdn.dummyjson.com/product-images/18/1.jpg"]),
            "sku": "APL-IPP129-M2",
            "weight": 682.0,
            "dimensions": "28.1 x 21.5 x 0.6 cm",
            "warranty_information": "1 year limited warranty",
            "shipping_information": "Ships within 2-3 business days",
            "availability_status": "In Stock",
            "return_policy": "14-day return policy",
            "minimum_order_quantity": 1
        },
        {
            "title": "Samsung Galaxy Tab S8 Ultra",
            "description": "Large 14.6-inch Super AMOLED display, S Pen included, perfect for productivity",
            "price": 899.99,
            "discount_percentage": 12.0,
            "rating": 4.6,
            "stock": 21,
            "brand": "Samsung",
            "category": "tablets",
            "thumbnail": "https://cdn.dummyjson.com/product-images/19/thumbnail.jpg",
            "images": str(["https://cdn.dummyjson.com/product-images/19/1.jpg"]),
            "sku": "SAM-GTS8U-256",
            "weight": 726.0,
            "dimensions": "32.6 x 20.8 x 0.6 cm",
            "warranty_information": "1 year manufacturer warranty",
            "shipping_information": "Free S Pen included",
            "availability_status": "In Stock",
            "return_policy": "15-day return policy",
            "minimum_order_quantity": 1
        },
        
        # Cameras (10 products)
        {
            "title": "Canon EOS R5",
            "description": "Professional mirrorless camera with 45MP sensor, 8K video, and in-body stabilization",
            "price": 3899.99,
            "discount_percentage": 8.0,
            "rating": 4.9,
            "stock": 7,
            "brand": "Canon",
            "category": "cameras",
            "thumbnail": "https://cdn.dummyjson.com/product-images/20/thumbnail.jpg",
            "images": str(["https://cdn.dummyjson.com/product-images/20/1.jpg"]),
            "sku": "CAN-EOSR5-BODY",
            "weight": 738.0,
            "dimensions": "13.8 x 9.8 x 8.8 cm",
            "warranty_information": "1 year international warranty",
            "shipping_information": "Ships within 1-2 weeks",
            "availability_status": "In Stock",
            "return_policy": "30-day return policy",
            "minimum_order_quantity": 1
        },
        {
            "title": "Sony Alpha A7 IV",
            "description": "Full-frame mirrorless camera with 33MP sensor, 4K 60p video, and advanced autofocus",
            "price": 2499.99,
            "discount_percentage": 6.0,
            "rating": 4.8,
            "stock": 14,
            "brand": "Sony",
            "category": "cameras",
            "thumbnail": "https://cdn.dummyjson.com/product-images/21/thumbnail.jpg",
            "images": str(["https://cdn.dummyjson.com/product-images/21/1.jpg"]),
            "sku": "SON-A7IV-BODY",
            "weight": 658.0,
            "dimensions": "13.1 x 9.6 x 7.9 cm",
            "warranty_information": "2 year manufacturer warranty",
            "shipping_information": "Ships within 3-5 business days",
            "availability_status": "In Stock",
            "return_policy": "30-day return policy",
            "minimum_order_quantity": 1
        },
        
        # Home Appliances (15 products)
        {
            "title": "Dyson V15 Detect",
            "description": "Cordless vacuum with laser dust detection and powerful suction for deep cleaning",
            "price": 749.99,
            "discount_percentage": 10.0,
            "rating": 4.7,
            "stock": 33,
            "brand": "Dyson",
            "category": "home-appliances",
            "thumbnail": "https://cdn.dummyjson.com/product-images/22/thumbnail.jpg",
            "images": str(["https://cdn.dummyjson.com/product-images/22/1.jpg"]),
            "sku": "DYS-V15DET-COR",
            "weight": 3100.0,
            "dimensions": "125.4 x 25.0 x 25.6 cm",
            "warranty_information": "2 year warranty",
            "shipping_information": "Free shipping",
            "availability_status": "In Stock",
            "return_policy": "30-day return policy",
            "minimum_order_quantity": 1
        },
        {
            "title": "KitchenAid Stand Mixer",
            "description": "Professional 5-quart stand mixer with 10 speeds and multiple attachments",
            "price": 449.99,
            "discount_percentage": 15.0,
            "rating": 4.8,
            "stock": 26,
            "brand": "KitchenAid",
            "category": "home-appliances",
            "thumbnail": "https://cdn.dummyjson.com/product-images/23/thumbnail.jpg",
            "images": str(["https://cdn.dummyjson.com/product-images/23/1.jpg"]),
            "sku": "KIT-SM5QT-RED",
            "weight": 11300.0,
            "dimensions": "35.3 x 22.1 x 35.6 cm",
            "warranty_information": "1 year warranty",
            "shipping_information": "Ships within 2-3 business days",
            "availability_status": "In Stock",
            "return_policy": "30-day return policy",
            "minimum_order_quantity": 1
        }
    ]
    
    # Add more products to reach 100+
    additional_categories = [
        ("fitness", "Fitness & Sports"),
        ("beauty", "Beauty & Personal Care"),
        ("books", "Books & Media"),
        ("clothing", "Clothing & Fashion"),
        ("jewelry", "Jewelry & Accessories"),
        ("automotive", "Automotive"),
        ("garden", "Garden & Outdoor"),
        ("toys", "Toys & Games"),
        ("office", "Office Supplies"),
        ("health", "Health & Wellness")
    ]
    
    # Generate additional products for each category
    for category, category_name in additional_categories:
        for i in range(8):  # 8 products per category = 80 more products
            mock_products.append({
                "title": f"{category_name} Product {i+1}",
                "description": f"High-quality {category} product with premium features and excellent performance",
                "price": round(50 + (i * 25) + (hash(category) % 200), 2),
                "discount_percentage": round(5 + (i % 15), 1),
                "rating": round(3.5 + (i % 15) / 10, 1),
                "stock": 20 + (i * 5) + (hash(category) % 50),
                "brand": f"{category.title()} Brand {(i % 3) + 1}",
                "category": category,
                "thumbnail": f"https://cdn.dummyjson.com/product-images/{(i % 20) + 1}/thumbnail.jpg",
                "images": str([f"https://cdn.dummyjson.com/product-images/{(i % 20) + 1}/1.jpg"]),
                "sku": f"{category.upper()}-{i+1:03d}-{hash(category) % 1000:03d}",
                "weight": round(100 + (i * 50) + (hash(category) % 500), 1),
                "dimensions": f"{10 + i} x {8 + i} x {2 + (i % 3)} cm",
                "warranty_information": f"{(i % 2) + 1} year warranty",
                "shipping_information": "Standard shipping available",
                "availability_status": "In Stock" if i % 10 != 0 else "Low Stock",
                "return_policy": "30-day return policy",
                "minimum_order_quantity": 1
            })
    
    return mock_products

def seed_database():
    """Seed the database with mock products"""
    print("🌱 Starting database seeding...")
    
    try:
        # Clear existing data
        db.session.query(Product).delete()
        db.session.commit()
        print("✅ Cleared existing products")
        
        # Create mock products
        mock_products = create_mock_products()
        print(f"📦 Created {len(mock_products)} mock products")
        
        # Add products to database
        for product_data in mock_products:
            product = Product(**product_data)
            db.session.add(product)
        
        db.session.commit()
        print(f"✅ Successfully seeded database with {len(mock_products)} products")
        
        # Print statistics
        total_products = Product.query.count()
        categories = Product.get_categories()
        brands = Product.get_brands()
        
        print(f"\n📊 Database Statistics:")
        print(f"   Total Products: {total_products}")
        print(f"   Categories: {len(categories)} ({', '.join(categories[:5])}...)")
        print(f"   Brands: {len(brands)} ({', '.join(brands[:5])}...)")
        print(f"   Average Price: ${Product.query.with_entities(db.func.avg(Product.price)).scalar():.2f}")
        
    except Exception as e:
        db.session.rollback()
        print(f"❌ Error seeding database: {e}")

if __name__ == "__main__":
    with app.app_context():
        # Create tables
        db.create_all()
        print("✅ Database tables created")
        
        # Seed with mock data
        seed_database()
        
        print("\n🎉 Database setup completed!")
        print("🚀 You can now run the Flask app with: python app.py")
