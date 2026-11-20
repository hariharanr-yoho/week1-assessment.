import csv
import json
import requests
import os
from dotenv import load_dotenv


import csv
employees = []
high_earners = []

with open("employees.csv", "r", newline="") as file:

    reader = csv.DictReader(file)

    reader.fieldnames = [name.strip().lower() for name in reader.fieldnames]

    for row in reader:
        employees.append(row)

        if int(row["salary"]) > 50000:

            high_earners.append(row)

print("Rows read:", len(employees))
print(" High earners:", len(high_earners))


import csv

with open("employees.csv", "r", newline="") as file:

    reader = csv.DictReader(file)

    print("Column names:", reader.fieldnames)

    for row in reader:
        print(row)

        employees = []
high_earners = []

with open("employees.csv", "r", newline="") as file:

    reader = csv.DictReader(file)

    reader.fieldnames = [
        name.strip().lower() for name in reader.fieldnames
    ]

    for row in reader:
        employees.append(row)

        if int(row["salary"]) > 50000:
            high_earners.append(row)

print("Rows read:", len(employees),
      "| High earners:", len(high_earners))

with open("employees.json", "w") as file:

    json.dump(employees, file, indent=4)

with open("high_earners.csv", "w", newline="") as file:

    fieldnames = [
        "id", "name", "department", "salary", "city"
    ]

    writer = csv.DictWriter(
        file,
        fieldnames=fieldnames
    )

    writer.writeheader()
    writer.writerows(high_earners)

    load_dotenv()

API_KEY = os.getenv("API_KEY")

print("API key loaded:", API_KEY is not None)

url = "https://jsonplaceholder.typicode.com/users"

try:

    response = requests.get(url, timeout=5)

    response.raise_for_status()

    users = response.json()

    for user in users[:3]:

        print(
            user["id"], "-",
            user["name"], "-",
            user["email"]
        )

    # STEP 16: Extract nested JSON
    user_details = []

    for user in users:

        details = {
            "id": user.get("id"),
            "name": user.get("name"),
            "email": user.get("email"),
            "city": user.get("address", {}).get("city"),
            "latitude": user.get("address", {}).get("geo", {}).get("lat"),
            "longitude": user.get("address", {}).get("geo", {}).get("lng")
        }

        user_details.append(details)

    # Save users.json
    with open("users.json", "w") as file:
        json.dump(user_details, file, indent=4)

    print("User details saved to users.json")

except requests.exceptions.Timeout:
    print("Error: Request timed out")

except requests.exceptions.ConnectionError:
    print("Error: Connection failed")

except requests.exceptions.HTTPError as e:
    print("HTTP Error:", e)

try:

    response = requests.get(
        "https://jsonplaceholder.typicode.com/users/9999",
        timeout=5
    )

    if response.status_code == 404:
        print("/users/9999 -> 404 Not found")

    else:
        response.raise_for_status()

except requests.exceptions.Timeout:
    print("Error: Request timed out")

except requests.exceptions.ConnectionError:
    print("Error: Connection failed")

except requests.exceptions.HTTPError as e:
    print("HTTP Error:", e)

# STEP 17: Check 404 error

try:
    response = requests.get(
        "https://jsonplaceholder.typicode.com/users/9999",
        timeout=5
    )

    if response.status_code == 404:
        print("/users/9999 -> 404 Not found")

    else:
        response.raise_for_status()

except requests.exceptions.Timeout:
    print("Error: Request timed out")

except requests.exceptions.ConnectionError:
    print("Error: Connection failed")

except requests.exceptions.HTTPError as e:
    print("HTTP Error:", e)
   