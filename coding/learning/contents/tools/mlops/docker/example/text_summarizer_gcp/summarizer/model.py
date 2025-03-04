from transformers import pipeline

# Tạo pipeline tóm tắt văn bản
summarizer = pipeline("summarization")


# Hàm tóm tắt văn bản
def summarize_text(text, max_len=150, min_len=30):
    summary = summarizer(
        text, max_length=max_len, min_length=min_len, do_sample=False
    )
    return summary[0]["summary_text"]
