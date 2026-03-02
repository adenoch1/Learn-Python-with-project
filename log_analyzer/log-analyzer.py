#!/usr/bin/env python3
"""
Log Analyzer
Parses a log file and outputs:
- total requests
- error rate (status >= 400)
- top 5 IPs by request count
- average latency (ms) per endpoint (path)

Expected line format (whitespace-separated):
<method> <path> <status_code> <latency_ms> <ip>

Example:
GET /api/login 200 31 10.0.0.1
"""

from __future__ import annotations

import argparse
from collections import Counter, defaultdict
from dataclasses import dataclass
from typing import Iterable, Optional


@dataclass(frozen=True)
class LogRecord:
    path: str
    status: int
    latency_ms: float
    ip: str


def parse_line(line: str) -> Optional[LogRecord]:
    """
    Returns LogRecord if parsing succeeds; otherwise None.

    Strictly expects 5 tokens:
    method, path, status, latency_ms, ip
    """
    line = line.strip()
    if not line or line.startswith("#"):
        return None

    parts = line.split()
    if len(parts) != 6:
        return None

    _, _method, path, status_s, latency_s, ip = parts

    try:
        status = int(status_s)
        latency_ms = float(latency_s)
    except ValueError:
        return None

    return LogRecord(path=path, status=status, latency_ms=latency_ms, ip=ip)


def analyze(records: Iterable[LogRecord]) -> dict:
    total = 0
    error_count = 0

    ip_counts = Counter()
    latency_sum = defaultdict(float)   # path -> total latency
    latency_count = defaultdict(int)   # path -> number of requests

    for r in records:
        total += 1
        ip_counts[r.ip] += 1

        if r.status >= 400:
            error_count += 1

        latency_sum[r.path] += r.latency_ms
        latency_count[r.path] += 1

    error_rate = (error_count / total) if total else 0.0

    avg_latency_per_path = {
        path: (latency_sum[path] / latency_count[path])
        for path in latency_sum
        if latency_count[path] > 0
    }

    # Sort avg latency desc for nicer reporting
    avg_latency_sorted = sorted(avg_latency_per_path.items(), key=lambda x: x[1], reverse=True)

    return {
        "total_requests": total,
        "error_count": error_count,
        "error_rate": error_rate,
        "top_5_ips": ip_counts.most_common(5),
        "avg_latency_sorted": avg_latency_sorted,
    }


def iter_records(file_path: str) -> Iterable[LogRecord]:
    with open(file_path, "r", encoding="utf-8") as f:
        for line in f:
            rec = parse_line(line)
            if rec is not None:
                yield rec


def main() -> int:
    parser = argparse.ArgumentParser(description="Analyze HTTP logs.")
    parser.add_argument("logfile", help="Path to log file")
    args = parser.parse_args()

    results = analyze(iter_records(args.logfile))

    total = results["total_requests"]
    error_count = results["error_count"]
    error_rate = results["error_rate"]
    top_5_ips = results["top_5_ips"]
    avg_latency_sorted = results["avg_latency_sorted"]

    print(f"Total requests: {total}")
    print(f"Errors (status >= 400): {error_count}")
    print(f"Error rate: {error_rate:.2%}")

    print("\nTop 5 IPs:")
    for ip, count in top_5_ips:
        print(f"  {ip}: {count}")

    print("\nAverage latency per endpoint (ms) (high -> low):")
    for path, avg_ms in avg_latency_sorted:
        print(f"  {path}: {avg_ms:.2f} ms")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())