import socket


def scan_ports(target):
    """Scan a list of common TCP ports on the target host."""

    ports = [22, 80, 443, 445, 3389, 8080]
    results = {}

    for port in ports:
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(1)

            result = sock.connect_ex((target, port))

            if result == 0:
                results[port] = "OPEN"
            else:
                results[port] = "CLOSED"

            sock.close()

        except socket.gaierror:
            print("Error: Invalid hostname or IP address.")
            break

        except Exception as e:
            print(f"Error scanning port {port}: {e}")

    return results


if __name__ == "__main__":
    target = input("Enter target IP or hostname: ")

    print("\nScanning...\n")

    results = scan_ports(target)

    print("Scan Results")
    print("-" * 25)

    for port, status in results.items():
        print(f"Port {port:<5} {status}")