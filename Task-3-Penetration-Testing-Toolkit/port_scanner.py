import socket
from datetime import datetime

def scan_ports(target):
    print("\n" + "-" * 50)
    print(f"Scanning Target : {target}")
    print(f"Scan started   : {datetime.now()}")
    print("-" * 50)

    # Common ports (safe & educational)
    common_ports = [21, 22, 23, 25, 53, 80, 110, 139, 143, 443, 445, 3389]

    for port in common_ports:
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(1)

            result = sock.connect_ex((target, port))
            if result == 0:
                print(f"[OPEN ] Port {port}")
            else:
                print(f"[CLOSED] Port {port}")

            sock.close()

        except socket.error:
            print(f"[ERROR] Could not scan port {port}")

def main():
    print("=== Basic Penetration Testing Toolkit ===")
    target = input("Enter target IP or domain: ").strip()

    if not target:
        print("❌ No target provided!")
        return

    try:
        scan_ports(target)
        print("\n✔ Scan completed successfully.")

    except socket.gaierror:
        print("❌ Hostname could not be resolved.")

    except KeyboardInterrupt:
        print("\n❌ Scan interrupted by user.")

if __name__ == "__main__":
    main()
