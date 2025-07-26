import streamlit as st
from summarizer import summarize_text
from utils import get_readability, get_word_count, extract_keywords, format_as_study_notes

# Page config
st.set_page_config(page_title="AI Text Summarizer", layout="wide")

# Theme toggle
if "dark_mode" not in st.session_state:
    st.session_state.dark_mode = False

col1, col2 = st.columns([1, 9])
with col1:
    if st.button("Toggle Theme"):
        st.session_state.dark_mode = not st.session_state.dark_mode

# Theme settings
dark = st.session_state.dark_mode
bg_gradient = "linear-gradient(135deg, #1e1e1e, #000000)" if dark else "linear-gradient(135deg, #e0c3fc, #8ec5fc)"
text_color = "#ffffff" if dark else "#000000"
card_color = "#2a2a2a" if dark else "#ffffffcc"
primary_btn = "#3f51b5" if dark else "#6a1b9a"
header_color = "#3949ab" if dark else "#1a237e"

# Custom styles
st.markdown(f"""
    <style>
    html, body, [data-testid="stAppViewContainer"] {{
        font-family: 'Segoe UI', sans-serif;
        background: {bg_gradient};
        color: {text_color};
    }}
    .title {{
        text-align: center;
        font-size: 40px;
        font-weight: bold;
        color: {header_color};
        margin-top: 20px;
    }}
    label, .stSelectbox label, .stTextArea label {{
        color: {text_color} !important;
        font-weight: bold;
    }}
    .summary-box {{
        background-color: {card_color};
        padding: 20px;
        border-radius: 10px;
        box-shadow: 0 5px 15px rgba(0,0,0,0.2);
        margin-top: 30px;
        color: {text_color};
    }}
    .stButton>button {{
        background-color: {primary_btn};
        color: white !important;
        border-radius: 6px;
        padding: 8px 24px;
        font-weight: bold;
    }}
    .stButton>button:hover {{
        background-color: white !important;
        color: {primary_btn} !important;
        border: 2px solid {primary_btn};
    }}
    .stDownloadButton>button {{
        background-color: #2e7d32;
        color: white;
        padding: 8px 20px;
        border-radius: 6px;
        font-weight: bold;
        margin-top: 10px;
    }}
    </style>
""", unsafe_allow_html=True)

# Title
st.markdown(f'<div class="title">AI Text Summarizer</div>', unsafe_allow_html=True)

# Input section
text_input = st.text_area("Paste your content here", height=300)
format_option = st.selectbox("Select summary format", ["Structured Headings", "Smart Notes", "Paragraph Summary"])

# Generate summary
if st.button("Generate Summary"):
    input_text = text_input.strip()

    if not input_text:
        st.error("No input provided. Please paste your content.")
    else:
        summary_type = (
            "detailed" if format_option == "Structured Headings"
            else "notes" if format_option == "Smart Notes"
            else "standard"
        )

        summary = summarize_text(input_text, summary_type=summary_type)
        word_count = get_word_count(input_text)
        summary_wc = get_word_count(summary)
        readability = get_readability(summary)
        keywords = extract_keywords(input_text)

        formatted = format_as_study_notes(summary, original_text=input_text) if summary_type == "notes" else summary

        st.markdown('<div class="summary-box">', unsafe_allow_html=True)
        st.markdown(f"**Structured Summary:**\n\n{formatted}")
        st.markdown('</div>', unsafe_allow_html=True)

        st.markdown(f"- Original Word Count: `{word_count}`")
        st.markdown(f"- Summary Word Count: `{summary_wc}`")
        st.markdown(f"- Readability Score: `{readability:.2f}`")
        st.markdown(f"- Extracted Keywords: `{', '.join(keywords)}`")

        st.download_button("Download Summary", data=formatted, file_name="summary.txt", mime="text/plain")
