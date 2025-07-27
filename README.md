# AI Text Summarizer

This repository contains a web-based application that generates clear, structured, and academically appropriate summaries from lengthy articles, documents, or pasted text. The application is built using Python, Streamlit, and Hugging Face Transformers and is optimized for both performance and usability. It is particularly useful for students, educators, and researchers seeking concise yet informative content from large textual inputs.

## Key Features

- **Multiple Summary Modes:**
  - **Paragraph Mode:** Coherent, compact summaries written in paragraph form.
  - **Smart Notes Mode:** Bullet-point notes with auto-generated, content-aware section headings.
  - **Detailed Summary Mode:** Well-organized summaries divided into meaningful sections, ideal for academic and study purposes.

- **File Upload Support:**
  - Accepts `.pdf`, `.docx`, and `.txt` file types.
  - Alternatively, users can paste text directly into the interface.

- **Output Enhancements:**
  - Displays original and summarized word count.
  - Calculates readability score using Flesch Reading Ease.
  - Extracts keywords using count-based vectorization.
  - Allows downloading summaries in `.txt` format.

- **Performance Improvements:**
  - Uses greedy decoding for significantly faster response times.
  - Limits processing to the most relevant chunks of text for efficiency.
  - Implements TF-IDF to dynamically generate section headings for contextual clarity.

## Technologies Used

- **Frontend:** Streamlit
- **NLP Model:** Hugging Face Transformers (`sshleifer/distilbart-cnn-12-6`)
- **Backend:** PyTorch
- **Text Analytics:** scikit-learn (TF-IDF), textstat
- **File Processing:** pdfplumber, python-docx

## Installation and Local Usage

To run the application locally:

```bash
git clone https://github.com/ArdhaniNamitha/ai-text-summarizer
cd ai-text-summarizer
pip install -r requirements.txt
streamlit run app.py
```

## File Structure

```
├── app.py               # Streamlit frontend and layout
├── summarizer.py        # Summarization logic using transformers
├── utils.py             # Text extraction, readability, keyword detection
├── requirements.txt     # List of Python dependencies
└── README.md            # Project documentation
```

## Model Details

- **Model Used:** [sshleifer/distilbart-cnn-12-6](https://huggingface.co/sshleifer/distilbart-cnn-12-6)
- **Framework:** Hugging Face Transformers
- **Decoding Strategy:** Greedy decoding for optimized performance

## Author

Developed and maintained by [Ardhani Namitha](https://github.com/ArdhaniNamitha).

