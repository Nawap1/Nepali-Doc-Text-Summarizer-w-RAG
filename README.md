# DocSum: Nepali Document Summarizer

**Table of Contents**

1. [Introduction](#introduction)
2. [Features](#features)
3. [Installation](#installation)
4. [Usage](#usage)
5. [Technical Details](#technical-details)
6. [Contributing](#contributing)
7. [License](#license)

## Introduction

DocSum is a Nepali document summarizer built using state-of-the-art Nepali LLM for summarization. It takes a Nepali document as input and returns a concise summary of the content. The goal of this project is to provide a tool for efficient and accurate summarization of Nepali documents, making it easier for users to quickly grasp the main points of a document.

## Features

* **Document Summarization**: DocSum can summarize Nepali documents in various formats, including PDF and text files.
* **Language Support**: DocSum is specifically designed to work with the Nepali language.
* **Easy to Use**: Simply upload your document, and DocSum will generate a summary for you.
* **Fast and Accurate**: DocSum uses advanced NLP techniques to ensure fast and accurate summarization.

## Installation

To install DocSum, follow these steps:

1. Clone the repository using `git clone https://github.com/your-username/docsum.git`
2. Install the required dependencies by running `pip install -r requirements.txt`
3. Start the application by running `uvicorn main:app --host 0.0.0.0 --port 8000`

## Usage

To use DocSum, follow these steps:

1. Open a web browser and navigate to `http://localhost:8000`
2. Click on the "Upload Document" button and select the document you want to summarize.
3. Click on the "Summarize" button to generate a summary of the document.
4. The summary will be displayed on the page.

## Technical Details

DocSum uses the following technologies:

* **FastAPI**: A modern, fast (high-performance), web framework for building APIs with Python 3.7+.
* **LangChain**: A library for building applications that use language models.
* **Hugging Face Transformers**: A library of pre-trained models that can be fine-tuned for specific tasks.
* **PyPDF2**: A library for reading and writing PDF files.
* **Torch**: A library for machine learning.

## Contributing

Contributions are welcome! If you'd like to contribute to DocSum, please fork the repository, make your changes, and submit a pull request.

## License

DocSum is licensed under the MIT License.