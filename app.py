import os
import logging
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

# Configuration via environment
MODEL_PATH = os.getenv("MODEL_PATH", "model/sentiment_model.pkl")
VECTORIZER_PATH = os.getenv("VECTORIZER_PATH", "model/vectorizer.pkl")
MAX_TEXT_LENGTH = int(os.getenv("MAX_TEXT_LENGTH", "1000"))



# Safe, lazy model loading
model = None
vectorizer = None
try:
    import joblib

    model = joblib.load(MODEL_PATH)
    vectorizer = joblib.load(VECTORIZER_PATH)
    logger.info("Loaded model from %s and vectorizer from %s", MODEL_PATH, VECTORIZER_PATH)
except Exception as e:
    logger.exception("Failed to load model/vectorizer: %s", e)
    model = None
    vectorizer = None


def validate_text(text):
    if not isinstance(text, str):
        return False, "text must be a string"
    t = text.strip()
    if not t:
        return False, "text is empty"
    if len(t) > MAX_TEXT_LENGTH:
        return False, f"text too long (max {MAX_TEXT_LENGTH})"
    return True, t


@app.errorhandler(500)
def handle_500(e):
    logger.exception("Internal server error: %s", e)
    return jsonify({"error": "internal server error"}), 500


@app.errorhandler(404)
def handle_404(e):
    return jsonify({"error": "not found"}), 404


@app.route("/", methods=["GET", "POST"])
def index():
    prediction = None

    if request.method == "POST":
        if model is None or vectorizer is None:
            logger.error("Model or vectorizer not available for prediction")
            if request.is_json:
                return jsonify({"error": "model not available"}), 503
            prediction = "Error: model not available"
            return render_template("index.html", prediction=prediction), 503

        # JSON API
        if request.is_json:
            data = request.get_json(silent=True) or {}
            ok, result = validate_text(data.get("text", ""))
            if not ok:
                logger.debug("Validation failed for JSON input: %s", result)
                return jsonify({"error": result}), 400
            text = result
            try:
                vector = vectorizer.transform([text])
                res = model.predict(vector)[0]
                label = "Positive" if res == 1 else "Negative"
                return jsonify({"prediction": label}), 200
            except Exception as e:
                logger.exception("Prediction error (JSON): %s", e)
                return jsonify({"error": "processing error"}), 500

        # HTML form
        ok, result = validate_text(request.form.get("text", ""))
        if not ok:
            logger.debug("Validation failed for form input: %s", result)
            prediction = f"Error: {result}"
        else:
            text = result
            try:
                vector = vectorizer.transform([text])
                res = model.predict(vector)[0]
                prediction = "Positive 😊" if res == 1 else "Negative 😐"
            except Exception as e:
                logger.exception("Prediction error (form): %s", e)
                prediction = "Error processing input"

    return render_template("index.html", prediction=prediction)


if __name__ == "__main__":
    debug_flag = os.getenv("FLASK_DEBUG", "0") == "1"
    app.run(debug=debug_flag, host="0.0.0.0", port=int(os.getenv("PORT", "5000")))
