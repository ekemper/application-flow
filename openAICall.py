import os
from openai import OpenAI
from dotenv import load_dotenv
load_dotenv()

from jobScoringPrompt import prompt 

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

if __name__ == "__main__":
    import json
    from appendToJsonFile import append

    with open('jobDetails.json') as file:
        jobDetailList = json.load(file)

    for item in jobDetailList:
        resp = callOpenAi(prompt(item))
        result = resp.model_dump_json()
        resp_data = json.loads(result)['output'][0]['content'][0]['text']

        # Log raw response data for debugging
        print("Raw response data:", resp_data)

        try:
            cleaned_data = clean_json(resp_data)
            outputData = json.loads(cleaned_data)
        except json.JSONDecodeError as e:
            print(f"Failed to parse JSON: {str(e)}")
            print("Problematic JSON:", cleaned_data)
            continue  # Skip this item and move to the next

        outputDict = {
            'input': item,
            'output': outputData
        }

        append(outputDict, 'output.json')
        