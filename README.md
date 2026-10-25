# Đồ án Tiền xử lý dữ liệu

- **Sinh viên:** Tạ Văn Đức
- **MSSV:** 23127528
- **Môn học:** Khai phá dữ liệu và ứng dụng, HCMUS
- **Book đã xuất bản:** https://TEN-GITHUB.github.io/TEN-REPO/

## Tập dữ liệu

| Phần | Dạng dữ liệu | Tập dữ liệu | Nguồn |
|---|---|---|---|
| (a) | Bảng | Adult Census Income | TODO: điền link (UCI / Kaggle / Hugging Face) |
| (b) | Văn bản | IMDB Dataset of 50K Movie Reviews | TODO: điền link (Kaggle / Hugging Face) |

Dữ liệu thô không được push vào repo. Mã tải dữ liệu nằm trong các notebook của book.

## Cài đặt môi trường

```bash
python -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

## Build book

```bash
jupyter book start               # xem thử trên máy
jupyter book build --html        # build ra thư mục _build/html
```

## Cấu trúc repo

```
book/        nguồn của cuốn Jupyter Book (notebook và trang markdown)
data/        thư mục dữ liệu cục bộ, không push dữ liệu thô
myst.yml     cấu hình book
```

## Tài nguyên ngoài

- TODO: liệt kê link dữ liệu, tài liệu tham khảo
