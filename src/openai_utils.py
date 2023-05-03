import openai
import os
from typing import Optional

def get_chatcompletion(
    prompt,
    model: int = "gpt-3.5-turbo",
    temperature: float = 0.0,
    max_tokens: int = 512,
    top_p: float = 1.0,
    n: int = 1,
):
    messages = [
        {"role": "user",
         "content": prompt},
    ]
    
    response = openai.ChatCompletion.create(
        model = model,
        messages = messages,
        max_tokens = max_tokens,
        temperature = temperature,
        top_p = top_p,
        n = n,   
    )
    
    return response