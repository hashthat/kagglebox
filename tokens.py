#!/usr/bin/env python3
import pandas as pd
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer
from sklearn.feature_extraction.text import TfidfVectorizer
import string


# Download necessary NLTK data
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('punkt_tab')
# Path to your dataset
file_path = '/home/kenobi/pyshell/kagglebox/data/Dataset Question Answering for Admission of Higher Education Institution/dataset_annotationfinal.json'

# Load dataset
df = pd.read_json(file_path)

# Check the column names to identify the correct one
print("Dataset Columns:", df.columns)

# The 'data' column seems to contain the relevant information, based on previous analysis

# Tokenization & Lowercasing
def tokenize_and_lowercase(text):
    return word_tokenize(text.lower())

# Remove punctuation
def remove_punctuation(tokens):
    table = str.maketrans('', '', string.punctuation)
    return [word.translate(table) for word in tokens if word.translate(table)]

# Remove stopwords
def remove_stopwords(tokens):
    stop_words = set(stopwords.words('english'))
    return [word for word in tokens if word not in stop_words]

# Stemming
def stem_tokens(tokens):
    stemmer = PorterStemmer()
    return [stemmer.stem(word) for word in tokens]

# Apply text preprocessing to the 'data' column (you might need to adjust this if 'data' is not the correct column)
df['tokens'] = df['data'].apply(lambda x: tokenize_and_lowercase(str(x)))  # Tokenize & Lowercase
df['tokens'] = df['tokens'].apply(remove_punctuation)  # Remove Punctuation
df['tokens'] = df['tokens'].apply(remove_stopwords)  # Remove Stopwords
df['tokens'] = df['tokens'].apply(stem_tokens)  # Apply Stemming

# Convert tokens back to text (if needed)
df['processed_text'] = df['tokens'].apply(lambda tokens: ' '.join(tokens))

# Optional: Vectorize text using TF-IDF
vectorizer = TfidfVectorizer(stop_words='english')
X = vectorizer.fit_transform(df['processed_text'])

# Convert TF-IDF result to a DataFrame for easier inspection
tfidf_df = pd.DataFrame(X.toarray(), columns=vectorizer.get_feature_names_out())

# Print the TF-IDF DataFrame (for checking the vectorized data)
print(tfidf_df.head())

# Save the preprocessed DataFrame (tokens and processed text) to CSV
df.to_csv('preprocessed_data.csv', index=False)
print("Preprocessed data saved to 'preprocessed_data.csv'")

