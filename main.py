import requests
import json
import time
import parsing
from openAICall import callOpenAi
from jobScoringPrompt import prompt 
import appendToJsonFile



scored_results = []

outputFileName = 'scored_results.json'

with open(outputFileName, 'w', encoding='utf-8') as json_file:
    json.dump(scored_results, json_file, indent=4)

def fetchScoredDataForJob(details_response):
    jobData = parsing.parseJobDetailsPage(details_response.text)
    
    resp = callOpenAi(prompt(jobData))
    result = resp.model_dump_json()
    resp_data = json.loads(result)['output'][0]['content'][0]['text']
    
    print(resp_data)
        
    return {
        'input': jobData,
        'output': json.loads(resp_data)
    }
    
def fetchDetailsForJobIds(job_ids):
    for job_id in job_ids:
        print(f'calling LI for details on jobId: {job_id}')
        details_response = requests.get(details_url.format(job_id))
    
        scoredJobData = fetchScoredDataForJob(details_response)
        scored_results.append(scoredJobData)
        appendToJsonFile.append(scoredJobData, outputFileName)
     
    
# def main():

    # for i in range(0,numberOfSearchResultPages):
    #     search_response = requests.get(search_url.format(i))

    #     if search_response.status_code == 200:
    #         job_ids = parsing.parseSearchResultHtmlPage(search_response.text)
    #         fetchDetailsForJobIds(job_ids)
            
    #     else:
    #         print(f"Failed to retrieve jobs. Status code: {search_response.status_code}")

    # print(len(scored_results))
        

if __name__ == "__main__":    

    # main()