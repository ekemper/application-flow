import requests
import parsing
import json

search_url = 'https://www.linkedin.com/jobs-guest/jobs/api/seeMoreJobPostings/search?keywords=Technical%20Program%20Manager&start={}'
numberOfSearchResultPages = 100
jobIds = []

for i in range(0,numberOfSearchResultPages):
    search_response = requests.get(search_url.format(i))

    if search_response.status_code == 200:
        jobIdsFromPage = parsing.parseSearchResultHtmlPage(search_response.text)
        jobIds = jobIds + jobIdsFromPage
        
    else:
        print(f"Failed to retrieve jobs. Status code: {search_response.status_code}")
        

with open('jobIdsFromSearch.json', 'w') as f:
    json.dump(jobIds, f, indent=4) 