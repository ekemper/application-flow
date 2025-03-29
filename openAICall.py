import os
from openai import OpenAI
from dotenv import load_dotenv
load_dotenv()


from jobScoringPrompt import prompt 

apiKey=os.environ.get("OPENAI_API_KEY")

client = OpenAI(api_key=apiKey)

def callOpenAi(prompt):
    response = client.responses.create(
        model="gpt-4o-mini",
        instructions="You are a helpful assistant.",
        input=prompt,
    )

    # print(response.output_text)

    return response

def write_json_to_file(json_string, output_file):
    try:
        # Parse the string to a Python object
        # data = json.loads(json_string)
        
        # Write to file with proper formatting
        with open(output_file, 'w', encoding='utf-8') as f:
            json.dump(json_string, f, indent=2, ensure_ascii=False)
            
        print(f"Successfully wrote JSON to {output_file}")
        return True
        
    except json.JSONDecodeError as e:
        print(f"Error parsing JSON: {e}")
        return False
    except IOError as e:
        print(f"Error writing to file: {e}")
        return False

if __name__ == "__main__":
    
    import json 
    from appendToJsonFile import append
    
    with open('jobDetailArray.json') as file:
        jobDetailList = json.load(file)
    
    
    for item in jobDetailList:
        
    
        resp = callOpenAi(prompt(item))
        result = resp.model_dump_json()
        resp_data = json.loads(result)['output'][0]['content'][0]['text']
        
        print(resp_data)
            
        del item['raw_html']
            
        outputDict = {
            'input': item,
            'output': json.loads(resp_data)
        }
        
        append(outputDict, 'output.json')
        