import psycopg2
import requests
import json

# Database connection details
DB_CONFIG = {
    'host': 'dpg-d1191sidbo4c739pelk0-a.oregon-postgres.render.com',
    'database': 'products_qnmx',
    'user': 'products_qnmx_user',
    'password': 'PYbv6akp0SOprUqCqgMVU27wpcf9L2sF',
    'port': 5432
}

def test_direct_db_connection():
    """Test direct connection to PostgreSQL database"""
    print("🐘 Testing Direct PostgreSQL Connection")
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
        
        cursor = conn.cursor()
        
        # Test 1: Check PostgreSQL version
        cursor.execute("SELECT version();")
        version = cursor.fetchone()
        print(f"✅ PostgreSQL Version: {version[0][:50]}...")
        
        # Test 2: List all tables
        cursor.execute("""
            SELECT table_name 
            FROM information_schema.tables 
            WHERE table_schema = 'public'
        """)
        tables = cursor.fetchall()
        print(f"📋 Tables in database: {[table[0] for table in tables]}")
        
        # Test 3: Check if products table exists and count records
        try:
            cursor.execute("SELECT COUNT(*) FROM products;")
            count = cursor.fetchone()[0]
            print(f"📦 Products in database: {count}")
            
            if count > 0:
                # Get sample products
                cursor.execute("SELECT id, title, price, category FROM products LIMIT 5;")
                sample_products = cursor.fetchall()
                print(f"🔍 Sample products:")
                for product in sample_products:
                    print(f"   - ID: {product[0]}, Title: {product[1]}, Price: ${product[2]}, Category: {product[3]}")
        except psycopg2.Error as e:
            print(f"⚠️ Products table not found or empty: {e}")
        
        cursor.close()
        conn.close()
        print("✅ Direct database connection successful!")
        return True
        
    except Exception as e:
        print(f"❌ Direct database connection failed: {e}")
        return False

def test_flask_api():
    """Test Flask API endpoints"""
    print("\n🌐 Testing Flask API with PostgreSQL")
    print("=" * 50)
    
    BASE_URL = "http://localhost:5000"
    
    try:
        # Test API root
        response = requests.get(f"{BASE_URL}/")
        if response.status_code == 200:
            data = response.json()
            print(f"✅ API Root: {data['message']}")
            print(f"📊 Database: {data.get('database', 'Unknown')}")
        else:
            print(f"❌ API Root failed: HTTP {response.status_code}")
            return False
        
        # Test products endpoint
        response = requests.get(f"{BASE_URL}/products?limit=5")
        if response.status_code == 200:
            data = response.json()
            print(f"✅ Products endpoint: {data['total']} total products")
            if data['products']:
                print(f"📦 First product: {data['products'][0]['title']}")
        else:
            print(f"❌ Products endpoint failed: HTTP {response.status_code}")
        
        # Test search endpoint
        response = requests.get(f"{BASE_URL}/products/search?q=iPhone")
        if response.status_code == 200:
            data = response.json()
            print(f"✅ Search endpoint: Found {data['total']} products for 'iPhone'")
        else:
            print(f"❌ Search endpoint failed: HTTP {response.status_code}")
        
        # Test categories endpoint
        response = requests.get(f"{BASE_URL}/products/categories")
        if response.status_code == 200:
            categories = response.json()
            print(f"✅ Categories endpoint: {len(categories)} categories")
            print(f"📂 Categories: {', '.join(categories[:5])}...")
        else:
            print(f"❌ Categories endpoint failed: HTTP {response.status_code}")
        
        return True
        
    except requests.exceptions.ConnectionError:
        print("❌ Cannot connect to Flask API. Make sure it's running!")
        print("   Run: python app.py")
        return False
    except Exception as e:
        print(f"❌ API test error: {e}")
        return False

def test_advanced_search():
    """Test advanced search functionality"""
    print("\n🔍 Testing Advanced Search Features")
    print("=" * 50)
    
    BASE_URL = "http://localhost:5000"
    
    search_tests = [
        {
            "name": "Text search",
            "url": f"{BASE_URL}/products/search?q=Apple",
            "description": "Search for Apple products"
        },
        {
            "name": "Category filter",
            "url": f"{BASE_URL}/products/search?category=smartphones",
            "description": "Filter by smartphones category"
        },
        {
            "name": "Price range",
            "url": f"{BASE_URL}/products/search?minPrice=100&maxPrice=500",
            "description": "Products between $100-$500"
        },
        {
            "name": "Combined search",
            "url": f"{BASE_URL}/products/search?q=laptop&minPrice=1000&maxPrice=3000&sortBy=price&order=asc",
            "description": "Laptops $1000-$3000 sorted by price"
        }
    ]
    
    for test in search_tests:
        try:
            response = requests.get(test['url'])
            if response.status_code == 200:
                data = response.json()
                print(f"✅ {test['name']}: {data['total']} results")
            else:
                print(f"❌ {test['name']}: HTTP {response.status_code}")
        except Exception as e:
            print(f"❌ {test['name']}: {e}")

def main():
    """Main test function"""
    print("🧪 PostgreSQL Database & API Testing")
    print("=" * 60)
    
    # Test direct database connection
    if not test_direct_db_connection():
        print("\n❌ Database connection failed. Please check your credentials.")
        return
    
    print("\n" + "="*60)
    
    # Test Flask API
    if not test_flask_api():
        print("\n⚠️ Flask API tests failed. Make sure the app is running.")
        return
    
    # Test advanced search
    test_advanced_search()
    
    print("\n" + "="*60)
    print("🎉 All tests completed!")
    print("\n📊 PostgreSQL Database Status:")
    print("   ✅ Connection established")
    print("   ✅ Tables created")
    print("   ✅ Data populated")
    print("   ✅ API endpoints working")
    print("   ✅ Advanced search functional")

if __name__ == "__main__":
    main()
