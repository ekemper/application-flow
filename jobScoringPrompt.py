import json

def prompt(job_description_json):
    # Load the contents of the text files
    with open("prompt_documents/resume.md", "r") as resume_file:
        resume_content = resume_file.read()

    with open("prompt_documents/coverletter_samples.md", "r") as coverletter_file:
        coverletter_samples = coverletter_file.read()

    with open("prompt_documents/prompt_instructions.md", "r") as instructions_file:
        prompt_instructions = instructions_file.read()

    return f"""

{prompt_instructions}

{resume_content}

{coverletter_samples}

Job Description:

{json.dumps(job_description_json, indent=2)}
"""


if __name__ == "__main__":
    # Test the prompt function
    with open("prompt_documents/TEST-jobDescription.txt", "r") as job_description_file:
        job_description = job_description_file.read()

    prompt_text = prompt(job_description)
    print(prompt_text)
