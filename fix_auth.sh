#!/bin/bash

# 🔑 GitHub Authentication Fix
# Since password authentication failed, here's how to fix it:

echo "🚨 SSH Failed - Using HTTPS with Token Instead"
echo ""
echo "STEP 1: Create a Personal Access Token"
echo "🌐 Go to: https://github.com/settings/tokens"
echo "🔧 Click: 'Generate new token (classic)'"
echo "📝 Name: 'sentiment-analysis-upload'"
echo "⏰ Expiration: 30 days (or longer)"
echo "✅ Scope: Check 'repo' (full control)"
echo "🔑 Generate and COPY the token (starts with ghp_)"
echo ""
echo "STEP 2: Switch back to HTTPS"
git remote set-url origin https://github.com/Panchadip-128/sentiment_analysis_google_reviews.git
echo "✅ Remote URL set to HTTPS"
echo ""
echo "STEP 3: Try the push with your token"
echo "When prompted:"
echo "  Username: Panchadip-128"
echo "  Password: ghp_xxxxxxxxxxxxxxxxxxxx (your token)"
echo ""

read -p "Ready to try again? Press Enter..."

echo "🔄 Retrying git push..."
git push -u origin main

if [ $? -eq 0 ]; then
    echo ""
    echo "🎉 SUCCESS! Repository uploaded to:"
    echo "📍 https://github.com/Panchadip-128/sentiment_analysis_google_reviews"
else
    echo ""
    echo "❌ Still having issues? Try these alternatives:"
    echo ""
    echo "Option 1: Use SSH instead of HTTPS"
    echo "git remote set-url origin git@github.com:Panchadip-128/sentiment_analysis_google_reviews.git"
    echo ""
    echo "Option 2: Use GitHub Desktop"
    echo "Download from: https://desktop.github.com/"
    echo ""
    echo "Option 3: Upload via web interface"
    echo "1. Go to: https://github.com/Panchadip-128/sentiment_analysis_google_reviews"
    echo "2. Click 'uploading an existing file'"
    echo "3. Drag and drop your project folder"
fi
