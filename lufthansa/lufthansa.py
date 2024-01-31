# Key:w5hn9ckvhjb2fjc6ts9k8p77s
# Secret:HkPR8YJxbw

import requests
from pprint import pprint
import json
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

def getToken ()->str: # return access_token
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

    # request send to get token
    data = {
        "client_id": client_id,
        "client_secret": client_secret,
        "grant_type": "client_credentials"
    }

    # send POST request
    response = requests.post(api_url, headers=headers, data=data)

    # take care reponse
    if response.status_code == 200:
        # Parsing JSON Responses
        json_response = response.json()

        # Extracting access tokens
        access_token = json_response.get("access_token")
        token_type = json_response.get("token_type")
        expires_in = json_response.get("expires_in")

        
        print(f"Access Token: {access_token}")
        print(f"Token Type: {token_type}")
        print(f"Expires In: {expires_in} seconds")
        print(response.text)
        # print(json_response)

        return access_token
    else:
        print(f"Error: {response.status_code}")
        print(response.text)

def get_headers_token(access_token: str) -> dict: #return headers_token
    """
    Create and return headers for API request.

    Parameters:
        access_token (str): The access token obtained from the authentication process.

    Returns:
        dict: A dictionary containing headers for the API request.
            The 'Authorization' key includes the access token.
            The 'Accept' key is set to 'application/json'.
    """
    headers_token = {
        "Authorization": f"Bearer {access_token}",
        "Accept": "application/json"
    }
    return headers_token

#token got,start to search 
def getRef(headers_token:dict):
    ref_url = "https://api.lufthansa.com/v1/mds-references/airports"


    ref = requests.get(url=ref_url,headers=headers_token)
    # pprint (ref.json())

    with open("/home/jayl/data/ref.json","w") as json_file:
        json.dump(ref.json(),json_file,indent=2)
    print("schedule write in ref.json")

def getSchedule(headers_token:dict):
    params = {
        "airlines": ["LH"], # Based on the return of 400 results cannot be "*"
        "flightNumberRanges": "100-400",#Based on the return of 400 results cannot be "*"
        "startDate": "01JAN23",  # Start date in 2023
        "endDate": "31DEC23",    # End date 2023
        "daysOfOperation": "1234567",  # Flights all weeks
        "timeMode": "UTC",
        "origin": "FRA",         # Departures
        "destination": "MUC"     # destination
    }

    schedule_url = "https://api.lufthansa.com/v1/flight-schedules/flightschedules/passenger"
    schedule = requests.get(url=schedule_url,headers=headers_token,params=params)
    print(type(schedule))
    # pprint(schedule.json())
    

    with open("/home/jayl/data/json.json","w") as json_file:
        json.dump(schedule.json(),json_file,indent=2)
    print("schedule write in json.json")

    return schedule


def SendMongo(schedule):
    uri_mongo = "mongodb+srv://jealiao:pfeXjC9afRTaeXpp@cluster0.hz5kuue.mongodb.net/?retryWrites=true&w=majority"

    # Create a new client and connect to the server
    client = MongoClient(uri_mongo, server_api=ServerApi('1'))
    
    # Send a ping to confirm a successful connection
    try:
        client.admin.command('ping')
        print("Pinged your deployment. You successfully connected to MongoDB!")
    except Exception as e:
        print(e)

    db = client["Cluster0"]
    collection = db["schedule"]

    result = collection.insert_many(schedule.json())
    print("schedule inserted in to mongodb  ")

def main():
     access_token = getToken()
     headers_token = get_headers_token(access_token) 
     getRef(headers_token)
     schedule = getSchedule(headers_token)
     SendMongo(schedule)


     # question1 how to got all the airport code.
     


if __name__=="__main__":
        main()