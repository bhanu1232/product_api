import os
import subprocess
import sys

def setup_environment():
    """Setup environment variables for PostgreSQL"""
    os.environ['DATABASE_URL'] = 'postgresql://products_qnmx_user:PYbv6akp0SOprUqCqgMVU27wpcf9L2sF@dpg-d1191sidbo4c739pelk0-a.oregon-postgres.render.com/products_qnmx'
    print("✅ Environment variables set for PostgreSQL")

def run_flask_app():
    """Run the Flask application with PostgreSQL"""
    try:
        print("🚀 Starting Flask Products API with PostgreSQL...")
        print("🐘 Database: PostgreSQL on Render")
        print("📍 API will be available at: http://localhost:5000")
        print("\n📋 Available endpoints:")
        print("   GET  / - API information")
        print("   GET  /products - Get all products (with filters)")
        print("   GET  /products/{id} - Get single product")
        print("   GET  /products/search - Advanced search")
        print("   GET  /products/categories - Get all categories")
        print("   GET  /products/brands - Get all brands")
        print("   GET  /products/category/{category} - Get products by category")
        print("   POST /products - Add new product")
        print("   PUT  /products/{id} - Update product")
        print("   DELETE /products/{id} - Delete product")
        print("\n🔍 Advanced Search Examples:")
        print("   /products/search?q=iPhone")
        print("   /products/search?category=smartphones&minPrice=500&maxPrice=1500")
        print("   /products/search?brand=Apple&sortBy=price&order=desc")
        print("\n" + "="*70)
        
        # Import and run the Flask app
        from app import app
        app.run(debug=True, host='0.0.0.0', port=5000)
        
    except Exception as e:
        print(f"❌ Error running Flask app: {e}")

def main():
    """Main function to run the PostgreSQL-powered Flask app"""
    print("🐘 Flask Products API - PostgreSQL Edition")
    print("=" * 60)
    
    # Setup environment
    setup_environment()
    
    # Run the app
    run_flask_app()

if __name__ == "__main__":
    main()
