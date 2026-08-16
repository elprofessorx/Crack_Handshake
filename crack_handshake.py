import os 
import  subprocess

ROCKYOU_PATH =  "/usr/share/wordlists/rockyou.txt" # path to rockyou.txt wordlist

def crack_handshake():
    if not os.path.exists(ROCKYOU_PATH):
        print(f"[-] Wordlist not found at {ROCKYOU_PATH}")
        print(f"[!] Make sure to extract the rockyou.txt file from the rockyou.txt.gz archive.")
        return

    handshake_file = input("Enter the path to the handshake file ( e .g., capture..cap): ").strip()
    if not os.path.exists(handshake_file):
        print(f"[-] Handshake file not found ")
        return

    print("\n[+] Starting the handshake cracking process...")

    cmd = ["aircrack-ng", "-w", ROCKYOU_PATH, handshake_file]

    try:
        subprocess.run(cmd)
    except KeyboardInterrupt:
        print("\n[!] Cracking process interrupted by user.")
    except Exception as e:
        print(f"[-] An error occurred: {e}")

if __name__ == "__main__":
    crack_handshake()
