#!/usr/bin/env python3
"""
JSON Transformer

Reads a JSON file of users and outputs only active users,
sorted by last_login (most recent first).

Expected input format:
[
  {
    "id": int,
    "name": str,
    "email": str,
    "active": bool,
    "last_login": ISO8601 datetime string
  }
]
"""

from __future__ import annotations

import argparse
import json
import sys
from dataclasses import dataclass
from datetime import datetime
from pathlib import Path
from typing import List


# ==========================
# Data Model
# ==========================

@dataclass(frozen=True)
class User:
    id: int
    name: str
    email: str
    active: bool
    last_login: datetime


# ==========================
# Core Logic
# ==========================

def parse_user(raw: dict) -> User:
    """
    Validate and convert raw dict into User object.
    Raises ValueError if invalid.
    """
    try:
        return User(
            id=int(raw["id"]),
            name=str(raw["name"]),
            email=str(raw["email"]),
            active=bool(raw["active"]),
            last_login=datetime.fromisoformat(raw["last_login"]),
        )
    except KeyError as e:
        raise ValueError(f"Missing required field: {e}") from e
    except Exception as e:
        raise ValueError(f"Invalid user data: {raw}") from e


def load_users(file_path: Path) -> List[User]:
    """
    Load and validate users from JSON file.
    """
    if not file_path.exists():
        raise FileNotFoundError(f"File not found: {file_path}")

    try:
        with file_path.open("r", encoding="utf-8") as f:
            data = json.load(f)
    except json.JSONDecodeError as e:
        raise ValueError("Invalid JSON file") from e

    if not isinstance(data, list):
        raise ValueError("JSON root must be a list of users")

    users: List[User] = []
    for raw_user in data:
        users.append(parse_user(raw_user))

    return users


def transform_users(users: List[User]) -> List[User]:
    """
    Filter active users and sort by last_login descending.
    """
    active_users = [u for u in users if u.active]

    return sorted(
        active_users,
        key=lambda u: u.last_login,
        reverse=True,
    )


def serialize_users(users: List[User]) -> List[dict]:
    """
    Convert User objects back to JSON-serializable dicts.
    """
    return [
        {
            "id": u.id,
            "name": u.name,
            "email": u.email,
            "active": u.active,
            "last_login": u.last_login.isoformat(),
        }
        for u in users
    ]


# ==========================
# CLI
# ==========================

def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Filter active users sorted by last login."
    )
    parser.add_argument(
        "input_file",
        type=Path,
        help="Path to users JSON file",
    )
    parser.add_argument(
        "-o",
        "--output",
        type=Path,
        help="Optional output file (default: stdout)",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()

    try:
        users = load_users(args.input_file)
        transformed = transform_users(users)
        output_data = serialize_users(transformed)

        if args.output:
            with args.output.open("w", encoding="utf-8") as f:
                json.dump(output_data, f, indent=2)
        else:
            json.dump(output_data, sys.stdout, indent=2)
            print()

        return 0

    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    sys.exit(main())