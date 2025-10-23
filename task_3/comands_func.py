import sys
from collections import namedtuple
from pathlib import Path
from typing import List, Dict

Log_entry = namedtuple("Log_entry", ["date", "time", "level", "messages"])

def parse_log_line(line: str) -> Log_entry:
    log_date, log_time, level, *message = line.split()
    message = " ".join(str(v) for v in message)
    return Log_entry(date=log_date, time=log_time, level=level.upper(), messages=message)


def load_logs(file_path: Path) -> List[Log_entry]:
    with open(file_path, encoding="utf-8") as logs_file:
        return [parse_log_line(line.strip()) for line in logs_file]


def filter_logs_by_level(logs: List[Log_entry], level: str) -> List[Log_entry]:
    level = level.upper()
    return [log for log in logs if log.level == level]


def count_logs_by_level(logs: List[Log_entry]) -> Dict[str, int]:
    counts = {}
    for log in logs:
        counts[log.level] = counts.get(log.level, 0) + 1
    return counts


def display_log_counts(counts: Dict[str, int]) -> None:
    print(f"\nStatistics by logging levels")
    print(f"_" * 30)
    print(f"{'Logging level':>10} | {'Quantity':>10}")
    print(f"-" * 30)
    for level, count in counts.items():
        print(f'{level:<13} | {count:>7}')


def display_log_filtered(logs: List[Log_entry], level: str) -> None:
    filtered = filter_logs_by_level(logs, level)
    print(f"_" * 30)
    print(f"")
    print(f"\nLog details for {level} level:")
    print(f"")
    for log in filtered:
        print(f"{log.date} {log.time} {log.level} {log.messages}")