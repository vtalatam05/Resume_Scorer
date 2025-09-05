# Resume Scorer

A Flask-based API that scores resumes (PDF or raw text) against a job description using Machine Learning.  
It extracts text from resumes, preprocesses it, and predicts how well the resume matches the job requirements.

---

## 🚀 Features
- Upload resume in **PDF format**
- Automatic text extraction from PDF resumes
- Preprocessing & cleaning (stopwords removal, tokenization, etc.)
- ML-based scoring using a trained model
- Flask REST API for easy integration

---

## 🛠️ Tech Stack
- **Python**
- **Flask**
- **scikit-learn**
- **NLTK**
- **PyPDF2**
- **joblib**

---

## 📂 Project Structure
Resume_Scorer/  
  ├─ app.py              # Flask API (accepts PDF upload or JSON text)  
  ├─ model.py            # Training script (processes resumes, trains and saves model)  
  ├─ prep.py             # Text preprocessing utilities (clean_text, etc.)  
  ├─ saved_model.pkl     # Trained ML model (generated after running model.py)  
  ├─ vectorizer.pkl      # TF-IDF vectorizer (generated after running model.py)  
  ├─ requirements.txt    # Python dependencies  
  └─ README.md           # This file

---

## ⚙️ Setup & Installation

1. (Optional) Create and activate a virtual environment:
   ~~~bash
   python -m venv venv
   # Windows (PowerShell)
   venv\Scripts\Activate
   # Mac/Linux
   source venv/bin/activate
  2. Install Requirements:
       pip install -r requirements.txt
  3. Run the training script:
       python model.py
  4. Start the Flask app:
       python app.py
     
---

## 🧪 API Endpoints

### 1) Score Resume (PDF upload)
**Endpoint:**  
`POST /upload_resume`

**Description:** Upload a resume in **PDF format** and receive a score.

#### Request (Postman – form-data):
- Method: `POST`
- URL: `http://127.0.0.1:5000/upload_resume`
- Body → `form-data`  
  - Key: `file`  
  - Type: `File`  
  - Value: *(choose your PDF resume)*

#### Example Response:
```json
{
  "score": 0.87
}
```

#### Example cURL:
```bash
curl -X POST http://127.0.0.1:5000/upload_resume -F "file=@/path/to/your_resume.pdf"
```

---

### 2) Score Resume (Raw Text)
**Endpoint:**  
`POST /rank`

**Description:** Send raw resume text as JSON instead of uploading a PDF.

#### Request (JSON body):
```json
{
  "resume": "Experienced Python developer skilled in Flask, ML, and NLP..."
}
```

#### Example Response:
```json
{
  "score": 0.92
}
```

#### Example cURL:
```bash
curl -X POST http://127.0.0.1:5000/rank -H "Content-Type: application/json" -d '{"resume":"Your resume text here"}'
```

---

## ✅ Postman Quick Steps
1. Start Flask server:
   ```bash
   python app.py
   ```
2. Open Postman → New → Request  
3. Choose **POST** method  
4. Enter URL (e.g., `http://127.0.0.1:5000/upload_resume`)  
5. Go to **Body**:
   - For PDF → select **form-data** → Key = `file` → Type = File → Upload resume.  
   - For Raw text → select **raw** → JSON → Paste JSON resume.  
6. Click **Send** → See response with score.

---

## 📌 Notes
- If the score is very low or always the same, check whether your model (`saved_model.pkl`) was trained properly.  
- For image-based PDFs, OCR (like `pytesseract`) is required, since PyPDF2 extracts only text.  
- Make sure `vectorizer.pkl` and `saved_model.pkl` are in the root directory before running `app.py`.

---
