from fastapi import FastAPI 
from route.endPoints import endPoints
from route.recipe import recipeRoot

app = FastAPI()

app.include_router(endPoints)
app.include_router(recipeRoot)