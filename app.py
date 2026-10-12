```python
from flask import Flask, request, jsonify
from result_logic import predict_result

app = Flask(__name__)


@app.route("/", methods=["GET"])
def home():
    return jsonify({
        "message": "Student Result Prediction API is running"
    })


@app.route("/predict", methods=["POST"])
def predict():
    data = request.get_json(silent=True)

    if not data:
        return jsonify({
            "error": "Please provide JSON input"
        }), 400

    if "internal_marks" not in data or "attendance" not in data:
        return jsonify({
            "error": "internal_marks and attendance are required"
        }), 400

    try:
        internal_marks = float(data["internal_marks"])
        attendance = float(data["attendance"])
    except (TypeError, ValueError):
        return jsonify({
            "error": "Marks and attendance must be numbers"
        }), 400

    result = predict_result(internal_marks, attendance)

    return jsonify({
        "internal_marks": internal_marks,
        "attendance": attendance,
        "predicted_result": result
    })


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=False)
```
