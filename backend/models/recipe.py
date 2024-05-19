from pydantic import BaseModel



class recipe(BaseModel):
    title: str
    img: str
    ingradient: str
    method: str
    time: int 
    difucallty: str
    rate: None

class updateRecipe(BaseModel):
    title: None
    img: None
    ingradient: None
    method: None
    time: None 
    difucallty: None
   
class rateRecipe(BaseModel):
    rate: str