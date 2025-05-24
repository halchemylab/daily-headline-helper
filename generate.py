import os
import csv
from dotenv import load_dotenv
from openai import OpenAI

# Load environment variables from .env file
load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

if not OPENAI_API_KEY:
    raise ValueError("OPENAI_API_KEY not found in environment. Please add it to your .env file.")

# Initialize the OpenAI client
client = OpenAI(api_key=OPENAI_API_KEY)

PROMPT_TEMPLATE = (
    "You are a master social media copywriter. Given the following raw idea, generate content for {platform}.\n"
    "Requirements:\n"
    "- Write a catchy headline suitable for {platform}.\n"
    "- Add 1-2 engaging sentences as the post, using a friendly and professional tone.\n"
    "- Include relevant emojis in both the headline and post.\n"
    "- Add 4-5 hashtags at the end, related to the topic.\n"
    "Idea: {idea}\n\n"
    "Output format:\n"
    "Headline: <headline>\n"
    "Post: <post>\n"
    "Hashtags: <hashtags>\n"
)

def generate_headlines(idea, platform="Linkedin"):
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": PROMPT_TEMPLATE.format(idea=idea, platform=platform)}
        ],
        max_tokens=150,
        n=1,
        stop=None,
        temperature=0.8,
    )
    return response.choices[0].message.content.strip()

def parse_output(output):
    """Parse the generated output into headline, post, and hashtags."""
    headline, post, hashtags = '', '', ''
    for line in output.splitlines():
        if line.startswith('Headline:'):
            headline = line.replace('Headline:', '').strip()
        elif line.startswith('Post:'):
            post = line.replace('Post:', '').strip()
        elif line.startswith('Hashtags:'):
            hashtags = line.replace('Hashtags:', '').strip()
    return headline, post, hashtags

def save_to_csv(idea, platform, headline, post, hashtags, filename="output.csv"):
    """Append a new row to the CSV file, creating it with headers if needed."""
    file_exists = os.path.isfile(filename)
    with open(filename, mode='a', encoding='utf-8', newline='') as csvfile:
        writer = csv.writer(csvfile)
        if not file_exists:
            writer.writerow(["Idea", "Platform", "Headline", "Post", "Hashtags"])
        writer.writerow([idea, platform, headline, post, hashtags])

def main():
    print("Enter your raw idea (or press Enter to use the example):")
    idea = input().strip()
    if not idea:
        idea = "New study reveals surprising link between coffee consumption and productivity."
    platform = "Linkedin"  # You can extend this to prompt for platform if needed
    print("\nGenerating headlines...\n")
    headlines = generate_headlines(idea, platform)
    print(headlines)
    headline, post, hashtags = parse_output(headlines)
    save_to_csv(idea, platform, headline, post, hashtags)
    print("\nSaved to output.csv.")

if __name__ == "__main__":
    main()
