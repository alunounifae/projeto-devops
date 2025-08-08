from fastapi import FastAPI
from app import models, database, crud
from app.schemas import TaskCreate, Task
from typing import List

models.Base.metadata.create_all(bind=database.engine)

app = FastAPI()

@app.post("/tasks/", response_model=Task)
def create_task(task: TaskCreate):
    return crud.create_task(database.get_db(), task)

@app.get("/tasks/", response_model=List[Task])
def read_tasks():
    return crud.get_tasks(database.get_db())

@app.get("/tasks/{task_id}", response_model=Task)
def read_task(task_id: int):
    return crud.get_task(database.get_db(), task_id)

@app.put("/tasks/{task_id}", response_model=Task)
def update_task(task_id: int, task: TaskCreate):
    return crud.update_task(database.get_db(), task_id, task)

@app.delete("/tasks/{task_id}")
def delete_task(task_id: int):
    return crud.delete_task(database.get_db(), task_id)
