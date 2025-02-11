import openai
import PyPDF2
from flask import Flask, request, jsonify, render_template

openai.api_key = "your-openai-api-key"

app = Flask(__name__)

def read_input(file_path: str) -> str:
    """
    Reads input from a file (txt or pdf).
    """
    if file_path.endswith('.txt'):
        with open(file_path, 'r', encoding='utf-8') as file:
            return file.read()
    elif file_path.endswith('.pdf'):
        text = ""
        with open(file_path, 'rb') as file:
            reader = PyPDF2.PdfReader(file)
            for page in reader.pages:
                text += page.extract_text()
        return text
    else:
        raise ValueError("Unsupported file type. Please upload a .txt or .pdf file.")

def grade_letter(letter: str) -> str:
    """
    Sends the letter to ChatGPT and gets the grade and suggestions.
    """
    prompt = f"""
    You are an expert in evaluating formal letters. Grade the following letter based on standard formal letter norms, 
    including structure, tone, grammar, and relevance. Provide:
    1. A grade (e.g., A, B, C) with reasons.
    2. Specific suggestions for improvement.
    
    Here is the letter:
    {letter}
    """
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",  # Updated to use gpt-3.5-turbo
        messages=[{"role": "user", "content": prompt}],
        temperature=0.7
    )
    return response['choices'][0]['message']['content']

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/grade', methods=['POST'])
def grade():
    data = request.form
    file = request.files['letter_file']
    
    if file:
        file_path = f"temp/{file.filename}"
        file.save(file_path)
        try:
            letter_content = read_input(file_path)
            grading_result = grade_letter(letter_content)
            return jsonify({"grading_result": grading_result})
        except Exception as e:
            return jsonify({"error": str(e)}), 400

    return jsonify({"error": "No file uploaded"}), 400

if __name__ == "__main__":
    app.run(debug=True)
