# Basic Encryption & Decryption

A modular command-line application implementing multiple cipher techniques for text encryption and decryption, built with Python.

## Features

- **Caesar Cipher** — Shift-based substitution with user-defined key (1–25)
- **Vigenère Cipher** — Polyalphabetic substitution using a keyword
- **ROT13 Cipher** — Fixed 13-shift rotation (self-inverse)
- **Frequency Analysis** — Character frequency histogram for cryptanalysis
- **File Encryption** — Encrypt file contents using Caesar Cipher, output to `.enc`
- **Input Validation** — All user inputs are validated with clear error feedback
- **24 Unit Tests** — Comprehensive test coverage across all ciphers

## Project Structure

```
.
├── app.py                  # Entry point — menu-driven CLI
├── ciphers/
│   ├── __init__.py         # Public API exports
│   ├── base.py             # Abstract base cipher class
│   ├── caesar.py           # Caesar Cipher implementation
│   ├── vigenere.py         # Vigenère Cipher implementation
│   └── rot13.py            # ROT13 Cipher implementation
├── utils/
│   ├── __init__.py
│   └── helpers.py          # I/O helpers, validation, frequency analysis
├── tests/
│   ├── __init__.py
│   └── test_ciphers.py     # 24 unit tests (unittest + pytest)
├── samples/                # Sample files for file encryption demo
└── ReadMe.md
```

## Getting Started

### Prerequisites

- Python 3.10+

### Run

```bash
python app.py
```

### Run Tests

```bash
python -m pytest tests/ -v
```

## Usage Example

```
================================================
         BASIC ENCRYPTION & DECRYPTION
================================================
  1. Caesar Cipher
  2. Vigenere Cipher
  3. ROT13 Cipher
  4. Frequency Analysis
  5. Encrypt File (Caesar)
  6. Exit
================================================
Enter your choice: 1

Enter text to encrypt: CyberSecurity
Enter shift value (1-25): 3

  Cipher used : Caesar Cipher (shift=3)
  Original    : CyberSecurity
  Encrypted   : FbehuVhfxulwb
  Decrypted   : CyberSecurity
```

## Design Decisions

- **Abstract base class** (`BaseCipher`) enforces a consistent interface across all ciphers — makes adding new ciphers trivial
- **Modular architecture** separates cipher logic, I/O utilities, and the CLI into distinct modules
- **Non-alpha preservation** — spaces, punctuation, and digits pass through unchanged
- **Case preservation** — uppercase/lowercase is maintained in all cipher operations
- **PyPI-discoverable structure** — the package layout follows standard Python conventions

## License

MIT
