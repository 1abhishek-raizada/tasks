import ollama 


x=input('enter you questions: ')
res=ollama.chat(
    model="llama3.2",
    messages=[
        {"role":"user","content":f"{x}"},
    ]
)
print(res["message"]["content"])