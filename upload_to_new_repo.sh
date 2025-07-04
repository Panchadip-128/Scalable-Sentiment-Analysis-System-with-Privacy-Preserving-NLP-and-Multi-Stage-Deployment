#!/bin/bash

# 🚀 Upload to NEW GitHub Repository
# Repository: https://github.com/Panchadip-128/sentiment_analysis_google_reviews

echo "🎯 Uploading to NEW GitHub Repository"
echo "======================================"
echo ""
echo "Repository: https://github.com/Panchadip-128/sentiment_analysis_google_reviews"
echo ""

# Check if we're in the right directory
if [[ ! -f "README.md" ]] || [[ ! -d "L1_Individual_Components" ]]; then
    echo "❌ Please run this script from the Sentiment_Analysis_Demo_Project directory"
    exit 1
fi

echo "✅ Found project files"
echo ""

# Initialize git if needed
if [[ ! -d ".git" ]]; then
    echo "🔧 Initializing Git repository..."
    git init
else
    echo "✅ Git repository already initialized"
fi

# Configure git user
echo "🔧 Setting up Git configuration..."
git config user.name "Panchadip-128"

# Ask for email if not set
if ! git config user.email > /dev/null; then
    read -p "Enter your GitHub email: " email
    git config user.email "$email"
else
    echo "✅ Git email already configured: $(git config user.email)"
fi

# Add all files
echo "📦 Adding all project files..."
git add .

# Check what's being added
echo ""
echo "📋 Files to be uploaded:"
git status --short | head -20
if [[ $(git status --short | wc -l) -gt 20 ]]; then
    echo "... and $(( $(git status --short | wc -l) - 20 )) more files"
fi
echo ""

# Create commit
echo "📝 Creating commit..."
git commit -m "🚀 Complete Sentiment Analysis ML Pipeline (L1-L6)

Multi-stage ML engineering project featuring:
- L1: Individual components (PII, Profanity, Sentiment)  
- L2: Integrated pipeline flow
- L3: Streamlit web interface
- L4: Docker containerization
- L5: FastAPI backend with heavy ML models
- L6: React frontend with modern UI

Tech Stack:
🔬 ML: DistilBERT, Transformers, PyTorch, OpenVINO
🔒 Privacy: Microsoft Presidio PII anonymization  
🚫 Content: Profanity filtering with better-profanity
🌐 Backend: FastAPI with async endpoints
🎨 Frontend: React + Material-UI + Tailwind CSS
🐳 DevOps: Docker containerization
📊 Data: CSV processing pipeline

Features:
✅ Production-ready REST API with OpenAPI docs
✅ Modern React frontend with file upload
✅ Heavy ML models (not toy implementations)
✅ Complete pipeline from data upload to results
✅ Docker deployment ready
✅ Mobile-responsive design
✅ Real-time ML processing

Server URLs:
- FastAPI Backend: http://localhost:13001
- React Frontend: http://localhost:13002
- API Documentation: http://localhost:13001/docs"

if [ $? -ne 0 ]; then
    echo "❌ Commit failed. Please check for errors."
    exit 1
fi

echo "✅ Commit created successfully"
echo ""

# Set up remote
echo "🌐 Setting up remote repository..."
git remote remove origin 2>/dev/null || true
git remote add origin https://github.com/Panchadip-128/sentiment_analysis_google_reviews.git
git branch -M main

echo "✅ Remote repository configured"
echo ""

# Authentication methods
echo "🔐 AUTHENTICATION OPTIONS:"
echo "=========================="
echo ""
echo "Choose your preferred authentication method:"
echo ""
echo "1) 🔑 Personal Access Token (Recommended)"
echo "   - Most secure and reliable"
echo "   - Works with 2FA enabled"
echo ""
echo "2) 🌐 Web Upload (Easiest)"
echo "   - No command line authentication needed"
echo "   - Drag and drop files in browser"
echo ""
echo "3) 📱 GitHub Desktop (User-friendly)"
echo "   - GUI application"
echo "   - Handles authentication automatically"
echo ""

read -p "Choose option (1/2/3): " choice

case $choice in
    1)
        echo ""
        echo "🔑 PERSONAL ACCESS TOKEN METHOD"
        echo "==============================="
        echo ""
        echo "STEP 1: Create Token"
        echo "🌐 Go to: https://github.com/settings/tokens/new"
        echo ""
        echo "STEP 2: Fill the form:"
        echo "📝 Note: sentiment-analysis-project"
        echo "📅 Expiration: 30 days (or longer)"
        echo "✅ Scopes: Check 'repo' (Full control of private repositories)"
        echo "🔄 Click 'Generate token'"
        echo ""
        echo "STEP 3: Copy the token (starts with 'ghp_')"
        echo ""
        read -p "Have you created and copied your token? (y/n): " token_ready
        
        if [[ $token_ready == "y" ]] || [[ $token_ready == "Y" ]]; then
            echo ""
            echo "🚀 Pushing to GitHub..."
            echo "When prompted, enter:"
            echo "  Username: Panchadip-128"
            echo "  Password: [PASTE YOUR TOKEN]"
            echo ""
            git push -u origin main
            
            if [ $? -eq 0 ]; then
                echo ""
                echo "🎉 SUCCESS! Repository uploaded!"
                echo "📍 https://github.com/Panchadip-128/sentiment_analysis_google_reviews"
            else
                echo ""
                echo "❌ Push failed. Try option 2 or 3 instead."
            fi
        else
            echo "Please create the token first, then run this script again."
        fi
        ;;
        
    2)
        echo ""
        echo "🌐 WEB UPLOAD METHOD"
        echo "==================="
        echo ""
        echo "STEP 1: Open your repository"
        echo "🌐 Go to: https://github.com/Panchadip-128/sentiment_analysis_google_reviews"
        echo ""
        echo "STEP 2: Upload files"
        echo "📁 Click 'uploading an existing file'"
        echo "📤 Drag ALL files from this directory to the browser"
        echo "📝 Add commit message: 'Complete Sentiment Analysis ML Pipeline'"
        echo "✅ Click 'Commit changes'"
        echo ""
        echo "Opening repository in browser..."
        if command -v explorer.exe > /dev/null; then
            explorer.exe "https://github.com/Panchadip-128/sentiment_analysis_google_reviews"
        elif command -v xdg-open > /dev/null; then
            xdg-open "https://github.com/Panchadip-128/sentiment_analysis_google_reviews"
        else
            echo "Please manually open: https://github.com/Panchadip-128/sentiment_analysis_google_reviews"
        fi
        ;;
        
    3)
        echo ""
        echo "📱 GITHUB DESKTOP METHOD"
        echo "========================"
        echo ""
        echo "STEP 1: Download GitHub Desktop"
        echo "🌐 Go to: https://desktop.github.com/"
        echo ""
        echo "STEP 2: Install and sign in"
        echo "🔐 Sign in with your GitHub account"
        echo ""
        echo "STEP 3: Add repository"
        echo "📁 Click 'Add an Existing Repository from your hard drive'"
        echo "📂 Select this directory: $(pwd)"
        echo "🚀 Click 'Publish repository'"
        echo ""
        echo "Opening GitHub Desktop download page..."
        if command -v explorer.exe > /dev/null; then
            explorer.exe "https://desktop.github.com/"
        elif command -v xdg-open > /dev/null; then
            xdg-open "https://desktop.github.com/"
        else
            echo "Please manually open: https://desktop.github.com/"
        fi
        ;;
        
    *)
        echo "Invalid choice. Please run the script again and choose 1, 2, or 3."
        ;;
esac

echo ""
echo "🎯 WHAT YOU'LL HAVE ON GITHUB:"
echo "=============================="
echo "✅ Complete ML pipeline (L1-L6)"
echo "✅ FastAPI backend code"
echo "✅ React frontend application"
echo "✅ Docker containerization"
echo "✅ Comprehensive documentation"
echo "✅ Production-ready deployment scripts"
echo ""
echo "📊 Repository showcases:"
echo "🔬 Advanced ML engineering"
echo "🌐 Full-stack development"
echo "🐳 DevOps and containerization"
echo "📱 Modern web technologies"
