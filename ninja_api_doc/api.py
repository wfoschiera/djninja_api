from ninja import NinjaAPI
from todo_list.api import router as todo_list_router

api = NinjaAPI()


api.add_router("todo", todo_list_router)
