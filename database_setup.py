import os
import subprocess
import sys

def install_requirements():
    """Install required packages"""
    print("📦 Installing requirements...")
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"])
        print("✅ Requirements installed successfully!")
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ Error installing requirements: {e}")
        return False

def setup_database():
    """Setup and initialize the database"""
    print("🗄️ Setting up database...")
    
    try:
        from app import app, db
        
        with app.app_context():
            # Create all tables
            db.create_all()
            print("✅ Database tables created successfully!")
            
            # Check if we need to seed data
            from database import Product
            product_count = Product.query.count()
            
            if product_count == 0:
                print("📊 Database is empty, running seed script...")
                exec(open('seed_database.py').read())
            else:
                print(f"📊 Database already contains {product_count} products")
                
        return True
        
    except Exception as e:
        print(f"❌ Error setting up database: {e}")
        return False

def main():
    """Main setup function"""
    print("🚀 Flask Products Database API Setup")
    print("=" * 50)
    
    # Step 1: Install requirements
    if not install_requirements():
        return
    
    # Step 2: Setup database
    if not setup_database():
        return
    
    print("\n🎉 Setup completed successfully!")
    print("\n📋 Next steps:")
    print("1. Run the Flask app: python app.py")
    print("2. Test the API: python test_advanced_api.py")
    print("3. Access API at: http://localhost:5000")
    print("\n🔍 Database location: products.db (SQLite)")
    print("📊 Total products: 100+")
    print("🔎 Advanced search capabilities enabled")

if __name__ == "__main__":
    main()
