import os
from openai import OpenAI
from dotenv import load_dotenv
load_dotenv()
from jobScoringPrompt import prompt 
import re

apiKey = os.environ.get("OPENAI_API_KEY")
client = OpenAI(api_key=apiKey)

def callOpenAi(prompt):
    response = client.responses.create(
        model="gpt-4o-mini",
        instructions="You are a helpful assistant.",
        input=prompt,
    )
    return response

def clean_json(data):
    # Remove control characters except for \n, \r, \t
    cleaned = ''.join(char for char in data if char.isprintable() or char in '\n\r\t')
    return cleaned

def parse_total_score_from_md(content):

    try:
        match = re.search(r"\*\*total_score=(\d+)\*\*", content)
        if match:
            return int(match.group(1))
        else:
            print("Total score not found in the file.")
            return 'error'
    except Exception as e:
        print(f"An error occurred while reading the file: {e}")
        return None


if __name__ == "__main__":
    import json
    from appendToJsonFile import append

    with open("jobDetails_Technical_Project_Manager.json") as file:
        jobDetailList = json.load(file)

    for item in jobDetailList:

        resp = callOpenAi(prompt(item))
        result = resp.model_dump_json()
        resp_data = json.loads(result)['output'][0]['content'][0]['text']

        score = parse_total_score_from_md(resp_data)

        filename = f'{score}__{item["company"]}__{item["title"]}.md'
        print(filename)
        content = resp_data + "\n\nHere is the original job description data:\n\n```json\n\n" + json.dumps(item, indent=2)

        try:
            with open("results/" + filename, "w") as file:
                file.write(content)
            # print(f"Markdown file '{filename}' created successfully.")
        except Exception as e:
            print(f"An error occurred while writing the file: {e}")
