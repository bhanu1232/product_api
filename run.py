import subprocess
import sys
import os

def install_requirements():
    """Install required packages"""
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"])
        print("✅ Requirements installed successfully!")
    except subprocess.CalledProcessError as e:
        print(f"❌ Error installing requirements: {e}")
        return False
    return True

def run_flask_app():
    """Run the Flask application"""
    try:
        print("🚀 Starting Flask Products API...")
        print("📍 API will be available at: http://localhost:5000")
        print("📋 Available endpoints:")
        print("   GET  /products - Get all products")
        print("   GET  /products/{id} - Get single product")
        print("   GET  /products/search?q={query} - Search products")
        print("   GET  /products/categories - Get all categories")
        print("   GET  /products/category/{category} - Get products by category")
        print("   POST /products - Add new product")
        print("   PUT  /products/{id} - Update product")
        print("   DELETE /products/{id} - Delete product")
        print("\n" + "="*50)
        
        # Import and run the Flask app
        from app import app
        app.run(debug=True, host='0.0.0.0', port=5000)
        
    except Exception as e:
        print(f"❌ Error running Flask app: {e}")

if __name__ == "__main__":
    print("🔧 Setting up Flask Products API...")
    
    if install_requirements():
        run_flask_app()
    else:
        print("❌ Setup failed. Please check the error messages above.")
