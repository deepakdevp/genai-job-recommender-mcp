import fitz
import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()
openai_client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")

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

    response = openai_client.chat.Completion.create(
        model="gpt-4o",
        messages=[

          {
            "role": "user",
            "content": prompt
          }
        ],
        max_tokens=max_tokens,
    )
    return response.choices[0].text