import json
import openai

# Set your OpenAI API key here
openai.api_key = "sk-..."  # ← replace this with your actual key

# Load the Docling-style JSON data
with open("docling_data.json", "r") as f:
    doc_data = json.load(f)

# Turn it into plain context
def flatten(entries):
    return "\n\n".join([entry["text"] for entry in entries])

# Ask GPT a question
def ask(doc, question):
    context = flatten(doc)
    prompt = f"""You are an AI assistant. Use the following information to answer questions.

{context}

Question: {question}
Answer:"""

    res = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.2
    )
    return res["choices"][0]["message"]["content"]

# Chat loop
if __name__ == "__main__":
    while True:
        q = input("Ask a question: ")
        print("\n" + ask(doc_data, q) + "\n")
