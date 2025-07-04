#!/bin/bash

echo "🚨 Git Authentication Keeps Failing - Let's Use Easier Methods"
echo "=============================================================="
echo ""
echo "Since token authentication isn't working, here are 3 GUARANTEED methods:"
echo ""

echo "🌐 METHOD 1: Web Upload (EASIEST - 5 minutes)"
echo "----------------------------------------------"
echo "1. Go to: https://github.com/Panchadip-128/sentiment_analysis_google_reviews"
echo "2. If repo doesn't exist, click 'Create repository'"
echo "3. Click 'uploading an existing file'"
echo "4. Select ALL files from this folder and drag them to the browser"
echo "5. Add commit message: 'Complete Sentiment Analysis ML Pipeline'"
echo "6. Click 'Commit changes'"
echo ""

echo "📱 METHOD 2: GitHub Desktop (RECOMMENDED)"
echo "-----------------------------------------"
echo "1. Download: https://desktop.github.com/"
echo "2. Install and sign in with your GitHub account"
echo "3. Click 'Add an Existing Repository from your hard drive'"
echo "4. Select this folder: $(pwd)"
echo "5. Click 'Publish repository'"
echo ""

echo "🔧 METHOD 3: Fix Git Authentication (Advanced)"
echo "----------------------------------------------"
echo "If you still want to use command line:"
echo ""
echo "Option A: Try with GitHub CLI"
echo "  • Install: https://cli.github.com/"
echo "  • Run: gh auth login"
echo "  • Then: git push -u origin main"
echo ""
echo "Option B: Clear and recreate credentials"
echo "  • Run: git config --global --unset credential.helper"
echo "  • Run: git config --global credential.helper manager"
echo "  • Then: git push -u origin main"
echo ""

echo "🎯 RECOMMENDATION:"
echo "=================="
echo "For fastest upload, use METHOD 1 (Web Upload)."
echo "It's the most reliable and takes just 5 minutes!"
echo ""

read -p "Which method do you want to try? (1/2/3): " choice

case $choice in
    1)
        echo ""
        echo "🌐 Opening GitHub in your default browser..."
        if command -v xdg-open > /dev/null; then
            xdg-open "https://github.com/Panchadip-128/sentiment_analysis_google_reviews"
        elif command -v open > /dev/null; then
            open "https://github.com/Panchadip-128/sentiment_analysis_google_reviews"
        else
            echo "Please manually open: https://github.com/Panchadip-128/sentiment_analysis_google_reviews"
        fi
        echo ""
        echo "📋 Instructions:"
        echo "1. If repo doesn't exist, create it"
        echo "2. Click 'uploading an existing file'"
        echo "3. Drag ALL files from this folder to browser"
        echo "4. Commit the changes"
        ;;
    2)
        echo ""
        echo "📱 Opening GitHub Desktop download page..."
        if command -v xdg-open > /dev/null; then
            xdg-open "https://desktop.github.com/"
        elif command -v open > /dev/null; then
            open "https://desktop.github.com/"
        else
            echo "Please manually open: https://desktop.github.com/"
        fi
        ;;
    3)
        echo ""
        echo "🔧 Trying credential reset..."
        git config --global --unset credential.helper
        git config --global credential.helper manager
        echo "Now try: git push -u origin main"
        ;;
    *)
        echo "Invalid choice. Please run the script again."
        ;;
esac
