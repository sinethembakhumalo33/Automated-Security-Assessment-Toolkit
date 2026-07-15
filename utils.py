import logging
import os


# Create the logs folder if it doesn't already exist
os.makedirs("logs", exist_ok=True)


# Configure logging
logging.basicConfig(
    filename="logs/tool.log",
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S"
)


def log_info(message):
    """Log an informational message."""
    logging.info(message)


def log_warning(message):
    """Log a warning message."""
    logging.warning(message)


def log_error(message):
    """Log an error message."""
    logging.error(message)

if __name__ == "__main__":
    log_info("Security Toolkit started.")
    log_warning("This is a warning message.")
    log_error("This is an error message.")

    print("Log messages written to logs/tool.log")