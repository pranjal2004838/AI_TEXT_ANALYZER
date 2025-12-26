AI Text Sentiment Analyzer

Lightweight Flask app that predicts text sentiment (Positive / Negative) using a small scikit-learn model. The repository includes a training script (`model.py`), a simple web UI template (`templates/index.html`), and a Flask server (`app.py`) that exposes both an HTML form and a JSON API.

## Requirements
- Python 3.8+
- See `requirements.txt` for Python packages (`flask`, `scikit-learn`, `joblib`).

## Setup
1. Create and activate a virtual environment (recommended):

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

2. Train the model (this creates `model/sentiment_model.pkl` and `model/vectorizer.pkl`):

```bash
python model.py
```

3. Run the Flask app:

```bash
python app.py
```

By default the server runs on `http://127.0.0.1:5000/` and serves the web UI.

## Usage

- Web UI: open `http://127.0.0.1:5000/`, enter text in the textarea and click "Analyze".

- JSON API: the server accepts JSON POST requests to `/` and returns JSON responses. The app also supports HTML form POST submissions from the UI. If you remove the HTML form, use the JSON API or add query-param GET handling.

Example with `curl`:

```bash
curl -X POST -H "Content-Type: application/json" \
  -d '{"text": "I love this product"}' \
  AI Text Sentiment Analyzer

  Lightweight Flask app that predicts text sentiment (Positive / Negative) using a small scikit-learn model. The repository includes a training script (`model.py`), a simple web UI template (`templates/index.html`), and a Flask server (`app.py`) that exposes both an HTML form and a JSON API.

  ## Requirements
  - Python 3.8+
  - See `requirements.txt` for Python packages (`flask`, `scikit-learn`, `joblib`).

  ## Setup
  1. Create and activate a virtual environment (recommended):

  ```bash
  python -m venv .venv
  source .venv/bin/activate
  pip install -r requirements.txt
  ```

  2. Train the model (this creates `model/sentiment_model.pkl` and `model/vectorizer.pkl`):

  ```bash
  python model.py
  ```

  3. Run the Flask app:

  ```bash
  python app.py
  ```

  By default the server runs on `http://127.0.0.1:5000/` and serves the web UI.

  ## Usage

  - Web UI: open `http://127.0.0.1:5000/`, enter text in the textarea and click "Analyze".

  - JSON API: the server accepts JSON POST requests to `/` and returns JSON responses. The app also supports HTML form POST submissions from the UI. If you remove the HTML form, use the JSON API or add query-param GET handling.

  Example with `curl`:

  ```bash
  curl -X POST -H "Content-Type: application/json" \
    -d '{"text": "I love this product"}' \
    http://127.0.0.1:5000/
  ```

  Example using Python `requests`:

  ```python
  import requests
  resp = requests.post("http://127.0.0.1:5000/", json={"text": "Great service"})
  print(resp.json())
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
