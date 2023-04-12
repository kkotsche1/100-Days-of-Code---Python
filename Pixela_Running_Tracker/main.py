import requests

# -------------- Created Pixela User Account ------------ #
USERNAME = "kotschi123"
TOKEN = "Kotschi.123"
headers = {
     "X-USER-TOKEN": TOKEN
}

#create_user = {"token":"Kotschi.123",
               #"username":"kotschi123",
               #"agreeTermsOfService":"yes",
               #"notMinor":"yes"}

#http_post = requests.post(url="https://pixe.la/v1/users", json=create_user)
#print(http_post.text)

# ------------- Created Graph ------------------- #

# PIXELA_ENDPOINT = "https://pixe.la/v1/users"
#
# graph_endpoint = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs"
#
# create_graph = {
#     "id":"graph1",
#     "name":"Running Graph",
#     "unit":"Km",
#     "type":"float",
#     "color":"ajisai"
# }
#


#
# response = requests.post(url=graph_endpoint, json=create_graph, headers=headers)
# print(response)

# --------------------- Pinning My Graph ---------------- #

# set_graph = {
#     "pinnedGraphID": "graph1"
# }
#
# request = requests.put(url="https://pixe.la/@kotschi123", headers=headers, json=set_graph)
# print(request)

#--------------------------- Adding Pixel ---------------#

from datetime import datetime

kilometers_ran = input("How many Kilometers did you run today? (eg. '10.2')")

now = datetime.now()
todays_date = now.strftime("%Y%m%d")


PIXEL_ENDPOINT = f"https://pixe.la/v1/users/{USERNAME}/graphs/graph1"

create_pixel =  {
    "date":todays_date,
    "quantity":kilometers_ran
}
request = requests.post(url=PIXEL_ENDPOINT, json=create_pixel, headers=headers)
print(request)