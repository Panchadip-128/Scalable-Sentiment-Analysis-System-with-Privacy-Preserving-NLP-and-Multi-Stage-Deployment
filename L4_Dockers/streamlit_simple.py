# Simple Dockerized Sentiment Analysis Pipeline
# Uses lightweight components to avoid heavy model conversion issues

import streamlit as st
import pandas as pd
import time
import sys
import os

# Add the current directory to Python path for imports
sys.path.append('/usr/app')

# Import simple components that work reliably
from googlereviews import CSVProcessor
from PII.pii_simple import SimplePIIService

# Simple profanity masker
class SimpleProfanityMasker:
    """Simple profanity masker using basic word filtering."""
    
    def __init__(self):
        """Initialize with basic profanity words."""
        self.profanity_words = [
            'damn', 'hell', 'shit', 'fuck', 'bitch', 'ass', 'crap', 'stupid',
            'idiot', 'moron', 'dumb', 'hate', 'suck', 'terrible', 'awful',
            'horrible', 'disgusting', 'pathetic', 'worst', 'useless'
        ]
    
    def mask_profanity(self, text):
        """Mask profanity words with asterisks."""
        if not text:
            return text
            
        masked_text = str(text).lower()
        for word in self.profanity_words:
            if word in masked_text:
                masked_text = masked_text.replace(word, '*' * len(word))
        return masked_text

# Simple sentiment classifier without complex model conversion
class SimpleSentimentClassifier:
    """Simple sentiment classifier using basic text analysis."""
    
    def __init__(self, checkpoint=None):
        """Initialize with basic sentiment words."""
        self.positive_words = [
            'good', 'great', 'excellent', 'amazing', 'wonderful', 'fantastic', 
            'awesome', 'brilliant', 'perfect', 'outstanding', 'superb', 'love',
            'best', 'nice', 'beautiful', 'impressed', 'satisfied', 'happy',
            'pleased', 'recommend', 'perfect', 'delicious', 'fresh', 'clean'
        ]
        
        self.negative_words = [
            'bad', 'terrible', 'awful', 'horrible', 'worst', 'hate', 'disgusting',
            'disappointing', 'poor', 'unacceptable', 'rude', 'slow', 'dirty',
            'expensive', 'overpriced', 'tasteless', 'cold', 'unfriendly', 'waste',
            'regret', 'avoid', 'never', 'wrong', 'problem', 'complaint'
        ]
    
    def infer(self, text):
        """Simple sentiment classification based on word matching."""
        if not text or not isinstance(text, str):
            return "UNKNOWN"
        
        text_lower = text.lower()
        positive_count = sum(1 for word in self.positive_words if word in text_lower)
        negative_count = sum(1 for word in self.negative_words if word in text_lower)
        
        if positive_count > negative_count:
            return "POSITIVE"
        elif negative_count > positive_count:
            return "NEGATIVE"
        else:
            return "NEUTRAL"

# Streamlit App
st.set_page_config(layout="wide")
st.title('📚 Simple Sentiment Analysis Pipeline 📚')
st.info("This is a lightweight version that works reliably in Docker containers.")

# Step 1: Upload the CSV file
uploaded_file = st.file_uploader("Upload your reviews file", type=["csv"])

if uploaded_file is not None:
    # Save the uploaded file
    csv_file_path = "reviews.csv"
    with open(csv_file_path, "wb") as f:
        f.write(uploaded_file.getvalue())
    
    st.success("File uploaded successfully!")
    
    # Process the file
    if st.button("🚀 Start Processing"):
        progress_bar = st.progress(0)
        status_text = st.empty()
        
        try:
            # Step 1: Load and preprocess data
            status_text.text("Step 1/4: Loading data...")
            progress_bar.progress(10)
            
            df = pd.read_csv(csv_file_path)
            st.write(f"Loaded {len(df)} rows")
            
            # Limit processing for demonstration
            sample_size = min(20, len(df))
            df_sample = df.head(sample_size)
            st.write(f"Processing first {sample_size} rows for demonstration")
            
            # Step 2: PII Anonymization
            status_text.text("Step 2/4: Anonymizing PII...")
            progress_bar.progress(30)
            
            pii_service = SimplePIIService()
            anonymized_texts = []
            
            for index, row in df_sample.iterrows():
                text = str(row.iloc[0])
                entities = pii_service.analyze_text(text)
                anonymized_text, _ = pii_service.anonymize_text(text, entities, "replace")
                anonymized_texts.append(anonymized_text)
            
            df_sample['Anonymized_Text'] = anonymized_texts
            
            # Step 3: Profanity Masking
            status_text.text("Step 3/4: Masking profanity...")
            progress_bar.progress(60)
            
            profanity_masker = SimpleProfanityMasker()
            masked_texts = []
            for text in anonymized_texts:
                masked_text = profanity_masker.mask_profanity(text)
                masked_texts.append(masked_text)
            
            df_sample['Masked_Text'] = masked_texts
            
            # Step 4: Sentiment Classification
            status_text.text("Step 4/4: Classifying sentiment...")
            progress_bar.progress(80)
            
            classifier = SimpleSentimentClassifier()
            sentiments = []
            for text in masked_texts:
                sentiment = classifier.infer(text)
                sentiments.append(sentiment)
            
            df_sample['Sentiment'] = sentiments
            
            # Complete
            progress_bar.progress(100)
            status_text.text("✅ Processing complete!")
            
            # Display results
            st.subheader("📊 Results")
            
            # Show sample results
            st.write("### Sample Processed Data")
            st.dataframe(df_sample[['Anonymized_Text', 'Masked_Text', 'Sentiment']].head(10))
            
            # Show sentiment distribution
            st.write("### Sentiment Distribution")
            sentiment_counts = df_sample['Sentiment'].value_counts()
            st.bar_chart(sentiment_counts)
            
            # Download processed data
            csv_output = df_sample.to_csv(index=False)
            st.download_button(
                label="📥 Download Processed Data",
                data=csv_output,
                file_name="processed_reviews.csv",
                mime="text/csv"
            )
            
        except Exception as e:
            st.error(f"Error during processing: {str(e)}")
            st.write("Please check your CSV file format and try again.")

else:
    st.info("👆 Please upload a CSV file to get started")
    
    # Show example format
    st.subheader("📋 Expected CSV Format")
    example_data = {
        'text': [
            'This restaurant is amazing! Great food and service.',
            'Terrible experience. Food was cold and staff was rude.',
            'Average place. Nothing special but okay.'
        ]
    }
    example_df = pd.DataFrame(example_data)
    st.dataframe(example_df)
