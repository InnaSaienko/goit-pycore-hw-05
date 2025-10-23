import sys
from pathlib import Path

from comands_func import load_logs, count_logs_by_level, display_log_counts, filter_logs_by_level, display_log_filtered


def main():
    if len(sys.argv) < 2:
        print(f"Usage: python main.py <logfile> [LEVEL]")
        sys.exit(1)

    file_path = Path(sys.argv[1])

    if not file_path.exists():
        print(f"Error: File not found — {file_path}", file=sys.stderr)
        sys.exit(1)

    log_level = sys.argv[2] if len(sys.argv) > 2 else None
    logs = load_logs(file_path)
    counts = count_logs_by_level(logs)
    display_log_counts(counts)

    if log_level:
        display_log_filtered(logs, log_level)


if __name__ == "__main__":
    main()

# use for call function with level :  python main.py example.log error