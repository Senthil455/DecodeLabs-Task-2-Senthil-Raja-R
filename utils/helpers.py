import os


def read_file(path: str) -> str:
    with open(path, "r", encoding="utf-8") as f:
        return f.read()


def write_file(path: str, content: str) -> None:
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)


def get_valid_int(prompt: str, min_val: int = None, max_val: int = None) -> int:
    while True:
        raw = input(prompt).strip()
        try:
            val = int(raw)
        except ValueError:
            print("Invalid input. Please enter a valid integer.")
            continue
        if min_val is not None and val < min_val:
            print(f"Value must be >= {min_val}.")
            continue
        if max_val is not None and val > max_val:
            print(f"Value must be <= {max_val}.")
            continue
        return val


def get_non_empty_string(prompt: str, alpha_only: bool = False) -> str:
    while True:
        raw = input(prompt).strip()
        if not raw:
            print("Input cannot be empty. Try again.")
            continue
        if alpha_only and not raw.isalpha():
            print("Input must contain only letters (no spaces, numbers, or symbols).")
            continue
        return raw


def analyze_frequency(text: str) -> dict:
    freq = {}
    for char in text.lower():
        if char.isalpha():
            freq[char] = freq.get(char, 0) + 1
    return dict(sorted(freq.items(), key=lambda x: x[1], reverse=True))


def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")
