#!/usr/bin/env python3
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from wordcloud import WordCloud
from collections import Counter
import re
import os

# Function to load and inspect the dataset
def load_dataset(file_path):
    # check if file exists
    if not os.path.exists(file_path):
        print(f"Error: The file '{file_path}' does not exist.")
        return None

    # Load the JSON dataset into a pandas DataFrame
    df = pd.read_json(file_path)
    return df

def normalize_data(df):
    # Check if the 'data' column exists
    if 'data' not in df.columns:
        print("Error: 'data' column not found in the dataset.")
        return None

    # Print the content of the first row to inspect the structure
    print(df['data'][0])  # This will print the JSON-like structure

    # Load the JSON content from the 'data' column (it's in the form of a string)
    json_data = json.loads(df['data'][0])  # Load the JSON from the first row
    normalized_data = pd.json_normalize(json_data, sep='_')  # Flatten the structure
    return normalized_data


# Apply the normalization function
normalized_df = normalize_data(df)

# Display the normalized data
print(normalized_df.head())

# Function to display basic information about the dataset
def display_basic_info(df):
    print("\n--- Basic Dataset Info ---")
    print(df.info())  # Get basic info: data types, non-null counts
    print("\n--- Basic Statistics ---")
    print(df.describe(include='all'))  # Summary statistics for all columns

# Function to check for missing data
def check_missing_data(df):
    print("\n--- Missing Data ---")
    missing_data = df.isnull().sum()
    print(missing_data)

    # Optionally fill missing data (example: with 'N/A')
    df.fillna('N/A', inplace=True)

# Function to visualize the distribution of a categorical column
def visualize_category_distribution(df):
    if 'Category' in df.columns:
        print("\n--- Category Distribution ---")
        plt.figure(figsize=(10,6))
        sns.countplot(data=df, x='Category', palette='Set2')
        plt.title('Distribution of Categories')
        plt.xlabel('Category')
        plt.ylabel('Frequency')
        plt.xticks(rotation=45)
        plt.show()

# Function to visualize the distribution of answer lengths
def visualize_answer_length(df):
    # Check if the 'Answer' column exists and create a new column for answer lengths
    if 'Answer' in df.columns:
        df['Answer Length'] = df['Answer'].apply(len)

        print("\n--- Answer Length Distribution ---")
        plt.figure(figsize=(10,6))
        df['Answer Length'].hist(bins=30, color='skyblue')
        plt.title('Distribution of Answer Lengths')
        plt.xlabel('Length of Answers')
        plt.ylabel('Frequency')
        plt.show()

# Function to create a word cloud from the 'Answer' column
def generate_word_cloud(df):
    if 'Answer' in df.columns:
        print("\n--- Word Cloud for Answers ---")
        # Combine all answers into a single string
        text = ' '.join(df['Answer'].astype(str))

        # Generate and display the word cloud
        wordcloud = WordCloud(width=800, height=400, background_color='white').generate(text)
        
        plt.figure(figsize=(10,6))
        plt.imshow(wordcloud, interpolation='bilinear')
        plt.axis('off')
        plt.title('Word Cloud of Answers')
        plt.show()

# Function to analyze word frequency in the 'Answer' column
def analyze_word_frequency(df):
    if 'Answer' in df.columns:
        print("\n--- Most Frequent Words in Answers ---")
        # Tokenize the text (remove non-alphabetic characters)
        words = ' '.join(df['Answer']).lower()
        words = re.findall(r'\b\w+\b', words)

        # Get the most common words
        word_counts = Counter(words)

        # Display the 10 most common words
        print(word_counts.most_common(10))

# Function to visualize relationships between columns (e.g., category vs. answer length)
def visualize_relationship(df):
    if 'Category' in df.columns and 'Answer Length' in df.columns:
        print("\n--- Answer Length by Category ---")
        plt.figure(figsize=(10,6))
        sns.boxplot(data=df, x='Category', y='Answer Length')
        plt.title('Answer Length by Category')
        plt.xlabel('Category')
        plt.ylabel('Answer Length')
        plt.xticks(rotation=45)
        plt.show()

# Main function to run the full EDA process
def main():
    # Step 1: Load the dataset
    file_path = "/home/kenobi/pyshell/kagglebox/data/Dataset Question Answering for Admission of Higher Education Institution/dataset_annotationfinal.json"
  # Replace with your actual file path
    df = load_dataset(file_path)

    # Step 2: Display basic information about the dataset
    display_basic_info(df)

    # Step 3: Check for missing data and handle them (filling with 'N/A')
    check_missing_data(df)

    # Step 4: Visualize the distribution of categories (if applicable)
    visualize_category_distribution(df)

    # Step 5: Visualize the distribution of answer lengths
    visualize_answer_length(df)

    # Step 6: Generate a word cloud for the answers
    generate_word_cloud(df)

    # Step 7: Analyze word frequency in the answers
    analyze_word_frequency(df)

    # Step 8: Visualize relationships between columns (e.g., category vs. answer length)
    visualize_relationship(df)

if __name__ == "__main__":
    main()

