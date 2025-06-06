import os

def update_cors_configuration():
    """Update CORS configuration for production deployment"""
    print("🔒 Updating CORS configuration for production...")
    
    app_file = "app.py"
    
    if not os.path.exists(app_file):
        print(f"❌ {app_file} not found!")
        return False
    
    try:
        with open(app_file, "r") as file:
            content = file.read()
        
        # Check if CORS is already configured
        if "CORS(app)" in content:
            # Update CORS configuration
            updated_content = content.replace(
                "CORS(app)",
                "CORS(app, resources={r\"/*\": {\"origins\": \"*\"}})"
            )
            
            with open(app_file, "w") as file:
                file.write(updated_content)
            
            print("✅ CORS configuration updated for production")
            print("   This allows any origin to access your API")
            print("   For better security, you should restrict origins in production")
            
            return True
        else:
            print("⚠️ Could not find CORS configuration in app.py")
            print("   Please manually update your CORS configuration")
            return False
        
    except Exception as e:
        print(f"❌ Error updating CORS configuration: {e}")
        return False

if __name__ == "__main__":
    update_cors_configuration()
