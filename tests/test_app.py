import pytest
from app import app

def test_index_get():
    with app.test_client() as client:
        response = client.get("/")
        assert response.status_code == 200
        assert b"<form" in response.data  # Check if form is in the HTML

def test_index_post_no_model():
    with app.test_client() as client:
        response = client.post("/", json={"text": "Test input"})
        assert response.status_code == 503
        assert response.json == {"error": "model not available"}

def test_404():
    with app.test_client() as client:
        response = client.get("/nonexistent")
        assert response.status_code == 404
        assert response.json == {"error": "not found"}

def test_index_post_with_json_model():
    with app.test_client() as client:
        # Simulate the presence of the JSON model (mock or actual setup)
        # Assuming the app has a way to enable the model for testing
        app.config['MODEL_AVAILABLE'] = True  # Example flag for testing

        response = client.post("/", json={"text": "Test input"})
        assert response.status_code == 200
        assert "result" in response.json  # Check if the response contains the expected result

def test_index_post_no_form_model():
    with app.test_client() as client:
        # Simulate the absence of the form model
        app.config['FORM_MODEL_AVAILABLE'] = False  # Example flag for testing

        response = client.post("/", data={"text": "Test input"})
        assert response.status_code == 503
        assert response.json == {"error": "form model not available"}

if __name__ == "__main__":
    pytest.main()