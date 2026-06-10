from ciphers import CaesarCipher, VigenereCipher, ROT13Cipher
from utils.helpers import (
    get_valid_int,
    get_non_empty_string,
    analyze_frequency,
    clear_screen,
)


def show_result(original: str, encrypted: str, decrypted: str, cipher_name: str):
    print()
    print(f"  Cipher used : {cipher_name}")
    print(f"  Original    : {original}")
    print(f"  Encrypted   : {encrypted}")
    print(f"  Decrypted   : {decrypted}")
    print()


def run_caesar():
    text = get_non_empty_string("Enter text to encrypt: ")
    shift = get_valid_int("Enter shift value (1-25): ", min_val=1, max_val=25)
    cipher = CaesarCipher(shift)
    encrypted = cipher.encrypt(text)
    decrypted = cipher.decrypt(encrypted)
    show_result(text, encrypted, decrypted, cipher.name)


def run_vigenere():
    text = get_non_empty_string("Enter text to encrypt: ")
    key = get_non_empty_string("Enter keyword (letters only): ", alpha_only=True)
    try:
        cipher = VigenereCipher(key)
    except ValueError as e:
        print(f"Error: {e}")
        return
    encrypted = cipher.encrypt(text)
    decrypted = cipher.decrypt(encrypted)
    show_result(text, encrypted, decrypted, cipher.name)


def run_rot13():
    text = get_non_empty_string("Enter text to encrypt: ")
    cipher = ROT13Cipher()
    encrypted = cipher.encrypt(text)
    decrypted = cipher.decrypt(encrypted)
    show_result(text, encrypted, decrypted, cipher.name)


def run_frequency_analysis():
    text = get_non_empty_string("Enter text to analyze: ")
    freq = analyze_frequency(text)
    if not freq:
        print("No alphabetic characters found.")
        return
    print()
    print("  Character Frequency (top 10):")
    for i, (char, count) in enumerate(freq.items()):
        if i >= 10:
            break
        bar = "#" * count
        print(f"    '{char}': {count:>4}  {bar}")
    print()


def run_file_encrypt():
    import os

    path = get_non_empty_string("Enter file path: ")
    if not os.path.exists(path):
        print("File not found.")
        return
    shift = get_valid_int("Enter shift value (1-25): ", min_val=1, max_val=25)
    from utils.helpers import read_file, write_file

    content = read_file(path)
    cipher = CaesarCipher(shift)
    encrypted = cipher.encrypt(content)
    out_path = path + ".enc"
    write_file(out_path, encrypted)
    print(f"Encrypted file saved as: {out_path}")


def menu():
    while True:
        print()
        print("=" * 48)
        print("         BASIC ENCRYPTION & DECRYPTION")
        print("=" * 48)
        print("  1. Caesar Cipher")
        print("  2. Vigenere Cipher")
        print("  3. ROT13 Cipher")
        print("  4. Frequency Analysis")
        print("  5. Encrypt File (Caesar)")
        print("  6. Exit")
        print("=" * 48)
        choice = get_valid_int("Enter your choice: ", min_val=1, max_val=6)
        print()

        if choice == 1:
            run_caesar()
        elif choice == 2:
            run_vigenere()
        elif choice == 3:
            run_rot13()
        elif choice == 4:
            run_frequency_analysis()
        elif choice == 5:
            run_file_encrypt()
        elif choice == 6:
            print("Goodbye!")
            break

        input("Press Enter to continue...")


if __name__ == "__main__":
    try:
        menu()
    except KeyboardInterrupt:
        print("\n\nGoodbye!")
