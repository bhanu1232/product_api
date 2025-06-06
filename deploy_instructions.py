import webbrowser
import os

def render_deployment_guide():
    """Complete guide for deploying to Render"""
    print("🚀 Render Deployment Guide - Flask Products API")
    print("=" * 60)
    
    print("\n📋 Step 1: Prepare Your Files")
    print("   ✅ app.py (your main Flask application)")
    print("   ✅ database.py (your database models)")
    print("   ✅ requirements.txt (Python dependencies)")
    print("   ✅ render.yaml (Render configuration)")
    print("   ✅ Procfile (alternative deployment config)")
    
    print("\n📋 Step 2: Create Render Web Service")
    print("   1. Go to https://render.com")
    print("   2. Click 'New +' → 'Web Service'")
    print("   3. Connect your GitHub repo or upload files")
    
    print("\n📋 Step 3: Configure Service Settings")
    print("   • Name: products-api")
    print("   • Environment: Python")
    print("   • Build Command: pip install -r requirements.txt")
    print("   • Start Command: gunicorn app:app")
    print("   • Instance Type: Free (for testing)")
    
    print("\n📋 Step 4: Environment Variables")
    print("   Add this environment variable in Render:")
    print("   Key: DATABASE_URL")
    print("   Value: postgresql://products_qnmx_user:PYbv6akp0SOprUqCqgMVU27wpcf9L2sF@dpg-d1191sidbo4c739pelk0-a.oregon-postgres.render.com/products_qnmx")
    
    print("\n📋 Step 5: Deploy")
    print("   • Click 'Create Web Service'")
    print("   • Wait for build and deployment (5-10 minutes)")
    print("   • Your API will be live at: https://products-api-xxxx.onrender.com")
    
    print("\n🔗 Your API Endpoints Will Be:")
    print("   GET  https://your-url.onrender.com/")
    print("   GET  https://your-url.onrender.com/products")
    print("   GET  https://your-url.onrender.com/products/search?q=iPhone")
    print("   GET  https://your-url.onrender.com/products/categories")
    print("   POST https://your-url.onrender.com/products")
    
    print("\n⚠️  Important Notes:")
    print("   • Free tier may have cold starts (first request takes longer)")
    print("   • Service sleeps after 15 minutes of inactivity")
    print("   • Database connection is already configured")
    print("   • CORS is enabled for all origins")
    
    # Open Render
    open_render = input("\n🌐 Open Render website now? (y/n): ")
    if open_render.lower() == 'y':
        webbrowser.open("https://render.com")

def heroku_deployment_guide():
    """Alternative deployment guide for Heroku"""
    print("\n🔄 Alternative: Heroku Deployment")
    print("=" * 60)
    
    print("\n📋 Heroku CLI Commands:")
    print("   1. Install Heroku CLI")
    print("   2. heroku login")
    print("   3. heroku create products-api")
    print("   4. heroku config:set DATABASE_URL=postgresql://products_qnmx_user:PYbv6akp0SOprUqCqgMVU27wpcf9L2sF@dpg-d1191sidbo4c739pelk0-a.oregon-postgres.render.com/products_qnmx")
    print("   5. git push heroku main")
    
    print("\n🔗 Your Heroku URL: https://products-api.herokuapp.com")

def test_deployment():
    """Instructions for testing the deployed API"""
    print("\n🧪 Testing Your Deployed API")
    print("=" * 60)
    
    print("\n📋 Quick Tests (replace YOUR_URL with actual URL):")
    print("   Browser: https://YOUR_URL.onrender.com/")
    print("   Products: https://YOUR_URL.onrender.com/products?limit=5")
    print("   Search: https://YOUR_URL.onrender.com/products/search?q=iPhone")
    
    print("\n📋 curl Commands:")
    print("   curl https://YOUR_URL.onrender.com/")
    print("   curl https://YOUR_URL.onrender.com/products")
    print("   curl https://YOUR_URL.onrender.com/products/categories")
    
    print("\n📋 JavaScript Fetch:")
    print("   fetch('https://YOUR_URL.onrender.com/products')")
    print("     .then(res => res.json())")
    print("     .then(data => console.log(data));")
    
    print("\n📋 Python Requests:")
    print("   import requests")
    print("   response = requests.get('https://YOUR_URL.onrender.com/products')")
    print("   print(response.json())")

def troubleshooting():
    """Common deployment issues and solutions"""
    print("\n🔧 Troubleshooting Common Issues")
    print("=" * 60)
    
    print("\n❌ Build Failed:")
    print("   • Check requirements.txt has all dependencies")
    print("   • Ensure Python version compatibility")
    print("   • Check for syntax errors in code")
    
    print("\n❌ Database Connection Failed:")
    print("   • Verify DATABASE_URL environment variable")
    print("   • Check PostgreSQL credentials")
    print("   • Ensure SSL mode is set to 'require'")
    
    print("\n❌ App Won't Start:")
    print("   • Verify start command: gunicorn app:app")
    print("   • Check app.py has the Flask app variable named 'app'")
    print("   • Review deployment logs in Render dashboard")
    
    print("\n❌ CORS Issues:")
    print("   • Ensure Flask-CORS is installed")
    print("   • Check CORS configuration in app.py")
    print("   • Verify frontend domain is allowed")

def main():
    """Main deployment guide"""
    print("🚀 Flask Products API - Complete Deployment Guide")
    print("=" * 70)
    
    # Main deployment guide
    render_deployment_guide()
    
    # Alternative options
    show_alternatives = input("\n🔄 Show alternative deployment options? (y/n): ")
    if show_alternatives.lower() == 'y':
        heroku_deployment_guide()
    
    # Testing instructions
    show_testing = input("\n🧪 Show testing instructions? (y/n): ")
    if show_testing.lower() == 'y':
        test_deployment()
    
    # Troubleshooting
    show_troubleshooting = input("\n🔧 Show troubleshooting guide? (y/n): ")
    if show_troubleshooting.lower() == 'y':
        troubleshooting()
    
    print("\n" + "=" * 70)
    print("🎉 You're ready to deploy!")
    print("📝 Remember: Start Command = gunicorn app:app")
    print("🔗 Your API will be publicly accessible once deployed")

if __name__ == "__main__":
    main()
