# VulnHunt-GPT: Smart Contract Vulnerabilities Detector

Phân tích lỗ hổng bảo mật trong Smart Contracts thông qua Chatbot AI ứng dụng RAG (Retrieval-Augmented Generation).

---

## 🚀 Mục tiêu

Dự án sử dụng các mô hình ngôn ngữ lớn (LLM) kết hợp với cơ chế truy xuất tri thức (RAG) để:

- Hiểu và phân tích hợp đồng thông minh.
- Tìm kiếm và giải thích các lỗ hổng bảo mật.
- Giao tiếp với người dùng thông qua chatbot AI thân thiện.

Dự án được xây dựng dựa trên bài báo:  
**Biagio Boi, Christian Esposito, and Sokjoon Lee. 2024. VulnHunt-GPT: a Smart Contract vulnerabilities detector based on OpenAI chatGPT.**  
In _Proceedings of the 39th ACM/SIGAPP Symposium on Applied Computing (SAC '24)_. Association for Computing Machinery, New York, NY, USA, 1517–1524. [https://doi.org/10.1145/3605098.3636003](https://doi.org/10.1145/3605098.3636003)

---

## 🧠 Công nghệ sử dụng

- **Python**
- **LangChain**
- **OpenAI GPT-4o mini** (tùy chọn)
- **Qwen2-1.5B-Instruct** (qua Hugging Face)
- **FAISS Vector Database**
- **Hugging Face Transformers**
- **Google Generative AI**

---

## 🏗️ Cấu trúc thư mục

```
VULNHUNT-GPT-LLM-RAG/
├── data/                 # Chứa dữ liệu đầu vào hoặc smart contracts
├── solidity/             # Chứa dữ liệu của Smart Contracts
├── streamlit/            # Dùng streamlit để tạo GUI cho người dùng
├── .env                  # File chứa các biến môi trường (API Keys)
├── .gitignore
├── Create_dtb.ipynb      # Dùng để khởi tạo vector database Pinecone và up dữ liệu
├── module_preprocessing.py          # Tiền xử lý dữ liệu
├── preprocessing.py         # Tiền xử lý dữ liệu
├── query.py        # Truy vấn với RAG
└── README.md
```

---

## ⚙️ Cài đặt

### 1. Clone repo:

```bash
git clone https://github.com/2uaan1ee/vulnhunt-gpt-llm-rag.git
cd vulnhunt-gpt-llm-rag
```

### 2. Cài đặt môi trường:

```bash
pip install -r requirements.txt
```

### 3. Cấu hình API keys:

Tạo file `.env` với nội dung:

```
OPENAI_API_KEY=your_openai_api_key
PINECONE_API_KEY=your_pinecone_api_key
GEMINI_API_KEY=your_gemini_api_key
```

---

## 📦 Chuẩn bị dữ liệu

Mở file `Create_dtb.ipynb` trong Jupyter Notebook và chạy từng cell theo thứ tự.

Dữ liệu sẽ được xử lý và lưu dưới dạng vector trong thư mục trên Pinecone. Hãy truy cập vào website và đăng nhập để xem.

---

## 🧪 Chạy chương trình

### Với GPT-4o (qua OpenAI):

```bash
python qabot-gpt.py
```

---

## 📌 Ghi chú

- Dự án hỗ trợ cả mô hình cloud (OpenAI).
- Có hỗ trợ cả CLI và GUI.
- Dự án đầu tay về LLM và RAG nên còn nhiều thiếu sót.

---

## 📜 License

MIT License

---

## 🙌 Đóng góp

Mọi đóng góp, chỉnh sửa hoặc mở rộng dự án đều rất hoan nghênh! Bạn có thể mở issue hoặc tạo pull request.

---

## 📬 Liên hệ

Nếu bạn có thắc mắc, hãy liên hệ qua GitHub Issues hoặc email quan.minhle26f@gmal.com
