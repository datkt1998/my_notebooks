from google.cloud import bigquery

# Kết nối BigQuery
client = bigquery.Client()


# Đọc dữ liệu từ BigQuery
def read_data_from_bigquery(query):
    query_job = client.query(query)
    return query_job.result()


# Ghi log và kết quả tóm tắt vào BigQuery
def write_to_bigquery(summary, original_text):
    table_id = "your_project.your_dataset.your_result_table"
    rows_to_insert = [{"original_text": original_text, "summary": summary}]

    # Ghi dữ liệu vào bảng
    errors = client.insert_rows_json(table_id, rows_to_insert)
    if errors == []:
        print("Ghi thành công!")
    else:
        print(f"Có lỗi: {errors}")
