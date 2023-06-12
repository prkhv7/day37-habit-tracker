import requests
from datetime import datetime

USERNAME = "tester852"
TOKEN = "qwewerert"
GRAPH_ID = "graph1"

# CREATE USER
pixela_endpoint = "https://pixe.la/v1/users"
user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)


# CREATE GRAPH
graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"
headers = {
    "X-USER-TOKEN": TOKEN,
}
graph_config = {
    "id": GRAPH_ID,
    "name": "Book pages",
    "unit": "page",
    "type": "int",
    "color": "ajisai",
}

# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)


# POST PIXEL
post_pixel_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"
today = datetime.now().strftime("%Y%m%d")
pixel_config = {
    "date": today,
    "quantity": input("How many pages did you read today? "),
}

response = requests.post(url=post_pixel_endpoint, headers=headers, json=pixel_config)
print(response.text)


# UPDATE PIXEL
pixel_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{today}"

update_pixel = {
    "quantity": "20",
}

# response = requests.put(url=pixel_endpoint, headers=headers, json=update_pixel)
# print(response.text)


# DELETE PIXEL
# response = requests.delete(url=pixel_endpoint, headers=headers)
# print(response.text)
