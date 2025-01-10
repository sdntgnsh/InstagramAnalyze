import requests
from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Configuration
LANGFLOW_URL = "https://api.langflow.astra.datastax.com/lf/d82f9e69-0085-4565-b516-0fdc65e458ae/api/v1/run/91c53020-0868-4ac6-a0ec-2560c75bc888"
DEFAULT_HEADERS = {
    'Content-Type': 'application/json',
    'Authorization': ""  # Replace with your actual token
}

def call_langflow_api(message):
    """
    Make a request to the Langflow API
    """
    payload = {
        "input_value": message,
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
        response = requests.post(
            f"{LANGFLOW_URL}?stream=false",
            headers=DEFAULT_HEADERS,
            json=payload
        )
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        return {"error": str(e)}

@app.route('/chat', methods=['POST'])
def chat():
    """
    Handle chat requests by forwarding them to Langflow API
    """
    try:
        user_message = request.json.get('message')
        if not user_message:
            return jsonify({"error": "No message provided"}), 400
            
        # Call Langflow API
        langflow_response = call_langflow_api(user_message)
        
        # Check for errors in Langflow response
        if "error" in langflow_response:
            return jsonify(langflow_response), 500
            
        return jsonify({
            "reply": langflow_response
        })
        
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/health', methods=['GET'])
def health_check():
    """
    Simple health check endpoint
    """
    return jsonify({"status": "healthy"})

if __name__ == '__main__':
    app.run(debug=True)