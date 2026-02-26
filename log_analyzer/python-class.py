# annotations

# from __future__ import annotations

# def add(a: int, b: int) -> int:
#     return a + b

# name: str = "Enoch"
# count: int = 5
# print: list[int] = [1, 3, 4, 6]

# Optional
from typing import Optional

def find_even(numbers: list[int]) -> Optional[int]:
    for n in numbers:
        if n % 2 == 0:
            return n
    return None


find_even()