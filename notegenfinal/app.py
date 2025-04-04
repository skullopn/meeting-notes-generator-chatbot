from flask import Flask, render_template, request, jsonify
import google.generativeai as genai  # Import Google Gemini API

app = Flask(__name__)

# Configure Google Gemini API (Replace 'YOUR_API_KEY' with your actual key)
genai.configure(api_key="AIzaSyASI-lW5b4O4fILI5A5K0WjqXfUfGS5WQg")

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/chatbot", methods=["POST"])
def chatbot():
    data = request.get_json()
    if not data or "message" not in data:
        return jsonify({"error": "Invalid request"}), 400

    user_message = data["message"]

    try:
        model = genai.GenerativeModel("models/gemini-1.5-pro-002")  # Or any valid model from your list
  # ✅ Correct model

  # Use Google's Gemini model
        response = model.generate_content(user_message)
        
        if response and hasattr(response, "text"):
            return jsonify({"reply": response.text})  # Send detailed response

        return jsonify({"reply": "Sorry, I couldn't generate a response."})

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)
