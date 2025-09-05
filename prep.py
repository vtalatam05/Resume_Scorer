import os
import re
import nltk
import string
from pdfminer.high_level import extract_text
from sklearn.feature_extraction.text import TfidfVectorizer
from nltk.corpus import stopwords

nltk.download('stopwords')
stop_words = set(stopwords.words('english'))

def extract_text_from_pdf(pdf_path):
    """Extract text from a PDF resume."""
    return extract_text(pdf_path)

def clean_text(text):
    """Basic text preprocessing."""
    text = text.lower()
    text = re.sub(r'\d+', '', text)  # Remove numbers
    text = text.translate(str.maketrans("", "", string.punctuation))  # Remove punctuation
    words = text.split()
    words = [word for word in words if word not in stop_words]
    return ' '.join(words)

def process_resumes(resume_folder):
    """Read, clean, and return text from all resumes."""
    resume_texts = []
    filenames = []
    
    for file in os.listdir(resume_folder):
        if file.endswith('.pdf'):
            text = extract_text_from_pdf(os.path.join(resume_folder, file))
            cleaned_text = clean_text(text)
            resume_texts.append(cleaned_text)
            filenames.append(file)
    
    return filenames, resume_texts

if __name__ == "__main__":
    filenames, resume_texts = process_resumes("resumes/")
    print(f"Processed {len(filenames)} resumes.")
