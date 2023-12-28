from pymongo import MongoClient

client = MongoClient(
    host="127.0.0.1",
    port = 27017
)

# print(client.list_database_names())

sample = client["sample"]
c_zips = sample["zips"]

# we can write like this also 
C_zips2 = client["sample"]["zips"]

# print(f"zips1: \n{c_zips.find_one()}")
# print(f"zips2: \n{C_zips2.find_one()}")


# rand = sample.create_collection(name = "rand")

#we can check the creation of ther collection with :
print(sample.list_collection_names())

data = [
  {"name": "Melthouse","bread":"Wheat","sauce": "Ceasar"},
  {"name": "Italian BMT", "extras": ["pickles","onions","lettuce"],"sauce":["Chipotle", "Aioli"]},
  {"name": "Steakhouse Melt","bread":"Parmesan Oregano"}, 
  {"name": "Germinal", "author":"Emile Zola"}, 
  {"pastry":"cream puff","flavour":"chocolate","size":"big"}
]

# rand.insert_many(data)
zips  =client["sample"]["zips"]

# for i in list(zips.find({},{"_id":0,"city":1})):
#     print(i)

# # limit in 12 units
# for i in list(zips.find({},{"_id":0,"city":1}).limit(12)):
#     print(i)

print(zips.find().distinct("state"))


from pprint import pprint
# print(client["sample"]["cie"].find_one())
# pprint(client["sample"]["cie"].find_one())


pprint(
    list(
        client["sample"]["cie"].aggregate(
            [
                {"$match": {"acquisitions.company.name": "Tumblr"}},
                {"$project": {"_id": 1, "society": "$name"}}
            ]
        )
    )
)