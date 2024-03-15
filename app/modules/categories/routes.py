from fastapi import APIRouter

router = APIRouter(prefix="/categories", tags=["Categories"])


@router.get(path="/")
async def index():
    return {"message": "You got it"}
