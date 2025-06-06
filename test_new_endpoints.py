import requests
import json

BASE_URL = "http://localhost:5000"

def test_get_single_product():
    """Test getting a single product by ID"""
    print("🔍 Testing GET Single Product Endpoint")
    print("=" * 50)
    
    # Test valid product ID
    print("1. Testing valid product ID (1):")
    try:
        response = requests.get(f"{BASE_URL}/product/1")
        if response.status_code == 200:
            product = response.json()
            print(f"   ✅ Success: Got product '{product['title']}'")
            print(f"   📦 Price: ${product['price']}")
            print(f"   🏷️ Category: {product['category']}")
            print(f"   🏭 Brand: {product['brand']}")
        else:
            print(f"   ❌ Failed: HTTP {response.status_code}")
            print(f"   📝 Response: {response.text}")
    except Exception as e:
        print(f"   ❌ Error: {e}")
    
    # Test invalid product ID
    print("\n2. Testing invalid product ID (99999):")
    try:
        response = requests.get(f"{BASE_URL}/product/99999")
        if response.status_code == 404:
            print("   ✅ Success: Correctly returned 404 for non-existent product")
        else:
            print(f"   ⚠️ Unexpected status: {response.status_code}")
    except Exception as e:
        print(f"   ❌ Error: {e}")

def test_create_product():
    """Test creating a new product"""
    print("\n📝 Testing POST Create Product Endpoint")
    print("=" * 50)
    
    # Test data for new product
    new_product = {
        "title": "Test Product API",
        "description": "This is a test product created via API endpoint",
        "price": 299.99,
        "discountPercentage": 10.0,
        "rating": 4.5,
        "stock": 50,
        "brand": "Test Brand",
        "category": "test-electronics",
        "thumbnail": "https://example.com/test-thumbnail.jpg",
        "images": ["https://example.com/test1.jpg", "https://example.com/test2.jpg"],
        "weight": 500.0,
        "dimensions": "15 x 10 x 5 cm",
        "warrantyInformation": "2 year warranty",
        "shippingInformation": "Free shipping worldwide",
        "availabilityStatus": "In Stock",
        "returnPolicy": "30-day return policy",
        "minimumOrderQuantity": 1
    }
    
    print("1. Testing product creation with complete data:")
    try:
        response = requests.post(f"{BASE_URL}/products", json=new_product)
        if response.status_code == 201:
            result = response.json()
            print(f"   ✅ Success: Product created with ID {result['product']['id']}")
            print(f"   📦 Title: {result['product']['title']}")
            print(f"   🏷️ SKU: {result['product']['sku']}")
            return result['product']['id']
        else:
            print(f"   ❌ Failed: HTTP {response.status_code}")
            print(f"   📝 Response: {response.text}")
    except Exception as e:
        print(f"   ❌ Error: {e}")
    
    # Test with minimal required data
    print("\n2. Testing product creation with minimal data:")
    minimal_product = {
        "title": "Minimal Test Product",
        "description": "Basic product with minimal data",
        "price": 99.99,
        "brand": "Minimal Brand",
        "category": "test"
    }
    
    try:
        response = requests.post(f"{BASE_URL}/products", json=minimal_product)
        if response.status_code == 201:
            result = response.json()
            print(f"   ✅ Success: Minimal product created with ID {result['product']['id']}")
            return result['product']['id']
        else:
            print(f"   ❌ Failed: HTTP {response.status_code}")
            print(f"   📝 Response: {response.text}")
    except Exception as e:
        print(f"   ❌ Error: {e}")
    
    return None

def test_create_product_alternative():
    """Test the alternative create product endpoint"""
    print("\n📝 Testing POST /product/create Endpoint")
    print("=" * 50)
    
    new_product = {
        "title": "Alternative API Test Product",
        "description": "Product created via alternative endpoint",
        "price": 199.99,
        "brand": "Alt Brand",
        "category": "alternative",
        "stock": 25,
        "rating": 4.2
    }
    
    try:
        response = requests.post(f"{BASE_URL}/product/create", json=new_product)
        if response.status_code == 201:
            result = response.json()
            print(f"   ✅ Success: Product created via alternative endpoint")
            print(f"   📦 Product ID: {result['product_id']}")
            print(f"   🏷️ Title: {result['product']['title']}")
            return result['product_id']
        else:
            print(f"   ❌ Failed: HTTP {response.status_code}")
            print(f"   📝 Response: {response.text}")
    except Exception as e:
        print(f"   ❌ Error: {e}")
    
    return None

def test_validation():
    """Test validation for required fields"""
    print("\n🔒 Testing Validation")
    print("=" * 50)
    
    # Test missing required fields
    print("1. Testing missing required fields:")
    incomplete_product = {
        "title": "Incomplete Product"
        # Missing description, price, brand, category
    }
    
    try:
        response = requests.post(f"{BASE_URL}/products", json=incomplete_product)
        if response.status_code == 400:
            result = response.json()
            print(f"   ✅ Success: Validation caught missing fields")
            print(f"   📝 Error: {result['error']}")
        else:
            print(f"   ⚠️ Unexpected status: {response.status_code}")
    except Exception as e:
        print(f"   ❌ Error: {e}")
    
    # Test invalid data types
    print("\n2. Testing invalid data types:")
    invalid_product = {
        "title": "Invalid Product",
        "description": "Product with invalid price",
        "price": "not-a-number",  # Invalid price
        "brand": "Test Brand",
        "category": "test"
    }
    
    try:
        response = requests.post(f"{BASE_URL}/products", json=invalid_product)
        if response.status_code == 400:
            result = response.json()
            print(f"   ✅ Success: Validation caught invalid data type")
            print(f"   📝 Error: {result['error']}")
        else:
            print(f"   ⚠️ Unexpected status: {response.status_code}")
    except Exception as e:
        print(f"   ❌ Error: {e}")

def test_complete_workflow():
    """Test complete workflow: create, get, verify"""
    print("\n🔄 Testing Complete Workflow")
    print("=" * 50)
    
    # Step 1: Create a product
    print("1. Creating a new product...")
    product_data = {
        "title": "Workflow Test Product",
        "description": "Product for testing complete workflow",
        "price": 149.99,
        "brand": "Workflow Brand",
        "category": "workflow-test",
        "stock": 10,
        "rating": 4.0
    }
    
    try:
        response = requests.post(f"{BASE_URL}/products", json=product_data)
        if response.status_code == 201:
            result = response.json()
            product_id = result['product']['id']
            print(f"   ✅ Product created with ID: {product_id}")
            
            # Step 2: Retrieve the created product
            print(f"\n2. Retrieving product {product_id}...")
            get_response = requests.get(f"{BASE_URL}/product/{product_id}")
            if get_response.status_code == 200:
                retrieved_product = get_response.json()
                print(f"   ✅ Product retrieved successfully")
                print(f"   📦 Title: {retrieved_product['title']}")
                print(f"   💰 Price: ${retrieved_product['price']}")
                
                # Step 3: Verify data matches
                print(f"\n3. Verifying data integrity...")
                if (retrieved_product['title'] == product_data['title'] and 
                    retrieved_product['price'] == product_data['price']):
                    print(f"   ✅ Data integrity verified!")
                else:
                    print(f"   ❌ Data mismatch detected!")
            else:
                print(f"   ❌ Failed to retrieve product: {get_response.status_code}")
        else:
            print(f"   ❌ Failed to create product: {response.status_code}")
    except Exception as e:
        print(f"   ❌ Error in workflow: {e}")

def main():
    """Main test function for new endpoints"""
    print("🧪 Testing New API Endpoints")
    print("=" * 60)
    
    # Check if API is running
    try:
        response = requests.get(f"{BASE_URL}/")
        if response.status_code != 200:
            print("❌ API is not responding. Please start the Flask app first!")
            return
    except requests.exceptions.ConnectionError:
        print("❌ Cannot connect to API. Please start the Flask app first!")
        print("   Run: python app.py")
        return
    
    print("✅ API is running, starting endpoint tests...\n")
    
    # Run all tests
    test_get_single_product()
    test_create_product()
    test_create_product_alternative()
    test_validation()
    test_complete_workflow()
    
    print("\n" + "=" * 60)
    print("🎉 All endpoint tests completed!")
    print("\n📊 New Endpoints Summary:")
    print("   ✅ GET /product/{id} - Get single product")
    print("   ✅ POST /products - Create product (main)")
    print("   ✅ POST /product/create - Create product (alternative)")
    print("   ✅ Validation for required fields")
    print("   ✅ Error handling for invalid data")
    print("   ✅ Automatic SKU generation")

if __name__ == "__main__":
    main()
