"""Cấu hình chung: đường dẫn thư mục và seed ngẫu nhiên.

Mọi notebook import từ đây để kết quả tái lập được và không phụ thuộc
vào thư mục làm việc hiện tại.
"""

import random
from pathlib import Path

import numpy as np

# Seed cố định cho toàn bộ đồ án
RANDOM_STATE = 42

# Thư mục gốc của repo (book/utils/config.py -> lên 2 cấp)
ROOT_DIR = Path(__file__).resolve().parents[2]
DATA_DIR = ROOT_DIR / "data"
RAW_DIR = DATA_DIR / "raw"
PROCESSED_DIR = DATA_DIR / "processed"

for _d in (RAW_DIR, PROCESSED_DIR):
    _d.mkdir(parents=True, exist_ok=True)


def set_seed(seed: int = RANDOM_STATE) -> None:
    """Đặt seed cho random và numpy."""
    random.seed(seed)
    np.random.seed(seed)
