import sys

from comands_func import load_logs


def main():
    if len(sys.argv) < 2:
        print(f"Used: python main.py {sys.argv}")
        sys.exit(1)

    file_path = sys.argv[1]
    level_arg = sys.argv[2] if len(sys.argv) > 2 else None

    logs = load_logs(file_path)




if __name__ == "__main__":
    main()