# Passwords CSV Obfuscator

Lightweight tools to obfuscate (encrypt) and recover (decrypt) password-export CSV files using a master password. Intended for quick, local protection of exported password lists — not a full password manager replacement.

**Features**
- Encrypt CSV exports containing password entries.
- Decrypt previously encrypted CSVs back to plain CSV.
- Simple CLI prompts; the master password is never stored.

**Requirements**
- Python 3.8 or newer
- Install dependencies:

```bash
pip install -r requirements.txt
```

**Quickstart**
- Interactive entrypoint: run [main.py](main.py) and follow the prompts to choose encrypt/decrypt.
- Encrypt a file (prompts for file path and password):

```bash
python encrypt.py
```

- Decrypt a file (prompts for file path and password):

```bash
python decrypt.py
```

If you prefer a single prompt flow that validates CSV headers before encryption, use [main.py](main.py).

**Important files**
- [encrypt.py](encrypt.py): encrypts a CSV file using the provided master password.
- [decrypt.py](decrypt.py): decrypts an encrypted file back to CSV when given the correct password.
- [main.py](main.py): interactive helper that validates CSV headers and routes to encrypt/decrypt.
- [crypto_funcs.py](crypto_funcs.py): low-level crypto helper functions.

**Security notes**
- The master password is not stored; you must remember it to decrypt your data.
- Use a strong, high-entropy master password — weak passwords are vulnerable to brute-force attacks.
- This project provides an additional layer of local protection. It is not a complete security solution; keep backups and consider full password manager solutions for long-term storage.

**License**
See [LICENCE.txt](LICENCE.txt) for licensing details.

I am not responsible for any data loss caused by this project.