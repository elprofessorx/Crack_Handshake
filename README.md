#  WPA/WPA2 Handshake Cracker
A simple Python script designed to automate WPA/WPA2 handshake cracking using 'aircrack-ng' and the 'rockyou.txt' wordlist on kali linux.

---

## Prerequisites 
Make sure your system meets the following requirement before running the script:

* **Linux OS** (Tested on kali linux)
* **Python 3.x**
* **aircrack-ng** installed
* **rockyou.txt** wordlist available at '/usr/share/wordlists/rockyou.txt'

If 'rockyou.txt' is compressed on your system , extract it first:
'''bash
sudo gzip -d /usr/share/wordlists/rockyou.txt.gz


Installation:

1. Open your terminal and clone the repository:
   '''git clone [https://github.com/elprofessorx/Crack_Handshake.git]

2. Navigate into the project directory:
   cd Crack_Handshake 


Usage:

1. Execute the Python script:
   python3 crack_handshake.py

2. When prompted, enter the path to your captured handshake file:
   Enter the path to the handshake file (e .g., capture..cap ): /path/to/your/handshake.cap

3. The script will automatically trigger aircrack-ng using the rockyou.txt wordlist to start cracking.

Disclaimer:

This tool is created strictly for educational and authorized security testing purposes only. Usage of this script against networks without prior mutual consent is illegal. The author assumes no liability for any misuse or damage caused by this program.
