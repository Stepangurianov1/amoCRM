import requests
import json
from bs4 import BeautifulSoup as BS
new_arr = []
arr = []
with open("data_file.json", "r") as read_file:
    request_dict = json.load(read_file)
refresh_code = request_dict['refresh_token']
access_token = request_dict['access_token']
api_call_headers = {'Authorization': 'Bearer ' + access_token}
api_statuses_response = requests.get('https://stepangurianov.amocrm.ru/events/list/', headers=api_call_headers,
                                     verify=True)

html = BS(api_statuses_response.content, 'html.parser')
for el in html.select(".list__table__holder"):
    t = el.select(".list-row")
for el, i in enumerate(t):
    new_arr.append(t[el].text)

for el in new_arr:
    arr.append(" ".join(el.split()))
print(arr)