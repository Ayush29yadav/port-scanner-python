import socket

# Target input
target = input("Enter target IP or domain: ")

# Convert domain to IP
try:
    target_ip = socket.gethostbyname(target)
except:
    print("Invalid target")
    exit()

# Common ports

ports = [21, 22, 23, 25, 53, 80, 110, 443]


print(f"\nScanning {target_ip}...\n")


for port in ports:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(1)
    
    result = s.connect_ex((target_ip, port))
    
    if result == 0:
        print(f"[OPEN] Port {port}")
    else:
        print(f"[CLOSED] Port {port}")
    
    s.close()