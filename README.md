# Đồ án Tiền xử lý dữ liệu

- **Sinh viên:** Tạ Văn Đức
- **MSSV:** 23127528
- **Môn học:** Khai phá dữ liệu và ứng dụng, HCMUS
- **Đề bài:** https://hcmus-cs-ta.github.io/lab-book/data-mining/projects/preprocessing/
- **Book đã xuất bản:** https://tavanduc2005.github.io/dm-preprocessing/

## Tập dữ liệu

| Phần | Dạng dữ liệu | Tập dữ liệu | Quy mô | Nguồn |
|---|---|---|---|---|
| (a) | Bảng | Adult Census Income | 32.561 dòng, 14 thuộc tính + 1 nhãn | [Hugging Face](https://huggingface.co/datasets/scikit-learn/adult-census-income) (gốc: [UCI](https://archive.ics.uci.edu/dataset/2/adult)) |
| (b) | Văn bản | IMDB Movie Reviews | 50.000 review, 2 nhãn | [Hugging Face](https://huggingface.co/datasets/stanfordnlp/imdb) (gốc: [Stanford](https://ai.stanford.edu/~amaas/data/sentiment/)) |

**Adult Census Income:** dữ liệu điều tra dân số Mỹ năm 1994. Gồm 6 thuộc tính số (`age`, `fnlwgt`, `education.num`, `capital.gain`, `capital.loss`, `hours.per.week`) và 8 thuộc tính phân loại (`workclass`, `education`, `marital.status`, `occupation`, `relationship`, `race`, `sex`, `native.country`). Nhãn `income` cho biết thu nhập `>50K` hay `<=50K` (mất cân bằng khoảng 76/24). Giá trị thiếu ký hiệu `?` ở `workclass`, `occupation` và `native.country`.

**IMDB:** review phim tiếng Anh, nhãn cảm xúc `0 = negative`, `1 = positive`, cân bằng 25.000/25.000. Giữ nguyên cách chia gốc 25K train và 25K test.

Dữ liệu thô không được push vào repo. Lần chạy đầu tiên, các notebook gọi [book/utils/data_loader.py](book/utils/data_loader.py) để tải dữ liệu từ Hugging Face về `data/raw/`; các lần sau đọc lại từ file cục bộ.

## Cài đặt môi trường

Yêu cầu Python 3.11.

```bash
python -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

## Chạy notebook và build book

```bash
jupyter lab                      # mở và chạy các notebook trong book/
jupyter book start               # xem thử book trên máy
jupyter book build --html        # build ra thư mục _build/html
```

Book hiển thị output đã lưu sẵn trong notebook. Vì vậy cần chạy lại toàn bộ notebook (Restart & Run All) trước khi commit. Mỗi lần push lên nhánh `main`, GitHub Actions ([.github/workflows/deploy.yml](.github/workflows/deploy.yml)) sẽ build và xuất bản book lên GitHub Pages.

## Cấu trúc repo

```
book/
  index.md              trang giới thiệu
  00_data.ipynb         tải dữ liệu và kiểm tra điều kiện đề bài
  01_EDA_tabular.ipynb  EDA dữ liệu bảng: phân phối, tương quan, dữ liệu thiếu
  utils/                code dùng chung (cấu hình, tải dữ liệu)
data/
  raw/                  dữ liệu gốc (không push)
  processed/            dữ liệu sau tiền xử lý (không push)
myst.yml                cấu hình book và mục lục
requirements.txt        danh sách thư viện
```

## Tài nguyên ngoài

- Adult Census Income: https://archive.ics.uci.edu/dataset/2/adult
- IMDB: Maas et al. (2011), *Learning Word Vectors for Sentiment Analysis*, ACL. https://ai.stanford.edu/~amaas/data/sentiment/
- Jupyter Book 2 / MyST: https://mystmd.org/guide
