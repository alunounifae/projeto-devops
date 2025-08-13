from pydantic import BaseModel
from typing import Optional


# Base comum para criação e atualização
class TaskBase(BaseModel):
    title: str
    description: Optional[str] = None


# Modelo usado para criar uma nova tarefa (entrada)
class TaskCreate(TaskBase):
    pass


# Modelo usado para atualizar uma tarefa (entrada)
class TaskUpdate(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None


# Modelo usado para resposta da API (saída)
class TaskResponse(TaskBase):
    id: int

    class Config:
        from_attributes = True  # Substitui orm_mode no Pydantic v2


# Lista de tarefas (para endpoints que retornam várias)
class TaskList(BaseModel):
    tasks: list[TaskResponse]
