### Personally Identifiable Information (PII) : masks personal information present

Install the dependencies in a virtual environment and execute the python script client.py

## Quick Setup (Recommended for Testing)
```bash 
$ python3 -m venv venv_new
$ source venv_new/bin/activate  # On Windows: venv_new\Scripts\activate
$ python3 -m pip install pandas
$ python3 client_simple.py  # Fast version using regex patterns
```

## Full Setup (Heavy ML Models)
```bash 
$ python3 -m venv venv_new
$ source venv_new/bin/activate  # On Windows: venv_new\Scripts\activate
$ python3 -m pip install -r requirements.txt
$ python3 client.py  # Full Presidio version (slow but more accurate)
```

## Available Clients:
- **client_simple.py**: Fast regex-based PII detection (recommended for testing)
- **client.py**: Full Presidio with ML models (slower but more accurate)
- **pii_simple.py**: Standalone simple PII service for testing

## Performance:
- Simple version: ~0.01 seconds per row
- Full version: ~10-30 seconds per row (depending on text length)