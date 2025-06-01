# ------------------------------------ Installations ----------------------------------
# pip install boto3 
# pip install python-dotenv


# ------------------------------------ Packages ----------------------------------
import boto3
from dotenv import load_dotenv
import json
import os
import pandas as pd



# ------------------------------------ Configure AWS Bedrock Model & Keys ----------------------------------
# https://console.aws.amazon.com/
# Request access to the Bedrock service in your AWS account.

# Get the access and secret keys from your AWS account.
#   *Go to the IAM dashboard
#   *Click Services → Search for IAM → Open Users.
#   *Create a new user or select an existing user.
#   *Select your user → Security credentials tab.
#   *Click Create access key (Located at the top right under the Summary section).
#   *Copy the Access key ID and Secret access key → Select 'Application runniing on an AWS compute service'
#   *Store the keys in the .env file 


# ------------------------------------ Load Environment Variables ----------------------------------
env_path = r"C:\Users\Laptop\Desktop\Coding\LLM\Personal Projects\Environment Variables\aws-bedrock.env"
load_dotenv(dotenv_path=env_path, override=True)

aws_access_key = os.getenv("AWS_ACCESS_KEY")
aws_secret_key = os.getenv("AWS_SECRET_KEY")
# Default to "us-east-1" if not set in .env file
aws_region = os.getenv("AWS_REGION", "us-east-1")

if not aws_access_key or not aws_secret_key:
    raise ValueError("Missing AWS credentials in .env file")


# ------------------------------------ Boto3 Client ----------------------------------
bedrock = boto3.client(
    service_name="bedrock-runtime",
    region_name=aws_region,
    aws_access_key_id=aws_access_key,
    aws_secret_access_key=aws_secret_key
)


# ------------------------------------ Claude Prompt ----------------------------------
def message_claude_sonnet(system_prompt, user_prompt):
    model_id = "anthropic.claude-3-5-sonnet-20240620-v1:0"

    payload = {
        "anthropic_version": "bedrock-2023-05-31",
        "max_tokens": 1000,
        "system": system_prompt,
        "messages": [
            {
                "role": "user",
                "content": user_prompt
            }
        ]
    }

    response = bedrock.invoke_model(
        modelId=model_id,
        contentType="application/json",
        accept="application/json",
        body=json.dumps(payload)
    )

    response_body = json.loads(response['body'].read())
    message_content = response_body["content"][0]["text"]
    return message_content


# ------------------------------------ Output Response ----------------------------------
# system_prompt = "You are a teacher with a sarcastic attitude."
# user_prompt = "Can you explain photosynthesis to me like I'm five?"

squirrel_data_path = r"C:\Users\Laptop\Desktop\Coding\LLM\Personal Projects\AWS Bedrock LLM\2018_Central_Park_Squirrel_Census.csv"
df = pd.read_csv(squirrel_data_path)

print(f"DataFrame shape: {df.shape}") # Print the dimensions of the DataFrame

system_prompt = """You are an expert urban ecologist and data journalist specializing in 
wildlife behavior. Your task is to analyze a dataset of squirrel observations from Central 
Park and then craft compelling, insightful narratives based on your findings. Focus on 
identifying relationships between squirrel characteristics (e.g., fur color, age, behaviors) 
and their observed locations or interactions within the park. Your analysis should be 
thorough, and your narratives should be engaging and informative, as if you are preparing a 
report for a public audience interested in urban wildlife. 

You will be given a dataset of squirrel observations as dictionary in a list in JSON format.
Here is an example:

[
    {
        "X":-73.9561344938,
        "Y":40.7940823884,
        "Unique Squirrel ID":"37F-PM-1014-03",
        "Hectare":"37F",
        "Shift":"PM",
        "Date":10142018,
        "Hectare Squirrel Number":3,
        "Age":null,
        "Primary Fur Color":null,
        "Highlight Fur Color":null,
        "Combination of Primary and Highlight Color":"+",
        "Color notes":null,
        "Location":null,
        "Above Ground Sighter Measurement":null,
        "Specific Location":null,
        "Running":false,"Chasing":false,
        "Climbing":false,"Eating":false,
        "Foraging":false,
        "Other Activities":null,
        "Kuks":false,
        "Quaas":false,
        "Moans":false,
        "Tail flags":false,
        "Tail twitches":false,
        "Approaches":false,
        "Indifferent":false,
        "Runs from":false,
        "Other Interactions":null,
        "Lat//Long":"POINT (-73.9561344937861 40.7940823884086)"
    }
]

Return to me a detailed analysis of the dataset in markdown format.  Use emojis.  
"""

# Convert the first 50 rows to JSON format for the prompt
# Only send the first 50 rows to limit token usage. 
user_prompt = df.head(50).to_json(orient='records')  

message = message_claude_sonnet(system_prompt=system_prompt,
                      user_prompt=user_prompt)

print(message)

# ------------------------------------ Save Output to Markdown File ----------------------------------
output_filename = r"C:\Users\Laptop\Desktop\Coding\LLM\Personal Projects\AWS Bedrock LLM\squirrel_analysis_report.md"
with open(output_filename, "w", encoding="utf-8") as f:
    f.write(message)

print(f"\nAnalysis saved to: {output_filename}")