#!/usr/bin/env python3
from kaggle.api.kaggle_api_extended import KaggleApi

# Set up Kaggle API client
api = KaggleApi()
api.authenticate()

# Replace 'dataset_id' with the actual dataset ID from the Kaggle page
dataset_id = 'jocelyndumlao/q-and-a-for-admission-of-higher-education-institution'  # Example: 'tensorflow/tensorflow'
api.dataset_download_files(dataset_id, path='data', unzip=True)

print("Dataset downloaded successfully.")

