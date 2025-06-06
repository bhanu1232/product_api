import requests
import json
import sys

def add_sample_product(api_url=None):
    """Add a sample product to the API"""
    print("📦 Add Sample Product Tool")
    print("=" * 50)
    
    # Get API URL if not provided
    if not api_url:
        api_url = input("Enter API URL (default: http://localhost:5000): ")
        if not api_url:
            api_url = "http://localhost:5000"
    
    if not api_url.startswith("http"):
        api_url = f"https://{api_url}"
    
    # Sample product data
    sample_product = {
        "title": "Sample Smartphone",
        "description": "A high-quality smartphone with advanced features",
        "price": 699.99,
        "discountPercentage": 10.0,
        "rating": 4.5,
        "stock": 50,
        "brand": "TechBrand",
        "category": "smartphones",
        "thumbnail": "https://example.com/smartphone-thumbnail.jpg",
        "images": [
            "https://example.com/smartphone-1.jpg",
            "https://example.com/smartphone-2.jpg",
            "https://example.com/smartphone-3.jpg"
        ],
        "weight": 180.0,
        "dimensions": "15 x 7 x 0.8 cm",
        "warrantyInformation": "1 year manufacturer warranty",
        "shippingInformation": "Free shipping",
        "availabilityStatus": "In Stock",
        "returnPolicy": "30-day return policy",
        "minimumOrderQuantity": 1
    }
    
    # Allow customization
    customize = input("Do you want to customize the sample product? (yes/no): ")
    if customize.lower() == "yes":
        sample_product["title"] = input(f"Title (default: {sample_product['title']}): ") or sample_product["title"]
        sample_product["price"] = float(input(f"Price (default: {sample_product['price']}): ") or sample_product["price"])
        sample_product["brand"] = input(f"Brand (default: {sample_product['brand']}): ") or sample_product["brand"]
        sample_product["category"] = input(f"Category (default: {sample_product['category']}): ") or sample_product["category"]
    
    # Send request
    try:
        print(f"\n📤 Sending POST request to {api_url}/products")
        response = requests.post(f"{api_url}/products", json=sample_product)
        
        if response.status_code == 201:
            result = response.json()
            product_id = result['product']['id']
            print(f"✅ Sample product created successfully!")
            print(f"📊 Product details:")
            print(f"   ID: {product_id}")
            print(f"   Title: {result['product']['title']}")
            print(f"   Price: ${result['product']['price']}")
            print(f"   Brand: {result['product']['brand']}")
            print(f"   Category: {result['product']['category']}")
            print(f"   SKU: {result['product']['sku']}")
            
            # Verify product was added
            print(f"\n📥 Verifying product was added...")
            get_response = requests.get(f"{api_url}/product/{product_id}")
            
            if get_response.status_code == 200:
                print(f"✅ Successfully verified product in database")
                
                # Check all products
                all_response = requests.get(f"{api_url}/products")
                if all_response.status_code == 200:
                    all_data = all_response.json()
                    print(f"\n📊 Total products in database: {all_data['total']}")
            else:
                print(f"❌ Failed to verify product: {get_response.status_code}")
            
            return product_id
        else:
            print(f"❌ Failed to create product: {response.status_code}")
            print(f"📝 Response: {response.text}")
    except Exception as e:
        print(f"❌ Error: {e}")
    
    return None

def add_multiple_products(api_url=None, count=5):
    """Add multiple sample products"""
    print(f"\n📦 Adding {count} Sample Products")
    print("=" * 50)
    
    # Get API URL if not provided
    if not api_url:
        api_url = input("Enter API URL (default: http://localhost:5000): ")
        if not api_url:
            api_url = "http://localhost:5000"
    
    if not api_url.startswith("http"):
        api_url = f"https://{api_url}"
    
    # Product categories
    categories = ["smartphones", "laptops", "tablets", "headphones", "cameras", "smartwatches", "speakers"]
    brands = ["TechBrand", "ElectroMax", "GadgetPro", "SmartTech", "InnovateTech", "FutureTech", "PrimeTech"]
    
    # Add products
    successful = 0
    product_ids = []
    
    for i in range(count):
        try:
            # Create product data
            import random
            category = random.choice(categories)
            brand = random.choice(brands)
            price = round(random.uniform(99.99, 1999.99), 2)
            stock = random.randint(5, 100)
            rating = round(random.uniform(3.0, 5.0), 1)
            
            product_data = {
                "title": f"{brand} {category.title()} {i+1}",
                "description": f"A high-quality {category} from {brand} with advanced features",
                "price": price,
                "discountPercentage": round(random.uniform(0, 20), 1),
                "rating": rating,
                "stock": stock,
                "brand": brand,
                "category": category,
                "thumbnail": f"https://example.com/{category}-thumbnail.jpg",
                "images": [
                    f"https://example.com/{category}-1.jpg",
                    f"https://example.com/{category}-2.jpg"
                ]
            }
            
            # Send request
            print(f"\n📤 Creating product {i+1}/{count}: {product_data['title']}")
            response = requests.post(f"{api_url}/products", json=product_data)
            
            if response.status_code == 201:
                result = response.json()
                product_id = result['product']['id']
                product_ids.append(product_id)
                print(f"✅ Created product ID: {product_id}")
                successful += 1
            else:
                print(f"❌ Failed: {response.status_code}")
        except Exception as e:
            print(f"❌ Error: {e}")
    
    print(f"\n🎉 Successfully created {successful}/{count} products")
    
    # Verify products
    if successful > 0:
        try:
            all_response = requests.get(f"{api_url}/products")
            if all_response.status_code == 200:
                all_data = all_response.json()
                print(f"\n📊 Total products in database: {all_data['total']}")
        except Exception as e:
            print(f"❌ Error checking total products: {e}")
    
    return product_ids

def main():
    """Main function"""
    print("🚀 Product Creation Tool")
    print("=" * 60)
    
    # Check if API URL was provided as argument
    api_url = sys.argv[1] if len(sys.argv) > 1 else None
    
    # Ask what to do
    print("What would you like to do?")
    print("1. Add a single sample product")
    print("2. Add multiple sample products")
    choice = input("Enter choice (1 or 2): ")
    
    if choice == "1":
        add_sample_product(api_url)
    elif choice == "2":
        count = int(input("How many products do you want to add? (default: 5): ") or "5")
        add_multiple_products(api_url, count)
    else:
        print("❌ Invalid choice")
    
    print("\n" + "=" * 60)
    print("🎉 Done!")

if __name__ == "__main__":
    main()
