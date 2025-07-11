# Headline Generator 🧠✍️

This is a simple, atomic tool that takes your raw ideas and turns them into punchy, polished headlines or social media posts using OpenAI's GPT API.

Designed for:
- Consultants and strategists crafting LinkedIn or slide content
- Founders distilling product ideas
- Content creators polishing their thoughts

## 🚀 Example

**Input Idea:**
> AI tool that helps marketers rewrite job posts for different candidate personas

**Generated Headlines:**
- "Write Job Posts That Actually Get Read—With Help from AI"
- "Speak Their Language: Personalized Hiring Copy in Seconds"
- "No More Guessing: Let AI Tailor Your Job Listings by Persona"

## ✨ Features

- Generates catchy headlines and posts for multiple platforms
- Adds relevant hashtags and emojis automatically
- Simple CLI and graphical UI (Tkinter)
- Saves all generations to a CSV file for easy tracking
- Customizable for different platforms

## 💡 Tips

- Try different platforms for varied tone and style.
- Edit the prompt in `generate.py` to fine-tune the output style.
- Use the CSV output to track your best ideas.

## 🛠️ How to Run

1. Clone the repo  
   ```bash
   git clone https://github.com/your-username/headline-generator.git
   cd headline-generator
   ```
2. Add your OpenAI API key to a .env file:
   ```bash
   OPENAI_API_KEY=your_api_key_here
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

### Run in the Terminal (CLI)

Use the command-line tool to generate headlines or posts:
```bash
python generate.py
```
You will be prompted to enter your idea and (optionally) a platform.

### Run the Graphical UI

Use the Tkinter-based UI for a simple graphical experience:
```bash
python ui.py
```
Enter your idea, select a platform, and click "Generate Headlines" to see results.

## 🧩 Troubleshooting

- **API Key Issues:** Make sure your `.env` file is in the project root and contains `OPENAI_API_KEY=...`.
- **No Output:** Check your internet connection and OpenAI API usage limits.
- **UI Not Launching:** Ensure you have `tkinter` installed (`pip install tk` on some systems).

## 💾 Output Saving

Every time you generate a headline/post (using either the CLI or the UI), the result is automatically saved to `output.csv` in your project folder. This CSV file includes columns for your input idea, selected platform, generated headline, post, and hashtags. Each new generation appends a new row to the file.

> **Note:** `output.csv` is included in `.gitignore` and will not be tracked by git.

📦 Output
You’ll get a catchy headline, a short post, and relevant hashtags—ready for LinkedIn, Facebook, Instagram, or X (Twitter)!
