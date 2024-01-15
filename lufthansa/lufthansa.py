# Key:w5hn9ckvhjb2fjc6ts9k8p77s
# Secret:HkPR8YJxbw

import requests
from pprint import pprint

# create API URL
api_url = "https://api.lufthansa.com/v1/oauth/token"

# client_id ID and client secret
client_id = "w5hn9ckvhjb2fjc6ts9k8p77s"
client_secret = "HkPR8YJxbw"

# construct header
# Request URI
# https://developer.lufthansa.com/docs/read/api_basics/Getting_Started
# as lufthansa's webpage:
# POST url should be : https://api.lufthansa.com/v1/oauth/token
# Content-Type should be: application/x-www-form-urlencoded
headers = {
    "Content-Type": "application/x-www-form-urlencoded"
}

# 构建请求参数
data = {
    "client_id": client_id,
    "client_secret": client_secret,
    "grant_type": "client_credentials"
}

# 发送 POST 请求
response = requests.post(api_url, headers=headers, data=data)

# take care reponse
if response.status_code == 200:
    # 解析 JSON 响应
    json_response = response.json()

     # 提取访问令牌等信息
    access_token = json_response.get("access_token")
    token_type = json_response.get("token_type")
    expires_in = json_response.get("expires_in")

    print(f"Access Token: {access_token}")
    print(f"Token Type: {token_type}")
    print(f"Expires In: {expires_in} seconds")
    print(response.text)
    # print(json_response)

else:
    print(f"Error: {response.status_code}")
    print(response.text)


flight_url = "https://api.lufthansa.com/v1/mds-references/airports/FRA"

flight_headers = {
     "Authorization": f"Bearer {access_token}",
     "Accept": "application/json"
}

flight = requests.get(url=flight_url,headers=flight_headers)
# pprint (flight.json())

schedule_url = "/flight-schedules/flightschedules/passenger?airlines=LH&flightNumberRanges=400-405&startDate=05DEC19&endDate=10DEC19&daysOfOperation=1234567&timeMode=UTC"
schedule = requests.get(url=schedule_url,headers=flight_headers)
