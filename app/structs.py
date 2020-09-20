from dataclasses import dataclass
from typing import List


@dataclass
class ColunaXLSXConfig:
    coluna: str
    linhas: List[int]
