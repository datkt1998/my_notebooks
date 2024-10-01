import streamlit as st
from summarizer.bigquery_utils import (
    read_data_from_bigquery,
    write_to_bigquery,
)
from summarizer.model import summarize_text

st.title("AI Text Summarizer")

# Cho phép người dùng nhập văn bản hoặc chọn từ BigQuery
option = st.selectbox(
    "Chọn nguồn dữ liệu", ["Nhập văn bản", "Dữ liệu từ BigQuery"]
)

if option == "Nhập văn bản":
    user_input = st.text_area("Nhập văn bản để tóm tắt")
    if st.button("Tóm tắt"):
        summary = summarize_text(user_input)
        st.write("Kết quả tóm tắt:")
        st.write(summary)

elif option == "Dữ liệu từ BigQuery":
    query = (
        "SELECT content FROM `your_project.your_dataset.your_table` LIMIT 1"
    )
    rows = read_data_from_bigquery(query)
    for row in rows:
        st.write("Văn bản gốc:")
        st.write(row.content)
        summary = summarize_text(row.content)
        st.write("Kết quả tóm tắt:")
        st.write(summary)

        # Ghi kết quả vào BigQuery
        write_to_bigquery(summary, row.content)
