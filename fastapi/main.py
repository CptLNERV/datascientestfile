from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel

users_db = [
    {
        'user_id': 1,
        'name': 'Alice',
        'subscription': 'free tier'
    },
    {
        'user_id': 2,
        'name': 'Bob',
        'subscription': 'premium tier'
    },
    {
        'user_id': 3,
        'name': 'Clementine',
        'subscription': 'free tier'
    }
]

api = FastAPI(
    title='My API'
)

# @api.get('/')
# def get_index():
#     return {'hello': 'bienvenue'}

@api.get("/")
def get_index(argument1):
    return {
        'data':argument1
    }

@api.get("/typed")
def get_index(argument1:int):
    return {
        'data':argument1+1
    }

@api.get("/addition")
def addtion(a:int,b:Optional[int]=None):
    if b:
        result = a+b
    else:
        result = a+1
    return{
        'addition_result':result
    }




@api.get("/users")
def get_users():
    return users_db

@api.get("/users/{userid}")
def get_data(userid:int):
    for user in users_db:
        if user["user_id"] == userid:
            return user




@api.get('/item/{itemid:int}')  
def get_item(itemid):
    return {
        'route': 'dynamic',
        'itemid': itemid
        }


@api.get('/item/{itemid}/description/{language}')
def get_item_language(itemid, language):
    if language == 'fr':
        return {
            'itemid': itemid,
            'description': 'un objet',
            'language': 'fr'
        }
    else:
        return {
            'itemid': itemid,
            'description': 'an object',
            'language': 'en'
        }

@api.get('/item/{itemid:float}')
def get_item_float(itemid):
    return {
        'route': 'dynamic',
        'itemid': itemid,
        'source': 'float'
    }

@api.get('/item/{itemid}')
def get_item_default(itemid):
    return {
        'route': 'dynamic',
        'itemid': itemid,
        'source': 'string'
    }


class Item(BaseModel):
    itemid:int
    description:str
    ower:Optional[str] = None


@api.post('/item')
def post_item(item:Item):
    return{
        "itemid":item.other
    }

class User(BaseModel):
    userid: Optional[int]
    name: str
    subscription: str


@api.put("/users")
def add_user(user:User):
    new_id = max([ user["user_id"] for user in users_db])
    new_user ={
        "userid":new_id+1,
        "name":user.name,
        "subscription":user.subscription
    }
    users_db.append(new_user)
    return new_user


    

    




def main():
    print(get_index())

if __name__ =="__main__":
    main()
