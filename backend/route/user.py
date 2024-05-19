from fastapi import APIRouter
from models.user import user, updateUser
from config.config import usersCollection
import datetime
from serializer.recipe import convertUser
from bson import ObjectId

userRoot= APIRouter()

@userRoot.post('/create/user')
async def createUser(doc:user):
    doc = dict(doc)
    current_date = datetime.date.today()
    doc['date'] = str(current_date)
    
    res = usersCollection.insert_one(doc)
    doc_id = str(res.inserted_id)
    return{
        "status" : "ok",
        "message " : "User created successfully",
        '_id' : doc_id
    } 


@userRoot.patch('/update/{_id}')
async def undateUser(_id:str, doc:updateUser):
    req = dict(doc)
    return req

@userRoot.delete('/delete/{_id}')
async def deleteUser(_id:str):
    usersCollection.find_one_and_delete(
        {'_id' : ObjectId(_id)}
    )

    return {
        "status":"OK",
        "data":"User deleted succesfully"
    }