#!/usr/bin/env python3
import csv
import os
import subprocess

# Define your dataset file path
DATASET_FILENAME = "Q&A_for_Admission.csv"  # Update with the actual filename
DATASET_PATH = os.path.join("data", DATASET_FILENAME)

# Download Dataset Function
def download_kaggle_dataset():
    """Download dataset using Kaggle API."""
    dataset_id = "<DATASET_ID>"  # Replace with actual Kaggle dataset ID
    try:
        if not os.path.exists("data"):
            os.makedirs("data")
        subprocess.run(["kaggle", "datasets", "download", "-d", dataset_id, "-p", "data"], check=True)
        print("Dataset downloaded successfully.")
    except subprocess.CalledProcessError as e:
        print("Failed to download dataset:", e)

# Read Dataset Function
def read_dataset(filename=DATASET_PATH):
    """Read the dataset from the CSV file."""
    if not os.path.exists(filename):
        print(f"Error: '{filename}' does not exist.")
        return []

    data = []
    with open(filename, mode='r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            # Extract relevant columns here (adjust based on the actual structure of the dataset)
            question = row.get("Question")
            answer = row.get("Answer")
            category = row.get("Category", "General")

            data.append({
                "Question": question,
                "Answer": answer,
                "Category": category
            })
    return data

# Display Function to Summarize or Extract Information
def display_summary(data):
    """Display a summary or sample of the dataset."""
    print("\n--- Sample of Q&A Data ---")
    for item in data[:10]:  # Display the first 10 records
        print(f"Question: {item['Question']}\nAnswer: {item['Answer']}\nCategory: {item['Category']}\n")

# Main Script
def main():
    # Step 1: Download the dataset
    download_kaggle_dataset()

    # Step 2: Load and display the dataset
    data = read_dataset()
    if data:
        display_summary(data)

if __name__ == "__main__":
    main()

