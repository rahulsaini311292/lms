from fastapi import APIRouter

root_router = APIRouter()

@root_router.get("/")
def root():
    return "Hello LMS"
