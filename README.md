# Next Word Prediction API

## Overview
This project is a Next Word Prediction API built using **FastAPI** and **GPT-2** from the **Hugging Face Transformers** library. The API takes a text input and predicts the next word using a pre-trained GPT-2 model.

## Features
- Predicts the next word given a text input.
- Health check endpoint to verify API availability.
- Fast and efficient inference using PyTorch and GPT-2.

## Endpoints
### 1. Next Word Prediction
- **URL**: `/next_word`
- **Method**: `POST`
- **Input**: JSON object with the following structure:
  ```json
  {
    "text": "Hello, how are"
  }
  ```
- **Response**: JSON object with the predicted next word:
  ```json
  {
    "predicted_next_word": "you"
  }
  ```

### 2. Health Check
- **URL**: `/health`
- **Method**: `GET`
- **Response**:
  ```json
  {
    "status": "API is running"
  }
  ```

## Installation
1. Clone the repository:
   ```bash
   git clone <repository_url>
   cd <repository_folder>
   ```

2. Install dependencies:
   ```bash
   pip install fastapi uvicorn transformers torch
   ```

## Running the API
To run the API locally:
```bash
uvicorn app:app --host 0.0.0.0 --port 8000 --reload
```

## Docker Deployment
1. Build the Docker image:
   ```bash
   docker build -t next-word-prediction .
   ```

2. Run the Docker container:
   ```bash
   docker run -d -p 8000:8000 next-word-prediction
   ```

## Accessing the API
Visit the following URL to interact with the API:
```
http://localhost:8000/docs
```

## Example Usage
Use `curl` to send a prediction request:
```bash
curl -X POST "http://localhost:8000/next_word" -H "Content-Type: application/json" -d '{"text": "Hello, how are"}'
```

## Technologies Used
- **FastAPI**: Web framework for building APIs.
- **GPT-2**: Pre-trained language model from Hugging Face.
- **PyTorch**: Deep learning library.
- **Docker**: Containerization for easy deployment.
