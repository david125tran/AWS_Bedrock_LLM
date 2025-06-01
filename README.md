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

## 📄 Output from Anthropic's Claude Sonnet 3.5:

👉 View the full markdown report here:
[squirrel_analysis_report.md](https://github.com/david125tran/AWS_Bedrock_LLM/blob/main/squirrel_analysis_report.md)

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

## 👶🏼 Age Distribution

- Adult: 35 (70%)
- Juvenile: 4 (8%)
- Not specified: 11 (22%)

## 🌳 Location

- Ground Plane: 27 (54%)
- Above Ground: 13 (26%)
- Not specified: 10 (20%)

## 🏃‍♂️ Behaviors

1. Movement:
   - Running: 10 (20%)
   - Chasing: 5 (10%)
   - Climbing: 6 (12%)

2. Feeding:
   - Eating: 7 (14%)
   - Foraging: 18 (36%)

3. Vocalizations:
   - No instances of kuks, quaas, or moans recorded

4. Tail Movements:
   - Tail flags: 3 (6%)
   - Tail twitches: 7 (14%)

5. Interactions:
   - Approaches: 2 (4%)
   - Indifferent: 19 (38%)
   - Runs from: 6 (12%)

## 🕒 Time of Day

- AM shifts: 22 (44%)
- PM shifts: 28 (56%)

## 🔍 Interesting Observations

1. 🌈 Color Variations: While gray is the dominant fur color, there's a rich diversity of highlight colors, including cinnamon and white.

2. 🍽️ Foraging Behavior: Foraging is the most commonly observed activity, suggesting that food-seeking is a primary daytime activity for Central Park squirrels.

3. 🤐 Quiet Creatures: No vocalizations were recorded in this dataset, which is surprising given the number of observations.

4. 🌳 Ground vs. Tree: More squirrels were observed on the ground than in trees, possibly due to foraging behavior.

5. 🏃‍♂️ Active Squirrels: Running, chasing, and climbing behaviors were frequently observed, indicating high activity levels.

6. 😌 Indifference to Humans: The most common interaction was indifference, suggesting these urban squirrels are accustomed to human presence.

7. 🌞 Day/Night Activity: Slightly more observations were made during PM shifts, but the difference is not significant.

8. 👀 Unique Behaviors: Some interesting activities noted include "wrestling with mother" and "eating upside down on a tree."

## 🧐 Conclusions

This dataset provides a fascinating glimpse into the lives of Central Park's squirrel population. The predominance of gray-furred adults engaging in foraging behavior on the ground paints a picture of a well-established urban wildlife community. The variety in fur colors and behaviors suggests a diverse and adaptable population. The squirrels' general indifference to human presence indicates their successful adaptation to the urban environment. Further studies could explore seasonal variations in behavior and more detailed analysis of their interactions with the park's ecosystem.
```



## 📦 Installation

Install required Python packages:

```bash
pip install boto3 python-dotenv pandas
