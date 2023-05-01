import openai

def get_completion(
    prompt,
    model: int = "gpt-3.5-turbo"
):
    messages = [
        {"role": "user",
         "content": prompt},
    ]
    
    response = openai.ChatCompletion.create(
        model = model,
        messages = messages,
        temperature = 0,
    )