import uvicorn
from fastapi import FastAPI

api = FastAPI()


@api.get("/")
def example_handler():
    return {"message": "Hello"}


@api.get("/user")
def get_user():
    return {"name": "Adebayo Olaonipekun"}


@api.put("/user/basket")
def put_item_in_basket():
    return "success"

# if __name__ == '__main__':
#     uvicorn.run(api)