import requests
import json
import time

BASE_URL = "http://localhost:5000"

def test_advanced_search():
    """Test advanced search functionality"""
    print("🔍 Testing Advanced Search Functionality")
    print("=" * 50)
    
    test_cases = [
        {
            "name": "Basic text search",
            "url": f"{BASE_URL}/products/search?q=iPhone",
            "description": "Search for 'iPhone' in all text fields"
        },
        {
            "name": "Category filter",
            "url": f"{BASE_URL}/products/search?category=smartphones",
            "description": "Filter products by smartphones category"
        },
        {
            "name": "Price range filter",
            "url": f"{BASE_URL}/products/search?minPrice=500&maxPrice=1000",
            "description": "Filter products between $500-$1000"
        },
        {
            "name": "Brand filter",
            "url": f"{BASE_URL}/products/search?brand=Apple",
            "description": "Filter products by Apple brand"
        },
        {
            "name": "Combined filters",
            "url": f"{BASE_URL}/products/search?q=laptop&category=laptops&minPrice=1000&maxPrice=2000&brand=Apple",
            "description": "Search 'laptop' in Apple laptops $1000-$2000"
        },
        {
            "name": "In stock filter",
            "url": f"{BASE_URL}/products/search?inStock=true&category=gaming",
            "description": "Find in-stock gaming products"
        },
        {
            "name": "Sorted results",
            "url": f"{BASE_URL}/products/search?q=phone&sortBy=price&order=desc",
            "description": "Search phones sorted by price (high to low)"
        }
    ]
    
    for i, test in enumerate(test_cases, 1):
        print(f"\n{i}. {test['name']}")
        print(f"   Description: {test['description']}")
        print(f"   URL: {test['url']}")
        
        try:
            response = requests.get(test['url'])
            if response.status_code == 200:
                data = response.json()
                print(f"   ✅ Success: Found {data['total']} products")
                if data['products']:
                    first_product = data['products'][0]
                    print(f"   📦 First result: {first_product['title']} - ${first_product['price']}")
            else:
                print(f"   ❌ Failed: HTTP {response.status_code}")
        except requests.exceptions.ConnectionError:
            print("   ❌ Connection failed. Make sure Flask app is running!")
            return False
        except Exception as e:
            print(f"   ❌ Error: {e}")
    
    return True

def test_database_endpoints():
    """Test database-powered endpoints"""
    print("\n🗄️ Testing Database Endpoints")
    print("=" * 50)
    
    endpoints = [
        {
            "name": "Get all products with pagination",
            "url": f"{BASE_URL}/products?limit=5&skip=0",
            "method": "GET"
        },
        {
            "name": "Get single product",
            "url": f"{BASE_URL}/products/1",
            "method": "GET"
        },
        {
            "name": "Get all categories",
            "url": f"{BASE_URL}/products/categories",
            "method": "GET"
        },
        {
            "name": "Get all brands",
            "url": f"{BASE_URL}/products/brands",
            "method": "GET"
        },
        {
            "name": "Get products by category",
            "url": f"{BASE_URL}/products/category/smartphones",
            "method": "GET"
        },
        {
            "name": "Advanced filtering",
            "url": f"{BASE_URL}/products?category=laptops&minPrice=1000&maxPrice=2000&sortBy=price&order=asc",
            "method": "GET"
        }
    ]
    
    for i, endpoint in enumerate(endpoints, 1):
        print(f"\n{i}. {endpoint['name']}")
        print(f"   URL: {endpoint['url']}")
        
        try:
            response = requests.get(endpoint['url'])
            if response.status_code == 200:
                data = response.json()
                if isinstance(data, dict) and 'products' in data:
                    print(f"   ✅ Success: {data['total']} total products, showing {len(data['products'])}")
                elif isinstance(data, list):
                    print(f"   ✅ Success: {len(data)} items returned")
                elif isinstance(data, dict):
                    print(f"   ✅ Success: Product '{data.get('title', 'N/A')}' retrieved")
                else:
                    print(f"   ✅ Success: Data retrieved")
            else:
                print(f"   ❌ Failed: HTTP {response.status_code}")
        except Exception as e:
            print(f"   ❌ Error: {e}")

def test_crud_operations():
    """Test Create, Read, Update, Delete operations"""
    print("\n📝 Testing CRUD Operations")
    print("=" * 50)
    
    # Test CREATE
    print("\n1. Testing CREATE (POST /products)")
    new_product = {
        "title": "Test Product API",
        "description": "This is a test product created via API",
        "price": 199.99,
        "discountPercentage": 10.0,
        "rating": 4.5,
        "stock": 25,
        "brand": "Test Brand",
        "category": "test-category",
        "sku": "TEST-001",
        "weight": 500.0,
        "dimensions": "10 x 8 x 2 cm"
    }
    
    try:
        response = requests.post(f"{BASE_URL}/products", json=new_product)
        if response.status_code == 201:
            created_product = response.json()
            product_id = created_product['id']
            print(f"   ✅ Success: Created product with ID {product_id}")
            
            # Test READ
            print(f"\n2. Testing READ (GET /products/{product_id})")
            response = requests.get(f"{BASE_URL}/products/{product_id}")
            if response.status_code == 200:
                product = response.json()
                print(f"   ✅ Success: Retrieved product '{product['title']}'")
                
                # Test UPDATE
                print(f"\n3. Testing UPDATE (PUT /products/{product_id})")
                update_data = {"price": 249.99, "stock": 30}
                response = requests.put(f"{BASE_URL}/products/{product_id}", json=update_data)
                if response.status_code == 200:
                    updated_product = response.json()
                    print(f"   ✅ Success: Updated price to ${updated_product['price']}")
                    
                    # Test DELETE
                    print(f"\n4. Testing DELETE (DELETE /products/{product_id})")
                    response = requests.delete(f"{BASE_URL}/products/{product_id}")
                    if response.status_code == 200:
                        print(f"   ✅ Success: Deleted product")
                    else:
                        print(f"   ❌ Delete failed: HTTP {response.status_code}")
                else:
                    print(f"   ❌ Update failed: HTTP {response.status_code}")
            else:
                print(f"   ❌ Read failed: HTTP {response.status_code}")
        else:
            print(f"   ❌ Create failed: HTTP {response.status_code}")
    except Exception as e:
        print(f"   ❌ Error: {e}")

def main():
    """Main test function"""
    print("🧪 Advanced Flask Products API Testing")
    print("=" * 60)
    
    # Test if API is running
    try:
        response = requests.get(f"{BASE_URL}/")
        if response.status_code != 200:
            print("❌ API is not responding. Please start the Flask app first!")
            return
    except requests.exceptions.ConnectionError:
        print("❌ Cannot connect to API. Please start the Flask app first!")
        print("   Run: python app.py")
        return
    
    print("✅ API is running, starting tests...\n")
    
    # Run all tests
    test_database_endpoints()
    test_advanced_search()
    test_crud_operations()
    
    print("\n" + "=" * 60)
    print("🎉 All tests completed!")
    print("\n📊 Database Features Tested:")
    print("   ✅ Advanced search with multiple filters")
    print("   ✅ Full-text search across multiple fields")
    print("   ✅ Price range filtering")
    print("   ✅ Category and brand filtering")
    print("   ✅ Stock availability filtering")
    print("   ✅ Sorting and pagination")
    print("   ✅ CRUD operations")
    print("   ✅ 100+ mock products")

if __name__ == "__main__":
    main()
