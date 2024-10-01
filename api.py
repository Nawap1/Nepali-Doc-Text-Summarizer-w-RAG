from fastapi import FastAPI, UploadFile, File
from fastapi.responses import HTMLResponse,FileResponse
from fastapi.staticfiles import StaticFiles
from PyPDF2 import PdfReader
from langchain import HuggingFaceHub
from langchain.text_splitter import RecursiveCharacterTextSplitter
import torch
import re
import dotenv
import os
import uvicorn
app = FastAPI()

# Serve static files
app.mount("/static", StaticFiles(directory="static"), name="static")

#Initializations
text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=512,
    chunk_overlap=50,
    length_function=len,
    is_separator_regex=False,
)

# Load environment variables from .env file
dotenv.load_dotenv()

# Get the Hugging Face token from the environment variables
hugging_face_token = os.getenv("HF_TOKEN")

summarizer = HuggingFaceHub(
    repo_id="csebuetnlp/mT5_multilingual_XLSum",
    model_kwargs={"temperature": 0, "max_length": 84},
    huggingfacehub_api_token=hugging_face_token,
)

#GPU
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
#Preprocessing
WHITESPACE_HANDLER = lambda k: re.sub('\s+', ' ', re.sub('\n+', ' ', k.strip()))

@app.get("/", response_class=HTMLResponse)
async def get_home():
    """Serve the HTML template."""
    return FileResponse("static/main.html")

@app.post("/summarize")
async def doc_summarizer(document: UploadFile = File(...)) -> str:
    '''
    Takes the document content and returns the summarized text.
    document: UploadFile - the document content to be summarized.
    returns: str - summarized text of the document.
    '''
    if document.filename.endswith('.txt'):
        text = text_splitter.split_text(WHITESPACE_HANDLER((await document.read()).decode()))
    elif document.filename.endswith('.pdf'):
        pdf_reader = PdfReader((await document.read()))
        extracted_text = ''
        for i in range(len(pdf_reader.pages)):
            page = pdf_reader.pages[i]
            extracted_text += page.extract_text()
        extracted_text = WHITESPACE_HANDLER(extracted_text)
        text = text_splitter.split_text(extracted_text)
    return summarizer(f"summarize: {text}!")

if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8000)