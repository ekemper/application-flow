import pandas as pd
import os

file_path = 'jobDetails.json'

# Check if the file exists and is not empty
if not os.path.exists(file_path) or os.stat(file_path).st_size == 0:
    print(f"Error: '{file_path}' does not exist or is empty.")
else:
    try:
        # Attempt to read the JSON file
        df = pd.read_json(file_path)
        print(len(df))

        subset_columns = ['job_id', 'title']

        # Identify duplicates based on 'job_id' and 'title'
        duplicates = df[df.duplicated(subset=subset_columns, keep='first')]

        # Count the number of duplicates
        num_duplicates = len(duplicates)
        print(f"Number of duplicate entries: {num_duplicates}")

    except ValueError as e:
        print(f"Error reading JSON file: {e}")