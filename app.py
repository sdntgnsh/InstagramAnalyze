from flask import Flask, request, render_template
import requests
import json
# Initialize Flask application
app = Flask(__name__)
# Initialize messages list to store chat history
messages = []

def call_langflow_api(question):
    url = "https://api.langflow.astra.datastax.com/lf/d82f9e69-0085-4565-b516-0fdc65e458ae/api/v1/run/91c53020-0868-4ac6-a0ec-2560c75bc888"
    
    headers = {
        'Content-Type': 'application/json',
        'Authorization': ''
    }
    
    payload = {
        "input_value": question,
        "output_type": "chat",
        "input_type": "chat",
        "tweaks": {
            "ChatInput-twARP": {},
            "Agent-eeeOw": {},
            "AstraDBToolComponent-OQUdo": {},
            "ChatOutput-bjBiv": {},
            "Prompt-EFtZz": {}
        }
    }
    
    try:
        response = requests.post(url, headers=headers, json=payload, stream=False)
        response.raise_for_status()  # Raise an error for bad status codes
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error calling Langflow API: {e}")
        return {"output_text": "Sorry, I encountered an error processing your request."}

@app.route('/ai_chatbot', methods=['GET', 'POST'])
def ai_chatbot():
    global messages
    
    if request.method == 'POST':
        # Get the user's question from the form
        question = request.form.get('question')
        
        if not question:
            return render_template('aichatbot.html', messages=messages, 
                                error="Please enter a question.")
        
        # Append the user's question to the messages list
        messages.append({'sender': 'user', 'content': question})
        
        # Call the Langflow API
        api_response = call_langflow_api(question)
        print(api_response)
        bot_response = api_response.get("output_text", 
                                      "Sorry, I couldn't process your request.")
        
        # Append the bot's response to the messages list
        messages.append({'sender': 'bot', 'content': bot_response})
    
    return render_template('aichatbot.html', messages=messages)

if __name__ == '__main__':
    app.run(debug=True)