#!/usr/bin/env python

"""
Log analyzer
Parse a log file and outputs:
- total request
- Error count (status >= 400)
- Error rate
- Top 5 IPs
- Average latency per endpoint

POST /login 401 15 10.0.0.3
"""

from __future__ import annotations
import argparse
from typing import Iterable, Optional
from collections import defaultdict, Counter
from dataclasses import dataclass

@dataclass(frozen=True)
class LogRecord:
    path: str
    status: int
    latency_ms: float
    ip: str


def iter_record(log_file: str) -> Iterable[LogRecord]:
    with open(log_file, "r", encoding="utf-8") as f:
        for line in f:
            rec = parse_line(line)
            if rec is not None:
                yield rec


def parse_line(line: str) -> Optional[LogRecord]:
    """return LogRecord if parsing succeeds; otherwise, None"""

    line = line.strip()
    if not line or line.startswith("#"):
        return None
    
    parts = line.split()
    if len(parts) != 5:
        return None

    _method, path, status_s, latency_s, ip = parts

    try:
        status = int(status_s)
        latency_ms = float(latency_s)
    except ValueError:
        return None

    return LogRecord(path=path, status=status, latency_ms=latency_ms, ip=ip)


def analyze(records: Iterable[LogRecord]) ->dict:
    total = 0
    error_count = 0

    ip_count = Counter()
    latency_count = defaultdict(int)
    latency_sum = defaultdict(float)

    for r in records:
        total += 1
        ip_count[r.ip] += 1

        if r.status >= 400:
            error_count += 1

        latency_count[r.path] += 1
        latency_sum[r.path] += r.latency_ms

    error_rate = (error_count / total) if total > 0 else 0.0

    avg_latency_per_path = {
        path : (latency_sum[path] / latency_count[path])
        for path in latency_sum
        if latency_count[path] > 0
    }

    avg_latency_sorted = sorted(avg_latency_per_path.items(), key=lambda x: x[1], reverse=True)

    return {
        "total_request": total,
        "error_count": error_count,
        "error_rate": error_rate,
        "top_5_IPs": ip_count.most_common(5),
        "avg_latency_sorted": avg_latency_sorted
    }


def main() -> int:
    parser = argparse.ArgumentParser(description="Analyze a log file")
    parser.add_argument("logfile", help="path to a log file")

    args = parser.parse_args()

    results = analyze(iter_record(args.logfile))

    total_request = results["total_request"]
    error_count = results["error_count"]
    error_rate = results["error_rate"]
    top_5_IPs = results["top_5_IPs"]
    avg_latency_sorted = results["avg_latency_sorted"]

    print(f"Total request: {total_request}")
    print(f"Error count: {error_count}")
    print(f"Error rate: {error_rate:.2%}")

    print("\nTop 5 IPs:")
    for ip, count in top_5_IPs:
        print(f"{ip}: {count}")

    print("\nAverage latency per endpoint:")
    for path, avg_ms in avg_latency_sorted:
        print(f"{path}: {avg_ms:.2f} ms")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())