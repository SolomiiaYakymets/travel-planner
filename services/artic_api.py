import requests

BASE_URL = "https://api.artic.edu/api/v1/artworks"


def validate_place(external_id: int):
    try:
        url = f"{BASE_URL}/{external_id}"
        response = requests.get(url, timeout=5)

        if response.status_code != 200:
            return False, None

        data = response.json().get("data", {})
        title = data.get("title", "Unknown")
        return True, title

    except requests.RequestException:
        return False, None
