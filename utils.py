import textstat
from docx import Document
import pdfplumber
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
import numpy as np
import re


def get_readability(text):
    return textstat.flesch_reading_ease(text)

def get_word_count(text):
    return len(text.split())

def extract_text_from_file(file_path, ext):
    text = ""
    if ext == ".pdf":
        with pdfplumber.open(file_path) as pdf:
            for page in pdf.pages:
                text += page.extract_text() or ""
    elif ext == ".docx":
        doc = Document(file_path)
        text = "\n".join([p.text for p in doc.paragraphs])
    elif ext == ".txt":
        with open(file_path, "r", encoding="utf-8") as f:
            text = f.read()
    return text

def extract_keywords(text, top_n=5):
    vec = CountVectorizer(stop_words="english", max_features=1000)
    X = vec.fit_transform([text])
    word_freq = np.array(X.sum(axis=0)).flatten()
    keywords = np.array(vec.get_feature_names_out())[word_freq.argsort()[::-1]]
    return keywords[:top_n]

def generate_dynamic_headings_for_chunks(chunks):
    headings = []
    vec = TfidfVectorizer(stop_words="english", max_features=100)
    texts = [" ".join(chunk) for chunk in chunks]
    tfidf = vec.fit_transform(texts)
    terms = np.array(vec.get_feature_names_out())

    for row in tfidf.toarray():
        scores = row
        top = terms[scores.argsort()[::-1]][:3]
        heading = " ".join(top).title()
        headings.append(heading if heading else "Topic Overview")

    return headings

def format_as_study_notes(summary_text, original_text=None):
    title = "Summary"
    if original_text:
        lines = original_text.strip().splitlines()
        for line in lines:
            if line.strip() and len(line.strip()) < 120:
                title = line.strip()
                break

    sentences = re.split(r'(?<=[.!?])\s+', summary_text)
    chunks = []
    current_chunk = []

    for i, sentence in enumerate(sentences):
        if sentence.strip():
            current_chunk.append(sentence.strip())
        if len(current_chunk) >= 4 or i == len(sentences) - 1:
            chunks.append(current_chunk)
            current_chunk = []

    # Generate all dynamic headings in one pass (faster)
    headings = generate_dynamic_headings_for_chunks(chunks)

    output = f"## {title}\n"
    for i, chunk in enumerate(chunks):
        heading = headings[i] if i < len(headings) else f"Section {i+1}"
        output += f"\n\n### {heading}\n\n"
        for sentence in chunk:
            output += f"- {sentence.rstrip('.')}\n"

    return output.strip()
