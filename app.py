from flask import Flask, render_template, request
import joblib

app = Flask(__name__)

# Load model
model = joblib.load("model/sentiment_model.pkl")
vectorizer = joblib.load("model/vectorizer.pkl")

@app.route("/", methods=["GET", "POST"])
def index():
    prediction = None

    if request.method == "POST":
        text = request.form["text"]
        vector = vectorizer.transform([text])
        result = model.predict(vector)[0]
        prediction = "Positive 😊" if result == 1 else "Negative 😐"

    return render_template("index.html", prediction=prediction)

if __name__ == "__main__":
    app.run(debug=True)
