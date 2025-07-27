from transformers import BartTokenizer, BartForConditionalGeneration
import torch
import re

# Use a faster model
model_name = "sshleifer/distilbart-cnn-12-6"
tokenizer = BartTokenizer.from_pretrained(model_name)
model = BartForConditionalGeneration.from_pretrained(model_name)

# Split large text into manageable chunks
def split_text(text, max_words=400):
    sentences = re.split(r'(?<=[.!?])\s+', text)
    chunks = []
    chunk = ""
    word_count = 0

    for sentence in sentences:
        words = sentence.split()
        if word_count + len(words) > max_words:
            chunks.append(chunk.strip())
            chunk = sentence + " "
            word_count = len(words)
        else:
            chunk += sentence + " "
            word_count += len(words)

    if chunk:
        chunks.append(chunk.strip())

    return chunks

def summarize_text(text, summary_type="standard"):
    chunks = split_text(text)[:4]  # Limit to 4 chunks for performance
    summaries = []

    for chunk in chunks:
        if summary_type == "detailed":
            prompt = (
                "Summarize the following text in a professional and educational style using appropriate section headings. "
                "Make the summary structured, relevant, and helpful for academic understanding:\n\n" + chunk
            )
        elif summary_type == "notes":
            prompt = (
                "Convert the following content into smart, structured study notes with bullet points and clear sections:\n\n" + chunk
            )
        else:
            prompt = (
                "Summarize this content into clear and informative paragraphs:\n\n" + chunk
            )

        inputs = tokenizer.encode(prompt, return_tensors="pt", max_length=1024, truncation=True)

        #  Fast greedy decoding (instead of sampling)
        summary_ids = model.generate(
            inputs,
            do_sample=False,
            max_length=300,
            min_length=150,
            no_repeat_ngram_size=3
        )

        summary = tokenizer.decode(summary_ids[0], skip_special_tokens=True)
        summaries.append(summary)

    return "\n\n".join(summaries)