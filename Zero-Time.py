#Made by c1b3r-p3d1a
#https://github.com/c1b3r-p3d1a

import os
import subprocess
import ctypes
import sys
import time
from colorama import init, Style

init(autoreset=True)

def clean():
    os.system("cls")

def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

def header_1():
    print("""
+-------------------------------------------------------+
|                                                       |
|                                                       |
|  _____                        _____ _                 |
| |__  /___ _ __ ___           |_   _(_)_ __ ___   ___  |
|   / // _ \ '__/ _ \   _____    | | | | '_ ` _ \ / _ \ |
|  / /|  __/ | | (_) | |_____|   | | | | | | | | |  __/ |
| /____\___|_|  \___/            |_| |_|_| |_| |_|\___| |
|                                                       |
|                                                       |
|                                                       |""")
    print("""|\t"From the rebells, for the rebells."            |
|                                                       |
|                                                       |
|                                                 v 1.0 |
+-------------------------------------------------------+  
\t\t\t      Made by >>> c1b3r-p3d1a <<<
\t\t\t\t         %s 
    """%"%sIcon from Icons8"%Style.DIM)

def header_2():
    print("""
+-------------------------------------------------------+
|                                                       |
|                                                       |
|  _____                        _____ _                 |
| |__  /___ _ __ ___           |_   _(_)_ __ ___   ___  |
|   / // _ \ '__/ _ \   _____    | | | | '_ ` _ \ / _ \ |
|  / /|  __/ | | (_) | |_____|   | | | | | | | | |  __/ |
| /____\___|_|  \___/            |_| |_|_| |_| |_|\___| |
|                                                       |
|                                                       |
|                                                       |
+-------------------------------------------------------+""")

def get_prnt_cntrl_state():
    output = subprocess.check_output(["sc", "query", "WpcMonSvc"])
    decoded_output = output.decode("utf-8", "ignore")
    
    lines = decoded_output.splitlines()
    line = lines[3]
    words = line.split()

    state = words[-1]

    return str(state)

def rmv_prnt_cntrl():
    try:
        subprocess.check_output(["sc", "config", "WpcMonSvc", "start=", "disabled"])
        time.sleep(1.5)
        subprocess.check_output(["sc", "stop", "WpcMonSvc"])
        print("\t\t  [+] State > %s"%get_prnt_cntrl_state())
        print("\n[+] Parental controls disabled correctly")
        input("\n[+] Press enter to finish...")
        main()
    except Exception as e:
        input("[-] Error while disabling parental control: %s.\n[-]Press enter to exit..."%e)

def enbl_prnt_cntrl():
    try:
        subprocess.check_output(["sc", "config", "WpcMonSvc", "start=", "auto"])
        time.sleep(1.5)
        subprocess.check_output(["sc", "start", "WpcMonSvc"])
        print("\t\t[+] State > %s"%get_prnt_cntrl_state())
        print("\n[+] Parental controls enabled correctly")
        input("\n[+] Press enter to finish...")
        main()
    except Exception as e:
        input("[-] Error while enabling parental control: %s.\n[-]Press enter to exit..."%e)

def main():
    clean()
    header_1()
    input("Press enter to start...")
    clean()
    header_2()
    selection = input("Parental control state: %s\n\n\t[1] Disable\n\n\t[2] Enable\n\n\t[3] Exit\n\n>"%get_prnt_cntrl_state())
    if selection == "1":
        clean()
        header_2()
        rmv_prnt_cntrl()
    elif selection == "2":
        clean()
        header_2()
        enbl_prnt_cntrl()
    elif selection == "3":
        sys.exit(0)
    else:
        clean()
        header_2()
        print("\n[-] Not a valid input. Aborting...")
        sys.exit(1)

if __name__ == "__main__":
    if is_admin():
        main()
    else:
        ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, 1)
    