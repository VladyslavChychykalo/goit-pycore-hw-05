import sys

def parse_log_line(line: str) -> dict:
    parts = line.split()
    return {
        'date': parts[0],
        'time': parts[1],
        'level': parts[2],
        'text': ' '.join(parts[3:]),
    }

def load_logs(file_path: str) -> list:
    try:
        logs = []
        with open(file_path, 'r') as file:
            for line in file:
                logs.append(parse_log_line(line))
        return logs
    except FileNotFoundError:
        print(f"File '{file_path}' not found.")
        sys.exit(1)

def filter_logs_by_level(logs: list, level: str) -> list:
    return list(filter(lambda log: log['level'] == level, logs))

def count_logs_by_level(logs: list) -> dict:
    levels = {}
    for log in logs:
        level = log['level']
        if level not in levels:
            levels[level] = 0
        levels[level] += 1
    return levels

def display_log_counts(counts: dict):
    print('Рівень логування | Кількість')
    print('-----------------|---------')
    for level, count in counts.items():
        print(f'{level:<16} | {count}')

def main(path: str):
    logs = load_logs(path)
    counts = count_logs_by_level(logs)
    display_log_counts(counts)

    if len(sys.argv) == 3:
        level = sys.argv[2].upper()
        filtered_logs = filter_logs_by_level(logs, level)
        print(f"\nДеталі логів для рівня '{level}':")
        for log in filtered_logs:
            print(f"{log['date']} {log['time']} - {log['text']}")

if __name__ == '__main__':
    try:
        main(sys.argv[1])
    except IndexError:
        print('Usage: python main.py <path_to_log_file> [log_level]')
        sys.exit(1)
 
