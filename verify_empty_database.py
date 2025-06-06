import os
import requests
import psycopg2

# Database connection details
DB_CONFIG = {
    'host': 'dpg-d1191sidbo4c739pelk0-a.oregon-postgres.render.com',
    'database': 'products_qnmx',
    'user': 'products_qnmx_user',
    'password': 'PYbv6akp0SOprUqCqgMVU27wpcf9L2sF',
    'port': 5432
}

def check_database_status():
    """Check if the database is empty and ready for use"""
    print("🔍 Checking Database Status")
    print("=" * 50)
    
    try:
        # Connect to PostgreSQL
        conn = psycopg2.connect(
            host=DB_CONFIG['host'],
            database=DB_CONFIG['database'],
            user=DB_CONFIG['user'],
            password=DB_CONFIG['password'],
            port=DB_CONFIG['port'],
            sslmode='require'
        )
        
        # Create a cursor
        cursor = conn.cursor()
        
        # Check if products table exists
        cursor.execute("""
            SELECT EXISTS (
                SELECT FROM information_schema.tables 
                WHERE table_schema = 'public'
                AND table_name = 'products'
            );
        """)
        table_exists = cursor.fetchone()[0]
        
        if not table_exists:
            print("❌ Products table does not exist!")
            return False
        
        # Check product count
        cursor.execute("SELECT COUNT(*) FROM products;")
        count = cursor.fetchone()[0]
        
        print(f"📊 Current product count: {count}")
        
        if count == 0:
            print("✅ Database is empty and ready for your data")
        else:
            print(f"⚠️ Database contains {count} products")
            
            # Show sample of existing products
            cursor.execute("SELECT id, title, brand, category FROM products LIMIT 5;")
            products = cursor.fetchall()
            
            print("\n📋 Sample of existing products:")
            for product in products:
                print(f"   ID: {product[0]}, Title: {product[1]}, Brand: {product[2]}, Category: {product[3]}")
            
            # Ask if user wants to clear the database
            clear_db = input("\n🗑️ Do you want to clear all products from the database? (yes/no): ")
            if clear_db.lower() == "yes":
                cursor.execute("DELETE FROM products;")
                cursor.execute("ALTER SEQUENCE products_id_seq RESTART WITH 1;")
                conn.commit()
                print("✅ All products have been deleted")
        
        # Close cursor and connection
        cursor.close()
        conn.close()
        
        return True
        
    except Exception as e:
        print(f"❌ Error checking database: {e}")
        return False

def test_api_connection():
    """Test connection to the API"""
    print("\n🌐 Testing API Connection")
    print("=" * 50)
    
    # Try local first
    local_url = "http://localhost:5000"
    try:
        response = requests.get(f"{local_url}/", timeout=5)
        if response.status_code == 200:
            print(f"✅ Connected to API at {local_url}")
            data = response.json()
            print(f"📊 Product count: {data.get('product_count', 'Unknown')}")
            return True
    except:
        print(f"❌ Could not connect to API at {local_url}")
    
    # Try deployed URL if provided
    deployed_url = input("\n🌐 Enter your deployed API URL (or press Enter to skip): ")
    if deployed_url:
        if not deployed_url.startswith("http"):
            deployed_url = f"https://{deployed_url}"
        
        try:
            response = requests.get(f"{deployed_url}/", timeout=10)
            if response.status_code == 200:
                print(f"✅ Connected to API at {deployed_url}")
                data = response.json()
                print(f"📊 Product count: {data.get('product_count', 'Unknown')}")
                return True
            else:
                print(f"❌ API returned status code {response.status_code}")
        except Exception as e:
            print(f"❌ Could not connect to API at {deployed_url}: {e}")
    
    return False

def add_test_product():
    """Add a test product to verify API is working"""
    print("\n🧪 Adding Test Product")
    print("=" * 50)
    
    # Ask if user wants to add a test product
    add_product = input("Do you want to add a test product? (yes/no): ")
    if add_product.lower() != "yes":
        return False
    
    # Get API URL
    api_url = input("Enter API URL (default: http://localhost:5000): ")
    if not api_url:
        api_url = "http://localhost:5000"
    
    if not api_url.startswith("http"):
        api_url = f"https://{api_url}"
    
    # Test product data
    test_product = {
        "title": "Test Product",
        "description": "This is a test product to verify the API is working",
        "price": 99.99,
        "brand": "Test Brand",
        "category": "test",
        "stock": 10,
        "rating": 4.5,
        "thumbnail": "https://example.com/test.jpg",
        "images": ["https://example.com/test1.jpg", "https://example.com/test2.jpg"]
    }
    
    try:
        # Add product
        print(f"📤 Sending POST request to {api_url}/products")
        response = requests.post(f"{api_url}/products", json=test_product)
        
        if response.status_code == 201:
            result = response.json()
            product_id = result['product']['id']
            print(f"✅ Test product created with ID: {product_id}")
            
            # Verify product was added
            print(f"📥 Verifying product was added...")
            get_response = requests.get(f"{api_url}/product/{product_id}")
            
            if get_response.status_code == 200:
                product = get_response.json()
                print(f"✅ Successfully retrieved product: {product['title']}")
                print(f"📊 Product details:")
                print(f"   ID: {product['id']}")
                print(f"   Title: {product['title']}")
                print(f"   Price: ${product['price']}")
                print(f"   Brand: {product['brand']}")
                print(f"   Category: {product['category']}")
                return True
            else:
                print(f"❌ Failed to retrieve product: {get_response.status_code}")
        else:
            print(f"❌ Failed to create product: {response.status_code}")
            print(f"📝 Response: {response.text}")
    except Exception as e:
        print(f"❌ Error: {e}")
    
    return False

def main():
    """Main function to verify empty database"""
    print("🔍 Database Verification Tool")
    print("=" * 60)
    
    # Check database status
    check_database_status()
    
    # Test API connection
    test_api_connection()
    
    # Add test product
    add_test_product()
    
    print("\n" + "=" * 60)
    print("🎉 Verification complete!")
    print("\n📝 Next steps:")
    print("1. Start your Flask API: python app.py")
    print("2. Add products using the API endpoints:")
    print("   - POST /products")
    print("   - POST /product/create")
    print("3. Deploy your API to Render for production use")

if __name__ == "__main__":
    main()
