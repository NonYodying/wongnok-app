from fastapi import APIRouter
from models.recipe import recipe, updateRecipe
from config.config import recipesCollection
import datetime
from serializer.recipe import convertRecipe, convertRecipes
from bson import ObjectId

recipeRoot= APIRouter()

@recipeRoot.post('/new/recipe')
async def newRecipes(doc:recipe):
    doc = dict(doc)
    current_date = datetime.date.today()
    doc['date'] = str(current_date)
    
    res = recipesCollection.insert_one(doc)
    doc_id = str(res.inserted_id)
    return{
        "status" : "ok",
        "message " : "Recipe posted successfully",
        '_id' : doc_id
    } 

@recipeRoot.get('/all/recipes')
async def allRecipes():
    res = recipesCollection.find()
    convertData = convertRecipes(res)

    return {
        "status":"ok",
        "data":convertData,
    }

@recipeRoot.get('/recipe/{_id}')
async def getRecipes(_id:str):
    res = recipesCollection.find_one({"_id": ObjectId(_id)})
    convert_Recipe = convertRecipe(res)
    return {
        "status":"OK",
        "data": convert_Recipe
    }

@recipeRoot.patch('/update/{_id}')
async def undateRecipe(_id:str, doc:updateRecipe):
    req = dict(doc)
    return req

@recipeRoot.delete('/delete/{_id}')
async def deleteRecipe(_id:str):
    recipesCollection.find_one_and_delete(
        {'_id' : ObjectId(_id)}
    )

    return {
        "status":"OK",
        "data":"Recipe deleted succesfully"
    }