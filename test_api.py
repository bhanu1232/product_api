import requests
import json

# Base URL for the API
BASE_URL = "http://localhost:5000"

def test_api_endpoints():
    """Test all API endpoints"""
    print("🧪 Testing Flask Products API...")
    print("="*50)
    
    # Test 1: Get all products
    print("1. Testing GET /products")
    try:
        response = requests.get(f"{BASE_URL}/products")
        if response.status_code == 200:
            data = response.json()
            print(f"   ✅ Success: Found {data['total']} products")
        else:
            print(f"   ❌ Failed: {response.status_code}")
    except requests.exceptions.ConnectionError:
        print("   ❌ Connection failed. Make sure the Flask app is running!")
        return
    
    # Test 2: Get single product
    print("2. Testing GET /products/1")
    try:
        response = requests.get(f"{BASE_URL}/products/1")
        if response.status_code == 200:
            data = response.json()
            print(f"   ✅ Success: Got product '{data['title']}'")
        else:
            print(f"   ❌ Failed: {response.status_code}")
    except Exception as e:
        print(f"   ❌ Error: {e}")
    
    # Test 3: Search products
    print("3. Testing GET /products/search?q=phone")
    try:
        response = requests.get(f"{BASE_URL}/products/search?q=phone")
        if response.status_code == 200:
            data = response.json()
            print(f"   ✅ Success: Found {data['total']} products matching 'phone'")
        else:
            print(f"   ❌ Failed: {response.status_code}")
    except Exception as e:
        print(f"   ❌ Error: {e}")
    
    # Test 4: Get categories
    print("4. Testing GET /products/categories")
    try:
        response = requests.get(f"{BASE_URL}/products/categories")
        if response.status_code == 200:
            categories = response.json()
            print(f"   ✅ Success: Found {len(categories)} categories: {', '.join(categories)}")
        else:
            print(f"   ❌ Failed: {response.status_code}")
    except Exception as e:
        print(f"   ❌ Error: {e}")
    
    # Test 5: Get products by category
    print("5. Testing GET /products/category/smartphones")
    try:
        response = requests.get(f"{BASE_URL}/products/category/smartphones")
        if response.status_code == 200:
            data = response.json()
            print(f"   ✅ Success: Found {data['total']} smartphones")
        else:
            print(f"   ❌ Failed: {response.status_code}")
    except Exception as e:
        print(f"   ❌ Error: {e}")
    
    # Test 6: Add new product
    print("6. Testing POST /products")
    try:
        new_product = {
            "title": "Test Product",
            "description": "This is a test product",
            "price": 99.99,
            "discountPercentage": 5.0,
            "rating": 4.5,
            "stock": 10,
            "brand": "Test Brand",
            "category": "test",
            "thumbnail": "https://example.com/test.jpg",
            "images": ["https://example.com/test1.jpg"]
        }
        
        response = requests.post(f"{BASE_URL}/products", json=new_product)
        if response.status_code == 201:
            data = response.json()
            print(f"   ✅ Success: Created product with ID {data['id']}")
        else:
            print(f"   ❌ Failed: {response.status_code}")
    except Exception as e:
        print(f"   ❌ Error: {e}")
    
    print("\n" + "="*50)
    print("🎉 API testing completed!")

if __name__ == "__main__":
    test_api_endpoints()
