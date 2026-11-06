import requests
todo_id = input("Enter to-do ID:")
try:
    response = requests.get(f"https://jsonplaceholder.typicode.com/todos/{todo_id}",timeout=5)
    print(response.status_code)
    if response.status_code == 200: 
        data = response.json()
        print(f"TO-DO ID: {data["id"]}")
        print(data["title"])
        print(data["completed"])
    else:
        print("Request failed. Please try again.")
except requests.exceptions.RequestException:
    print("Unable to complete API request.")