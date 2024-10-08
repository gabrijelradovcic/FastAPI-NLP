# FastAPI NLP Similarity Checker

This project is a FastAPI application that provides an endpoint to find the most similar title from a list based on a reference title using sentence embeddings.

### Model Description

In this application, I decided to use the **`SentenceTransformer`** model with the pre-trained model **`'all-MiniLM-L6-v2'`** for several reasons:

- **Performance**: The `all-MiniLM-L6-v2` model is a lightweight model that provides a good balance between performance and accuracy, making it suitable for applications where speed is important.

- **Quality of Embeddings**: This model produces high-quality embeddings for a variety of sentence-level tasks, including semantic similarity, which is essential for our application where we need to determine how similar one title is to another.

- **Efficiency**: Being smaller than many other transformer models, it requires less computational power, allowing it to run efficiently even on machines with limited resources.

- **Ease of Use**: The Sentence Transformers library makes it straightforward to obtain sentence embeddings with just a few lines of code, allowing for rapid development and integration.


## Features

- Use of FastAPI for building APIs.
- Sentence Transformers for calculating similarity.
- Easy-to-use endpoints for input and output in JSON format.

## Table of Contents

- [Installation](#installation)
- [API Endpoints](#api-endpoints)
- [Example Input](#example-input)

## Installation

### Prerequisites

- [Python 3.10 or later](https://www.python.org/downloads/) — Ensure that Python is installed on your system.
- [Poetry](https://python-poetry.org/docs/#installation) — Poetry is used for dependency management in this project.
Ensure that after installations Poetry and Python are added to PATH environmental variable

### Steps

1. **Clone the Repository**:
git clone "https://github.com/gabrijelradovcic/FastAPI-NLP.git"

Make sure you are in right directory when running server using Command Prompt
- "cd FastAPI-NLP"

2. **Install Dependencies**:
Using Poetry, run the following command to install all required dependencies:
- "poetry install"

3. **Activate the Poetry Environment**:
 - "poetry shell"

4. **Run the FastAPI Application**:
Start the FastAPI server in Command Prompt with Uvicorn:
 - "uvicorn main:app --reload"
To test open another Command prompt and run examples using curl.

### API Endpoints

1. **POST /process-input/**: This endpoint returning the most similar title given the input json object "input.json.

### Example Input
Input should be a JSON object with the following structure saved as input.json in directory where the main.py is.

```json
{
"reference": "Higgs boson in particle physics",
"other": [
 "Best soup recipes",
 "Basel activities",
 "Particle physics at CERN"
]
}
**Example Using `curl`**:
  To test this endpoint, you can use the following `curl` command in different Command Prompt then where server is run:
  ```bash
  curl -X POST "http://127.0.0.1:8000/process-input/"
  ```
- **Expected Output**:
  The response will be a JSON object containing the most similar title:
  ```json
  {
    "top_result": "Particle physics at CERN"
  }


2. **POST /similar-title/**: This endpoint accepts a JSON body with a reference title and a list of other titles, returning the most similar title.

### Example Input
The request should be a JSON object with the following structure saved as input.json in directory where the main.py is.

```json
{
"reference": "Higgs boson in particle physics",
"other": [
 "Best soup recipes",
 "Basel activities",
 "Particle physics at CERN"
]
}
- **Example Using `curl`**:
  To test this endpoint, you can use the following `curl` command in different Command Prompt then where server is run:
  ```bash
  curl -X POST "http://127.0.0.1:8000/similar-title/" -H "Content-Type: application/json" -d "{\"reference\": \"Higgs boson in particle physics\", \"other\": [\"Best soup recipes\", \"Basel activities\", \"Particle physics at CERN\"]}"
  ```
- **Expected Output**:
  The response will be a JSON object containing the most similar title:
  ```json
  {
    "top_result": "Particle physics at CERN"
  }
  ```


