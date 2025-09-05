from flask import Flask, request, jsonify
import joblib
import PyPDF2
import os
from prep import clean_text

app = Flask(__name__)

# Load trained model and vectorizer
model = joblib.load("saved_model.pkl")
vectorizer = joblib.load("vectorizer.pkl")

UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

def extract_text_from_pdf(pdf_path):
    """Extracts text from a PDF file."""
    with open(pdf_path, "rb") as file:
        reader = PyPDF2.PdfReader(file)
        text = ""
        for page in reader.pages:
            text += page.extract_text() if page.extract_text() else ""
        return text

@app.route("/rank", methods=["POST"])
def rank_resume():
    """Ranks a resume based on job description."""
    if "file" not in request.files:
        return jsonify({"error": "No file uploaded"}), 400

    file = request.files["file"]
    
    if file.filename == "":
        return jsonify({"error": "No selected file"}), 400
    
    if not file.filename.endswith(".pdf"):
        return jsonify({"error": "Only PDF files are allowed"}), 400

    file_path = os.path.join(app.config["UPLOAD_FOLDER"], file.filename)
    file.save(file_path)

    # Extract text and preprocess
    resume_text = extract_text_from_pdf(file_path)
    cleaned_resume = clean_text(resume_text)
    resume_vector = vectorizer.transform([cleaned_resume])

    # Predict score
    score = model.predict_proba(resume_vector)[0][1]  # Probability of being a good match
    return jsonify({"score": float(score)})

if __name__ == "__main__":
    app.run(debug=True)
