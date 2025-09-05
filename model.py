import joblib
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from prep import process_resumes, clean_text

# Load resumes
filenames, resume_texts = process_resumes("resumes/")

# Load job description
with open("job_description.txt", "r", encoding="utf-8") as f:
    job_description = clean_text(f.read())

# Vectorization (TF-IDF)
vectorizer = TfidfVectorizer()
X_resumes = vectorizer.fit_transform(resume_texts)
X_job = vectorizer.transform([job_description])

# Generate labels (1: Good match, 0: Poor match) - Placeholder labels
y_labels = np.random.randint(0, 2, size=len(resume_texts))

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X_resumes, y_labels, test_size=0.2, random_state=42)

# Train model
model = RandomForestClassifier()
model.fit(X_train, y_train)

# Save model
joblib.dump(model, "saved_model.pkl")
joblib.dump(vectorizer, "vectorizer.pkl")

print("Model trained and saved.")
