import json
import openai
from dotenv import load_dotenv
import os

load_dotenv()

client = openai.OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

with open("Edward Kemper Resume 2025.html", "r") as resume_file:
    resume_content = resume_file.read()

with open("coverletter_samples.md", "r") as coverletter_file:
    coverletter_samples = coverletter_file.read()

with open("prompt_instructions.md", "r") as instructions_file:
    instructions = instructions_file.read()

with open("job_description.txt", "r") as job_description_file:
    job_description = job_description_file.read()

# Call the GPT-4 Turbo model
response = client.chat.completions.create(
    model="gpt-4-0125-preview",
    messages=[
        {"role": "system", "content": instructions},
        {"role": "user", "name": "job_description", "content": job_description},
        {"role": "user", "name": "resume", "content": resume_content},
        {"role": "user", "name": "cover_letter", "content": coverletter_samples},
    ],
    temperature=0.4
)

output = response.choices[0].message.content.strip()

try:
    data = json.loads(output)
    print("✅ Data type of 'data':", type(data))
    
    with open("suggested_resume.html", "w") as resume_output_file:
        resume_output_file.write(data['resume'])

    with open("suggested_coverletter.html", "w") as coverletter_output_file:
        coverletter_output_file.write(data['cover_letter'])


except json.JSONDecodeError:
    print("❌ Failed to parse JSON. Raw output below:\n")
    print(output)
