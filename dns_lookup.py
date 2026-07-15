import socket


def dns_lookup(domain):
    """
    Perform a basic DNS lookup.
    Returns the domain, IP address, and reverse DNS name.
    """

    try:
        # Resolve domain to IP address
        ip_address = socket.gethostbyname(domain)

        # Perform reverse lookup
        try:
            reverse_name = socket.gethostbyaddr(ip_address)[0]
        except socket.herror:
            reverse_name = "No reverse DNS record found"

        return {
            "Domain": domain,
            "IP Address": ip_address,
            "Reverse DNS": reverse_name
        }

    except socket.gaierror:
        return {
            "Error": "Unable to resolve the domain."
        }


if __name__ == "__main__":
    domain = input("Enter a domain name: ")

    results = dns_lookup(domain)

    print("\nDNS Lookup Results")
    print("-" * 30)

    for key, value in results.items():
        print(f"{key}: {value}")