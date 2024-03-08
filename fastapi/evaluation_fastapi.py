import pandas as pd
import os
from fastapi import FastAPI,HTTPException
import random
from fastapi.testclient import TestClient
from pydantic import BaseModel
import json

# pwd =os.getcwd()

df_question = pd.read_csv(f"questions.csv")
df_question.replace(float("NaN"),"NaN",inplace=True)
# print(df_question.head(5))

qcmapi =  FastAPI(
    title = 'QCM ',
    description = 'An api for question',
    version = "1.0.6"
)

@qcmapi.get("/")
def index():
    
    return {"test":"Welcome"}

# class argument(BaseModel):
#         use:str
#         subject:list[str]
#         number:int

class argument(BaseModel):
        use:str
        subject:list[str]
        number:int

description = '''use must be one of ['Test de positionnement', 'Test de validation', 'Total Bootcamp'] \n 
subjet must be a list which contiain ['BDD', 'Systèmes distribués', 'Streaming de données', 'Docker',
       'Classification', 'Sytèmes distribués', 'Data Science','Machine Learning', 'Automation'\n
       Before sending out the data, ask the front-end to validate the data.]'''


@qcmapi.post("/question",name="Generate the questions",description=description)
def generationqcm(arg:argument):
    df_question_2 = df_question[df_question["use"]==arg.use]
    df_question_3 = df_question_2[df_question_2["subject"].isin(arg.subject)]

    try:
        if len(df_question_3)<arg.number:
             raise ValueError("Doesn't match database, please do data check before sending")

        random_rows = random.sample(range(len(df_question_3)),arg.number)
        
        quesiton_list= []
        for i in random_rows:
            quesiton_list.append(df_question_3.iloc[i].to_dict())

        return quesiton_list
    except Exception as e:
        print(f'find error: {e}')
    
class User(BaseModel):
     username:str
     password:str

users = {
    "alice": "wonderland",
    "bob": "builder",
    "clementine": "mandarine"
    }

@qcmapi.post("/login")
def login(user:User):
     # check if username exist 
     if user.username not in users:
          raise HTTPException(status_code=401,detail="Invaild username")
     
     # check passward correct
     if users[user.username] != user.password:
          raise HTTPException(status_code=401,detail="Invalid password")
     
     return{"message":"Login successful"}

admin_name = "Admin"
admin_password = "4dm1N"

class Question(BaseModel):
    question:str
    subject: str
    use: str
    correct: str
    responseA: str
    responseB: str
    responseC: str
    responseD: str
    remark: str

@qcmapi.post("/add_question")
def add_question(user:User,question:Question):
     #valide admin
    if(user.username != admin_name or user.password != admin_password ):
          raise HTTPException(status_code=401,detail="invalid admin identifiant")
     
    with open("questions.csv","a") as file:
        file.write("\n")
        file.write("\t".join([
             question.question,
             question.subject,
             question.use,
             question.correct,
             question.responseA,
             question.responseB,
             question.responseC,
             question.responseD,
             question.remark

        ]))
    return{"message":"new question adde successfully"}



#  curl -X 'POST' -i 'http://127.0.0.1:8000/login' -H 'Content-Type: application/json'   -d '{username="alice": password="wonderland"}'


# TEST PART################################################  
# client = TestClient(qcmapi)
# # print(client.get("/question?use=Test%20de%20validation&subject=BDD&subject=Docker&number=2").json())
# print(client.get("/question",params=data))
