# AI Text Sentiment Analyzer

Lightweight Flask app that predicts text sentiment (Positive / Negative) using a small scikit-learn model. The repository includes a training script (`model.py`), a simple web UI template (`templates/index.html`), and a Flask server (`app.py`) that exposes both an HTML form and a JSON API.

## Quick Start Guide

Follow these simple steps to get the app running in under 5 minutes:

### 1. Clone the Repository

```bash
git clone https://github.com/pranjal2004838/AI_TEXT_ANALYZER.git
cd AI_TEXT_ANALYZER
```

### 2. Set Up the Environment

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

### 3. Train the Model

```bash
python model.py
```

This will create `sentiment_model.pkl` and `vectorizer.pkl` in the `model/` directory.

### 4. Run the Application

```bash
python app.py
```

The app will be available at `http://127.0.0.1:5000/`.

### 5. Use the Application

- **Web UI**: Open `http://127.0.0.1:5000/` in your browser, enter text, and click "Analyze".
- **JSON API**: Send a POST request to `/` with JSON data. Example:

```bash
curl -X POST -H "Content-Type: application/json" \
  -d '{"text": "I love this product"}' \
  http://127.0.0.1:5000/
```

## Files

- `model.py` — trains and saves the model and vectorizer to `model/`.
- `app.py` — Flask application that loads the model and serves UI/API.
- `templates/index.html` — simple HTML interface.
- `model/` — directory that will contain `sentiment_model.pkl` and `vectorizer.pkl`.

## Notes

- The included training data is minimal and intended for demonstration. For production use, train with a larger, labeled dataset, and add input validation and security checks.

## License

This project is provided as-is for learning and experimentation.
