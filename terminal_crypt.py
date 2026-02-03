import os
import sys
from cryptography.fernet import Fernet
from pathlib import Path

class HackerCrypt:
    def __init__(self):
        self.fernet = None
        self.key = None

    def clear_screen(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    def print_header(self):
        print("""
        ╔════════════════════════════════════════╗
        ║     NETRUNNER // TERMINAL_MODULE       ║
        ║           [ SYSTEM: ONLINE ]           ║
        ╚════════════════════════════════════════╝
        """)

    def get_file_path(self):
        print("> SELECT TARGET FILE PATH:")
        path = input(">> ").strip('"').strip("'")
        
        if not os.path.exists(path):
            print(f"[ERROR] FILE NOT FOUND: {path}")
            return None
        
        return path

    def encrypt_file(self):
        target = self.get_file_path()
        if not target: return

        # Confirm destruction
        print(f"\n[WARNING] THIS WILL OVERWRITE: {Path(target).name}")
        confirm = input("> CONFIRM OVERWRITE? [Y/N]: ")
        if confirm.upper() != 'Y':
            print("[ABORTED] Operation cancelled.")
            return

        try:
            # Init Encryption
            self.key = Fernet.generate_key()
            self.fernet = Fernet(self.key)
            
            print(f"> READING PAYLOAD...")
            
            with open(target, 'rb') as file:
                original_data = file.read()

            print("> GENERATING KEY HASH...")
            encrypted = self.fernet.encrypt(original_data)
            
            # OVERWRITE THE ORIGINAL FILE
            with open(target, 'wb') as file:
                file.write(encrypted)

            # Save Key to file
            key_path = target + ".key"
            with open(key_path, 'wb') as file:
                file.write(self.key)

            print("\n[SUCCESS] PAYLOCK ENGAGED.")
            print(f">> FILE OVERRIDDEN: {target}")
            print(f">> KEY SAVED TO:   {key_path}")
            
            # Print Key to Terminal for copying
            print("\n>> KEY HASH (COPY THIS):")
            print("----------------------------------------")
            print(self.key.decode())
            print("----------------------------------------")

        except Exception as e:
            print(f"[FATAL] ENCRYPTION FAILED: {str(e)}")

    def decrypt_file(self):
        target = self.get_file_path()
        if not target: return

        key_path = input("> ENTER KEY FILE PATH: ").strip('"').strip("'")
        
        if not os.path.exists(key_path):
            print(f"[ERROR] KEY NOT FOUND: {key_path}")
            return

        try:
            with open(key_path, 'rb') as file:
                self.key = file.read()
            
            self.fernet = Fernet(self.key)
            
            print(f"> LOADING ENCRYPTED PAYLOAD...")
            with open(target, 'rb') as file:
                encrypted_data = file.read()

            print("> DECRYPTING STREAM...")
            decrypted = self.fernet.decrypt(encrypted_data)
            
            # OVERWRITE THE ENCRYPTED FILE WITH CLEAN DATA
            with open(target, 'wb') as file:
                file.write(decrypted)

            print("\n[SUCCESS] PAYLOAD RESTORED.")
            print(f">> FILE DECRYPTED: {target}")

        except Exception as e:
            print(f"[FATAL] DECRYPTION FAILED: {str(e)}")
            print("[NOTE] Ensure you are using the correct key for this specific file.")

    def run(self):
        while True:
            self.clear_screen()
            self.print_header()
            
            print("1. ENCRYPT (OVERWRITE)")
            print("2. DECRYPT (RESTORE)")
            print("3. EXIT SYSTEM")
            
            choice = input("\n> SELECT OPERATION [1-3]: ")
            
            if choice == '1':
                print("\n> INITIALIZING ENCRYPTION PROTOCOL...")
                self.encrypt_file()
                input("\n[PRESS ENTER TO RETURN]")
            
            elif choice == '2':
                print("\n> INITIALIZING DECRYPTION PROTOCOL...")
                self.decrypt_file()
                input("\n[PRESS ENTER TO RETURN]")
            
            elif choice == '3':
                print("\n[SYSTEM] SHUTTING DOWN...")
                sys.exit()
                
            else:
                print("[ERROR] INVALID COMMAND.")
                input("[PRESS ENTER TO CONTINUE]")

if __name__ == "__main__":
    app = HackerCrypt()
    app.run()
