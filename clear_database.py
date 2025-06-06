import os
import psycopg2
from psycopg2 import sql

# Database connection details
DB_CONFIG = {
    'host': 'dpg-d1191sidbo4c739pelk0-a.oregon-postgres.render.com',
    'database': 'products_qnmx',
    'user': 'products_qnmx_user',
    'password': 'PYbv6akp0SOprUqCqgMVU27wpcf9L2sF',
    'port': 5432
}

def clear_all_products():
    """Clear all products from the database but keep the table structure"""
    print("🗑️ Clearing all products from the database...")
    
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
        
        # Check how many products exist before deletion
        cursor.execute("SELECT COUNT(*) FROM products;")
        count_before = cursor.fetchone()[0]
        print(f"📊 Current product count: {count_before}")
        
        # Delete all products
        cursor.execute("DELETE FROM products;")
        
        # Reset the ID sequence to start from 1 again
        cursor.execute("ALTER SEQUENCE products_id_seq RESTART WITH 1;")
        
        # Commit the changes
        conn.commit()
        
        # Verify deletion
        cursor.execute("SELECT COUNT(*) FROM products;")
        count_after = cursor.fetchone()[0]
        
        print(f"✅ Successfully deleted {count_before} products")
        print(f"📊 Current product count: {count_after}")
        
        # Close cursor and connection
        cursor.close()
        conn.close()
        
        return True
        
    except Exception as e:
        print(f"❌ Error clearing database: {e}")
        return False

def verify_empty_database():
    """Verify that the database is empty and ready for new data"""
    print("\n🔍 Verifying empty database...")
    
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
        
        if count == 0:
            print("✅ Database is empty and ready for your data")
        else:
            print(f"⚠️ Database still contains {count} products")
        
        # Check table structure
        cursor.execute("""
            SELECT column_name, data_type 
            FROM information_schema.columns
            WHERE table_name = 'products'
            ORDER BY ordinal_position;
        """)
        
        columns = cursor.fetchall()
        print(f"\n📋 Table structure preserved with {len(columns)} columns:")
        for i, (column, data_type) in enumerate(columns[:10], 1):
            print(f"   {i}. {column} ({data_type})")
        
        if len(columns) > 10:
            print(f"   ... and {len(columns) - 10} more columns")
        
        # Close cursor and connection
        cursor.close()
        conn.close()
        
        return count == 0
        
    except Exception as e:
        print(f"❌ Error verifying database: {e}")
        return False

def main():
    """Main function to clear the database"""
    print("🗑️ Database Cleanup Tool")
    print("=" * 50)
    print("This script will remove ALL mock data from your database.")
    print("Only data you add manually through the API will remain.")
    print("=" * 50)
    
    # Confirm before proceeding
    confirm = input("Are you sure you want to delete ALL products? (yes/no): ")
    if confirm.lower() != "yes":
        print("❌ Operation cancelled")
        return
    
    # Clear the database
    if clear_all_products():
        # Verify the database is empty
        verify_empty_database()
        
        print("\n" + "=" * 50)
        print("🎉 Database successfully cleared!")
        print("\n📝 Next steps:")
        print("1. Start your Flask API: python app.py")
        print("2. Add new products using the API endpoints:")
        print("   - POST /products")
        print("   - POST /product/create")
        print("3. Retrieve your products:")
        print("   - GET /products")
        print("   - GET /product/{id}")
    else:
        print("\n❌ Failed to clear the database")

if __name__ == "__main__":
    main()
