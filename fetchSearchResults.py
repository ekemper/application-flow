import requests
import json
import os
import time
from pprint import pprint
import reprlib
from dotenv import load_dotenv
load_dotenv()


# Configure truncation limits
r = reprlib.Repr()
r.maxstring = 50  # Max characters for strings
r.maxlist = 5     # Max items for lists
r.maxdict = 5     # Max items for dictionaries


def fetch_google_jobs(query, num_pages=1):
    results = []

    next_page_token = None
    end = False

    for page in range(num_pages):

        if end:
            break

        time.sleep(1.3)

        params = {
            "engine": "google_jobs",
            "q": query,
            "location": "United States",
            "api_key": os.environ.get("SERPAPI_KEY"),
            "next_page_token": next_page_token
        }

        response = requests.get("https://serpapi.com/search", params=params)
        data = response.json()

        try:    
            next_page_token = data['serpapi_pagination']['next_page_token']
        except Exception as e:
            print(f"Error Type: {type(e).__name__}")
            print(f"Error Message: {str(e)}")
            print(f'ending search...')
            end = True

        jobs = data.get("jobs_results", [])
        print(len(jobs))
        for job in jobs:
            salary = job.get("detected_extensions", {}).get("salary")  # May not be present
            results.append(
                {
                    "title": job.get("title"),
                    "name": job.get("name"),
                    "company": job.get("company_name"),
                    "location": job.get("location"),
                    "via": job.get("via"),
                    "posted": job.get("detected_extensions", {}).get("posted_at"),
                    "salary": salary,
                    "extensions": job.get("extensions"),
                    "detected_extensions": job.get("detected_extensions"),
                    "description": job.get("description"),
                    "share_link": job.get("share_link"),
                    "job_highlights": job.get("job_highlights"),
                    "apply_options": job.get("apply_options"),
                    "job_id": job.get("job_id"),
                }
            )

    return results

if __name__ == "__main__":
    
    query = "Technical Program Manager"
    jobs = fetch_google_jobs(query, num_pages=50)
    file_path = 'jobDetails.json'

    try:
        # Attempt to serialize the Python object to JSON
        json_data = json.dumps(jobs, indent=4)
        
        # Write the serialized JSON to the file
        with open(file_path, 'w') as f:
            f.write(json_data)
        print(f"Data successfully written to {file_path}")
    except (TypeError, ValueError) as e:
        print(f"Error serializing data to JSON: {e}")
    except Exception as e:
        print(f"Unexpected error: {type(e).__name__} - {e}")