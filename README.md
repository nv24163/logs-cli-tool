# Log Filter CLI Tool

## Overview

This is a command-line tool that reads a log file (logs.txt), filters valid log entries, writes matching results to an output file, and prints a short summary.

Invalid lines are ignored automatically.

---

## Log Format

Each valid log line must follow this format:

timestamp | level | service | message

Example:

2026-02-05 08:11:20 | ERROR | db | DB timeout while fetching user profile

A line is valid if:

- It has exactly 4 fields separated by |
- The level (after converting to uppercase) is one of:
  - INFO
  - WARN
  - ERROR

Any other format or level (like DEBUG) is ignored.

---

## Requirements

- Python 3 installed
- logs.txt must be in the same folder as log_tool.py

---

## How to Run

Open a terminal in the project folder and run:

python log_tool.py [options]

---

## Command Line Options

--level  
Filter by log level (INFO, WARN, ERROR).  
Case-insensitive (error works as ERROR).

Example:
python log_tool.py --level ERROR

---

--service  
Filter by service name.

Example:
python log_tool.py --service auth

---

--out  
Specify output file name.  
Default: filtered_logs.txt

Example:
python log_tool.py --service auth --out auth_logs.txt

---

## Filtering Rules

- Invalid lines are always ignored.
- If --level is provided, only logs with that level are kept.
- If --service is provided, only logs with that service are kept.
- If both are provided, logs must match BOTH conditions.
- Output always writes level in uppercase.

---

## Output File Format

timestamp | LEVEL | service | message

Example:

2026-02-05 08:11:20 | ERROR | db | DB timeout while fetching user profile

If no lines match, an empty file is created.

---

## Terminal Summary

After running, the program prints exactly:

Valid lines scanned: X  
Lines written: Y  
Output file: filename

Where:
- X = number of valid log lines found
- Y = number of lines written after filtering
- filename = output file name

---

## Example Commands

python log_tool.py --level ERROR

python log_tool.py --service auth --out auth_logs.txt

python log_tool.py --level WARN --service api --out warn_api.txt

---

## Project Files

log_tool.py – main program  
logs.txt – input file  
filtered_logs.txt – default output file  
run_proof.txt – proof of executed commands  

---

## Notes

- Invalid lines are ignored.
- DEBUG and unsupported levels are ignored.
- Output file is always created.
