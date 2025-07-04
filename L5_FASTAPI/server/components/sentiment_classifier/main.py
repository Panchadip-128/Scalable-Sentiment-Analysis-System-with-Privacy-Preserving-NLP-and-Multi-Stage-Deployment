import warnings
from pathlib import Path
import time
import numpy as np

# Try to import heavy ML dependencies, fall back to simple classifier if not available
try:
    from transformers import AutoModelForSequenceClassification, AutoTokenizer
    import openvino as ov
    import torch
    HEAVY_DEPS_AVAILABLE = True
except ImportError:
    HEAVY_DEPS_AVAILABLE = False
    print("⚠️  Heavy ML dependencies not available, using lightweight sentiment classifier")

class SimpleSentimentClassifier:
    """Lightweight rule-based sentiment classifier as fallback"""
    
    def __init__(self):
        self.positive_words = {
            'good', 'great', 'excellent', 'amazing', 'wonderful', 'fantastic', 'awesome', 
            'love', 'like', 'enjoy', 'happy', 'pleased', 'satisfied', 'perfect', 'best',
            'brilliant', 'outstanding', 'superb', 'terrific', 'marvelous', 'fabulous'
        }
        self.negative_words = {
            'bad', 'terrible', 'awful', 'horrible', 'hate', 'dislike', 'angry', 'sad',
            'disappointed', 'frustrated', 'annoying', 'worst', 'poor', 'disgusting',
            'pathetic', 'useless', 'boring', 'mediocre', 'appalling', 'dreadful'
        }
    
    def predict(self, text):
        """Simple sentiment prediction based on word matching"""
        text_lower = text.lower()
        words = text_lower.split()
        
        positive_score = sum(1 for word in words if word in self.positive_words)
        negative_score = sum(1 for word in words if word in self.negative_words)
        
        if positive_score > negative_score:
            return "POSITIVE", 0.7 + min(0.3, positive_score * 0.1)
        elif negative_score > positive_score:
            return "NEGATIVE", 0.7 + min(0.3, negative_score * 0.1)
        else:
            return "NEUTRAL", 0.5

class TextClassifier:
    def __init__(self, checkpoint=None, model_dir="my_models/", max_seq_length=128):
        self.checkpoint = checkpoint
        self.model_dir = model_dir
        self.max_seq_length = max_seq_length
        
        if HEAVY_DEPS_AVAILABLE and checkpoint:
            try:
                self._init_heavy_model()
                self.use_heavy_model = True
                print(f"✅ Loaded heavy ML model: {checkpoint}")
            except Exception as e:
                print(f"⚠️  Failed to load heavy model: {e}")
                self._init_simple_model()
                self.use_heavy_model = False
        else:
            self._init_simple_model()
            self.use_heavy_model = False
    
    def _init_heavy_model(self):
        """Initialize the heavy ML-based model"""
        self.model = AutoModelForSequenceClassification.from_pretrained(self.checkpoint)
        self.tokenizer = AutoTokenizer.from_pretrained(self.checkpoint)
        self.ir_xml_name = self.checkpoint + ".xml"
        self.ir_xml_path = Path(self.model_dir) / self.ir_xml_name
        self.input_info = [(ov.PartialShape([1, -1]), ov.Type.i64), (ov.PartialShape([1, -1]), ov.Type.i64)]
        self.default_input = torch.ones(1, self.max_seq_length, dtype=torch.int64)
        self.inputs = {
            "input_ids": self.default_input,
            "attention_mask": self.default_input,
        }
        self.ov_model = ov.convert_model(self.model, input=self.input_info, example_input=self.inputs)
        ov.save_model(self.ov_model, self.ir_xml_path)
        self.core = ov.Core()
        self.device = 'AUTO'
        self.compiled_model = self.core.compile_model(self.ov_model, self.device)
        self.infer_request = self.compiled_model.create_infer_request()
    
    def _init_simple_model(self):
        """Initialize the simple rule-based model"""
        self.simple_classifier = SimpleSentimentClassifier()
        print("✅ Using lightweight rule-based sentiment classifier")

    def softmax(self, x):
        e_x = np.exp(x - np.max(x))
        res = e_x / e_x.sum()
        return res

    def infer(self, input_text):
        """Main inference method that chooses between heavy and simple models"""
        if self.use_heavy_model:
            return self._infer_heavy(input_text)
        else:
            return self._infer_simple(input_text)
    
    def _infer_heavy(self, input_text):
        """Heavy ML model inference"""
        input_text = self.tokenizer(
            input_text,
            truncation=True,
            return_tensors="np",
        )
        inputs = dict(input_text)
        label = {0: "NEGATIVE", 1: "POSITIVE"}
        result = self.infer_request.infer(inputs=inputs)
        for i in result.values():
            probability = np.argmax(self.softmax(i))
        return label[probability]
    
    def _infer_simple(self, input_text):
        """Simple rule-based inference"""
        sentiment, confidence = self.simple_classifier.predict(input_text)
        return sentiment
