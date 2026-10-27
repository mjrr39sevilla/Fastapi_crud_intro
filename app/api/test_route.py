from fastapi import APIRouter

router = APIRouter()

@router.get("/", tags=["Test"], status_code=200)
def read_test():
    return {"message": "Test route"}

