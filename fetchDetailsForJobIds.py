import requests
import json
import time
import parsing
from typing import Optional, Dict, Any
from appendToJsonFile import append

details_url = 'https://www.linkedin.com/jobs-guest/jobs/api/jobPosting/{}'


def make_request_with_retry(url: str, 
                          params: Optional[Dict[str, Any]] = None,
                          headers: Optional[Dict[str, Any]] = None,
                          max_attempts: int = 3) -> Optional[requests.Response]:
    """
    Makes HTTP GET request with retry functionality.
    
    Args:
        url: URL to make the request to
        params: Optional dictionary of URL parameters
        headers: Optional dictionary of HTTP headers
        max_attempts: Maximum number of attempts before giving up
        
    Returns:
        requests.Response object if successful, None if all attempts fail
    """
    attempt = 1
    while attempt <= max_attempts:
        try:
            
            response = requests.get(url, params=params, headers=headers)
            
            text = response.text
            if 'authwall' in text.lower():
                raise Exception('Error: hit LinkedIn rate limit. Api response redirected to auth wall')
                
            # Check if response was successful (200-299 status code)
            if 200 <= response.status_code < 300:
                return response
            
            # For demonstration purposes, let's show what happens on failure
            # print(f"Attempt {attempt}: Failed with status code {response.status_code}")
            
        except Exception as e:
            print(f"Attempt {attempt}: Request failed with error: {str(e)}")
        
        # Only wait if we haven't reached our last attempt
        if attempt < max_attempts:
            if attempt == 2:
                waitDuration = 8
            elif attempt == 3:
                waitDuration = 15
            else:
                waitDuration = 0.5                
            
            time.sleep(waitDuration)
            print(f"Waiting {waitDuration} seconds before next attempt...")
        
        attempt += 1
    
    print("All attempts failed")
    return None

def fetchDetailsForJobIds(job_ids):
    
    detailsForJobs = []
    
    for job_id in job_ids:
        print(f'calling LI for details on jobId: {job_id}')
        details_response = make_request_with_retry(details_url.format(job_id))
        
        jobData = parsing.parseJobDetailsPage(details_response.text)
        
        append(jobData,'jobDetailArray.json')
        # detailsForJobs.append(jobData)
        
    return detailsForJobs    
        
        
if __name__ == "__main__":
    
    with open('jobIdsFromSearch.json', 'r') as file:
        jobIds = json.load(file)
    
    deets = fetchDetailsForJobIds(jobIds)
    
    # with open('jobDetailArray.json', 'w') as f:
    #     json.dump(deets, f, indent=4) 