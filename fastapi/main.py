from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel
from fastapi import FastAPI

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

# api = FastAPI(
#     title='My API'
# )

# # @api.get('/')
# # def get_index():
# #     return {'hello': 'bienvenue'}

# @api.get("/")
# def get_index(argument1):
#     return {
#         'data':argument1
#     }

# @api.get("/typed")
# def get_index(argument1:int):
#     return {
#         'data':argument1+1
#     }

# @api.get("/addition")
# def addtion(a:int,b:Optional[int]=None):
#     if b:
#         result = a+b
#     else:
#         result = a+1
#     return{
#         'addition_result':result
#     }




# @api.get("/users")
# def get_users():
#     return users_db

# @api.get("/users/{ex}")
# def get_data(userid:int):
#     for user in users_db:
#         if user["user_id"] == userid:
#             return user




# @api.get('/item/{itemid:int}')  
# def get_item(itemid):
#     return {
#         'route': 'dynamic',
#         'itemid': itemid
#         }


# @api.get('/item/{itemid}/description/{language}')
# def get_item_language(itemid, language):
#     if language == 'fr':
#         return {
#             'itemid': itemid,
#             'description': 'un objet',
#             'language': 'fr'
#         }
#     else:
#         return {
#             'itemid': itemid,
#             'description': 'an object',
#             'language': 'en'
#         }

# @api.get('/item/{itemid:float}')
# def get_item_float(itemid):
#     return {
#         'route': 'dynamic',
#         'itemid': itemid,
#         'source': 'float'
#     }

# @api.get('/item/{itemid}')
# def get_item_default(itemid):
#     return {
#         'route': 'dynamic',
#         'itemid': itemid,
#         'source': 'string'
#     }


# class Item(BaseModel):
#     itemid:int
#     description:str
#     ower:Optional[str] = None


# @api.post('/item')
# def post_item(item:Item):
#     return{
#         "itemid":item.other
#     }

# class User(BaseModel):
#     userid: Optional[int]
#     name: str
#     subscription: str


# @api.put("/users")
# def add_user(user:User):
#     new_id = max([ user["user_id"] for user in users_db])
#     new_user ={
#         "userid":new_id+1,
#         "name":user.name,
#         "subscription":user.subscription
#     }
#     users_db.append(new_user)
#     return new_user


###########################################################
# from fastapi import FastAPI
# from fastapi import Header

# api = FastAPI(
#     title="My API",
#     description="My own API powered by FastAPI.",
#     version="1.0.86")

# @api.get('/',name="Hello World")
# def get_index():
#     """Returns greetings
#     """
#     return {'greetings': 'welcome'}
    

# def main():
#     print(get_index())

# if __name__ =="__main__":
#     main()


# from pydantic import BaseModel
# from typing import Optional

# class Computer(BaseModel):
#     computerid: int
#     cpu: Optional[str]
#     gpu: Optional[str]
#     price: float

# @api.put('/computer', name='Create a new computer')
# def get_computer(computer: Computer):
#     """Creates a new computer within the database
#     """
#     return computer


# @api.get("/custom",name="Get custom header")
# def get_content(custom_header:Optional[str]=Header(None,description="My own personal header")):
#     return{
#         "Custom_Header":custom_header
#     }



#####################################################################################
# c. Organiser la documentation

# from fastapi import FastAPI

# api = FastAPI(openapi_tags=[
#     {
#         'name': 'home',
#         'description': 'default functions'
#     },
#     {
#         'name': 'items',
#         'description': 'functions that are used to deal with items'
#     }
# ])

# @api.get('/', tags=['home'])
# def get_index():
#     """returns greetings
#     """
#     return {
#         'greetings': 'hello world'
#     }

# @api.get('/items', tags=['home', 'items'])
# def get_items():
#     """returns an item
#     """
#     return {
#         'item': "some item"
#     }


#################################################
# d. Utilisation des erreurs
# from fastapi import FastAPI

# api = FastAPI()

# data = [1, 2, 3, 4, 5]

# @api.get('/data')
# def get_data(index):
#     return {
#         'data': data[int(index)]
#     }


from fastapi import HTTPException
api = FastAPI()
@api.get('/data')
def get_data(index):
    try:
        return {
            'data': data[int(index)]
        }
    except IndexError:
        raise HTTPException(
            status_code=404,
            detail='Unknown Index')
    except ValueError:
        raise HTTPException(
            status_code=400,
            detail='Bad Type'
        )
    
class MyException(Exception):
    def __init__(self,
                 name : str,
                 date: str):
        self.name = name
        self.date = date


from fastapi import Request
from fastapi.responses import JSONResponse
import datetime

@api.exception_handler(MyException)
def MyExceptionHandler(
    request: Request,
    exception: MyException
    ):
    return JSONResponse(
        status_code=418,
        content={
            'url': str(request.url),
            'name': exception.name,
            'message': 'This error is my own',
            'date': exception.date
        }
    )

@api.get('/my_custom_exception')
def get_my_custom_exception():
    raise MyException(
      name='my error',
      date=str(datetime.datetime.now())
      )

responses = {
    200: {"description": "OK"},
    404: {"description": "Item not found"},
    302: {"description": "The item was moved"},
    403: {"description": "Not enough privileges"},
}

@api.get('/thing', responses=responses)
def get_thing():
    return {
        'data': 'hello world'
    }