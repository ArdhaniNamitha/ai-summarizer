from transformers import BartTokenizer, BartForConditionalGeneration
import torch
import re

model_name = "sshleifer/distilbart-cnn-12-6"
tokenizer = BartTokenizer.from_pretrained(model_name)
model = BartForConditionalGeneration.from_pretrained(model_name)

def split_text(text, max_words=400):
    sentences = re.split(r'(?<=[.!?])\s+', text)
    chunks, chunk, word_count = [], "", 0

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
    chunks = split_text(text)[:4]  # Safety cap for performance
    summaries = []

    for chunk in chunks:
        if summary_type == "detailed":
            prompt = (
                "Provide a well-structured, informative summary of the following content. The summary should include key points, concepts, and explanations helpful for academic or study purposes:\n\n" + chunk
            )
        elif summary_type == "notes":
            prompt = (
                "Convert the following text into organized, concise study notes with bullet points and clear topic sections:\n\n" + chunk
            )
        else:
            prompt = (
                "Summarize this content clearly and thoroughly with coherent structure and detail:\n\n" + chunk
            )

        inputs = tokenizer.encode(prompt, return_tensors="pt", max_length=1024, truncation=True)
        summary_ids = model.generate(
            inputs,
            do_sample=False,
            max_length=280,  # Higher limit for longer summaries
            min_length=150,
            no_repeat_ngram_size=3
        )
        summary = tokenizer.decode(summary_ids[0], skip_special_tokens=True)
        summaries.append(summary)

    return "\n\n".join(summaries)
