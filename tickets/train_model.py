import os
from pathlib import Path

from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
import joblib

def main():
    print("Starting training model...")

    # Inline training data samples
    texts = [
        # Billing
        "I was charged incorrectly on my last bill.",
        "Need to update my payment method.",
        "Why was my credit card declined?",
        # Technical
        "My internet is not working properly.",
        "Cannot connect to the server.",
        "The app crashes when I open it.",
        # General
        "What are your support hours?",
        "How do I reset my password?",
        "I want information about your services.",
        # Complaint
        "I'm unhappy with the way my issue was handled.",
        "The support was rude and unhelpful.",
        "I want to file a complaint about the service."
    ]
    categories = [
        "Billing",
        "Billing",
        "Billing",
        "Technical",
        "Technical",
        "Technical",
        "General",
        "General",
        "General",
        "Complaint",
        "Complaint",
        "Complaint"
    ]

    pipeline = Pipeline([
        ('tfidf', TfidfVectorizer()),
        ('clf', LogisticRegression(max_iter=500))
    ])

    pipeline.fit(texts, categories)
    preds = pipeline.predict(texts)
    accuracy = accuracy_score(categories, preds)
    print(f"Training accuracy on inline dataset: {accuracy:.2%}")

    ml_dir = Path(__file__).parent / 'ml'
    ml_dir.mkdir(parents=True, exist_ok=True)
    model_path = ml_dir / "model.pkl"
    joblib.dump(pipeline, model_path)
    print(f"Model saved to {model_path}")

if __name__ == "__main__":
    main()
