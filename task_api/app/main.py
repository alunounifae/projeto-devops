from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from app import models, database, crud
from app.schemas import TaskCreate, Task
from typing import List

models.Base.metadata.create_all(bind=database.engine)

app = FastAPI()

# ✅ Corrigido com Depends
@app.post("/tasks/", response_model=Task)
def create_task(task: TaskCreate, db: Session = Depends(database.get_db)):
    return crud.create_task(db, task)

@app.get("/tasks/", response_model=List[Task])
def read_tasks(db: Session = Depends(database.get_db)):
    return crud.get_tasks(db)

@app.get("/tasks/{task_id}", response_model=Task)
def read_task(task_id: int, db: Session = Depends(database.get_db)):
    return crud.get_task(db, task_id)

@app.put("/tasks/{task_id}", response_model=Task)
def update_task(task_id: int, task: TaskCreate, db: Session = Depends(database.get_db)):
    return crud.update_task(db, task_id, task)

@app.delete("/tasks/{task_id}")
def delete_task(task_id: int, db: Session = Depends(database.get_db)):
    return crud.delete_task(db, task_id)
