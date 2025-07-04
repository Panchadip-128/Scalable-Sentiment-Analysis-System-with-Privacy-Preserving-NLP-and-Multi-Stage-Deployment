# Docker Sentiment Analysis - Complete Setup Guide

## 🚀 Step-by-Step Instructions from Scratch

### Prerequisites
- Docker installed on your system
- Terminal/Command Prompt access

## ⚠️ Quick Fix for Common Issues

### If you get "container name already in use" error:
```bash
# Check what's running
docker ps

# Stop and remove existing container
docker stop sentiment-app
docker rm sentiment-app

# Or use a different name
docker run -d --name sentiment-app-new -p 8501:8501 sentiment-analysis-simple
```

### If port 8501 is already in use:
```bash
# Use a different port
docker run -d --name sentiment-app -p 8502:8501 sentiment-analysis-simple
# Then access at: http://localhost:8502
```

### Step 1: Navigate to Project Directory
```bash
cd /mnt/d/Sentiment_Analysis_Demo_Project/L4_Dockers
```

### Step 2: Build the Docker Image

#### Option A: Lightweight Version (Recommended - Fast)
```bash
docker build -f Dockerfile.simple -t sentiment-analysis-simple .
```

#### Option B: Full Version (Heavy ML models)
```bash
docker build -t sentiment-analysis-full .
```

### Step 3: Run the Application

#### Web Interface (Streamlit)
```bash
# Lightweight version
docker run -d --name sentiment-app -p 8501:8501 sentiment-analysis-simple

# Access at: http://localhost:8501
```

#### Command Line Processing
```bash
# Process default data
docker run --rm sentiment-analysis-simple python main_simple.py

# Process your own data (volume mounting)
docker run --rm -v "$(pwd):/app/data" sentiment-analysis-simple python main_simple.py
```

### Step 4: Check Results
```bash
# View output files
docker run --rm sentiment-analysis-simple ls -la output_*.csv

# Copy results to host
docker cp sentiment-app:/usr/app/output_classified_simple.csv ./results.csv
```

### Step 5: Stop and Clean Up
```bash
# Stop running containers
docker stop sentiment-app

# Remove containers
docker rm sentiment-app

# Remove images (optional)
docker rmi sentiment-analysis-simple
```

## Quick Commands Reference

### Management Commands
```bash
# List running containers
docker ps

# List all containers
docker ps -a

# List images
docker images

# View logs
docker logs sentiment-app

# Execute commands in running container
docker exec -it sentiment-app bash
```

### File Operations
```bash
# Copy file to container
docker cp your-file.csv sentiment-app:/usr/app/

# Copy file from container
docker cp sentiment-app:/usr/app/output.csv ./

# Mount directory
docker run -v "$(pwd):/app/data" sentiment-analysis-simple
```

## Troubleshooting

### Common Issues
1. **Port already in use**: Change port `-p 8502:8501`
2. **Permission denied**: Use `sudo docker` (Linux/Mac)
3. **Out of space**: Clean up with `docker system prune`
4. **Build fails**: Check requirements.txt files

### Debug Commands
```bash
# Interactive shell
docker run -it sentiment-analysis-simple bash

# Check container status
docker inspect sentiment-app

# Monitor resource usage
docker stats sentiment-app
```
