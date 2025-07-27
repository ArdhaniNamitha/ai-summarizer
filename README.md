---
title: AI Text Summarizer  
colorFrom: indigo  
colorTo: blue  
sdk: streamlit  
sdk_version: "1.32.2"  
app_file: app.py  
pinned: false  
---

# AI Text Summarizer

**Live Demo:** [https://namitha-ai-text-summarizer.hf.space](https://huggingface.co/spaces/cs23-namitha/ai-summarizer)

AI Text Summarizer is a Streamlit-based web application that generates clean, structured summaries from long academic or general-purpose texts using advanced NLP models. The tool supports multiple input formats and provides flexible output styles, making it ideal for students, educators, researchers, and professionals.

---

## Key Features

### Input Options
- Upload files: `.pdf`, `.docx`, `.txt`
- Direct text input (copy-paste)

### Summary Formats
- **Paragraph Summary**: Compact, continuous text
- **Smart Notes**: Bullet-pointed highlights with context-aware grouping
- **Structured Headings**: Hierarchical format ideal for academic use

### Additional Functionality
- Word count comparison (original vs summarized)
- Readability score (Flesch Reading Ease)
- Keyword extraction using `scikit-learn`'s `CountVectorizer`
- Export summaries as downloadable `.txt` files
- Theme toggle (light/dark mode)
- Responsive and clean interface using Streamlit markdown components

---

## Model and Libraries

- **Summarization Model**: `sshleifer/distilbart-cnn-12-6` from Hugging Face
- **Decoding Strategy**: Greedy decoding (efficient and deterministic)
- **NLP Stack**: 
  - `transformers` (Hugging Face)
  - `torch`
  - `scikit-learn`
  - `nltk`, `spacy`
  - `textstat`
- **Text Extraction**: `pdfplumber`, `python-docx`, `PyMuPDF`

---

## Project Structure

```
ai-summarizer/
├── app.py               # Streamlit frontend
├── summarizer.py        # Summarization and NLP logic
├── utils.py             # File parsing, keyword extraction, readability metrics
├── requirements.txt     # Python dependencies
└── README.md            # Project documentation
```

---

## Installation

To run the project locally:

```bash
git clone https://github.com/ArdhaniNamitha/ai-summarizer
cd ai-summarizer
pip install -r requirements.txt
streamlit run app.py
```

---

## Dependencies

```
streamlit>=1.18.0
transformers>=4.25.1
torch>=1.13.1
pdfplumber>=0.7.6
python-docx>=0.8.11
PyMuPDF>=1.21.1
scikit-learn>=1.2.0
textstat>=0.7.3
spacy>=3.4.0
nltk>=3.7
```

---

## License

This project is licensed under the [MIT License].

---

## Author

**Ardhani Namitha**  
GitHub: [github.com/ArdhaniNamitha](https://github.com/ArdhaniNamitha)
