from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from transformers import GPT2LMHeadModel, GPT2Tokenizer
import torch
import uvicorn

app = FastAPI()

# Load pre-trained GPT-2 model and tokenizer
tokenizer = GPT2Tokenizer.from_pretrained("gpt2")
model = GPT2LMHeadModel.from_pretrained("gpt2")

# Pydantic model for input Data
class TextInput(BaseModel): # defines input data
    text: str

@app.post("/next_word")
def next_word_prediction(input_data: TextInput):
    try:
        # Tokenize the input text
        input_ids = tokenizer.encode(input_data.text, return_tensors="pt") # tokenizes the input text using GPT-2 tokenizer

        # Generate the next word prediction
        with torch.no_grad():
            outputs = model.generate(input_ids, max_length=len(input_ids[0]) + 1, num_return_sequences=1)

        # Decode the predicted token and return it
        predicted_token = tokenizer.decode(outputs[0, -1], skip_special_tokens=True)
        return {"predicted_next_word": predicted_token}

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/health")
def health_check():
    return {"status": "API is running"}

if __name__ == "__main__":
    uvicorn.run("app:app", host="0.0.0.0", port=8000, reload=True)
