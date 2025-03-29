
from bs4 import BeautifulSoup
import re

def parseSearchResultHtmlPage(htmlString):
     # Parsing HTML to extract job IDs
    soup = BeautifulSoup(htmlString, 'html.parser')
    job_elements = soup.find_all(attrs={"data-entity-urn": True})
    job_ids = [elem['data-entity-urn'].split(':')[-1] for elem in job_elements]
    print("Extracted Job IDs:", job_ids)
    return job_ids
  
def parseJobDetailsPage(htmlString):
    
    htmlString = remove_html_whitespace(htmlString)
    
    soup_details = BeautifulSoup(htmlString, 'html.parser')

    try:

        job_title = soup_details.select_one('h2.top-card-layout__title').text.strip()
        company_name = soup_details.select_one('a.topcard__org-name-link').text.strip()
        job_description = soup_details.select_one('div.description__text').text.strip()
        pay_information = soup_details.find(string=lambda text: "$" in text if text else False)
        page_link = soup_details.find('a', class_='topcard__link')['href']
        job_location =  soup_details.find("span", class_="topcard__flavor--bullet").get_text(strip=True),
        
    except Exception as e:
        print(f"Unexpected error: {str(e)}")
        print(f'html string passed to soup: \n\n{htmlString}')
        
    jobData = {
        'job_title': job_title,
        'company_name': company_name,
        'job_description': job_description,
        'pay_information': pay_information,
        'job_description_page_link': page_link,
        'job_location': job_location,
        'raw_html': htmlString 
    }
    
    return jobData

def remove_html_whitespace(html_string):
    # Remove whitespace between tags
    html_string = re.sub(r'>\s+<', '><', html_string)
    # Remove leading/trailing whitespace
    html_string = re.sub(r'^\s+|\s+$', '', html_string)
    return html_string