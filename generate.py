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
    "You are a master wordsmith, skilled in crafting headlines that grab attention and drive action."
    "Given the following raw idea, generate 3-4 clear and concise headlines that explain the core concept in an easy-to-grasp way, suitable for quick understanding in various contexts."
    "Think about how to break it down into its most essential elements for instant comprehension.\n\n"
    "Idea: {idea}\n\nHeadlines:"
)

def generate_headlines(idea):
    response = client.chat.completions.create(
        model="gpt-4o-mini",
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
