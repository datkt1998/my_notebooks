# Generative AI Overview

## What is the GenAI ?

Generative AI is an exciting branch of artificial intelligence that focuses on creating new content instead of simply analyzing or processing existing data. It leverages patterns learned from vast amounts of training data to produce entirely original outputs. Key points include:
- **Creation of Novel Content:** Generative AI can produce text, images, videos, 3D models, code, and more. For instance, ChatGPT generates dynamic, real-time responses based on extensive language training.
- **Underlying Techniques:** Various methods power generative AI, such as:
    - **Large Language Models (LLMs):** These models, like ChatGPT, are trained on vast text corpora to predict and generate human-like language.
    - **Diffusion Models:** Often used for image generation, these start with random noise and refine it into detailed visuals.
    - **Generative Adversarial Networks (GANs):** By pitting a generator against a discriminator, GANs iteratively improve the realism of the produced content.
    - **Neural Radiance Fields**: These advanced techniques help in generating complex 3D models
    - **Hybrid Models:** Combine strengths of multiple approaches (**LLMs + GANs**)
- **Industry Impact:** With significant investments from major tech firms worldwide, generative AI is recognized as a key domain that could transform creative industries, corporate workflows, and technological innovation.

Overall, generative AI represents a transformative technology that not only powers innovative applications like ChatGPT and image generators but also heralds a new era in content creation and digital interaction.

**1. Vector Embedding**

- Là quá trình chuyển đổi từ ngữ, câu hoặc đoạn văn bản thành các vector số trong không gian đa chiều.
- Mỗi vector chứa đựng các đặc trưng ngữ nghĩa và ngữ cảnh của từ, giúp các mô hình hiểu được sự tương đồng và mối quan hệ giữa các từ.
- Các phương pháp như word2vec, GloVe và FastText đều sử dụng ý tưởng này để biểu diễn ngôn ngữ dưới dạng số học, từ đó hỗ trợ nhiều tác vụ như phân loại, tìm kiếm và sinh văn bản.

---

**2. Vector Database**

- Đây là loại cơ sở dữ liệu chuyên dụng để lưu trữ và truy vấn các vector embedding.
- Được tối ưu cho các truy vấn tìm kiếm gần đúng (nearest neighbor search), vector database cho phép nhanh chóng xác định những vector có độ tương đồng cao với vector truy vấn.
- Ứng dụng của chúng rất phổ biến trong các hệ thống đề xuất, tìm kiếm ngữ nghĩa và các ứng dụng xử lý dữ liệu văn bản quy mô lớn.

---

**3. Transformer Model trong NLP**

- Transformer là kiến trúc mạng nơ-ron tiên tiến, được giới thiệu qua bài báo "Attention is All You Need" năm 2017.
- Điểm nổi bật của Transformer là cơ chế tự chú ý (self-attention), cho phép mô hình xử lý toàn bộ chuỗi dữ liệu song song thay vì theo tuần tự, từ đó khai thác được mối quan hệ giữa các từ trong câu một cách hiệu quả.
- Transformer đã tạo nền tảng cho các mô hình ngôn ngữ hiện đại như BERT, GPT và RoBERTa, mang lại những bước tiến vượt bậc trong các tác vụ như dịch máy, tóm tắt văn bản, và sinh văn bản tự động.

---

**4. LM Models là gì?**  
LM (Language Models) là các mô hình được thiết kế để dự đoán xác suất của chuỗi từ (hoặc token) trong ngôn ngữ tự nhiên. Chúng học cách hiểu cấu trúc và ngữ cảnh của ngôn ngữ qua việc xử lý một lượng lớn dữ liệu văn bản. Mục tiêu chính là dự đoán từ tiếp theo trong một chuỗi dựa trên các từ đã có, từ đó hỗ trợ các tác vụ như sinh văn bản, dịch máy, tóm tắt, và nhiều ứng dụng khác trong NLP.

**Các loại LM Models**

- **Mô hình thống kê (Statistical Language Models):**
    - **Mô hình n-gram:**  
        Dựa trên xác suất thống kê của chuỗi từ liền kề (ví dụ: 2-gram, 3-gram, v.v.). Mặc dù đơn giản và dễ triển khai, nhưng chúng thường không nắm bắt được ngữ cảnh dài hạn và phụ thuộc nhiều vào dữ liệu để ước tính xác suất.
    
- **Mô hình dựa trên mạng nơ-ron (Neural Language Models):**
    - **RNN (Recurrent Neural Networks):**  
        Các mô hình như LSTM hay GRU được thiết kế để xử lý dữ liệu tuần tự. Chúng cho phép ghi nhớ thông tin trong các chuỗi dài, nhưng đôi khi gặp khó khăn với việc xử lý song song và giữ thông tin rất dài.
        
    - **Transformer Models:**
        - **Autoregressive Models:**  
            Ví dụ như GPT (Generative Pre-trained Transformer), sử dụng cơ chế tự chú ý (self-attention) để sinh ra văn bản theo trình tự từ trái sang phải. Những mô hình này dự đoán từ tiếp theo dựa trên toàn bộ ngữ cảnh đã có.
        - **Masked Language Models:**  
            Ví dụ như BERT, không trực tiếp sinh văn bản mà tập trung vào việc hiểu ngữ cảnh bằng cách che khuất một số token trong câu và huấn luyện mô hình dự đoán các token bị che đó.
            
**Cơ chế sinh ra từ tiếp theo trong LLM Models**

Trong các mô hình ngôn ngữ lớn (LLM) như GPT, quá trình sinh từ tiếp theo diễn ra theo cơ chế tự hồi (autoregressive) theo các bước sau:

1. **Nhận và Mã hóa Input:**  
    Mô hình nhận một chuỗi văn bản (prompt) và chuyển đổi chúng thành các vector nhúng (embeddings).
2. **Xử lý qua Kiến trúc Transformer:**  
    Với cơ chế tự chú ý, Transformer xử lý toàn bộ chuỗi input để hiểu được mối quan hệ giữa các token, tạo ra các biểu diễn ngữ cảnh giàu thông tin.
3. **Dự đoán Xác suất:**  
    Một lớp tuyến tính (linear layer) kết hợp với hàm softmax được sử dụng để chuyển đổi các biểu diễn ngữ cảnh thành một phân phối xác suất cho mỗi token trong từ điển.
4. **Chọn Token Tiếp Theo:**  
    Từ phân phối xác suất, mô hình chọn token có xác suất cao nhất (hoặc áp dụng các kỹ thuật như top-k sampling hay nucleus sampling) để sinh ra token tiếp theo.
5. **Lặp lại Quá trình:**  
    Token mới sinh ra được thêm vào chuỗi đầu vào và quá trình dự đoán lặp lại cho đến khi đạt được độ dài mong muốn hoặc gặp token kết thúc.

Như vậy, thông qua việc sử dụng cơ chế tự chú ý và dự đoán theo trình tự, LLM models có thể tạo ra các văn bản tự nhiên, mạch lạc và phù hợp với ngữ cảnh được cung cấp.

---

**5. Self-supervised learning**  
Self-supervised learning là một phương pháp huấn luyện mô hình mà không cần đến dữ liệu được gán nhãn thủ công. Thay vào đó, mô hình tự sinh ra "nhãn" từ chính dữ liệu đầu vào của nó. Ví dụ, trong xử lý ngôn ngữ tự nhiên, một mô hình có thể che đi một số từ trong câu và yêu cầu mô hình dự đoán từ bị che đó dựa trên ngữ cảnh xung quanh.

**Ứng dụng của Self-supervised Learning trong LLM**

- **Tiền huấn luyện (Pre-training):**  
    Các mô hình ngôn ngữ lớn (LLM) như GPT và BERT được tiền huấn luyện trên lượng dữ liệu văn bản khổng lồ sử dụng các nhiệm vụ tự giám sát như:
    
    - **Dự đoán từ tiếp theo (Next Token Prediction):**  
        Áp dụng trong các mô hình autoregressive như GPT, mô hình học cách dự đoán từ tiếp theo dựa trên các từ đã biết.
    - **Masked Language Modeling (MLM):**  
        Áp dụng trong các mô hình như BERT, trong đó một số token được che đi và mô hình học cách dự đoán các token đó dựa trên ngữ cảnh.
- **Tận dụng dữ liệu không gán nhãn:**  
    Nhờ self-supervised learning, LLM có thể khai thác lượng lớn dữ liệu văn bản không cần nhãn, giúp mô hình nắm bắt cấu trúc ngôn ngữ, cú pháp, và ngữ nghĩa một cách tự nhiên và hiệu quả.
    
- **Transfer Learning và Fine-tuning:**  
    Sau quá trình tiền huấn luyện, mô hình đã nắm được những kiến thức nền tảng về ngôn ngữ có thể được điều chỉnh (fine-tune) cho các tác vụ cụ thể như phân loại văn bản, dịch máy, tóm tắt, trích xuất thông tin,... Điều này giúp tiết kiệm thời gian và công sức so với việc huấn luyện mô hình từ đầu.
    

Tóm lại, self-supervised learning là nền tảng quan trọng giúp LLM khai thác hiệu quả dữ liệu không gán nhãn, xây dựng các biểu diễn ngôn ngữ mạnh mẽ và chuyển giao kiến thức này cho các ứng dụng xử lý ngôn ngữ tự nhiên khác nhau.

## Sự phát triển của các Core Techniques (NLP)

### 1. Mô hình N-gram

**Cơ chế & Đặc điểm:**

- **Nguyên lý hoạt động:** Mô hình n-gram dựa trên giả định rằng từ hiện tại chỉ phụ thuộc vào một số từ liền trước (n-1 từ). Ví dụ, mô hình bigram (n=2) chỉ tính xác suất của một từ dựa trên từ liền trước đó.
- **Đặc điểm:**
    - Dễ triển khai và tính toán.
    - Yêu cầu thống kê tần suất từ tập dữ liệu huấn luyện để ước lượng xác suất.

**Ưu điểm:**

- **Đơn giản:** Thực hiện dễ dàng và hiệu quả với dữ liệu có kích thước nhỏ.
- **Giải thích trực quan:** Có thể dễ dàng hiểu và diễn giải thông qua thống kê tần suất.

**Nhược điểm:**

- **Sự phụ thuộc ngữ cảnh hạn chế:** Không thể nắm bắt được mối quan hệ dài hạn giữa các từ nếu n không đủ lớn.
- **Vấn đề “data sparsity”:** Khi n tăng lên, số lượng kết hợp có thể tăng rất lớn, dẫn đến nhiều trường hợp chưa xuất hiện trong tập huấn luyện.
- **Không linh hoạt:** Không thể tự động học được các mối quan hệ phức tạp và ẩn giấu giữa các từ.

**Vấn đề giải quyết so với mô hình trước:**

- So với các mô hình thống kê đơn giản hơn, n-gram đã cố gắng tận dụng thông tin ngữ cảnh gần để cải thiện độ chính xác trong việc dự đoán từ tiếp theo, mặc dù vẫn còn hạn chế về khả năng nắm bắt ngữ cảnh xa.

---

### 2. Recurrent Neural Networks (RNN)

**Cơ chế & Đặc điểm:**

- **Nguyên lý hoạt động:** RNN xử lý dữ liệu tuần tự bằng cách duy trì một trạng thái ẩn (hidden state) được cập nhật liên tục qua từng bước thời gian, cho phép thông tin từ các bước trước được truyền qua các bước sau.
- **Đặc điểm:**
    - Thích hợp cho các dữ liệu tuần tự như văn bản, chuỗi thời gian.
    - Có khả năng mô hình hóa phụ thuộc thời gian.

**Ưu điểm:**

- **Xử lý chuỗi liên tục:** Có khả năng nhớ thông tin từ các bước trước, giúp nắm bắt mối liên hệ giữa các phần của câu.
- **Tính linh hoạt:** Dễ dàng áp dụng vào nhiều bài toán liên quan đến dữ liệu tuần tự (dịch máy, tổng hợp ngôn ngữ,…).

**Nhược điểm:**

- **Vấn đề gradient biến mất (vanishing gradient) và gradient bùng nổ (exploding gradient):** Khó khăn trong việc huấn luyện khi chuỗi dài.
- **Khó nắm bắt thông tin dài hạn:** Do hạn chế của cơ chế lan truyền thông tin qua nhiều bước.

**Vấn đề giải quyết so với n-gram:**

- RNN cho phép học được các mối quan hệ dài hạn trong chuỗi dữ liệu, vượt qua giới hạn ngữ cảnh cố định của mô hình n-gram, giúp mô hình hóa được mối liên hệ phức tạp hơn giữa các từ trong câu.

---

### 3. Long Short-Term Memory (LSTM)

**Cơ chế & Đặc điểm:**

- **Nguyên lý hoạt động:** LSTM là một biến thể của RNN, được thiết kế đặc biệt để giải quyết vấn đề gradient biến mất thông qua các cơ chế “cổng” (gates) – gồm cổng đầu vào, cổng quên, và cổng đầu ra – giúp kiểm soát thông tin lưu giữ và loại bỏ thông tin không cần thiết.
- **Đặc điểm:**
    - Có khả năng nhớ thông tin dài hạn tốt hơn RNN truyền thống.
    - Cấu trúc phức tạp hơn so với RNN cơ bản.

**Ưu điểm:**

- **Khắc phục vấn đề gradient:** Cơ chế cổng giúp duy trì thông tin qua chuỗi dài, giảm thiểu hiện tượng gradient biến mất.
- **Hiệu quả trên chuỗi dài:** Nắm bắt được các mối quan hệ phức tạp và dài hạn trong văn bản.

**Nhược điểm:**

- **Đòi hỏi tính toán cao:** Cấu trúc phức tạp dẫn đến chi phí tính toán lớn hơn so với RNN cơ bản.
- **Cấu trúc phức tạp:** Khó tối ưu hóa và tinh chỉnh mô hình hơn, đòi hỏi kinh nghiệm trong quá trình huấn luyện.

**Vấn đề giải quyết so với RNN:**

- LSTM giải quyết được vấn đề “vanishing gradient” của RNN truyền thống, cho phép mô hình học và ghi nhớ các mối quan hệ dài hạn hiệu quả hơn, đặc biệt là trong các bài toán ngôn ngữ và chuỗi dài.

---

### 4. Transformer

**Cơ chế & Đặc điểm:**

- **Nguyên lý hoạt động:** Kiến trúc Transformer dựa trên cơ chế attention (chú ý) thay vì xử lý tuần tự. Nó xử lý tất cả các phần tử của chuỗi song song và sử dụng attention để định lượng mức độ liên quan giữa các từ trong câu.
- **Đặc điểm:**
    - Không phụ thuộc vào thứ tự tuần tự, cho phép xử lý song song.
    - Tích hợp cơ chế self-attention giúp mô hình nắm bắt mối liên hệ phức tạp giữa các từ một cách hiệu quả.
    - Cấu trúc linh hoạt và mở rộng được cho các mô hình lớn (như GPT, BERT,…).

**Ưu điểm:**

- **Xử lý song song:** Giảm đáng kể thời gian huấn luyện so với các mô hình tuần tự (RNN/LSTM).
- **Hiệu quả trên dữ liệu lớn:** Khả năng xử lý các mối quan hệ phức tạp trong dữ liệu văn bản, thậm chí với các chuỗi rất dài.
- **Khả năng mở rộng:** Dễ dàng mở rộng thành các mô hình có quy mô lớn (large-scale models).

**Nhược điểm:**

- **Yêu cầu tài nguyên cao:** Các mô hình Transformer thường có số lượng tham số rất lớn, đòi hỏi phần cứng mạnh để huấn luyện và triển khai.
- **Phức tạp trong thiết kế:** Cần nhiều kỹ thuật tinh chỉnh và kiến trúc phức tạp để tối ưu hiệu suất.

**Vấn đề giải quyết so với LSTM/RNN:**

- Transformer khắc phục giới hạn của xử lý tuần tự bằng cách cho phép tính toán song song, cải thiện hiệu quả xử lý các mối liên hệ phức tạp trong dữ liệu và giảm thiểu thời gian huấn luyện. Điều này đã mở đường cho việc xây dựng các mô hình ngôn ngữ quy mô lớn và đạt hiệu suất cao trong nhiều tác vụ NLP.

## Các giai đoạn phát triển model LLMs

![[images/Pasted image 20250224181116.png]]
### 1. Model Design

#### 1.1 Xác định mục tiêu và bài toán

- **Mục tiêu:** Hiểu rõ mô hình sẽ giải quyết loại bài toán nào (ví dụ: sinh văn bản, dịch máy, hỏi-đáp, tóm tắt, v.v.).
- **Công việc:**
    - Thảo luận với đội ngũ kỹ thuật và các bên liên quan để làm rõ mục đích sử dụng.
    - Xác định các chỉ số đo lường thành công (KPIs): độ chính xác, độ trôi chảy (fluency), tốc độ phản hồi,…

#### 1.2 Lựa chọn kiến trúc

- **Mục tiêu:** Chọn kiểu kiến trúc mạng phù hợp: Transformer (Encoder-Decoder, Decoder-only, …).
- **Công việc:**
    - Tham khảo các mô hình phổ biến (GPT, BERT, T5, LLaMA, …).
    - Xác định kích thước mô hình (số lớp, số tham số, kích thước embedding, …).
    - Xác định các kỹ thuật hỗ trợ (Positional Embedding, Rotary Embedding, Attention Masking,…).
- **Kết quả:**
    - Tài liệu thiết kế mô hình (model architecture blueprint).
    - Danh sách siêu tham số ban đầu (hyperparameter configuration).

#### 1.3 Kế hoạch tài nguyên và hạ tầng

- **Mục tiêu:** Bảo đảm có đủ GPU/TPU và hạ tầng cho việc huấn luyện và triển khai.
- **Công việc:**
    - Tính toán dung lượng bộ nhớ, số GPU cần dùng, thời gian huấn luyện dự kiến.
    - Lên kế hoạch tài chính, cân đối chi phí.
### 2. Dataset Engineering

#### 2.1 Thu thập dữ liệu

- **Mục tiêu:** Thu thập một lượng dữ liệu văn bản khổng lồ, đa dạng về ngôn ngữ, thể loại, miền kiến thức.
- **Công việc:**
    - Khai thác từ nhiều nguồn: web, sách, báo, tài liệu nội bộ, API,…
    - Xây dựng pipeline quét dữ liệu (web crawling) nếu cần.
    - Đảm bảo tuân thủ quy định pháp lý và quyền sở hữu nội dung.

#### 2.2 Làm sạch và chuẩn hóa

- **Mục tiêu:** Loại bỏ nội dung không mong muốn, dữ liệu trùng lặp, ký tự lỗi, v.v.
- **Công việc:**
    - Loại bỏ các đoạn text chứa nội dung độc hại, nhạy cảm nếu vi phạm chính sách.
    - Lọc trùng lặp, sắp xếp theo chuẩn mã hóa (UTF-8, NFC,…).
    - Tách câu, tokenization (nếu cần).

#### 2.3 Gắn nhãn và tổ chức dữ liệu (nếu cần)

- **Mục tiêu:** Chuẩn bị tập dữ liệu có cấu trúc (có nhãn hoặc không nhãn).
- **Công việc:**
    - Đối với bài toán có giám sát (supervised), gắn nhãn dữ liệu bằng công cụ hoặc thủ công.
    - Với bài toán tự giám sát, chỉ cần đảm bảo định dạng thống nhất (ví dụ: [BOS] token, [EOS] token,…).
- **Kết quả:**
    - Tập dữ liệu khổng lồ ở dạng raw text (hoặc tokenized).
    - Tập validation/test ban đầu (nếu có).
### 3. Pretraining

#### 3.1 Cấu hình huấn luyện

- **Mục tiêu:** Thiết lập codebase, framework (PyTorch, TensorFlow,…), và script huấn luyện.
- **Công việc:**
    - Định nghĩa hàm mất mát (cross-entropy, causal language modeling, masked LM, …).
    - Xác định batch size, learning rate, số epoch.
    - Triển khai mô hình song song (distributed training) nếu cần.

#### 3.2 Huấn luyện sơ bộ (Self-supervised Learning)

- **Mục tiêu:** Dạy mô hình “hiểu” ngôn ngữ từ dữ liệu lớn.
- **Công việc:**
    - Dựa vào nhiệm vụ dự đoán từ tiếp theo (Next Token Prediction) hoặc “điền vào chỗ trống” (Masked Language Modeling).
    - Giám sát loss, các chỉ số (perplexity), tốc độ huấn luyện, kiểm tra phân bổ GPU.
    - Lưu checkpoint định kỳ (mỗi N step).

#### 3.3 Xử lý sự cố và tối ưu

- **Mục tiêu:** Giải quyết các vấn đề có thể phát sinh trong quá trình huấn luyện.
- **Công việc:**
    - Nếu loss không giảm, kiểm tra lại siêu tham số, dữ liệu.
    - Điều chỉnh learning rate, batch size, áp dụng gradient clipping để tránh exploding gradient.
- **Kết quả:**
    - Mô hình tiền huấn luyện (pretrained model) – hay còn gọi là “mô hình nền tảng” (foundation model).
    - Checkpoint, log huấn luyện, biểu đồ theo dõi loss.
### 4. Preliminary Evaluation

#### 4.1 Đánh giá cơ bản

- **Mục tiêu:** Kiểm tra chất lượng mô hình tiền huấn luyện trước khi chuyển sang giai đoạn sau.
- **Công việc:**
    - Dùng một tập con validation (không quá lớn) để tính perplexity, hoặc thực hiện một số bài test đơn giản (ví dụ: cloze test, so sánh với baseline).
    - Ghi nhận các lỗi phổ biến (chẳng hạn lặp từ, “hallucination”, …).
- **Kết quả:**
    - Báo cáo đánh giá ban đầu: mô hình có đáp ứng được ngưỡng mong đợi không?
    - Quyết định có cần huấn luyện thêm hay điều chỉnh gì không.
### 5. Post-Training

#### 5.1 Tối ưu mô hình (nếu cần)

- **Mục tiêu:** Giảm kích thước hoặc tăng tốc độ suy luận.
- **Công việc:**
    - Thực hiện các kỹ thuật như pruning (cắt bớt trọng số ít ảnh hưởng), quantization (nén 8-bit, 4-bit,…), knowledge distillation (chuyển tri thức sang mô hình nhỏ hơn).
    - Kết hợp checkpoint, chuyển từ float32 sang float16/bfloat16 để tiết kiệm bộ nhớ.

#### 5.2 Đánh giá lại

- **Mục tiêu:** Đảm bảo rằng tối ưu mô hình không làm giảm chất lượng quá nhiều.
- **Công việc:**
    - Đo lường lại perplexity, tốc độ suy luận, độ trễ.
    - So sánh mô hình gốc với mô hình đã tối ưu.
### 6. Fine-Tuning

#### 6.1 Chuẩn bị dữ liệu đặc thù

- **Mục tiêu:** Tinh chỉnh mô hình cho một hoặc nhiều tác vụ cụ thể.
- **Công việc:**
    - Thu thập/gắn nhãn dữ liệu chuyên biệt (QA, tóm tắt, phân loại cảm xúc,…).
    - Kiểm tra chất lượng dữ liệu, loại bỏ nhãn sai, format dữ liệu thống nhất.

#### 6.2 Tinh chỉnh mô hình

- **Mục tiêu:** Huấn luyện mô hình đã pretrain để đạt hiệu suất cao nhất trên tác vụ.
- **Công việc:**
    - Thiết lập pipeline huấn luyện ngắn hơn, batch size nhỏ hơn, learning rate thấp hơn.
    - Có thể dùng các kỹ thuật như LoRA, Prompt-tuning, Adapter,… để tiết kiệm tài nguyên.
    - Giám sát metric chuyên biệt (accuracy, F1, ROUGE, BLEU, v.v.).

#### 6.3 Kiểm tra overfitting

- **Mục tiêu:** Đảm bảo mô hình không “nhớ” máy móc mà mất khả năng tổng quát.
- **Công việc:**
    - Dùng tập validation khác miền, hoặc cross-validation.
    - Theo dõi gap giữa train/val loss.
- **Kết quả:**
    - Mô hình chuyên biệt (fine-tuned model) cho tác vụ.
### 7. Final Testing & Evaluation

#### 7.1 Kiểm thử toàn diện

- **Mục tiêu:** Xác nhận chất lượng cuối cùng của mô hình trước khi đưa vào sản xuất.
- **Công việc:**
    - Dùng tập test (hoặc bộ benchmark) mà mô hình chưa thấy trước đó.
    - Đánh giá trên nhiều chỉ số:
        - **Hiệu suất:** (accuracy, F1, BLEU, ROUGE, MRR, v.v.)
        - **Tốc độ suy luận:** (throughput, latency)
        - **Tài nguyên sử dụng:** (RAM, VRAM, CPU/GPU usage)
    - Thực hiện A/B testing nếu cần (so sánh với mô hình cũ).

#### 7.2 Đánh giá tính ổn định, đạo đức và an toàn

- **Mục tiêu:** Kiểm tra xem mô hình có tạo ra nội dung sai lệch, phản cảm hoặc vi phạm chính sách không.
- **Công việc:**
    - Chạy mô hình với các prompt nhạy cảm, corner cases để kiểm tra mức độ an toàn.
    - Kiểm duyệt (nếu có) và thiết lập bộ lọc nội dung.

#### 7.3 Báo cáo và triển khai

- **Mục tiêu:** Kết luận mô hình đã sẵn sàng ra mắt.
- **Công việc:**
    - Viết báo cáo tổng kết về chất lượng, rủi ro, đề xuất cải tiến tương lai.
    - Đóng gói mô hình (model weights, tokenizer, code) lên hệ thống.
    - Triển khai mô hình dưới dạng dịch vụ (REST API, gRPC, container, …).

## LLMs Optimization

|**Approach**|**Key Idea**|**Weight Change?**|**Complexity**|**Model Behavior**|**Notes**|
|---|---|---|---|---|---|
|**Prompt Engineering**|Explain to the model how to behave (via prompts/instructions)|No|Easy|The model itself does **not** change; it **adapts** by following instructions|No extra data needed; only modifies the prompt.|
|**RAG**  <br>(Retrieval-Augmented Generation)|Expand context by attaching a library or database|No|Medium|The model does **not** change; it gains knowledge from an external source|Useful when you want up-to-date or domain-specific info without retraining.|
|**Fine-tuning**|Additional training on an already trained model (extra data)|Yes|Hard|The model **does** change; weights are updated|More expensive but yields specialized performance for specific tasks/domains.|

- **Prompt Engineering** focuses on carefully crafting the input so the model’s responses adapt to your instructions, but no internal parameters are changed.
- **RAG** augments the model’s knowledge by adding an external database or knowledge store, again without touching the model’s weights.
- **Fine-tuning** requires further training with domain-specific or task-specific data, changing the model’s weights and often leading to better specialized results, but at higher cost and complexity.