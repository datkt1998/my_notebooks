# Pull vs Push API

## 1. Định nghĩa và Cơ Chế Hoạt Động

### Pull API

- **Cơ chế:**  
    Client chủ động gửi yêu cầu (request) tới server theo chu kỳ (polling) để lấy dữ liệu mới.
- **Ưu điểm:**
    - Kiểm soát được tần suất truy vấn của client.
    - Dễ triển khai khi không yêu cầu kết nối mở liên tục.
- **Nhược điểm:**
    - Tăng lưu lượng mạng và độ trễ (latency) giữa thời điểm dữ liệu có sẵn và thời điểm client nhận được dữ liệu.
    - Không hiệu quả nếu dữ liệu cập nhật liên tục hoặc theo thời gian thực.

### Push API

- **Cơ chế:**  
    Server chủ động gửi (push) dữ liệu tới client ngay khi có thông tin mới, thông qua các kênh như webhook, kết nối mở (long-lived connection), hoặc giao thức messaging.
- **Ưu điểm:**
    - Giảm độ trễ: thông tin được đẩy ngay khi có sự kiện mới.
    - Tiết kiệm băng thông khi không cần polling định kỳ.
- **Nhược điểm:**
    - Đòi hỏi client phải có endpoint khả dụng để nhận dữ liệu.
    - Cần xử lý các vấn đề về bảo mật (ví dụ: xác thực webhook) và đảm bảo khả năng chịu lỗi (retry khi không thành công).

---

## 2. Yêu Cầu Về Thiết Kế và Tổ Chức Cho Client và Server

### Pull API

#### Server:

- **Endpoint ổn định:** Cung cấp API RESTful cho phép client gọi GET (hoặc các phương thức phù hợp) để lấy dữ liệu mới.
- **Quản lý trạng thái:** Nếu cần, cung cấp các tham số để hỗ trợ phân trang hoặc chỉ lấy dữ liệu sau một mốc thời gian nhất định.
- **Tối ưu hóa hiệu suất:** Cache dữ liệu và phân phối tài nguyên để đáp ứng lượng request lớn từ client polling.

#### Client:

- **Polling logic:** Xây dựng cơ chế gửi yêu cầu định kỳ (ví dụ: mỗi 30 giây, 1 phút) và xử lý dữ liệu trả về.
- **Quản lý trạng thái cục bộ:** Lưu trữ timestamp hoặc marker của lần gọi trước để chỉ lấy dữ liệu mới kể từ lần truy vấn cuối cùng.
- **Xử lý lỗi:** Cần có cơ chế retry hoặc fallback khi gặp lỗi kết nối.

### Push API

#### Server:

- **Cấu hình hệ thống push:** Cần có cơ chế đẩy thông báo đến các client đã đăng ký (subscribers) khi có dữ liệu mới.
- **Retry và đảm bảo giao hàng:** Khi gửi dữ liệu (ví dụ, qua webhook), nếu client không phản hồi thành công, server phải có cơ chế retry.
- **Bảo mật và xác thực:** Xác thực các yêu cầu đẩy đến client (ví dụ, sử dụng token, chữ ký số) để đảm bảo chỉ gửi đến các endpoint hợp lệ.

#### Client:

- **Endpoint nhận dữ liệu:** Cung cấp một URL endpoint công khai (hoặc qua VPN, tùy theo cấu hình bảo mật) để server push dữ liệu đến.
- **Xác thực thông tin đẩy:** Xác nhận nguồn gốc của thông báo push (kiểm tra chữ ký, token) để tránh giả mạo.
- **Xử lý dữ liệu bất đồng bộ:** Sử dụng các cơ chế như queue nội bộ hoặc xử lý đa luồng để xử lý thông tin đến theo thời gian thực.

---

## 3. Ví Dụ Áp Dụng – Hệ Thống Cung Cấp Tin Tức

Giả sử có một hệ thống trong đó:

- **Provider:** Cung cấp tin tức mới.
- **Subscriber:** Nhận tin tức mới.

### Mô hình Pull:

- **Server (Provider):**
    - Cung cấp endpoint API ví dụ: `GET /api/news?since=timestamp` trả về danh sách bài báo mới kể từ thời điểm `timestamp`.
    - Quản lý cơ sở dữ liệu tin tức, đánh dấu thời gian cập nhật của mỗi bài.
- **Client (Subscriber):**
    - Thực hiện polling định kỳ (ví dụ: mỗi 1 phút) tới endpoint trên.
    - Sau mỗi lần polling, lưu lại timestamp của lần truy vấn cuối để chỉ nhận tin tức mới trong lần gọi kế tiếp.
- **Ưu điểm trong Pull:**
    - Client chủ động kiểm soát thời gian truy vấn.
- **Nhược điểm trong Pull:**
    - Có thể không nhận được tin tức ngay lập tức nếu có sự kiện xảy ra giữa các lần polling.

### Mô hình Push:

- **Server (Provider):**
    - Khi có tin tức mới, ngay lập tức gửi thông báo tới các endpoint đăng ký của client qua HTTP POST (webhook) hoặc qua một kênh messaging.
    - Quản lý danh sách các subscriber và đảm bảo thông báo được gửi thành công (retry nếu cần).
- **Client (Subscriber):**
    - Cung cấp một endpoint (ví dụ: `POST /webhook/news`) để nhận thông báo.
    - Xác thực thông báo đến (kiểm tra header, token, chữ ký số).
    - Xử lý thông báo nhận được và cập nhật giao diện người dùng hoặc lưu vào cơ sở dữ liệu.
- **Ưu điểm trong Push:**
    - Nhận tin tức theo thời gian thực, giảm độ trễ.
- **Nhược điểm trong Push:**
    - Yêu cầu client phải có khả năng nhận và xử lý các kết nối đến từ server.

---

## 4. Phân Loại Theo Môi Trường: Cloud (GCP PubSub) vs. On-Premise

### Môi trường Cloud – GCP PubSub

- **GCP PubSub:**
    - **Kiến trúc:**
        - **Publisher (Provider):** Gửi tin nhắn (message) vào một topic khi có tin mới.
        - **Subscriber (Client):** Có thể đăng ký nhận tin thông qua hai chế độ:
            - **Pull Subscription:** Client tự chủ động lấy tin nhắn từ subscription.
            - **Push Subscription:** GCP sẽ gửi tin nhắn tới endpoint đã đăng ký của client.
    - **Yêu cầu:**
        - **Bảo mật:** Xác thực bằng IAM, sử dụng token và SSL/TLS.
        - **Quản lý và Scale:** Tích hợp sẵn các tính năng tự động scale và retry.
        - **Dữ liệu đảm bảo:** Đảm bảo thông điệp được giao đúng (at-least-once delivery) và có thể cấu hình thêm dead-letter queue.
    - **Ưu điểm:**
        - Giảm tải quản lý hạ tầng, tích hợp với các dịch vụ khác của GCP.
        - Hỗ trợ cả mô hình pull và push theo nhu cầu của ứng dụng.

### Môi trường On-Premise

- **Giải pháp hosted on-premise:**
    - **Công cụ:** Có thể sử dụng các giải pháp như RabbitMQ, Apache Kafka, ActiveMQ,...
    - **Push API on-premise:**
        - Server có thể tích hợp mô hình push qua webhook hoặc sử dụng hệ thống messaging nội bộ để gửi dữ liệu ngay khi có tin.
        - Yêu cầu client cung cấp endpoint nội bộ có thể nhận dữ liệu, đảm bảo an toàn qua firewall và xác thực nội bộ.
    - **Pull API on-premise:**
        - Cung cấp REST API trên server để client polling dữ liệu mới từ cơ sở dữ liệu hoặc từ message queue.
        - Quản lý tài nguyên và tối ưu hiệu năng cho các request polling thường xuyên.
    - **Yêu cầu:**
        - Quản lý mạng nội bộ và bảo mật khi mở endpoint cho các kết nối từ bên ngoài (nếu cần).
        - Đảm bảo cơ sở hạ tầng đủ mạnh để xử lý số lượng request lớn (đối với pull) hoặc số lượng thông báo liên tục (đối với push).

---

## 5. Các Vấn Đề Liên Quan Cần Cân Nhắc

- **Bảo mật và xác thực:**
    
    - Với push API, việc bảo mật endpoint nhận thông báo là vô cùng quan trọng (xác thực nguồn, mã hóa, SSL/TLS).
    - Với pull API, việc bảo mật API endpoint và giới hạn tốc độ (rate limiting) là cần thiết để ngăn chặn tấn công DoS.
- **Độ trễ và hiệu năng:**
    
    - Pull API có thể dẫn đến độ trễ do khoảng thời gian giữa các lần polling, trong khi Push API cung cấp cập nhật gần như thời gian thực.
- **Khả năng mở rộng:**
    
    - Trong môi trường cloud như GCP, khả năng mở rộng tự động và quản lý tải được tích hợp sẵn.
    - Trong on-premise, cần xây dựng kiến trúc có khả năng scale theo yêu cầu (sử dụng load balancer, clustering, …).
- **Độ tin cậy:**
    
    - Cần có cơ chế retry và xử lý lỗi cho cả hai mô hình. Đối với push, việc retry khi không nhận được phản hồi từ client là quan trọng.
- **Quản lý trạng thái:**
    
    - Trong pull API, việc quản lý trạng thái (lưu mốc thời gian của lần polling cuối) là cần thiết để không bỏ sót dữ liệu.
    - Trong push API, cần đảm bảo rằng các thông điệp được gửi lại khi có lỗi giao hàng.

---

## 6. Kết Luận

- **Pull API** phù hợp khi client cần kiểm soát tần suất truy vấn và không yêu cầu cập nhật ngay lập tức. Nó dễ triển khai nhưng có thể gây lãng phí tài nguyên do polling liên tục.
- **Push API** lại thích hợp cho các ứng dụng yêu cầu cập nhật thời gian thực và giảm tải cho client. Tuy nhiên, nó đòi hỏi thiết kế bảo mật và khả năng xử lý lỗi mạnh mẽ từ phía server và client.
- **Trong môi trường cloud (GCP PubSub):**
    - Hệ thống đã tích hợp sẵn các cơ chế push và pull, cho phép linh hoạt cấu hình theo nhu cầu và được quản lý tự động về mặt scale, bảo mật và retry.
- **Trong môi trường on-premise:**
    - Việc lựa chọn giải pháp phù hợp (RabbitMQ, Kafka, …) phụ thuộc vào yêu cầu về hiệu năng, bảo mật và khả năng mở rộng của hệ thống, đồng thời cần tự triển khai các cơ chế xử lý lỗi, retry và bảo mật.