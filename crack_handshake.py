import os 
import sys
import shutil
import subprocess

RED = "\033[92m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
BLUE = "\033[94m"
RESET = "\033[0m"

DEFAULT_ROCKYOU = "/usr/share/wordlists/rockyou.txt"\

def check_dependencies():

    if not shutil.which("aircrack-ng"):
        print(f"{RED}[!] Error: 'aircrack-ng' is not installed on this system.{RESET}")
        print(f"{YELLOW}[*] Install it using : sudo apt install aircrak-ng{RESET}")
        sys.exit(1)

def get_valid_file_path(prompt_text):

    while True:
        try:
            file_path = input(prompt_text).strip()

            if not file_path:
                continue
            if file_path.lower() in['exit', 'quit', 'q']:
                print(f"{YELLOW}[*]Exiting program.{RESET}")
                sys.exit(0)
            if os.path.isfile(file_path):
                return file_path
            else:
                print(f"{RED}[-] File not found at '{file_path}'. Please try again (or type 'q' to quit).{RESET}")
        except (KeyboardInterrupt,EOFError):
            print(f"\n{YELLOW}[*] Process cancelled by user.{RESET}")
            sys.exit(0)

def crack_handshake():
    print(f"{BLUE}== WPA/WPA2 Handshake Cracker Automator =={RESET}\n")

    check_dependencies()

    handshake_file = get_valid_file_path(f"{BLUE}[?] Enter path to Handshake file (.cap / .pcap): {RESET}")

    print(f"\n{YELLOW}[*] Default Wordlist : {DEFAULT_ROCKYOU}{RESET}")
    custom_wordlist = input(f"{BLUE}[?] Press Enter to use default, or input custom wordlist path: {RESET}").strip()

    wordlist_path = custom_wordlist if custom_wordlist else DEFAULT_ROCKYOU

    if not os.path.isfile(wordlist_path):
        print(f"{RED}[-] Wordlist not found at '{wordlist_path}'.{RESET}")
        if wordlist_path == DEFAULT_ROCKYOU:
            print(f"{YELLOW}[!] Extract rockyou using : sudo gzip -d /usr/share/wordlists/rockyou.txt.gz{RESET}:")
        return

    print(f"\n{GREEN}[+] Launching aircrack_ng attack...{RESET}")
    cmd = ["aircrack-ng", "-w", wordlist_path, handshake_file]

    try:
        subprocess.run(cmd)
    except KeyboardInterrupt:
        print(f"\n{YELLOW}[!] Cracking process interrupted by user.{RESET}")
    except Exception as e:
        print(f"{RED}[-] Unexpected error occurred: {e}{RESET}")

if __name__ == "__main__":
    crack_handshake()
