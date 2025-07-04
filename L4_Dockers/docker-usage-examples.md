# Docker Usage Examples for Sentiment Analysis Pipeline

## Quick Start

### 1. Web Interface (Streamlit)
```bash
# Start the web application
docker run -d --name sentiment-app -p 8501:8501 sentiment-analysis-simple

# Access in browser: http://localhost:8501
# Stop when done: docker stop sentiment-app && docker rm sentiment-app
```

### 2. Command Line Processing
```bash
# Process default reviews.csv
docker run --rm sentiment-analysis-simple python main_simple.py

# See the results
docker run --rm sentiment-analysis-simple ls -la output_*.csv
```

## Processing Your Own Data

### Method 1: Volume Mounting (Recommended)
```bash
# Place your CSV file in the current directory as 'reviews.csv'
# Then run with volume mounting:
docker run --rm \
  -v "$(pwd):/app/data" \
  sentiment-analysis-simple \
  python main_simple.py

# Your output files will be saved in the current directory
```

### Method 2: Copy Files Into Container
```bash
# Start a container
docker run -it --name temp-sentiment sentiment-analysis-simple bash

# In another terminal, copy your file
docker cp your-reviews.csv temp-sentiment:/usr/app/reviews.csv

# Back in the container terminal:
python main_simple.py

# Copy results back
docker cp temp-sentiment:/usr/app/output_classified.csv ./results.csv

# Cleanup
docker rm temp-sentiment
```

### Method 3: Interactive Processing
```bash
# Start interactive container with volume
docker run -it --rm \
  -v "$(pwd):/app/data" \
  sentiment-analysis-simple \
  bash

# Inside container, you can:
python main_simple.py
python -c "from PII.client_simple import process_csv_file; process_csv_file('your-file.csv', 'output.csv')"
```

## Advanced Usage

### Environment Variables
```bash
# Set processing limits
docker run --rm \
  -e MAX_ROWS=1000 \
  -e OUTPUT_DIR=/app/results \
  sentiment-analysis-simple \
  python main_simple.py
```

### Custom Commands
```bash
# Run individual components
docker run --rm sentiment-analysis-simple python -c "
from PII.client_simple import process_csv_file
process_csv_file('reviews.csv', 'anonymized.csv')
print('PII anonymization complete!')
"

# Check available datasets
docker run --rm sentiment-analysis-simple ls -la *.csv

# Test the simple PII service
docker run --rm sentiment-analysis-simple python PII/pii_simple.py
```

### Port Mapping
```bash
# Custom port for Streamlit
docker run -d -p 8080:8501 sentiment-analysis-simple

# Multiple instances
docker run -d -p 8501:8501 --name app1 sentiment-analysis-simple
docker run -d -p 8502:8501 --name app2 sentiment-analysis-simple
```

## File Formats

### Input CSV Format
Your input CSV should have columns like:
- `review_text` or `text` or `comment`
- Any other columns will be preserved

### Output Files
- `output_anonymized.csv` - PII removed/masked
- `output_masked.csv` - Profanity filtered  
- `output_classified.csv` - With sentiment scores

## Troubleshooting

### Common Issues
```bash
# Port already in use
docker ps | grep 8501
docker stop <container_id>

# Permission issues
sudo docker run ...

# Check logs
docker logs <container_name>

# Container won't start
docker run -it sentiment-analysis-simple bash
```

### Performance Optimization
```bash
# Limit memory usage
docker run --memory=2g sentiment-analysis-simple python main_simple.py

# Use multiple CPU cores
docker run --cpus=2 sentiment-analysis-simple python main_simple.py
```

## Data Volumes

### Persistent Data
```bash
# Create a data volume
docker volume create sentiment-data

# Use the volume
docker run --rm \
  -v sentiment-data:/app/data \
  sentiment-analysis-simple \
  python main_simple.py

# Access volume data
docker run --rm -v sentiment-data:/data alpine ls -la /data
```

## Production Usage

### Background Processing
```bash
# Run as daemon
docker run -d \
  --name sentiment-processor \
  --restart unless-stopped \
  -v /host/data:/app/data \
  sentiment-analysis-simple \
  tail -f /dev/null

# Execute processing jobs
docker exec sentiment-processor python main_simple.py
```

### Health Checks
```bash
# Container with health check
docker run -d \
  --health-cmd="python -c 'import pandas; print(\"OK\")'" \
  --health-interval=30s \
  sentiment-analysis-simple
```
