# 🐿️ Squirrel Census Analysis with AWS Bedrock + Claude 3.5

This project demonstrates how to use **AWS Bedrock** and **Anthropic Claude 3.5 Sonnet** to generate narrative insights from structured data — in this case, the 2018 Central Park Squirrel Census 🏙️🌳.

I chose a simple, quirky dataset as a proof of concept to explore prompt engineering, AWS Bedrock integration, and markdown-based output generation. The long-term goal is to build a more sophisticated project with real-world utility, but this serves as a fun and practical starting point.

---

## 🚀 Highlights

- 🔍 **Real-World Dataset**: Based on the 2018 Central Park Squirrel Census.
- 🧠 **LLM-Powered Analysis**: Uses Claude 3.5 via AWS Bedrock to generate compelling narratives.
- ☁️ **AWS Integration**: Connects securely using `boto3` and environment variables.
- 📝 **Markdown Reporting**: Saves output in structured, human-readable `.md` format.
- 🎯 **Prompt Control**: Custom system/user prompts to guide the tone and focus of analysis.

---

## 🧰 Tech Stack

| Tech              | Purpose                                 |
|-------------------|------------------------------------------|
| `Python`          | Core programming language                |
| `boto3`           | AWS SDK for Python                       |
| `python-dotenv`   | Environment variable management          |
| `pandas`          | Data loading and manipulation            |
| `AWS Bedrock`     | Access to Anthropic's Claude LLM         |
| `Claude 3.5 Sonnet` | The language model for analysis         |

---

## 📦 Installation

Install required Python packages:

```bash
pip install boto3 python-dotenv pandas

📄 Sample Output

👉 View the full markdown report here:
squirrel_analysis_report.md

Here’s a short preview:
