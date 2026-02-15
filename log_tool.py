"""
PL202 — Day 2 (45 min) — Log Filter CLI Tool (Individual)

You will create a command-line tool that:
- Reads logs.txt
- Ignores invalid lines
- Filters by --level and/or --service (optional)
- Writes matching valid lines to an output file (--out, default: filtered_logs.txt)
- Prints a short summary

Log format (valid line):
  timestamp | level | service | message

Valid rules:
  - exactly 4 fields after splitting by '|'
  - level (after uppercasing) is one of: INFO, WARN, ERROR

Examples:
  python log_tool.py --level ERROR
  python log_tool.py --service auth --out auth_logs.txt
  python log_tool.py --level WARN --service api --out warn_api.txt
"""

import argparse
from pathlib import Path

LOG_FILE = Path("logs.txt")
DEFAULT_OUT = "filtered_logs.txt"
ALLOWED_LEVELS = {"INFO", "WARN", "ERROR"}


def parse_line(line: str):
    """
    Parse a log line.
    Returns (timestamp, level, service, message) OR None if invalid format.

    NOTE:
    - Empty lines are invalid.
    - Split by '|', trim whitespace around each part.
    - Must have exactly 4 parts.
    """
    # TODO 1: strip the line and treat empty as invalid (return None)
    line = line.strip()
    if not line:
        return None

    # TODO 2: split by '|' and strip whitespace around each part
    parts = [part.strip() for part in line.split("|")]

    # TODO 3: if number of parts != 4, return None
    if len(parts) != 4:
        return None

    # TODO 4: return (timestamp, level, service, message)
    timestamp, level, service, message = parts
    return timestamp, level, service, message


def is_valid_level(level: str) -> bool:
    """Return True if level is one of INFO/WARN/ERROR."""
    # TODO 5: uppercase the level then check ALLOWED_LEVELS
    return level.upper() in ALLOWED_LEVELS


def matches_filters(level: str, service: str, level_filter, service_filter) -> bool:
    """Return True if the line matches the provided filters."""
    # TODO 6: implement the matching logic
    if level_filter is not None and level != level_filter:
        return False

    if service_filter is not None and service != service_filter:
        return False

    return True


def build_arg_parser() -> argparse.ArgumentParser:
    """Create and return the argparse parser."""
    parser = argparse.ArgumentParser(description="Filter cloud logs by level and/or service.")

    # TODO 7: Add optional argument --level (accept INFO/WARN/ERROR; allow case-insensitive input)
    parser.add_argument("--level", type=str, help="Filter by level (INFO, WARN, ERROR)")

    # TODO 8: Add optional argument --service (string)
    parser.add_argument("--service", type=str, help="Filter by service name")

    # TODO 9: Add optional argument --out (string, default=DEFAULT_OUT)
    parser.add_argument("--out", type=str, default=DEFAULT_OUT, help="Output file name")

    return parser


def main():
    parser = build_arg_parser()
    args = parser.parse_args()

    # Normalize filters (so --level error works)
    level_filter = args.level.upper() if getattr(args, "level", None) else None
    service_filter = args.service if getattr(args, "service", None) else None
    out_path = Path(args.out)

    if not LOG_FILE.exists():
        print(f"ERROR: Cannot find {LOG_FILE}. Put logs.txt in the same folder as this file.")
        return

    total_valid_scanned = 0
    lines_written = 0
    output_lines = []

    # TODO 10: Read LOG_FILE line by line
    with LOG_FILE.open("r", encoding="utf-8") as f:
        for line in f:
            parsed = parse_line(line)
            if parsed is None:
                continue

            timestamp, level, service, message = parsed

            # normalize level to uppercase
            level = level.upper()

            if level not in ALLOWED_LEVELS:
                continue

            # now it's a valid line:
            total_valid_scanned += 1

            if matches_filters(level, service, level_filter, service_filter):
                output_lines.append(f"{timestamp} | {level} | {service} | {message}")
                lines_written += 1

    # TODO 11: Write output_lines to out_path (one per line). If no matches, create empty file.
    with out_path.open("w", encoding="utf-8") as f:
        for line in output_lines:
            f.write(line + "\n")

    # TODO 12: Print EXACTLY these 3 lines (numbers will vary):
    # Valid lines scanned: X
    # Lines written: Y
    # Output file: filename
    print(f"Valid lines scanned: {total_valid_scanned}")
    print(f"Lines written: {lines_written}")
    print(f"Output file: {out_path.name}")


if __name__ == "__main__":
    main()
