from flask import Flask, render_template, request
import requests

app = Flask(__name__)

# Function to trigger the API call
def initiate_call(phone_number):
    url = "https://api.bland.ai/v1/calls"
    payload = {
        "phone_number": phone_number,
        "voice": "91040297-765d-4251-a210-7dfbafb0c266",
        "task": "Your name is Shivangi...",
        "pathway_id": "4d0851a4-498c-41b6-b4f1-3e98e3f74dc5",
        "request_data": {}
    }
    headers = {
        "authorization": "sk-acozs8mj8440jx4fu0e4cufvl1za0pjvylj59kc0nr5h1ir9jr5c6zfyorew6gp369",
        "Content-Type": "application/json"
    }

    response = requests.post(url, json=payload, headers=headers)

    if response.status_code == 200:
        response_data = response.json()
        call_id = response_data.get("call_id")
        
        # Use call_id to retrieve call details (if needed)
        call_details_url = f"https://api.bland.ai/v1/calls/{call_id}"
        call_details_response = requests.get(call_details_url, headers=headers)
        if call_details_response.status_code == 200:
            call_details = call_details_response.json()
            from_number = call_details.get("from")
            return from_number
    return None

# Flask route to render the form and handle form submissions
@app.route("/", methods=["GET", "POST"])
def index():
    from_number = None
    if request.method == "POST":
        phone_number = request.form["phone_number"]
        from_number = initiate_call(phone_number)  # Initiate the call using the provided phone number
    return render_template("index.html", from_number=from_number)

if __name__ == "__main__":
    app.run(debug=True)
