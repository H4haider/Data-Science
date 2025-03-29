import groq as gr

Client=gr.Groq(api_key="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")

def answer(text):
    messages=[{"role":"user", "content": text }]
    model="llama3-8b-8192"
    temperature=0.5
    response=Client.chat.completions.create(messages=messages, temperature=temperature, model= model)
    res=response.choices[0].message.content.strip()
    for word in res:
        yield word


