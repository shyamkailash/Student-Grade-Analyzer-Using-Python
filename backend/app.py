from grade_calculator import generate_report

from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


@app.route("/")
def home():
    return jsonify({
        "message": "Student Grade Analyzer Backend is running!"
    })


@app.route("/api/health")
def health():
    return jsonify({
        "status": "success",
        "message": "Backend connected successfully"
    })


@app.route("/api/calculate", methods=["POST"])
def calculate():
    from flask import request

    data = request.get_json()

    if not data:
        return jsonify({"error": "No data received"}), 400

    student_name = data.get("student_name", "").strip()
    marks = data.get("marks")

    if not student_name:
        return jsonify({"error": "Student name is required"}), 400

    if not isinstance(marks, dict) or not marks:
        return jsonify({"error": "Enter at least one subject"}), 400

    for subject, mark in marks.items():
        if not isinstance(subject, str) or not subject.strip():
            return jsonify({"error": "Invalid subject name"}), 400

        if isinstance(mark, bool) or not isinstance(mark, (int, float)):
            return jsonify({"error": "Marks must be numbers"}), 400

        if not 0 <= mark <= 100:
            return jsonify({"error": "Marks must be between 0 and 100"}), 400

    report = generate_report(student_name, marks)

    return jsonify(report)


if __name__ == "__main__":
    app.run(debug=True, port=5000)
