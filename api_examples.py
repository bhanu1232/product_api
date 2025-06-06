import requests
import json

def show_api_examples():
    """Show practical examples of using the API endpoints"""
    print("📚 API Usage Examples")
    print("=" * 60)
    
    # Replace with your actual API URL
    API_URL = "https://your-api-url.onrender.com"  # Update this!
    LOCAL_URL = "http://localhost:5000"
    
    print(f"🔗 API URL: {API_URL}")
    print(f"🏠 Local URL: {LOCAL_URL}")
    
    print("\n1️⃣ GET Single Product")
    print("=" * 30)
    print("📋 Endpoint: GET /product/{id}")
    print("🌐 URL Examples:")
    print(f"   {API_URL}/product/1")
    print(f"   {API_URL}/product/5")
    print(f"   {API_URL}/product/10")
    
    print("\n📝 JavaScript Example:")
    print("""
    fetch('https://your-api-url.onrender.com/product/1')
      .then(response => response.json())
      .then(product => {
        console.log('Product:', product.title);
        console.log('Price:', product.price);
        console.log('Category:', product.category);
      })
      .catch(error => console.error('Error:', error));
    """)
    
    print("\n📝 Python Example:")
    print("""
    import requests
    
    response = requests.get('https://your-api-url.onrender.com/product/1')
    if response.status_code == 200:
        product = response.json()
        print(f"Product: {product['title']}")
        print(f"Price: ${product['price']}")
    else:
        print(f"Error: {response.status_code}")
    """)
    
    print("\n📝 curl Example:")
    print(f"   curl {API_URL}/product/1")
    
    print("\n2️⃣ CREATE New Product")
    print("=" * 30)
    print("📋 Endpoint: POST /products")
    print("📋 Alternative: POST /product/create")
    
    print("\n📝 JavaScript Example:")
    print("""
    const newProduct = {
      title: "Amazing Smartphone",
      description: "Latest smartphone with advanced features",
      price: 699.99,
      brand: "TechBrand",
      category: "smartphones",
      stock: 50,
      rating: 4.5,
      discountPercentage: 10,
      images: [
        "https://example.com/phone1.jpg",
        "https://example.com/phone2.jpg"
      ],
      warrantyInformation: "2 year warranty",
      shippingInformation: "Free shipping"
    };
    
    fetch('https://your-api-url.onrender.com/products', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify(newProduct)
    })
    .then(response => response.json())
    .then(result => {
      console.log('Product created:', result.product.id);
      console.log('SKU:', result.product.sku);
    })
    .catch(error => console.error('Error:', error));
    """)
    
    print("\n📝 Python Example:")
    print("""
    import requests
    
    new_product = {
        "title": "Amazing Laptop",
        "description": "High-performance laptop for professionals",
        "price": 1299.99,
        "brand": "LaptopBrand",
        "category": "laptops",
        "stock": 25,
        "rating": 4.7
    }
    
    response = requests.post(
        'https://your-api-url.onrender.com/products',
        json=new_product
    )
    
    if response.status_code == 201:
        result = response.json()
        print(f"Product created with ID: {result['product']['id']}")
    else:
        print(f"Error: {response.status_code} - {response.text}")
    """)
    
    print("\n📝 curl Example:")
    print(f"""
    curl -X POST {API_URL}/products \\
      -H "Content-Type: application/json" \\
      -d '{{
        "title": "Test Product",
        "description": "A test product",
        "price": 99.99,
        "brand": "TestBrand",
        "category": "test"
      }}'
    """)
    
    print("\n3️⃣ Required Fields for Creating Products")
    print("=" * 45)
    print("✅ Required Fields:")
    print("   • title (string)")
    print("   • description (string)")
    print("   • price (number)")
    print("   • brand (string)")
    print("   • category (string)")
    
    print("\n🔧 Optional Fields:")
    print("   • discountPercentage (number)")
    print("   • rating (number)")
    print("   • stock (number)")
    print("   • thumbnail (string)")
    print("   • images (array)")
    print("   • sku (string - auto-generated if not provided)")
    print("   • weight (number)")
    print("   • dimensions (string)")
    print("   • warrantyInformation (string)")
    print("   • shippingInformation (string)")
    print("   • availabilityStatus (string)")
    print("   • returnPolicy (string)")
    print("   • minimumOrderQuantity (number)")
    
    print("\n4️⃣ Error Handling")
    print("=" * 20)
    print("📋 Common HTTP Status Codes:")
    print("   • 200 - Success (GET)")
    print("   • 201 - Created (POST)")
    print("   • 400 - Bad Request (missing/invalid data)")
    print("   • 404 - Not Found (product doesn't exist)")
    print("   • 500 - Server Error")
    
    print("\n📝 Error Response Example:")
    print("""
    {
      "error": "Missing required fields: title, price",
      "required_fields": ["title", "description", "price", "brand", "category"],
      "provided_fields": ["description", "brand", "category"]
    }
    """)
    
    print("\n5️⃣ Complete API Endpoints")
    print("=" * 30)
    endpoints = [
        ("GET", "/", "API information"),
        ("GET", "/products", "Get all products (with filters)"),
        ("GET", "/product/{id}", "Get single product"),
        ("POST", "/products", "Create new product"),
        ("POST", "/product/create", "Create new product (alternative)"),
        ("PUT", "/products/{id}", "Update product"),
        ("DELETE", "/products/{id}", "Delete product"),
        ("GET", "/products/search", "Search products"),
        ("GET", "/products/categories", "Get all categories"),
        ("GET", "/products/brands", "Get all brands"),
        ("GET", "/products/category/{category}", "Get products by category")
    ]
    
    for method, endpoint, description in endpoints:
        print(f"   {method:6} {endpoint:25} - {description}")

def test_live_api():
    """Test if the API is accessible"""
    print("\n🧪 Testing API Accessibility")
    print("=" * 40)
    
    # Test local first
    try:
        response = requests.get("http://localhost:5000/", timeout=5)
        if response.status_code == 200:
            print("✅ Local API (localhost:5000) is running")
        else:
            print(f"⚠️ Local API returned status: {response.status_code}")
    except:
        print("❌ Local API is not running")
    
    # Prompt for live API URL
    live_url = input("\n🌐 Enter your live API URL (or press Enter to skip): ")
    if live_url:
        try:
            if not live_url.startswith('http'):
                live_url = 'https://' + live_url
            
            response = requests.get(live_url, timeout=10)
            if response.status_code == 200:
                print(f"✅ Live API ({live_url}) is accessible")
                data = response.json()
                print(f"📊 API Version: {data.get('version', 'Unknown')}")
            else:
                print(f"⚠️ Live API returned status: {response.status_code}")
        except Exception as e:
            print(f"❌ Cannot access live API: {e}")

def main():
    """Main function to show API examples"""
    show_api_examples()
    test_live_api()
    
    print("\n" + "=" * 60)
    print("🎉 API Examples Complete!")
    print("\n📝 Next Steps:")
    print("1. Deploy your API to get a live URL")
    print("2. Replace 'your-api-url.onrender.com' with your actual URL")
    print("3. Test the endpoints using the examples above")
    print("4. Integrate with your frontend application")

if __name__ == "__main__":
    main()
