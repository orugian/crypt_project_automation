NETRUNNER // CRYPTO_MODULE
==========================

A no-nonsense, terminal-based Python encryption utility designed for immediate file locking. It utilizes Fernet symmetric encryption to secure payloads directly within the terminal, offering a clean "Hacker UI" experience.

> Note: This project focuses on functionality and efficiency, stripping away graphical overhead for raw command-line control.

⚠️ WARNING: DESTRUCTIVE ENCRYPTION
----------------------------------

This tool performs in-place encryption. When you encrypt a file, it overwrites the original data. The file remains in the same location but becomes unreadable without the generated key.

*Do not test this on files you are not willing to lose immediate access to.*

Installation
------------

1.  Ensure you have Python installed.
2.  Install the cryptography dependency via pip:

```
pip install cryptography
```

Usage
-----

Run the script directly from your terminal:

bash

python terminal_crypt.py

### Interface Guide

The application launches a terminal menu system:

1.  ENCRYPT (OVERWRITE): Select this to lock a file.
    -   Select the target file (supports drag-and-drop).
    -   Confirm overwrite.
    -   The tool generates a key, saves it to `[filename].key`, and prints the hash to the terminal.
2.  DECRYPT (RESTORE): Select this to recover a file.
    -   Select the locked file.
    -   Select the associated `.key` file.
    -   The tool restores the original file contents.

Project Files
-------------

-   `terminal_crypt.py`: The main executable script.
-   `README.md`: This documentation file.
-   `teste_files/`: (Example usage folder containing test scripts).
-   `images/`: (Screenshots of the tool in action).

Features
--------

-   Instant Locking: No temporary copies. The file is encrypted in place.
-   Key Persistence: Automatically saves a `.key` file alongside the encrypted payload.
-   Hash Visibility: Prints the generated key to the terminal for immediate clipboard copying.
-   Robust UX: Handles path formatting and validates file existence before execution.

Example Workflow
----------------

### Encryption

text

> SELECT TARGET FILE PATH:

>> "C:\Users\LO\Documents\secrets.txt"

[WARNING] THIS WILL OVERWRITE: secrets.txt

> CONFIRM OVERWRITE? [Y/N]: Y

> GENERATING KEY HASH...

[SUCCESS] PAYLOCK ENGAGED.

>> KEY HASH (COPY THIS):

----------------------------------------

gAAAAABlXy...

----------------------------------------

### Decryption

text

> SELECT TARGET FILE PATH:

>> "C:\Users\LO\Documents\secrets.txt"

> ENTER KEY FILE PATH: "C:\Users\LO\Documents\secrets.txt.key"

> DECRYPTING STREAM...

[SUCCESS] PAYLOAD RESTORED.

Credits
-------

Built with Python and `cryptography.fernet`. Designed for efficient script automation and protection.
