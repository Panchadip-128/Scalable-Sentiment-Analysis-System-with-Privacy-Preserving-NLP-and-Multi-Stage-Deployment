#!/bin/bash

# FastAPI Server Startup Script
echo "🚀 Starting FastAPI Sentiment Analysis Server..."

cd /mnt/d/Sentiment_Analysis_Demo_Project/L5_FASTAPI/server

echo "📦 Checking dependencies..."
python3 -c "import fastapi, uvicorn; print('✅ FastAPI and Uvicorn available')" || {
    echo "❌ Installing FastAPI..."
    pip install fastapi uvicorn
}

echo "🔬 Checking ML dependencies..."
python3 -c "import transformers, torch, openvino; print('✅ Heavy ML dependencies available')" || {
    echo "⚠️  Some ML dependencies missing, but server will start with fallbacks"
}

echo "🧠 Checking NLP dependencies..."
python3 -c "import presidio_analyzer, presidio_anonymizer; print('✅ Presidio NLP tools available')" || {
    echo "⚠️  Presidio dependencies missing"
}

echo "🤬 Checking profanity filter..."
python3 -c "import better_profanity; print('✅ Profanity filter available')" || {
    echo "❌ Installing profanity filter..."
    pip install better-profanity
}

echo "🔧 Starting server on port 13001..."
echo "📖 Access the API at: http://localhost:13001"
echo "📚 API Documentation: http://localhost:13001/docs"
echo "� Pipeline endpoints:"
echo "   • GET /process_csv - Process uploaded CSV"
echo "   • GET /anonymise - Anonymize PII data"
echo "   • GET /mask_profanity - Mask profanity"
echo "   • GET /classify - Classify sentiment"
echo "   • GET /download - Download results"
echo "   • GET /read-data - Read processed data"
echo "�🛑 Press Ctrl+C to stop the server"
echo ""

uvicorn main:app --host 0.0.0.0 --port 13001 --reload
