import warnings
from pathlib import Path
import time
from transformers import AutoModelForSequenceClassification, AutoTokenizer, pipeline
import numpy as np
import torch

class TextClassifier:
    def __init__(self, checkpoint, max_seq_length=128):
        self.checkpoint = checkpoint
        self.max_seq_length = max_seq_length
        
        # Initialize the sentiment analysis pipeline
        self.classifier = pipeline(
            "sentiment-analysis",
            model=checkpoint,
            return_all_scores=True
        )
        
    def infer(self, text):
        """
        Perform sentiment analysis on the input text.
        
        Args:
            text (str): Input text to analyze
            
        Returns:
            str: Sentiment label ('POSITIVE' or 'NEGATIVE')
        """
        try:
            # Ensure text is a string and handle edge cases
            if text is None:
                return "UNKNOWN"
            
            # Convert to string if it's not already
            text_str = str(text).strip()
            
            # Handle empty text
            if not text_str:
                return "UNKNOWN"
            
            # Get prediction
            results = self.classifier(text_str)
            
            # Find the prediction with highest score
            best_prediction = max(results[0], key=lambda x: x['score'])
            
            return best_prediction['label']
            
        except Exception as e:
            print(f"Error during inference: {e}")
            print(f"Text type: {type(text)}, Text value: {repr(text)}")
            return "UNKNOWN"
