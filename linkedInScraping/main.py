import requests
from bs4 import BeautifulSoup
import json

search_url = 'https://www.linkedin.com/jobs-guest/jobs/api/seeMoreJobPostings/search?keywords=Technical%20Program%20Manager&start={}'
details_url = 'https://www.linkedin.com/jobs-guest/jobs/api/jobPosting/{}'
parsed_job_desc_data = []

numberOfSearchResultPages = 10


def main():

    for i in range(0,numberOfSearchResultPages):
        search_response = requests.get(search_url.format(i))

        if search_response.status_code == 200:
            with open('linkedin_job_search_results.html', 'w', encoding='utf-8') as file:
                file.write(search_response.text)
            # print(search_response.text)
            
            job_ids = parseSearchResultHtmlPage(search_response.text)
            
            for job_id in job_ids:
                details_response = requests.get(details_url.format(job_id))
            
                # with open('job_details_results.html', 'w', encoding='utf-8') as file:
                #     file.write(details_response.text)
                
                jobData = parseJobDetailsPage(details_response.text)
                # print(jobData)
                parsed_job_desc_data.append(jobData)
            
            
        else:
            print(f"Failed to retrieve jobs. Status code: {search_response.status_code}")

    print(len(parsed_job_desc_data))

    with open('parsed_details.json', 'w', encoding='utf-8') as json_file:
        json.dump(parsed_job_desc_data, json_file, indent=4)
        
    
def parseSearchResultHtmlPage(htmlString):
     # Parsing HTML to extract job IDs
    soup = BeautifulSoup(htmlString, 'html.parser')
    job_elements = soup.find_all(attrs={"data-entity-urn": True})
    job_ids = [elem['data-entity-urn'].split(':')[-1] for elem in job_elements]
    print("Extracted Job IDs:", job_ids)
  
def parseJobDetailsPage(htmlString):
    
    soup_details = BeautifulSoup(htmlString, 'html.parser')

    job_title = soup_details.select_one('h2.top-card-layout__title').text.strip()
    company_name = soup_details.select_one('a.topcard__org-name-link').text.strip()
    job_description = soup_details.select_one('div.description__text').text.strip()
    pay_information = soup_details.find(string=lambda text: "$" in text if text else False)
    page_link = soup_details.find('a', class_='topcard__link')['href']
    job_location =  soup_details.find("span", class_="topcard__flavor--bullet").get_text(strip=True),
    
    jobData = {
        'job_title': job_title,
        'company_name': company_name,
        'job_description': job_description,
        'pay_information': pay_information,
        'job_description_page_link': page_link,
        'job_location': job_location 
    }
    
    return jobData
