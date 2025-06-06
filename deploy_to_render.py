import os
import subprocess
import sys
import zipfile
import webbrowser
import time

def create_deployment_package():
    """Create a deployment package for Render"""
    print("📦 Creating deployment package...")
    
    # Files to include in the deployment package
    essential_files = [
        "app.py",
        "database.py",
        "requirements.txt",
        "wsgi.py",
        "render.yaml"
    ]
    
    # Check if all files exist
    missing_files = [file for file in essential_files if not os.path.exists(file)]
    if missing_files:
        print(f"❌ Missing required files: {', '.join(missing_files)}")
        return False
    
    # Create a zip file for deployment
    try:
        with zipfile.ZipFile('render-deploy.zip', 'w') as zipf:
            for file in essential_files:
                zipf.write(file)
                print(f"✅ Added {file} to deployment package")
        
        print("📦 Deployment package created: render-deploy.zip")
        return True
    except Exception as e:
        print(f"❌ Error creating deployment package: {e}")
        return False

def deployment_instructions():
    """Display deployment instructions for Render"""
    print("\n🚀 Deployment Instructions for Render")
    print("=" * 60)
    
    print("\n📋 Step 1: Create a Render account")
    print("   Go to https://render.com and sign up for an account if you don't have one")
    
    print("\n📋 Step 2: Create a new Web Service")
    print("   1. Click 'New +' in the Render dashboard")
    print("   2. Select 'Web Service'")
    print("   3. Connect your GitHub repository or upload the deployment package")
    
    print("\n📋 Step 3: Configure your Web Service")
    print("   1. Name: products-api (or your preferred name)")
    print("   2. Environment: Python")
    print("   3. Build Command: pip install -r requirements.txt")
    print("   4. Start Command: gunicorn wsgi:app")
    
    print("\n📋 Step 4: Add Environment Variables")
    print("   Add the following environment variable:")
    print("   DATABASE_URL: postgresql://products_qnmx_user:PYbv6akp0SOprUqCqgMVU27wpcf9L2sF@dpg-d1191sidbo4c739pelk0-a.oregon-postgres.render.com/products_qnmx")
    
    print("\n📋 Step 5: Deploy")
    print("   Click 'Create Web Service' and wait for deployment to complete")
    
    print("\n🔗 Your API will be available at:")
    print("   https://your-service-name.onrender.com")
    
    print("\n📝 Example API calls:")
    print("   GET https://your-service-name.onrender.com/products")
    print("   GET https://your-service-name.onrender.com/products/search?q=iPhone")
    print("   GET https://your-service-name.onrender.com/products/categories")
    
    # Open Render website
    open_website = input("\n🌐 Would you like to open the Render website now? (y/n): ")
    if open_website.lower() == 'y':
        webbrowser.open("https://render.com")

def alternative_deployment_options():
    """Display alternative deployment options"""
    print("\n🔄 Alternative Deployment Options")
    print("=" * 60)
    
    print("\n1️⃣ Heroku")
    print("   - Create a Procfile with: web: gunicorn wsgi:app")
    print("   - Deploy using Heroku CLI or GitHub integration")
    print("   - Set DATABASE_URL environment variable")
    print("   - URL format: https://your-app-name.herokuapp.com")
    
    print("\n2️⃣ Vercel")
    print("   - Create a vercel.json configuration file")
    print("   - Deploy using Vercel CLI or GitHub integration")
    print("   - Set environment variables in Vercel dashboard")
    print("   - URL format: https://your-app-name.vercel.app")
    
    print("\n3️⃣ AWS Elastic Beanstalk")
    print("   - Create an application and environment")
    print("   - Deploy using AWS CLI or AWS console")
    print("   - Set environment variables in configuration")
    print("   - URL format: http://your-env.eba-xyz.region.elasticbeanstalk.com")
    
    print("\n4️⃣ Google Cloud Run")
    print("   - Create a Dockerfile for your application")
    print("   - Deploy using Google Cloud CLI or console")
    print("   - Set environment variables during deployment")
    print("   - URL format: https://your-service-hash-region.run.app")

def test_api_instructions():
    """Display instructions for testing the API"""
    print("\n🧪 Testing Your Deployed API")
    print("=" * 60)
    
    print("\n📋 Basic API Tests:")
    print("   1. Replace YOUR_API_URL with your actual deployment URL")
    print("   2. Use a tool like curl, Postman, or your browser to test endpoints")
    
    print("\n📋 Example curl commands:")
    print("   curl https://YOUR_API_URL/")
    print("   curl https://YOUR_API_URL/products?limit=5")
    print("   curl https://YOUR_API_URL/products/search?q=iPhone")
    print("   curl https://YOUR_API_URL/products/categories")
    
    print("\n📋 Using the API in your frontend:")
    print("   fetch('https://YOUR_API_URL/products')")
    print("     .then(response => response.json())")
    print("     .then(data => console.log(data));")

def main():
    """Main deployment helper function"""
    print("🚀 Flask Products API Deployment Helper")
    print("=" * 60)
    
    # Create deployment package
    create_deployment_package()
    
    # Display deployment instructions
    deployment_instructions()
    
    # Show alternative options
    show_alternatives = input("\n🔄 Would you like to see alternative deployment options? (y/n): ")
    if show_alternatives.lower() == 'y':
        alternative_deployment_options()
    
    # Show testing instructions
    show_testing = input("\n🧪 Would you like to see API testing instructions? (y/n): ")
    if show_testing.lower() == 'y':
        test_api_instructions()
    
    print("\n" + "=" * 60)
    print("🎉 You're ready to deploy your Flask Products API!")
    print("   Once deployed, you'll have a public URL to access your API endpoints.")

if __name__ == "__main__":
    main()
