# annotations

from __future__ import annotations
from typing import Iterable

# def add(a: int, b: int) -> int:
#     return a + b

# name: str = "Enoch"
# count: int = 5
# prices: Iterable[float] = [0.4, 1.2, 3.5]

# Optional

from typing import Optional

# def find_even(numbers: Iterable[int]) -> Optional[int]:
#     for n in numbers:
#         if n % 2 == 0:
#             return n
#     return None

# print(find_even([1, 3, 5]))
# print(find_even([1, 4, 7]))


# dataclass

from dataclasses import dataclass

# class User:
#     def __init__(self, height, weight):
#         self.height = height
#         self.weight = weight

# @dataclass
# class User:
#     height: float
#     weight: float

# Mike = User(6.2, 90.5)
# print(Mike)
# print(Mike.height)

# Counter

from collections import Counter

# ips = ["1.1.1.1", "2.2.2.2", "1.1.1.1"]

# count = Counter(ips)
# print(count)
# print(count.most_common(2))

# defaultdict

# from collections import defaultdict

# scores = defaultdict(int)

# scores["math"] += 10
# scores["math"] += 5

# print(scores)

# argparse

# import argparse

# parser = argparse.ArgumentParser(description="Just learning Python")
# parser.add_argument("name", help="Name of a staff")
# parser.add_argument("--age", type=int, default=20)

# args = parser.parse_args()

# print("Hello", args.name, args.age)

# Parsing logic

# line = "GET /home 200 31, 10.0.0.1"
# parts = line.split()

# print(parts)

# method, path, status, latency, ip = parts

# print(method)

# print(path)