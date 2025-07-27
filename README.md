# AI Text Summarizer

This is a web-based application that intelligently summarizes large bodies of text into clear, concise formats. Built with Streamlit and powered by Hugging Face Transformers, it supports multiple input formats and summary styles tailored for educational and research purposes.

## Features

- **Multiple Summary Styles:**
  - Paragraph Summary – Short, cohesive summary in paragraph form.
  - Smart Notes – Structured bullet-point notes with auto-generated headings.
  - Structured Headings – Detailed academic-style summaries with section titles.

- **Flexible Input Options:**
  - Upload files in `.pdf`, `.docx`, or `.txt` format.
  - Paste custom text directly into the app.

- **Extra Insights:**
  - Word count (original vs. summary)
  - Readability score (Flesch Reading Ease)
  - Keyword extraction using TF-IDF

- **Custom Themes:**
  - Toggle between light and dark modes
  - Modern UI with responsive design

- **Fast Processing:**
  - Uses greedy decoding for faster inference
  - Limits token processing intelligently for performance

## Model & NLP Stack

- **Transformer Model:** `sshleifer/distilbart-cnn-12-6` (via Hugging Face)
- **Libraries Used:**
  - `transformers`, `torch`, `scikit-learn`, `textstat`, `pdfplumber`, `python-docx`, `spacy`, `nltk`

## File Structure

```
├── app.py               # Main Streamlit app
├── summarizer.py        # Text chunking and summarization logic
├── utils.py             # File reading, keyword extraction, and formatting
├── requirements.txt     # All dependencies
└── README.md            # Project documentation
```

## Installation & Running Locally

1. Clone the repository:
   ```bash
   git clone https://github.com/ArdhaniNamitha/ai-summarizer
   cd ai-summarizer
   ```

2. Install the required libraries:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the app:
   ```bash
   streamlit run app.py
   ```

## Requirements

```txt
transformers>=4.25.1
torch>=1.13.1
streamlit>=1.18.0
pdfplumber>=0.7.6
python-docx>=0.8.11
PyMuPDF>=1.21.1
scikit-learn>=1.2.0
textstat>=0.7.3
spacy>=3.4.0
nltk>=3.7
```

## Author

Developed by [Ardhani Namitha](https://github.com/ArdhaniNamitha)

---

This application is built for learners, educators, and professionals who need meaningful, quick summaries without sacrificing context.
