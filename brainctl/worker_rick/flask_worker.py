# brainctl/worker_rick/flask_worker.py

from flask import Flask, request, jsonify
from brainctl.worker_rick.core import SkillRegistry

app = Flask(__name__)
SkillRegistry.load_skills()

@app.route("/ask", methods=["POST"])
def ask():
    data = request.get_json()
    question = data.get("question", "")
    if not question:
        return jsonify({"error": "No question provided"}), 400

    response = SkillRegistry.handle_question(question)
    return jsonify({"response": response})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

