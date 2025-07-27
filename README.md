---
title: AI Text Summarizer
emoji: ""
colorFrom: indigo
colorTo: blue
sdk: streamlit
sdk_version: "1.32.2"
app_file: app.py
pinned: false
---

# AI Text Summarizer

This is a web-based application that generates clear, structured, and academically useful summaries from large documents or text inputs. Built using Python, Streamlit, and Hugging Face Transformers, this app is designed for students, researchers, and educators looking for faster content digestion.

## Features

- Multiple Summary Modes  
  - Paragraph Summary: Clear, concise summaries in paragraph format.  
  - Smart Notes: Bullet-style notes with generated section headings for easy revision.  
  - Structured Headings: Summaries broken into academic-style sections for in-depth understanding.  
- Flexible Input  
  - Supports .pdf, .docx, and .txt uploads.  
  - Option to paste text directly into the interface.  
- Smart Output  
  - Word count (original vs summary)  
  - Readability score using Flesch Reading Ease  
  - Keyword extraction with CountVectorizer  
  - Option to download the summary  
- Performance Optimizations  
  - Greedy decoding for fast summarization  
  - Summarization limited to top 4 chunks for efficiency  
  - Uses TF-IDF for smart headings in notes format

## Tech Stack

- Frontend: Streamlit  
- Model: sshleifer/distilbart-cnn-12-6 (Hugging Face Transformers)  
- NLP/Backend: PyTorch, scikit-learn, textstat  
- File Handling: pdfplumber, python-docx

## How to Run Locally

```bash
git clone https://github.com/ArdhaniNamitha/ai-summarizer
cd ai-summarizer
pip install -r requirements.txt
streamlit run app.py
```

## Project Structure

├── app.py               # Streamlit frontend and layout  
├── summarizer.py        # Summarization logic using transformers  
├── utils.py             # Text extraction, readability, keyword detection  
├── requirements.txt     # Python dependencies  
└── README.md            # Project documentation

## Model Info

- Model: sshleifer/distilbart-cnn-12-6  
- Strategy: Greedy decoding  
- Use Case: Long-document summarization

## Author

Developed by Ardhani Namitha
