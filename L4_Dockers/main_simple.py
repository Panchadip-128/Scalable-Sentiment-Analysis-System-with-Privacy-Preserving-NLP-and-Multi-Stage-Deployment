#!/usr/bin/env python3
"""
Fixed simple main script for sentiment analysis pipeline.
"""

import pandas as pd
import time
import sys
import os

# Add current directory to path for imports
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from googlereviews import CSVProcessor
from PII.pii_simple import SimplePIIService

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
            'bad', 'terrible', 'awful', 'horrible', 'disgusting', 'worst',
            'hate', 'disappointed', 'angry', 'frustrated', 'annoyed', 'upset',
            'sad', 'poor', 'cheap', 'dirty', 'slow', 'rude', 'unfriendly'
        ]
    
    def infer(self, text):
        """Simple sentiment inference based on word counts."""
        if not text:
            return "NEUTRAL"
            
        text_lower = str(text).lower()
        positive_count = sum(1 for word in self.positive_words if word in text_lower)
        negative_count = sum(1 for word in self.negative_words if word in text_lower)
        
        if positive_count > negative_count:
            return "POSITIVE"
        elif negative_count > positive_count:
            return "NEGATIVE"
        else:
            return "NEUTRAL"

def main():
    """Main pipeline function."""
    print("🚀 Starting Simple Sentiment Analysis Pipeline")
    print("=" * 50)
    
    # Step 1: Load Data
    print("📁 Step 1: Loading data...")
    
    # Try to find CSV file
    csv_files = ['reviews.csv', 'data/reviews.csv', '/app/data/reviews.csv']
    csv_file = None
    
    for file_path in csv_files:
        if os.path.exists(file_path):
            csv_file = file_path
            break
    
    if not csv_file:
        print("❌ No reviews.csv file found!")
        return
        
    try:
        df = pd.read_csv(csv_file)
        print(f"✅ Loaded {len(df)} rows")
    except Exception as e:
        print(f"❌ Error loading CSV: {e}")
        return
    
    # Process a small sample for demonstration
    sample_size = min(20, len(df))
    df_sample = df.head(sample_size).copy()  # Make a copy to avoid warnings
    print(f"🔢 Processing first {sample_size} rows for demonstration")
    
    # Step 2: PII Anonymization
    print("🔒 Step 2: Anonymizing PII...")
    pii_service = SimplePIIService()
    anonymized_texts = []
    
    for index, row in df_sample.iterrows():
        text = str(row.iloc[0]) if len(row) > 0 else ""
        
        # Analyze and anonymize PII
        entities = pii_service.analyze_text(text)
        anonymized_text, mapping = pii_service.anonymize_text(text, entities, "replace")
        anonymized_texts.append(anonymized_text)
        
        if (index + 1) % 5 == 0:
            print(f"   Processed {index + 1}/{sample_size} rows")
    
    df_sample['Anonymized_Text'] = anonymized_texts
    print("✅ PII anonymization complete")
    
    # Step 3: Profanity Masking
    print("🚫 Step 3: Masking profanity...")
    profanity_masker = SimpleProfanityMasker()
    masked_texts = []
    
    for text in anonymized_texts:
        masked_text = profanity_masker.mask_profanity(text)
        masked_texts.append(masked_text)
    
    df_sample['Masked_Text'] = masked_texts
    print("✅ Profanity masking complete")
    
    # Step 4: Sentiment Classification
    print("💭 Step 4: Classifying sentiment...")
    classifier = SimpleSentimentClassifier()
    sentiments = []
    
    for text in masked_texts:
        sentiment = classifier.infer(text)
        sentiments.append(sentiment)
    
    df_sample['Sentiment'] = sentiments
    print("✅ Sentiment classification complete")
    
    # Step 5: Save Results
    print("💾 Step 5: Saving results...")
    
    output_files = {
        'output_anonymized_simple.csv': df_sample[['Anonymized_Text']].copy(),
        'output_masked_simple.csv': df_sample[['Masked_Text']].copy(),
        'output_classified_simple.csv': df_sample.copy()
    }
    
    for filename, data in output_files.items():
        try:
            data.to_csv(filename, index=False)
            print(f"   ✅ Saved {filename}")
        except Exception as e:
            print(f"   ❌ Error saving {filename}: {e}")
    
    # Show summary
    print("\n📊 Processing Summary:")
    print(f"   📥 Input rows: {len(df_sample)}")
    print(f"   🔒 PII entities found: {sum(len(pii_service.analyze_text(str(text))) for text in df_sample.iloc[:, 0])}")
    
    sentiment_counts = pd.Series(sentiments).value_counts()
    for sentiment, count in sentiment_counts.items():
        print(f"   {sentiment}: {count} reviews")
    
    print(f"\n⏱️ Pipeline completed successfully!")
    print("🎉 Check the output files for results!")

if __name__ == "__main__":
    main()
