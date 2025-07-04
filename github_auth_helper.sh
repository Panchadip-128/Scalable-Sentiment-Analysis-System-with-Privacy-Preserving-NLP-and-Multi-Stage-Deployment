#!/bin/bash

echo "🔐 GitHub Personal Access Token Required"
echo "=========================================="
echo ""
echo "Since authentication keeps failing, let's set this up step by step:"
echo ""

# Check if we can reach GitHub
echo "🌐 Testing GitHub connectivity..."
if curl -s https://github.com > /dev/null; then
    echo "✅ GitHub is reachable"
else
    echo "❌ Cannot reach GitHub - check internet connection"
    exit 1
fi

echo ""
echo "📋 STEP-BY-STEP TOKEN CREATION:"
echo ""
echo "1. Open this URL in your browser:"
echo "   👉 https://github.com/settings/tokens/new"
echo ""
echo "2. Fill the form:"
echo "   📝 Note: sentiment-analysis-project"
echo "   📅 Expiration: 30 days"
echo "   ✅ Scopes: Check 'repo' (Full control of private repositories)"
echo ""
echo "3. Click 'Generate token'"
echo "4. COPY the token (it starts with 'ghp_')"
echo ""

read -p "Have you created and copied your token? (y/n): " response

if [[ $response != "y" && $response != "Y" ]]; then
    echo "❌ Please create the token first, then run this script again."
    exit 1
fi

echo ""
echo "🔑 Now let's set up authentication with your token:"
echo ""

# Method 1: Try with credential helper
echo "Setting up credential storage..."
git config credential.helper store

echo ""
echo "📤 Attempting to push..."
echo "When prompted, enter:"
echo "  Username: Panchadip-128"
echo "  Password: [PASTE YOUR TOKEN HERE - starts with ghp_]"
echo ""

git push -u origin main

if [ $? -eq 0 ]; then
    echo ""
    echo "🎉 SUCCESS! Your project is now on GitHub!"
    echo "📍 https://github.com/Panchadip-128/sentiment_analysis_google_reviews"
    echo ""
    echo "✅ Your credentials have been saved for future use."
else
    echo ""
    echo "❌ Push failed. Let's try an alternative method..."
    echo ""
    echo "🔄 ALTERNATIVE: Embed token in URL"
    echo "Please paste your token (starts with ghp_):"
    read -s token
    
    if [[ $token == ghp_* ]]; then
        git remote set-url origin "https://${token}@github.com/Panchadip-128/sentiment_analysis_google_reviews.git"
        echo "✅ Token embedded in remote URL"
        echo "🔄 Trying push again..."
        git push -u origin main
        
        if [ $? -eq 0 ]; then
            echo "🎉 SUCCESS! Repository uploaded!"
            # Remove token from URL for security
            git remote set-url origin "https://github.com/Panchadip-128/sentiment_analysis_google_reviews.git"
            echo "✅ Token removed from URL for security"
        else
            echo "❌ Still failed. Please check your token is correct."
        fi
    else
        echo "❌ Invalid token format. Tokens should start with 'ghp_'"
    fi
fi
