# 🐿️ Squirrel Census Analysis with AWS Bedrock + Claude 3.5

This project uses **AWS Bedrock** and **Anthropic Claude 3.5 Sonnet** to perform natural language analysis on urban wildlife data — specifically, the 2018 Central Park Squirrel Census 🏙️🌳. It leverages a large language model (LLM) to generate engaging, narrative-style insights from structured observational data.  I chose a random & simple dataset to play around with proof of concept with the LLM to build a simple project.  My intent is to build a more sophisticated project with real world utility later.  But I wanted to start simple.  

## 🚀 Highlights

- 🔍 **Real-World Dataset**: Uses the 2018 Central Park Squirrel Census.
- 🧠 **LLM-Driven Analysis**: Engages Claude 3.5 via AWS Bedrock for narrative generation.
- ☁️ **Cloud-Backed**: Securely connects to AWS using `boto3` and `.env` configuration.
- 📄 **Markdown Reporting**: Outputs a structured, readable analysis file.
- 🧪 **Custom Prompting**: Craft custom system and user prompts to direct LLM behavior.

## 🧰 Tech Stack

| Tech | Description |
|------|-------------|
| `Python` | Core programming language |
| `boto3` | AWS SDK for Python |
| `dotenv` | Environment variable management |
| `pandas` | Data handling and preprocessing |
| `AWS Bedrock` | Serverless access to foundation models |
| `Claude 3.5 Sonnet` | Powerful LLM from Anthropic |

## 📦 Installation

Install required Python packages:

```bash
pip install boto3 python-dotenv pandas
