# 🚀 Sentiment Analysis Google Reviews - Complete ML Pipeline

A comprehensive sentiment analysis platform built progressively from individual components to a full-stack web application with heavy ML capabilities, Docker containerization, and modern web interfaces.

## 📋 Project Overview

This project demonstrates a complete ML engineering pipeline for sentiment analysis of Google reviews, featuring:
- **PII Anonymization** using Microsoft Presidio
- **Profanity Masking** with automated content filtering
- **Sentiment Classification** using DistilBERT transformer models
- **Multiple Deployment Options** from Streamlit to full-stack React apps
- **Production-Ready** Docker containerization and REST APIs

## 🏗️ Architecture Progression

### L1: Individual Components
- **PII Anonymization**: Detect and anonymize personal information
- **Profanity Masker**: Filter inappropriate content
- **Sentiment Classifier**: ML-based sentiment analysis

### L2: Flow Integration
- Orchestrated pipeline combining all components
- End-to-end data processing workflow

### L3: Streamlit Interface
- Interactive web application
- File upload and result visualization
- Real-time ML processing

### L4: Docker Containerization
- Containerized applications for deployment
- Scalable and portable infrastructure

### L5: FastAPI Backend
- Professional REST API with OpenAPI documentation
- Async processing and production-ready endpoints
- Heavy ML model integration

### L6: Full-Stack Frontend
- Modern React application with Material-UI
- Complete user experience with data visualization
- Seamless backend integration

## 🚀 Quick Start

### Prerequisites
```bash
# Python 3.10+
# Node.js 18+
# Docker (optional)
```

### FastAPI Backend (L5)
```bash
cd L5_FASTAPI/server
pip install -r requirements.txt
./start_server.sh
# Access: http://localhost:13001/docs
```

### React Frontend (L6)
```bash
cd L6_FrontEnd
npm install
npm run dev
# Access: http://localhost:13002
```

### Docker Deployment (L4)
```bash
cd L4_Dockers
docker build -t sentiment-analysis .
docker run -p 8501:8501 sentiment-analysis
```

### Streamlit App (L3)
```bash
cd L3_Streamlit
pip install -r requirements.txt
streamlit run streamlitSentiment.py --server.enableCORS false --server.enableXsrfProtection false
```

## 📊 API Endpoints

### FastAPI (Port 13001)
- `POST /upload` - Upload CSV files
- `GET /process_csv` - Process uploaded data
- `GET /anonymise` - PII anonymization
- `GET /mask_profanity` - Profanity filtering
- `GET /classify` - Sentiment analysis
- `GET /download` - Download results
- `GET /read-data` - JSON data access
- `GET /docs` - Interactive API documentation

## 🛠️ Technology Stack

### Backend
- **FastAPI** - Modern Python web framework
- **Presidio** - Microsoft PII detection and anonymization
- **Transformers** - Hugging Face transformer models
- **DistilBERT** - Sentiment classification model
- **PyTorch** - ML framework
- **OpenVINO** - Model optimization

### Frontend
- **React 18** - Modern component architecture
- **Vite** - Fast build tool
- **Material-UI** - Professional components
- **Tailwind CSS** - Utility-first styling
- **Axios** - HTTP client

### DevOps
- **Docker** - Containerization
- **Docker Compose** - Multi-service orchestration
- **Streamlit** - Rapid prototyping

## 📁 Project Structure

```
Sentiment_Analysis_Demo_Project/
├── L1_Individual_Components/     # Core ML components
│   ├── PII/                     # Personal information handling
│   ├── profanity_masker/        # Content filtering
│   └── sentiment_classifier/    # ML sentiment analysis
├── L2_Flow/                     # Pipeline integration
├── L3_Streamlit/               # Web interface
├── L4_Dockers/                 # Containerized deployment
├── L5_FASTAPI/                 # Production API
│   └── server/                 # FastAPI application
└── L6_FrontEnd/                # React frontend
    ├── src/                    # React components
    └── server/                 # Express backend
```

## 🔧 Development Features

### Machine Learning
- **Heavy ML Models**: Real transformer models, not toy implementations
- **Production Optimization**: Model caching and efficient inference
- **Scalable Architecture**: Microservices-ready design

### Web Development
- **Modern Stack**: React + FastAPI
- **Responsive Design**: Mobile-friendly interfaces
- **Real-time Processing**: Live ML pipeline execution

### DevOps
- **Containerization**: Docker-ready applications
- **API Documentation**: Auto-generated OpenAPI specs
- **Error Handling**: Comprehensive error management

## 📈 Performance

- **ML Models**: DistilBERT sentiment classification
- **API Response**: < 1s for typical requests
- **Scalability**: Container-ready for cloud deployment
- **Memory Usage**: Optimized for production environments

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Submit a pull request

## 📄 License

This project is licensed under the MIT License.

## 👨‍💻 Author

**Panchadip Samanta**
- GitHub: [@Panchadip-128](https://github.com/Panchadip-128)
- LinkedIn: [Your LinkedIn Profile]

## 🙏 Acknowledgments

- Microsoft Presidio for PII detection
- Hugging Face for transformer models
- React and FastAPI communities

---

**Built with ❤️ for ML Engineering Excellence**
