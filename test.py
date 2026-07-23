import requests

url = "https://nsearchives.nseindia.com/content/nsccl/oi_cli_limit_23-JUL-2026.lst"

headers = {
    "User-Agent": (
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/138.0 Safari/537.36"
    ),
    "Referer": "https://www.nseindia.com/",
    "Accept": "*/*"
}

print("Downloading...")

response = requests.get(url, headers=headers, timeout=30)

print("Status:", response.status_code)
print(response.text[:500])
