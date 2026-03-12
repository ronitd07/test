import requests
import json

# API endpoint (Example: Public API for Random Users)
url = "https://randomuser.me/api/?results=5"

# Fetch data from API
response = requests.get(url)

# Check if request was successful
if response.status_code == 200:
    data = response.json()
    print("API Data Fetched Successfully!\n")

    # Print fetched data
    print(json.dumps(data, indent=4))

    # Process data (Extract only names and emails)
    users = []
    for user in data['results']:
        users.append({
            "name": f"{user['name']['first']} {user['name']['last']}",
            "email": user['email']
        })

# Save processed data to JSON
    with open("users.json", "w",encoding="utf-8") as f:
        json.dump(users, f, indent=4,ensure_ascii=False)

    print("\nProcessed user data saved to users.json")

else:
    print(f"Error: Unable to fetch data (Status Code: {response.status_code})")