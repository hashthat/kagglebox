#!/usr/bin/env python3
import os
import pandas as pd
import json
import random
import string

# Define constants
DATASET_FILENAME = "dataset_annotationfinal.json"  # Path to your downloaded JSON file
DATASET_PATH = "/home/kenobi/pyshell/kagglebox/data/Dataset Question Answering for Admission of Higher Education Institution/" + DATASET_FILENAME

# Helper function to generate synthetic large dataset if needed
def generate_large_dataset(output_filename, num_rows=100000):
    """
    Generates a large synthetic dataset to simulate a larger file.
    This is only necessary if you need to create a big dataset for testing.
    """
    questions = [
        "What is your motivation for applying?",
        "Describe your long-term career goals.",
        "How do you handle stress?",
        "What is your research experience?",
        "Explain how you plan to contribute to the university community."
    ]
    
    categories = ["General", "Science", "Arts", "Technology", "Social Science"]
    
    # Generate random answers to the questions
    data = []
    for _ in range(num_rows):
        question = random.choice(questions)
        answer = ''.join(random.choices(string.ascii_uppercase + string.digits, k=300))  # Random "answer"
        category = random.choice(categories)
        data.append([question, answer, category])
    
    # Create DataFrame
    df = pd.DataFrame(data, columns=["Question", "Answer", "Category"])
    
    # Save to CSV
    df.to_csv(output_filename, index=False)
    print(f"Large dataset with {num_rows} rows generated successfully: {output_filename}")

# Read and format the JSON dataset
def read_and_format_dataset(filename=DATASET_PATH):
    """
    Reads the dataset from a JSON file, formats it, and returns the data as a pandas DataFrame.
    The function will handle missing values, and apply some basic formatting.
    """
    if not os.path.exists(filename):
        print(f"Error: The file '{filename}' does not exist.")
        return None
    
    # Load the JSON file into a pandas DataFrame
    print("Loading dataset...")
    with open(filename, "r") as f:
        data = json.load(f)
    
    # Print out the structure of the JSON data (just for understanding)
    print(f"Dataset structure: {type(data)}")
    
    # Print the top-level keys to understand the structure
    if isinstance(data, dict):
        print(f"Top-level keys in the JSON file: {data.keys()}")
    
    # Check if the data is a list of records or a dictionary with nested records
    if isinstance(data, list):
        df = pd.DataFrame(data)
    else:
        # If it's a dictionary, you may need to extract nested information
        print("Dataset seems to be a dictionary, inspecting keys...")
        for key in data.keys():
            print(f"Key: {key}, Value: {data[key]}")  # Print key-value pairs
    
        df = pd.json_normalize(data)  # Normalize nested structures if needed
    
    return df

# Display the formatted dataset in a user-friendly way
def display_data_summary(df):
    """
    Displays a summary of the dataset to the user.
    Shows the first few records and provides basic statistics for each column.
    """
    if df is None or df.empty:
        print("The dataset is empty or failed to load.")
        return
    
    print("\n--- Dataset Summary ---")
    print(f"Total records in dataset: {len(df)}")
    
    # Display the first 10 rows
    print("\nFirst 10 records in the dataset:")
    print(df.head(10))  # Display top 10 records
    
    # Display basic statistics (if applicable)
    print("\nBasic Statistics of Columns:")
    print(df.describe(include='all'))  # Summary statistics for all columns
    
    print("\n--- End of Dataset Summary ---\n")

# Main function to run the program
def main():
    # Uncomment the line below to generate a large dataset if needed
    # generate_large_dataset("large_qa_dataset.csv", num_rows=100000)  # Generate a large file with 100,000 rows

    # Step 1: Read the dataset and format it
    print(f"Dataset file path: {DATASET_PATH}")  # Check the dataset path
    df = read_and_format_dataset(DATASET_PATH)

    if df is not None:
        # Step 2: Display the data summary to the user
        display_data_summary(df)

        # Step 3: Additional processing if needed (e.g., save the formatted dataset)
        output_filename = "formatted_qa_data.csv"
        df.to_csv(output_filename, index=False)
        print(f"\nFormatted data saved to {output_filename}")
    else:
        print("Failed to load dataset. Please check the file path.")

if __name__ == "__main__":
    main()

