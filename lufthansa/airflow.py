# API Key: 337b9104-c0af-42f9-b206-05a3a6eb0a62


import requests
from pprint import pprint
import json
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi


def getToken():

    airlines_url =  ""
    # requests = 



def ping():

    params = {
    'api_key': '337b9104-c0af-42f9-b206-05a3a6eb0a62',
    'params1': 'value1'
    }
    method = 'ping'
    api_base = 'http://airlabs.co/api/v9/'
    api_result = requests.get(api_base+method, params)
    api_response = api_result.json()

    print(json.dumps(api_response, indent=4, sort_keys=True))

def getCity():
    url="https://airlabs.co/api/v9/cities"
    params={
        "api_key": "337b9104-c0af-42f9-b206-05a3a6eb0a62",
        "country_code": "FR,CN"
    }

    city_result = requests.get(url=url,params=params)
    city_response = city_result.json()
    pprint(city_response)

    with open("/home/jayl/data/cities.json","w") as json_file:
        json.dump(city_result.json(),json_file,indent=2)
    print("schedule write in cities.json")

def getFleets():
    url = "https://airlabs.co/api/v9/fleets"
    params={
    "api_key": "337b9104-c0af-42f9-b206-05a3a6eb0a62",
    "limit":50,
    "offes":5000,
    "airline_iata":"LH"
        }

    fleets_result = requests.get(url=url,params=params)
    pprint(fleets_result.json())

    with open("/home/jayl/data/fleets.json","w") as json_file:
        json.dump(fleets_result.json(),json_file,indent=2)
    print("schedule write in fleets.json")


def connexionMongo(nameC, datas):
    urlString = "mongodb+srv://vananhdang2277:vYNdjz6bAE1Ec8Av@airlines.pwurtcd.mongodb.net/"
    client = MongoClient(urlString, tls=True, tlsAllowInvalidCertificates=True)
    print(client.list_database_names())

    collections = client["airlabs"][nameC]
    collections.insert_many(datas)


def main():
    # getCity()
    fleets = getFleets()
    connexionMongo("Fleets",fleets)
    # ping()


if __name__ == "__main__":
    main()