"""Tải dữ liệu thô từ Hugging Face và lưu cục bộ vào data/raw/.

Lần đầu gọi sẽ tải từ Hugging Face; các lần sau đọc trực tiếp từ file
parquet đã lưu nên không cần mạng.

Nguồn dữ liệu:
- Adult Census Income: https://huggingface.co/datasets/scikit-learn/adult-census-income
  (bản gốc: https://archive.ics.uci.edu/dataset/2/adult)
- IMDB 50K Movie Reviews: https://huggingface.co/datasets/stanfordnlp/imdb
  (bản gốc: https://ai.stanford.edu/~amaas/data/sentiment/)
"""

import pandas as pd

from .config import RAW_DIR

ADULT_HF_ID = "scikit-learn/adult-census-income"
IMDB_HF_ID = "stanfordnlp/imdb"

ADULT_PATH = RAW_DIR / "adult.parquet"
IMDB_PATH = RAW_DIR / "imdb.parquet"


def load_adult(force_download: bool = False) -> pd.DataFrame:
    """Trả về DataFrame Adult Census Income (32.561 dòng, 15 cột).

    Giá trị thiếu trong dữ liệu gốc được ký hiệu bằng chuỗi "?" và được
    giữ nguyên ở bước này; việc chuyển sang NaN thực hiện trong notebook EDA.
    """
    if ADULT_PATH.exists() and not force_download:
        return pd.read_parquet(ADULT_PATH)

    from datasets import load_dataset

    df = load_dataset(ADULT_HF_ID, split="train").to_pandas()
    df.to_parquet(ADULT_PATH, index=False)
    return df


def load_imdb(force_download: bool = False) -> pd.DataFrame:
    """Trả về DataFrame IMDB gồm 50.000 review có nhãn.

    Cột:
    - text: nội dung review
    - label: 0 = negative, 1 = positive
    - split: "train" hoặc "test" (giữ nguyên cách chia gốc 25K/25K,
      dùng để tính OOV rate trên tập test)
    """
    if IMDB_PATH.exists() and not force_download:
        return pd.read_parquet(IMDB_PATH)

    from datasets import load_dataset

    parts = []
    for split in ("train", "test"):
        part = load_dataset(IMDB_HF_ID, split=split).to_pandas()
        part["split"] = split
        parts.append(part)
    df = pd.concat(parts, ignore_index=True)
    df.to_parquet(IMDB_PATH, index=False)
    return df
