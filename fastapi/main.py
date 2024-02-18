from fastapi import FastAPI
from typing import Optional

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




def main():
    print(get_index())

if __name__ =="__main__":
    main()
