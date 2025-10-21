import sys


def parse_log_line(line: str) -> dict:
    try:
        log_date, log_time, level, *message = line.split()
        message = " ".join(str(v) for v in message)
        return {"date": log_date, "time": log_time, "level": level.upper(), "message": message}
    except Exception as e:
        return {"date": "", "time": "", "level": "UNKNOWN", "message": line.strip()}


def load_logs(file_path: str) -> list:
    logs = []
    try:
        with open(file_path, encoding="utf-8") as logs_file:
            for line in logs_file:
                line = line.strip()
                logs.append(parse_log_line(line))
        return logs
    except FileNotFoundError:
        print(f"Error: File with path {file_path} doesn't exist.")
        sys.exit(1)
    except Exception as e:
        print(f"An error occurred: {e}")

def filter_logs_by_level(logs: list, level: str) -> list:
    pass

def count_logs_by_level(logs: list) -> dict:
    pass

def display_log_counts(counts: dict):
    pass