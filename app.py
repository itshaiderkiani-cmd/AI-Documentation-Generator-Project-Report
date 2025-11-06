from flask import Flask, request, jsonify, send_from_directory
import requests
import os
import ast

app = Flask(__name__)

# Get API key from environment variable
API_KEY = os.environ.get('GROQ_API_KEY', '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')  # Using provided Groq key

@app.route('/')
def index():
    return send_from_directory('.', 'index.html')

@app.route('/generate-docs', methods=['POST'])
def generate_docs():
    try:
        data = request.get_json()
    except Exception:
        return jsonify({'error': 'Invalid JSON'}), 400

    code = data.get('code', '')

    if not code:
        return jsonify({'error': 'No code provided'}), 400

    if len(code) > 10000:
        return jsonify({'error': 'Input too large'}), 413

    # Create prompt
    prompt = f"Generate a docstring or block comment for the following code:\n\n{code}"

    # Groq API call
    url = 'https://api.groq.com/openai/v1/chat/completions'
    headers = {
        'Authorization': f'Bearer {API_KEY}',
        'Content-Type': 'application/json'
    }
    payload = {
        'model': 'llama-3.1-8b-instant',
        'messages': [{'role': 'user', 'content': prompt}],
        'max_tokens': 1000
    }

    try:
        response = requests.post(url, headers=headers, json=payload)
        if response.status_code != 200:
            error_data = response.json()
            error_message = error_data.get('error', {}).get('message', 'Unknown error from Groq API')
            return jsonify({'error': error_message}), response.status_code
        result = response.json()
        documentation = result['choices'][0]['message']['content'].strip()

        # Preserve exact formatting and fix indentation issues by validating with ast.parse if it's Python code
        try:
            ast.parse(documentation)
            # If it's valid Python, reformat to fix indentation
            documentation = ast.unparse(ast.parse(documentation))
        except SyntaxError:
            # If not valid Python, leave as is (assuming it's a docstring/comment)
            pass

        return jsonify({'documentation': documentation})
    except requests.exceptions.RequestException as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
