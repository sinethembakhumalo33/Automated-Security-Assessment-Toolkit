# Automated Security Assessment Toolkit

## Overview

The Automated Security Assessment Toolkit is a modular Python application that automates several common tasks used during authorized security assessments.

## Features

- Collects system information
- Scans common TCP ports
- Performs DNS lookups
- Retrieves HTTP response headers
- Generates timestamped reports
- Logs assessment activity
- Modular design for easy extension

## Technologies

- Python 3
- requests
- psutil

## Project Structure

```text
toolkit.py
system_info.py
scanner.py
dns_lookup.py
web_headers.py
report.py
utils.py
```

## Installation

Clone the repository.

```bash
git clone https://github.com/YourUsername/Automated-Security-Assessment-Toolkit.git
```

Install dependencies.

```bash
pip install -r requirements.txt
```

Run the toolkit.

```bash
python toolkit.py
```

## Example Output

```text
Assessment completed successfully.

Report saved:
reports/report_20260715_164210.txt
```

## Disclaimer

This project is intended for educational purposes and authorized security assessments only.
