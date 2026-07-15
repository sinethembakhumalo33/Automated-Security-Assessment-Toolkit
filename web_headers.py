import requests


def get_headers(url):
    """
    Retrieve HTTP response headers from a website.
    """

    try:
        response = requests.get(url, timeout=5)

        headers = response.headers

        return {
            "URL": url,
            "Status Code": response.status_code,
            "Server": headers.get("Server", "Not Provided"),
            "Content-Type": headers.get("Content-Type", "Not Provided"),
            "Date": headers.get("Date", "Not Provided"),
            "Content-Length": headers.get("Content-Length", "Not Provided"),
            "Strict-Transport-Security": headers.get(
                "Strict-Transport-Security", "Not Present"
            ),
            "Content-Security-Policy": headers.get(
                "Content-Security-Policy", "Not Present"
            ),
            "X-Frame-Options": headers.get(
                "X-Frame-Options", "Not Present"
            ),
            "X-Content-Type-Options": headers.get(
                "X-Content-Type-Options", "Not Present"
            )
        }

    except requests.exceptions.RequestException as e:
        return {
            "Error": str(e)
        }


if __name__ == "__main__":
    url = input("Enter website URL (include https://): ")

    results = get_headers(url)

    print("\nHTTP Header Results")
    print("-" * 35)

    for key, value in results.items():
        print(f"{key}: {value}")