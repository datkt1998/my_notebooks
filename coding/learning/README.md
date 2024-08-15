# Hướng Dẫn Thêm Tài Liệu Mới Vào Jupyter Book

## Mục lục
- [1. Cấu trúc thư mục](#2-cấu-trúc-thư-mục)
- [2. Thêm tài liệu mới](#3-thêm-tài-liệu-mới)
- [3. Cập nhật Table of Contents (toc)](#4-cập-nhật-table-of-contents-toc)
- [4. Build và kiểm tra sách](#5-build-và-kiểm-tra-sách)
- [5. Troubleshooting](#6-troubleshooting)

## 2. Cấu trúc thư mục
Trước khi thêm tài liệu mới, hãy chắc chắn bạn đã hiểu về cấu trúc thư mục của dự án Jupyter Book:
```bash
project-root/
├── _config.yml
├── _toc.yml
├── _jupyterbook_config/
│ └── <Các file intro, thumbnail,...>
│
├── content/
│ ├── part 1/
│ │ ├── chapter 1/
│ │ │ ├── section 1.md
│ │ │ └── <<<new section>>>
│ │ │
│ │ ├──chapter 2/
│ │ │ └──...
│ │ │
│ │ └── <<<new chapter>>>
│ │
│ │
│ ├── part 2/
│ └── <<<new part>>>
│
└── ...
```

- **`_config.yml`**: File cấu hình chính của Jupyter Book.
- **`_toc.yml`**: File định nghĩa mục lục cho sách.
- **`content/`**: Thư mục chứa toàn bộ các tài liệu (markdown, notebook, v.v.).

## 3. Thêm tài liệu mới
Để thêm một tài liệu mới vào Jupyter Book, cần thực hiện các bước sau:

1. **Tạo file tài liệu mới**:  
   Trong thư mục `content/`, tạo một file Markdown (`.md`) hoặc Jupyter Notebook (`.ipynb`). 

   Trong đó, File được structure theo dạng **duy nhất 1 header level 1** vì header 1 sẽ đại diện cho title của File, ví dụ:
   ```markdown
    # Chapter 1 title <level 1> ---> TITLE FILE (chapter, section, sub-section)

    ## Chapter 1 second header <level 2>

    ### Chapter 1 third header <level 3>

    ## Chapter 2 second header <level 2>
    ...
   ```

   > Với mỗi một chapter hoặc section thì luôn phải có 

2. **Cập nhật Table of Contents (toc)**
   - Thêm đường dẫn file vừa tạo vào mục lục (`_toc.yml`) để hiển thị trong Jupyter Book
   > Có 3 level of TOC: part --> chapter --> section  --> sub-section -->

   - Nếu là một group (chapter, section của một list sub-section) sẽ hiện ở left-side của trang web thì cần tạo file tiêu đề `.md`: 
   ```markdown
    # <Title>

    ```{tableofcontents}
    ```                                                    .
   ```

   - Nếu file là 1 section:
   ```yaml
    - title: Chapter 2
      sections:
        - file: chapter2/your-new-document
    ```

    - Nếu file là 1 section trong section khác:
   ```yaml
    - title: Chapter 2
      sections:
        - file: chapter2/section1
          section:
            - file: chapter2/section1/section1.1
    ```
    > Tips: Ta hoàn toàn có thể lồng các section trong 1 section khác


    *Các loại contents*
    - `file`: đường dẫn đến 1 file đại điện cho `chapter`, `section`, hoặc `sub-section`
    - `url`: đường dẫn đến 1 website
      - `title`: text đại diện cho `url` thay vì hiện full hyperlink
    - `glob`: đường dẫn thể hiện ở dạng multi local file, thứ tự khi insert vào book được order theo tên
3. **Build và check**

    ```bash
    jupyter-book build ./coding/learning
    ```

    Sau khi build thành công, mở file index.html trong thư mục `_build/html/` bằng trình duyệt để kiểm tra.

    Nếu trong quá trình build gặp lỗi, sử dụng `jupyter-book clean ./coding/learning` để xóa các file build trước đó và thử build lại từ đầu. 

4. **Publish to website**

    ```bash
    pip install jupyter-book nbmanips ghp-import
    ghp-import -n -p -f ./coding/learning/_build/html
    ```