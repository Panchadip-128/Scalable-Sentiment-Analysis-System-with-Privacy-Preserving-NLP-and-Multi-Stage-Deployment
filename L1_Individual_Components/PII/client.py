from typing import List, Optional, Tuple, Dict
from pii import TextAnalyzerService
import pandas as pd

if __name__ == "__main__":
    print("Loading CSV file...")
    # Load the CSV file
    df = pd.read_csv("reviews.csv")
    print(f"Loaded {len(df)} rows")

    print("Initializing TextAnalyzerService...")
    # Create an instance of TextAnalyzerService with the desired model
    text_analyzer_service_model1 = TextAnalyzerService(model_choice="obi/deid_roberta_i2b2")
    print("TextAnalyzerService initialized successfully")

    # Define lists to store anonymized and deanonymized texts
    anonymized_texts = []
    deanonymized_texts = []

    print("Processing rows...")
    # Iterate over each row in the first column of the DataFrame
    for index, row in df.iterrows():
        if index % 10 == 0:  # Print progress every 10 rows
            print(f"Processing row {index + 1}/{len(df)}")
        
        text = row.iloc[0]  # Assuming the first column is the one you want to anonymize

        # Analyze text with the chosen model
        entities_model1 = text_analyzer_service_model1.analyze_text(text)

        # Anonymize text
        anonymized_text, req_dict = text_analyzer_service_model1.anonymize_text(text, entities_model1, operator="entity_counter")

        # Deanonymize text
        deanonymized_text = text_analyzer_service_model1.deanonymize_text(anonymized_text)

        # Append anonymized and deanonymized texts to lists
        anonymized_texts.append(anonymized_text)
        deanonymized_texts.append(deanonymized_text)

    # Add anonymized and deanonymized texts as new columns in the DataFrame
    df['Anonymized_Text'] = anonymized_texts
    df['Deanonymized_Text'] = deanonymized_texts

    # Drop "Deanonymized_Text" and "Rate" columns
    # df = df.drop(columns=["Deanonymized_Text","rating"])

    # Save the DataFrame to a new CSV file
    print("Saving output to CSV...")
    df.to_csv("output_anonymized.csv", index=False)
    print("Processing completed! Output saved to output_anonymized.csv")

