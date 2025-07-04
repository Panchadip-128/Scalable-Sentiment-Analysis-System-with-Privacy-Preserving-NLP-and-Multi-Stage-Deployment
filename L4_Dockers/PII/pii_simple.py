import re
import hashlib
from typing import List, Tuple, Dict
import pandas as pd

class SimplePIIService:
    """
    A lightweight PII service that uses regex patterns instead of heavy ML models.
    Much faster for basic PII detection and anonymization.
    """
    
    def __init__(self):
        """Initialize the simple PII service with regex patterns."""
        # Define regex patterns for common PII
        self.patterns = {
            'email': r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b',
            'phone': r'(\+?\d{1,4}[-.\s]?)?\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4}',
            'ssn': r'\b\d{3}-\d{2}-\d{4}\b',
            'credit_card': r'\b\d{4}[-\s]?\d{4}[-\s]?\d{4}[-\s]?\d{4}\b',
            'name': r'\b[A-Z][a-z]+ [A-Z][a-z]+\b',  # Simple name pattern
        }
        
        self.replacement_map = {}
        
    def analyze_text(self, text: str) -> List[Dict]:
        """
        Analyze text for PII entities using regex patterns.
        
        Args:
            text: Text to analyze
            
        Returns:
            List of detected entities
        """
        entities = []
        
        for entity_type, pattern in self.patterns.items():
            matches = re.finditer(pattern, text)
            for match in matches:
                entities.append({
                    'entity_type': entity_type,
                    'start': match.start(),
                    'end': match.end(),
                    'text': match.group()
                })
        
        return entities
    
    def anonymize_text(self, text: str, entities: List[Dict], operator: str = "replace") -> Tuple[str, Dict]:
        """
        Anonymize text by replacing detected PII entities.
        
        Args:
            text: Original text
            entities: List of detected entities
            operator: Anonymization method ('replace', 'mask', 'encrypt')
            
        Returns:
            Tuple of (anonymized_text, mapping_dict)
        """
        anonymized_text = text
        mapping = {}
        
        # Sort entities by start position in reverse order to avoid index shifting
        sorted_entities = sorted(entities, key=lambda x: x['start'], reverse=True)
        
        for entity in sorted_entities:
            original_text = entity['text']
            entity_type = entity['entity_type']
            start = entity['start']
            end = entity['end']
            
            if operator == "replace":
                replacement = f"[{entity_type.upper()}]"
            elif operator == "mask":
                replacement = "*" * len(original_text)
            elif operator == "encrypt":
                # Simple hash-based encryption
                hash_obj = hashlib.md5(original_text.encode())
                replacement = f"[{entity_type.upper()}_{hash_obj.hexdigest()[:8]}]"
            else:
                replacement = f"[{entity_type.upper()}]"
            
            # Replace the text
            anonymized_text = anonymized_text[:start] + replacement + anonymized_text[end:]
            
            # Store mapping for deanonymization
            mapping[replacement] = original_text
        
        return anonymized_text, mapping
    
    def deanonymize_text(self, anonymized_text: str) -> str:
        """
        Deanonymize text by restoring original values.
        For this simple implementation, we just return the anonymized text.
        """
        return anonymized_text

# Create a simple client for testing
if __name__ == "__main__":
    # Test the simple PII service
    pii_service = SimplePIIService()
    
    test_text = "Hello John Smith, your email is john.smith@example.com and phone is 555-123-4567"
    print(f"Original: {test_text}")
    
    entities = pii_service.analyze_text(test_text)
    print(f"Entities found: {entities}")
    
    anonymized, mapping = pii_service.anonymize_text(test_text, entities, "replace")
    print(f"Anonymized: {anonymized}")
    print(f"Mapping: {mapping}")
