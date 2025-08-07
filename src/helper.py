import fitz
import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()  # Make sure .env is in the root or specify path
api_key = os.getenv("OPENAI_API_KEY")
if not api_key:
    raise ValueError("OPENAI_API_KEY not found in environment variables.")
openai_client = OpenAI(api_key=api_key)

def extract_text_from_pdf(file):
    """
    Extract text from a PDF file.

    Args:
        pdf_path (str): The path to the PDF file.

    Returns:
        str: The extracted text from the PDF file.
    """
    doc = fitz.open(stream=file.read(), filetype="pdf")
    text = ""
    for page in doc:
        text += page.get_text()
    return text

def call_openai(prompt, max_tokens=500):
    """
    Call the OpenAI API to generate a response.

    Args:
        prompt (str): The prompt to generate a response for.

    Returns:
        str: The generated response from the OpenAI API.
    """

    response = openai_client.chat.completions.create(
        model="gpt-4o",
        messages=[

          {
            "role": "user",
            "content": prompt
          }
        ],
        max_tokens=max_tokens,
        temperature=0.5,
    )
    return response.choices[0].message.content