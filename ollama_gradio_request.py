import requests
import gradio as gr
import json

url = "http://localhost:11434/api/generate"
headers = {
    "accept": "application/json",
    "Content-Type": "application/json",
}

history = []

def generate_response(prompt):
    history.append(prompt)
    final_prompt = "\n".join(history)
    data = {
        "prompt": final_prompt,
        "history": history,
        "model": "llama3.1",
        "stram": False
    }

    response = requests.post(url, headers=headers, data=json.dumps(data))
    if response.status_code==200:
        response=response.text
        data = json.loads(response)
        actual_response = data['response']
        return actual_response
    else:
        print("Error:", response.status_code, response.text)

interface=gr.Interface(
    fn=generate_response,
    inputs=gr.Textbox(lines=2, placeholder="Enter your query here..."),
    outputs="text"
)
interface.launch(share=True, debug=True)
