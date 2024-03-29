# API Key: 337b9104-c0af-42f9-b206-05a3a6eb0a62


import requests
from pprint import pprint
import json
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
import os

#airlines dont need a token
def getToken():
    pass
    # airlines_url =  ""
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
    print(os.getcwd())

    with open("../data/cities.json","w") as json_file:
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

    with open("../data/fleets.json","w") as json_file:
        json.dump(fleets_result.json(),json_file,indent=2)
    print("schedule write in fleets.json")



def getCountry():
    url="https://airlabs.co/api/v9/countries"
    params={
        "api_key": "337b9104-c0af-42f9-b206-05a3a6eb0a62",
        "country_code": "FR,CN",
        "continent":"EU,AS"
    }
    country_result = requests.get(url=url,params=params)
    # print(country_result.json())

    country_result = country_result.json().get("response")
    
    with open("../../data/countries.json","w") as json_file:
        json.dump(country_result,json_file,indent=2)
    print("inserted country data")

    return country_result


def connexionMongo(nameC:str, datas:requests.models.Response)-> None:
    urlString = "mongodb+srv://vananhdang2277:vYNdjz6bAE1Ec8Av@airlines.pwurtcd.mongodb.net/"
    client = MongoClient(urlString, tls=True, tlsAllowInvalidCertificates=True)
    print(client.list_database_names())

    collections = client["airlabs"][nameC]
    collections.insert_many(datas)
    print(f"successful insert data {nameC}")

def SendMongoVan(data:requests.models.Response,col_name:str)-> None:
    uri_mongo = "mongodb+srv://vananhdang2277:vYNdjz6bAE1Ec8Av@airlines.pwurtcd.mongodb.net/?retryWrites=true&w=majority"

    # Create a new client and connect to the server
    client = MongoClient(uri_mongo, server_api=ServerApi('1'))
    
    # Send a ping to confirm a successful connection
    try:
        client.admin.command('ping')
        print("Pinged your deployment. You successfully connected to MongoDB!")
    except Exception as e:
        print(e)

    db = client["airlabs"]
    collection = db[col_name]

    collection.insert_many([data.json()]) #insert_many only allow insert list type data
    print(f"successfully {col_name} inserted in to mongodb of Van ")

def SendMongoJay(data:requests.models.Response,col_name:str)-> None:
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
    collection = db[col_name]

    collection.insert_many([data.json()]) #insert_many only allow insert list type data
    print(f"successfully {col_name} inserted in to mongodb of Jay ")

def printjson(data:requests.models.Response)-> None:
    print(type(data))
    print(data)
    # print(data.json())
    

def main():
    # getCity()
    countries= getCountry()
    # connexionMongo("countries",countries)
    # printjson(countries)
    # SendMongoJay(countries,"countries")
    # SendMongoVan(countries,"countries")
    # fleets = getFleets()
    # connexionMongo("Fleets",fleets)
    # ping()


if __name__ == "__main__":
    main()