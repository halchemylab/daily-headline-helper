import os
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
    "You are a world-class copywriter. "
    "Given the following raw idea, generate 2-3 punchy, professional headlines suitable for LinkedIn, email subject lines, or slide titles. "
    "Be concise, creative, and persuasive.\n\n"
    "Idea: {idea}\n\nHeadlines:"
)

def generate_headlines(idea):
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": PROMPT_TEMPLATE.format(idea=idea)}
        ],
        max_tokens=150,
        n=1,
        stop=None,
        temperature=0.8,
    )
    return response.choices[0].message.content.strip()

def main():
    print("Enter your raw idea (or press Enter to use the example):")
    idea = input().strip()
    if not idea:
        idea = "AI tool that helps marketers rewrite job posts for different candidate personas"
    print("\nGenerating headlines...\n")
    headlines = generate_headlines(idea)
    print(headlines)

if __name__ == "__main__":
    main()
