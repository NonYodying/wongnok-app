from fastapi import APIRouter

endPoints = APIRouter()

@endPoints.get('/')
async def home():
    return {
        "TEST":'OK'
    }