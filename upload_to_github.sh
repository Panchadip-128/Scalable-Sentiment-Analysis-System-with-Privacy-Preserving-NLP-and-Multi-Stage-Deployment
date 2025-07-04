#!/bin/bash

# 🚀 GitHub Upload Script for Sentiment Analysis Project
# Repository: https://github.com/Panchadip-128/sentiment_analysis_google_reviews

echo "🔧 Setting up Git configuration..."

# Set your actual email here
read -p "Enter your GitHub email: " email
git config user.email "$email"

echo "📦 Checking repository status..."
git status

echo "🔄 Adding all files to Git..."
git add .

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
✅ Real-time ML processing"

echo "🌐 Setting up remote repository..."
git remote set-url origin https://github.com/Panchadip-128/sentiment_analysis_google_reviews.git

echo "🚀 Pushing to GitHub..."
echo "⚠️  You may need to authenticate with GitHub..."
echo "💡 If prompted, use your GitHub username and personal access token"

git push -u origin main

echo ""
echo "🎉 SUCCESS! Your project has been uploaded to:"
echo "📍 https://github.com/Panchadip-128/sentiment_analysis_google_reviews"
echo ""
echo "🔗 Next steps:"
echo "1. Visit your GitHub repository"
echo "2. Add a description and topics"
echo "3. Enable GitHub Pages if desired"
echo "4. Share your project!"
echo ""
echo "📊 Repository contains:"
echo "  • Complete ML pipeline (L1-L6)"
echo "  • FastAPI backend on port 13001"
echo "  • React frontend on port 13002"
echo "  • Docker containerization"
echo "  • Production-ready code"
