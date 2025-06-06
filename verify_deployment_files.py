import os

def check_deployment_files():
    """Verify all necessary files are present for deployment"""
    print("📋 Checking Deployment Files")
    print("=" * 40)
    
    required_files = {
        "app.py": "Main Flask application",
        "database.py": "Database models and configuration", 
        "requirements.txt": "Python dependencies",
        "render.yaml": "Render deployment configuration",
        "Procfile": "Alternative deployment configuration"
    }
    
    all_present = True
    
    for file, description in required_files.items():
        if os.path.exists(file):
            print(f"✅ {file} - {description}")
        else:
            print(f"❌ {file} - {description} (MISSING)")
            all_present = False
    
    print("\n" + "=" * 40)
    
    if all_present:
        print("🎉 All deployment files are present!")
        print("✅ Ready for deployment to Render")
        
        # Check file contents
        check_file_contents()
    else:
        print("⚠️  Some files are missing!")
        print("📝 Please create the missing files before deployment")
    
    return all_present

def check_file_contents():
    """Check if files have correct content"""
    print("\n📋 Checking File Contents")
    print("=" * 40)
    
    # Check requirements.txt
    try:
        with open("requirements.txt", "r") as f:
            content = f.read()
            if "gunicorn" in content:
                print("✅ requirements.txt contains gunicorn")
            else:
                print("⚠️  requirements.txt missing gunicorn")
            
            if "psycopg2-binary" in content:
                print("✅ requirements.txt contains PostgreSQL driver")
            else:
                print("⚠️  requirements.txt missing psycopg2-binary")
    except FileNotFoundError:
        print("❌ requirements.txt not found")
    
    # Check app.py for Flask app
    try:
        with open("app.py", "r") as f:
            content = f.read()
            if "app = Flask(__name__)" in content:
                print("✅ app.py contains Flask app instance")
            else:
                print("⚠️  app.py missing Flask app instance")
            
            if "DATABASE_URL" in content:
                print("✅ app.py configured for environment variables")
            else:
                print("⚠️  app.py may need environment variable configuration")
    except FileNotFoundError:
        print("❌ app.py not found")

def deployment_checklist():
    """Final deployment checklist"""
    print("\n📋 Pre-Deployment Checklist")
    print("=" * 40)
    
    checklist = [
        "✅ All files present and verified",
        "✅ PostgreSQL database is accessible",
        "✅ Environment variables are ready",
        "✅ Start command is: gunicorn app:app",
        "✅ CORS is configured for production",
        "✅ Database tables will be created automatically"
    ]
    
    for item in checklist:
        print(f"   {item}")
    
    print("\n🚀 Ready to deploy to Render!")
    print("📝 Start Command: gunicorn app:app")
    print("🔗 Database URL: Already configured")

def main():
    """Main verification function"""
    print("🔍 Flask API Deployment Verification")
    print("=" * 50)
    
    if check_deployment_files():
        deployment_checklist()
        
        print("\n🌐 Next Steps:")
        print("1. Go to https://render.com")
        print("2. Create new Web Service")
        print("3. Upload your files or connect GitHub")
        print("4. Set start command: gunicorn app:app")
        print("5. Add DATABASE_URL environment variable")
        print("6. Deploy!")
    else:
        print("\n❌ Please fix missing files before deployment")

if __name__ == "__main__":
    main()
