import requests

response = requests.get("https://gitlab.com/api/v4/users/arturmachura/projects")
my_projects= response.json()

for project in my_projects:
    print(f"Project Name: {project['name']}, Project ID: {project['id']}")