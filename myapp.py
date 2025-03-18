import requests


def fetch_data(url):
    try:
        response = requests.get(url, timeout=5)  # Set a timeout of 5 seconds
        print(f"Fetching data from: {url}")
        print(f"Status Code: {response.status_code}")

        # Check if request was successful
        if response.status_code == 200:
            try:
                data = response.json()  # Try to parse JSON
                return data
            except requests.exceptions.JSONDecodeError:
                print(f"Error: Unable to parse JSON from {url}")
                print(f"Response content:\n{response.text}")  # Print raw response
                return None
        else:
            print(
                f"Error: API request failed with status {response.status_code} for {url}"
            )
            return None

    except requests.exceptions.RequestException as e:
        print(f"Error fetching {url}: {e}")
        return None


category_data = fetch_data("http://127.0.0.1:8000/category_json/")
subcategory_data = fetch_data("http://127.0.0.1:8000/subcategory_json/")
product_data = fetch_data("http://127.0.0.1:8000/product_json/")

print("\n------ Category JSON Data ------")
print(category_data, "\n")

print("------ Subcategory JSON Data ------")
print(subcategory_data, "\n")

print("------ Product JSON Data ------")
print(product_data, "\n")
