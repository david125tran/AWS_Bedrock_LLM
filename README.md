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

## 📄 Sample Output

👉 View the full markdown report here:
squirrel_analysis_report.md

## 📄 Output Preview

```markdown
# 🐿️ Central Park Squirrel Census Analysis 🌳

## 📊 Dataset Overview

This dataset contains 50 squirrel observations from Central Park, New York City. Each entry includes detailed information about the squirrel's location, physical characteristics, behaviors, and interactions with the environment.

## 🗺️ Geographical Distribution

- Observations span across various hectares of Central Park, from 02B to 40B.
- Latitude range: 40.7681954366911 to 40.7982886348696
- Longitude range: -73.9801666435401 to -73.9532170504865

## 🎨 Fur Color Analysis

1. Primary Fur Colors:
   - Gray: 33 (66%)
   - Cinnamon: 4 (8%)
   - Black: 2 (4%)
   - Not specified: 11 (22%)

2. Highlight Fur Colors:
   - Cinnamon: 11
   - White: 7
   - Gray: 1
   - Multiple highlights: 3
   - Not specified: 28



## 📦 Installation

Install required Python packages:

```bash
pip install boto3 python-dotenv pandas
