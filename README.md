# AI Documentation Generator

A simple web application that generates documentation for code snippets using Groq's Llama3-8B model.

## Prerequisites

- Python 3.6 or higher

## Installation

1. Clone or download this project to your local machine.

2. Install the required Python libraries:
   ```
   pip install Flask requests
   ```

## Setup

1. The app uses Groq API. The API key is already configured in the code.

   If you want to use your own Groq API key, set it as an environment variable:
   - On Windows: `set GROQ_API_KEY=your_groq_api_key_here`
   - On macOS/Linux: `export GROQ_API_KEY=your_groq_api_key_here`

   Alternatively, you can edit the `app.py` file and replace the key with your own.

## Running the Application

1. Navigate to the project directory in your terminal.

2. Run the Flask server:
   ```
   python app.py
   ```

3. Open your web browser and go to `http://localhost:5000`

## Usage

1. Paste your code snippet into the textarea.
2. Click the "Generate Documentation" button.
3. The AI-generated documentation will appear in the output area below.

## API Endpoint

- `GET /`: Serves the main HTML page
- `POST /generate-docs`: Accepts JSON with `code` field and returns generated documentation

## Notes

- The application uses Groq's Llama3-8B model for documentation generation.
- Make sure your Groq API key has sufficient credits.
- The generated documentation is limited to 200 tokens for brevity.
