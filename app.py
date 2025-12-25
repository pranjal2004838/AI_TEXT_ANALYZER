from flask import Flask, render_template, request, jsonify
import joblib

app = Flask(__name__)

# Load model
model = joblib.load("model/sentiment_model.pkl")
vectorizer = joblib.load("model/vectorizer.pkl")

@app.route("/", methods=["GET", "POST"])
def index():
    prediction = None

    if request.method == "POST":
        # If the client sent JSON, accept JSON and return JSON
        if request.is_json:
            data = request.get_json(silent=True) or {}
            text = (data.get("text") or "").strip()
            if not text:
                return jsonify({"error": "no text provided"}), 400
            try:
                vector = vectorizer.transform([text])
                result = model.predict(vector)[0]
                label = "Positive" if result == 1 else "Negative"
                return jsonify({"prediction": label}), 200
            except Exception:
                return jsonify({"error": "processing error"}), 500

        # Otherwise handle regular HTML form submission and render template
        text = request.form.get("text", "").strip()
        if text:
            vector = vectorizer.transform([text])
            result = model.predict(vector)[0]
            prediction = "Positive 😊" if result == 1 else "Negative 😐"

    return render_template("index.html", prediction=prediction)

if __name__ == "__main__":
    app.run(debug=True)
