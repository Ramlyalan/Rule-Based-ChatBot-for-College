from flask import Flask, render_template, request, jsonify
from chatbot import chatbot_response

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/get", methods=["POST"])
def get_bot_response():
    user_input = request.form["msg"]
    bot_data = chatbot_response(user_input)
    return jsonify(bot_data)

if __name__ == "__main__":
    app.run(debug=True)