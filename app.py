from flask import Flask, render_template, request

app = Flask(__name__)

# Chatbot responses
responses = {
    "hello": "Hello! How can I assist you today?",
    "how are you": "I'm just a bot, but I'm doing great!",
    "bye": "Goodbye! Have a nice day!",
}

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/get", methods=["GET"])
def chatbot_response():
    user_text = request.args.get("msg").lower()
    return responses.get(user_text, "I'm not sure how to respond to that.")

if __name__ == "__main__":
    app.run(debug=True)
