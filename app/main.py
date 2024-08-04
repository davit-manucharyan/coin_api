from fastapi import FastAPI

from database import engine
from models.models import Base


Base.metadata.create_all(bind=engine)

app = FastAPI()


@app.get("/")
def hi():
    return "hi"


# 0b3ca1c1-ebd8-4c09-87e9-ab8b90cff2d6
