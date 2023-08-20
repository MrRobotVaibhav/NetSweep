import socket as sc
import subprocess
import argparse
from datetime import datetime
from colorama import init, Fore

init()
GREEN = Fore.GREEN
RED = Fore.RED

subprocess.call('clear', shell=True)

print(''' 
  _   _      _    _____                        
 | \ | |    | |  / ____|                       
 |  \| | ___| |_| (_____      _____  ___ _ __  
 | . ` |/ _ \ __|\___ \ \ /\ / / _ \/ _ \ '_ \ 
 | |\  |  __/ |_ ____) \ V  V /  __/  __/ |_) |
 |_| \_|\___|\__|_____/ \_/\_/ \___|\___| .__/ 
                                        | |    
 By:Vaibhav Jaywant                     |_|    

''')




def argument():
    parser = argparse.ArgumentParser()
    parser.add_argument("-t", dest="target_ip", help="Target IP [e.g, 127.0.0.1]")
    args = parser.parse_args()
    if not args.target_ip:
        parser.error("[-] Please Enter IP Address")
    return args.target_ip

target = argument()

def get_service_name(port):
    try:
        service = sc.getservbyport(port)
        return service
    except:
        return "Unknown"

def port_scan(target):
    try:
        ip = sc.gethostbyname(target)

        print("-" * 80)
        print("Starting to Scan...... ")
        print("Scanning IP:", ip, "| Started on:", datetime.now())
        print("-" * 80)

        for port in range(1, 65535):
            sock = sc.socket(sc.AF_INET, sc.SOCK_STREAM)
            sock.settimeout(1)  # Shorter timeout for faster scanning
            result = sock.connect_ex((ip, port))
            if result == 0:
                print(f"Port {port} : {GREEN}OPEN{Fore.RESET}")
                service = get_service_name(port)
                print(f"Port {port} - {service} is open")
                try:
                    banner = sock.recv(1024).decode('utf-8').strip()
                    print(f"{GREEN}Banner: {banner}")
                except UnicodeDecodeError:
                    print(f"{RED}Banner decoding error")
            sock.close()

    except KeyboardInterrupt:
        print(f"{RED}\nInterruption Detected\nExiting...")

    except sc.gaierror:
        print(f"{RED}\nHostName could not be resolved.")

    except sc.error:
        print(f"{RED}\nNOT CONNECTED TO SERVER.")

    except Exception as e:
        print(f"{RED}\nError: {e}")

port_scan(target)
