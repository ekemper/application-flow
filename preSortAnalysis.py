import pandas as pd

df = pd.read_json('preScoredJobDetails_sans_raw_html.json', lines=True)

subset_columns = ['company_name', 'job_title', 'job_description']
# Drop rows with missing values in the relevant columns
df = df.dropna(subset=subset_columns)

# Identify duplicates based on 'company name', 'job title', and 'job description'
duplicates = df[df.duplicated(subset=subset_columns, keep='first')]

# Count the number of duplicates
num_duplicates = len(duplicates)
print(f"Number of duplicate entries: {num_duplicates}")

# Store duplicates in a separate DataFrame or object
if num_duplicates > 0:
    print("Duplicate entries:")
    print(duplicates)
# Save the updated DataFrame back to a JSON file if needed
# df.to_json('.json', orient='records', lines=True)