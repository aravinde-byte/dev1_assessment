import requests

def fetch_and_display_users(num_users):
    url = "https://jsonplaceholder.typicode.com/users"
    try:
        response = requests.get(url, timeout=5)
        response.raise_for_status()
        users = response.json()
        for user in users[:num_users]:
            print(f"Name: {user['name']}, Email: {user['email']}, City: {user['address']['city']}")
    except requests.exceptions.RequestException as e:
        print(f"Network error: {e}")
    except (KeyError, TypeError) as e:
        print(f"Data parsing error: {e}")

# Example calls
fetch_and_display_users(3)
fetch_and_display_users(15)
