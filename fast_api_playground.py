from typing import Optional
from fastapi import FastAPI
from pydantic import BaseModel

class Student(BaseModel):
    name:str
    age:Optional[int]=None
    course:str
    is_nri:Optional[bool]=False

app=FastAPI()

@app.get("/")
async def home():
    return {"message":"hello world"}

@app.get("/items/{item_name}")
async def items(item_name: bool):
    return dict(item_provided=item_name)

@app.post("/student")
async def student(student: Student):
    return student