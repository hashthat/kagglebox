#!/usr/bin/env python3
import pandas as pd
import json
import os
import matplotlib.pyplot as plt
import seaborn as sns
from wordcloud import WordCloud

# Load the dataset (with the correct path)
def load_dataset(file_path):
    # Check if the file exists at the specified path
    if not os.path.exists(file_path):
        print(f"Error: The file '{file_path}' does not exist.")
        return None

    # Load the JSON data from the file
    df = pd.read_json(file_path)
    return df

# Normalize the nested JSON data
def normalize_data(df):
    # Ensure 'data' column exists in the dataframe
    if 'data' not in df.columns:
        print("Error: 'data' column not found in the dataset.")
        return None

    # Print the content of the first row in the 'data' column to inspect it
    print("\n--- Inspecting the data column ---")
    print(df['data'][0])  # Print the first entry in 'data' to inspect its structure

    # Since the first entry in 'data' is already a dict, you don't need json.loads
    json_data = df['data'][0]  # This is already a dictionary

    # Flatten the JSON dictionary
    normalized_data = pd.json_normalize(json_data, sep='_')  # Flatten the structure into a DataFrame
    return normalized_data

# Basic summary of the dataset
def display_basic_info(df):
    print("\n--- Basic Dataset Info ---")
    print(df.info())
    print("\n--- Basic Statistics ---")
    print(df.describe(include='all'))

# Check for missing data
def check_missing_data(df):
    print("\n--- Missing Data ---")
    missing_data = df.isnull().sum()
    print(missing_data)

# Visualize the distribution of a specific column (if applicable)
def visualize_category_distribution(df):
    if 'category' in df.columns:
        print("\n--- Category Distribution ---")
        plt.figure(figsize=(10,6))
        sns.countplot(data=df, x='category', palette='Set2')
        plt.title('Distribution of Categories')
        plt.xlabel('Category')
        plt.ylabel('Frequency')
        plt.xticks(rotation=45)
        plt.show()

# Word Cloud for textual data (if applicable)
def generate_word_cloud(df):
    if 'text' in df.columns:  # Assuming the normalized data has a 'text' field
        print("\n--- Word Cloud ---")
        text = ' '.join(df['text'].astype(str))  # Combine all text fields into one string
        wordcloud = WordCloud(width=800, height=400, background_color='white').generate(text)

        plt.figure(figsize=(10,6))
        plt.imshow(wordcloud, interpolation='bilinear')
        plt.axis('off')
        plt.title('Word Cloud')
        plt.show()

# Main function
def main():
    # Correct file path
    file_path = "/home/kenobi/pyshell/kagglebox/data/Dataset Question Answering for Admission of Higher Education Institution/dataset_annotationfinal.json"

    # Step 1: Load the dataset
    df = load_dataset(file_path)

    if df is not None:
        # Step 2: Normalize the nested JSON structure
        normalized_df = normalize_data(df)

        if normalized_df is not None:
            # Step 3: Perform EDA on the normalized data
            display_basic_info(normalized_df)
            check_missing_data(normalized_df)

            # Step 4: Visualize (optional, based on columns available)
            visualize_category_distribution(normalized_df)  # Example visualization
            generate_word_cloud(normalized_df)  # Example word cloud for text columns
        else:
            print("Error: Normalization of data failed.")
    else:
        print("Failed to load dataset. Please check the file path.")

if __name__ == "__main__":
    main()

