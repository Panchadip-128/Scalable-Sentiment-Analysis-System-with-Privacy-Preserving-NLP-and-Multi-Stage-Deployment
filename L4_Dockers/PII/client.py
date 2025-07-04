from typing import List, Optional, Tuple, Dict
from pii import TextAnalyzerService
import pandas as pd
import time

if __name__ == "__main__":
    print("Starting PII Processing with Presidio...")
    print("Warning: This uses heavy transformer models and may be slow!")
    
    start_time = time.time()
    
    # Load the CSV file
    print("Loading CSV file...")
    df = pd.read_csv("../reviews.csv")
    print(f"Loaded {len(df)} rows")
    
    # Create an instance of TextAnalyzerService with a lighter, faster model
    # Using spaCy-based model instead of heavy transformer model
    print("Initializing TextAnalyzerService...")
    text_analyzer_service_model1 = TextAnalyzerService(model_choice="en_core_web_sm")
    
    # Define lists to store anonymized and deanonymized texts
    anonymized_texts = []
    deanonymized_texts = []
    
    # Process only first 5 rows to avoid long processing time
    sample_size = min(5, len(df))
    print(f"Processing first {sample_size} rows (for demonstration)...")
    
    # Iterate over each row in the first column of the DataFrame
    for index, row in df.head(sample_size).iterrows():
        print(f"Processing row {index + 1}/{sample_size}")
        text = str(row.iloc[0])  # Use iloc for position-based access

        # Analyze text with the chosen model
        entities_model1 = text_analyzer_service_model1.analyze_text(text)

        # Anonymize text
        anonymized_text, req_dict = text_analyzer_service_model1.anonymize_text(text, entities_model1, operator="encrypt")

        # Deanonymize text
        deanonymized_text = text_analyzer_service_model1.deanonymize_text(anonymized_text)

        # Append anonymized and deanonymized texts to lists
        anonymized_texts.append(anonymized_text)
        deanonymized_texts.append(deanonymized_text)

    # Create a sample dataframe with processed data
    sample_df = df.head(sample_size).copy()
    sample_df['Anonymized_Text'] = anonymized_texts
    sample_df['Deanonymized_Text'] = deanonymized_texts

    # Drop "Deanonymized_Text" and "rating" columns if they exist
    columns_to_drop = [col for col in ["Deanonymized_Text", "rating"] if col in sample_df.columns]
    if columns_to_drop:
        sample_df = sample_df.drop(columns=columns_to_drop)

    # Save the DataFrame to a new CSV file
    output_file = "output_anonymized.csv"
    sample_df.to_csv(output_file, index=False)
    
    end_time = time.time()
    processing_time = end_time - start_time
    
    print(f"\nProcessing completed!")
    print(f"Processed {sample_size} rows in {processing_time:.2f} seconds")
    print(f"Output saved to: {output_file}")
    print(f"Average time per row: {processing_time/sample_size:.3f} seconds")

