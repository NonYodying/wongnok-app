from fastapi import FastAPI 
from route.endPoints import endPoints
from route.recipe import recipeRoot
import uvicorn

app = FastAPI()

app.include_router(endPoints)
app.include_router(recipeRoot)

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)