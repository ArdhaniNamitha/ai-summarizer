# AI Text Summarizer

This project is a web-based AI text summarizer built using Python and Streamlit. It uses Hugging Face's transformer models to generate well-structured and informative summaries for long-form text. The application is designed with academic and educational use in mind, delivering structured or note-style outputs suitable for study, research, or analysis.

## Features

- **Input via Text Area**  
  Users can paste any article or large block of content directly into the interface. No file upload is required, making the interface lightweight and simple.

- **Multiple Summary Styles**  
  - **Structured Headings**: A multi-section summary organized with relevant headings.
  - **Smart Notes**: Bullet-point notes grouped under automatically generated topics.
  - **Paragraph Summary**: A coherent and readable paragraph summary.

- **Performance-Oriented Summarization**  
  The model intelligently segments large input into manageable chunks before summarizing. This helps optimize speed and ensures completeness.

- **Output Analytics**  
  - Original and summarized word counts  
  - Readability score using Flesch Reading Ease  
  - Top keywords extracted from the input text  

- **Downloadable Output**  
  Summaries can be downloaded as plain text files for offline use.

## Technologies Used

- **Frontend**: Streamlit  
- **Model**: Hugging Face Transformers — `sshleifer/distilbart-cnn-12-6`  
- **Backend Framework**: PyTorch  
- **NLP Utilities**: scikit-learn, textstat  

## Setup and Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/ArdhaniNamitha/ai-text-summarizer
   cd ai-text-summarizer
