from transformers import pipeline

class TextClassifier:
    def __init__(self, checkpoint):
        """
        Initialize the TextClassifier with a pretrained model.
        
        Args:
            checkpoint: The model checkpoint/name from HuggingFace
        """
        self.checkpoint = checkpoint
        # Use transformers pipeline which handles everything internally
        self.classifier = pipeline(
            "sentiment-analysis", 
            model=checkpoint,
            return_all_scores=False
        )
    
    def infer(self, text):
        """
        Perform sentiment classification on the input text.
        
        Args:
            text: Input text to classify
            
        Returns:
            str: Sentiment label (POSITIVE or NEGATIVE)
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
            
            # Perform classification
            result = self.classifier(text_str)
            return result[0]['label']
        except Exception as e:
            print(f"Error in classification: {e}")
            print(f"Text type: {type(text)}, Text value: {repr(text)}")
            return "UNKNOWN"
