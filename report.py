import os
from datetime import datetime


def save_report(system_info, port_scan, dns_info, header_info):
    """
    Save the assessment results to a timestamped report.
    """

    # Create reports folder if it doesn't exist
    os.makedirs("reports", exist_ok=True)

    # Generate filename
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"reports/report_{timestamp}.txt"

    # Write the report
    with open(filename, "w", encoding="utf-8") as report:

        report.write("=" * 60 + "\n")
        report.write("        SECURITY ASSESSMENT REPORT\n")
        report.write("=" * 60 + "\n\n")

        report.write(f"Generated: {datetime.now()}\n\n")

        # System Information
        report.write("SYSTEM INFORMATION\n")
        report.write("-" * 30 + "\n")

        for key, value in system_info.items():
            report.write(f"{key}: {value}\n")

        report.write("\n")

        # Port Scan
        report.write("PORT SCAN RESULTS\n")
        report.write("-" * 30 + "\n")

        for port, status in port_scan.items():
            report.write(f"Port {port}: {status}\n")

        report.write("\n")

        # DNS Results
        report.write("DNS LOOKUP\n")
        report.write("-" * 30 + "\n")

        for key, value in dns_info.items():
            report.write(f"{key}: {value}\n")

        report.write("\n")

        # HTTP Headers
        report.write("HTTP HEADERS\n")
        report.write("-" * 30 + "\n")

        for key, value in header_info.items():
            report.write(f"{key}: {value}\n")

        report.write("\n")

        # Summary
        report.write("=" * 60 + "\n")
        report.write("Assessment completed successfully.\n")
        report.write("=" * 60 + "\n")

    return filename

if __name__ == "__main__":

    system = {
        "Hostname": "DESKTOP-123",
        "IP Address": "192.168.1.100",
        "Operating System": "Windows 11",
        "CPU": "Intel Core i7",
        "RAM (GB)": 16
    }

    ports = {
        22: "CLOSED",
        80: "OPEN",
        443: "OPEN"
    }

    dns = {
        "Domain": "example.com",
        "IP Address": "93.184.216.34",
        "Reverse DNS": "No reverse record"
    }

    headers = {
        "Server": "ExampleServer",
        "Content-Type": "text/html",
        "Status Code": 200
    }

    report_file = save_report(system, ports, dns, headers)

    print(f"Report saved as: {report_file}")