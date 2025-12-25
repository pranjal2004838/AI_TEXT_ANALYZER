from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
import joblib

# Sample training data (small but valid)
texts = [
    "I love this product",
    "This is amazing",
    "Very happy with the service",
    "I hate this",
    "This is terrible",
    "Worst experience ever"
]

labels = [1, 1, 1, 0, 0, 0]  # 1 = Positive, 0 = Negative

# Vectorize text
vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(texts)

# Train model
model = LogisticRegression()
model.fit(X, labels)

# Save model and vectorizer
joblib.dump(model, "model/sentiment_model.pkl")
joblib.dump(vectorizer, "model/vectorizer.pkl")

print("✅ Model trained and saved")
