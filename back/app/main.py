from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from .routers import todo
from .db import models, database

models.Base.metadata.create_all(bind=database.engine)

app = FastAPI()


# def get_db():
#     db = database.sessionLocal()
#     try:
#         yield db
#     finally:
#         db.close()


origins = ['*']
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(todo.router)
