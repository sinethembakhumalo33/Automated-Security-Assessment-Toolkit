from system_info import get_system_info
from scanner import scan_ports
from dns_lookup import dns_lookup
from web_headers import get_headers
from report import save_report
from utils import log_info, log_error


def main():
    print("=" * 60)
    print("      AUTOMATED SECURITY ASSESSMENT TOOLKIT")
    print("=" * 60)

    log_info("Assessment started.")

    # ----------------------------
    # System Information
    # ----------------------------
    print("\n[1/4] Collecting system information...")

    try:
        system_info = get_system_info()
        log_info("System information collected.")
    except Exception as e:
        log_error(f"System information failed: {e}")
        system_info = {"Error": str(e)}

    # ----------------------------
    # Port Scan
    # ----------------------------
    target = input("\nEnter target IP or hostname: ")

    print("\n[2/4] Scanning common TCP ports...")

    try:
        port_scan = scan_ports(target)
        log_info(f"Port scan completed for {target}.")
    except Exception as e:
        log_error(f"Port scan failed: {e}")
        port_scan = {"Error": str(e)}

    # ----------------------------
    # DNS Lookup
    # ----------------------------
    domain = input("\nEnter domain name (example.com): ")

    print("\n[3/4] Performing DNS lookup...")

    try:
        dns_info = dns_lookup(domain)
        log_info(f"DNS lookup completed for {domain}.")
    except Exception as e:
        log_error(f"DNS lookup failed: {e}")
        dns_info = {"Error": str(e)}

    # ----------------------------
    # HTTP Headers
    # ----------------------------
    url = input("\nEnter website URL (include https://): ")

    print("\n[4/4] Retrieving HTTP headers...")

    try:
        header_info = get_headers(url)
        log_info(f"Retrieved HTTP headers from {url}.")
    except Exception as e:
        log_error(f"HTTP header retrieval failed: {e}")
        header_info = {"Error": str(e)}

    # ----------------------------
    # Save Report
    # ----------------------------
    print("\nGenerating report...")

    try:
        report_file = save_report(
            system_info,
            port_scan,
            dns_info,
            header_info
        )

        log_info(f"Report saved: {report_file}")

        print("\nAssessment completed successfully.")
        print(f"Report saved to: {report_file}")

    except Exception as e:
        log_error(f"Report generation failed: {e}")
        print(f"\nError creating report: {e}")


if __name__ == "__main__":
    main()