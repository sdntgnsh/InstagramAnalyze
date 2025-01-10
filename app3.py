import argparse
import json
from argparse import RawTextHelpFormatter
import requests
from typing import Optional
import warnings
from flask import Flask, request, jsonify
from flask_cors import CORS

try:
    from langflow.load import upload_file
except ImportError:
    warnings.warn("Langflow provides a function to help you upload files to the flow. Please install langflow to use it.")
    upload_file = None

BASE_API_URL = "https://api.langflow.astra.datastax.com"
LANGFLOW_ID = "d82f9e69-0085-4565-b516-0fdc65e458ae"
FLOW_ID = "91c53020-0868-4ac6-a0ec-2560c75bc888"
APPLICATION_TOKEN = ""
ENDPOINT = ""  # You can set a specific endpoint name in the flow settings

# Default tweaks
TWEAKS = {
    "ChatInput-twARP": {},
    "Agent-eeeOw": {},
    "AstraDBToolComponent-OQUdo": {},
    "ChatOutput-bjBiv": {},
    "Prompt-EFtZz": {}
}

def run_flow(
    message: str,
    endpoint: str,
    output_type: str = "chat",
    input_type: str = "chat",
    tweaks: Optional[dict] = None,
    application_token: Optional[str] = None
) -> dict:
    """
    Run a flow with a given message and optional tweaks.
    """
    api_url = f"{BASE_API_URL}/lf/{LANGFLOW_ID}/api/v1/run/{endpoint}"

    payload = {
        "input_value": message,
        "output_type": output_type,
        "input_type": input_type,
    }
    headers = None
    if tweaks:
        payload["tweaks"] = tweaks
    if application_token:
        headers = {"Authorization": "Bearer " + application_token, "Content-Type": "application/json"}
    response = requests.post(api_url, json=payload, headers=headers)
    return response.json()

app = Flask(__name__)
CORS(app)

@app.route('/chat', methods=['POST'])
def chat():
    """
    Flask route to handle chat requests.
    """
    user_message = request.json.get('message', '')
    if not user_message:
        return jsonify({"error": "Message is required"}), 400

    try:
        response = run_flow(
            message=user_message,
            endpoint=ENDPOINT or FLOW_ID,
            tweaks=TWEAKS,
            application_token=APPLICATION_TOKEN
        )
        return jsonify(response)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="""Run the server or execute a single flow.""", formatter_class=RawTextHelpFormatter)
    parser.add_argument("--run_server", action="store_true", help="Run the Flask server")
    parser.add_argument("--message", type=str, help="Run a single flow with this message", default=None)
    parser.add_argument("--endpoint", type=str, default=ENDPOINT or FLOW_ID, help="The ID or the endpoint name of the flow")
    parser.add_argument("--tweaks", type=str, help="JSON string representing the tweaks to customize the flow", default=json.dumps(TWEAKS))
    parser.add_argument("--application_token", type=str, default=APPLICATION_TOKEN, help="Application Token for authentication")
    args = parser.parse_args()

    if args.run_server:
        app.run(debug=True)
    elif args.message:
        try:
            tweaks = json.loads(args.tweaks)
        except json.JSONDecodeError:
            raise ValueError("Invalid tweaks JSON string")

        response = run_flow(
            message=args.message,
            endpoint=args.endpoint,
            tweaks=tweaks,
            application_token=args.application_token
        )
        print(json.dumps(response, indent=2))
    else:
        parser.print_help()


#