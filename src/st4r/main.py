"""Minimal, in-memory academic task management API.

This is a prototype. Data is lost when the process restarts, and there is
no authentication or third-party service integration.
"""
from datetime import date
from itertools import count
from typing import Literal

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field

app = FastAPI(title="ST4R Academic Workspace", version="0.1.0")
_next_id = count(1)
_tasks: dict[int, "Task"] = {}


class TaskInput(BaseModel):
    title: str = Field(min_length=1, max_length=200)
    course: str | None = Field(default=None, max_length=120)
    due_date: date | None = None


class Task(TaskInput):
    id: int
    status: Literal["todo", "done"] = "todo"


@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok"}


@app.get("/tasks", response_model=list[Task])
def list_tasks() -> list[Task]:
    return list(_tasks.values())


@app.post("/tasks", response_model=Task, status_code=201)
def create_task(data: TaskInput) -> Task:
    task = Task(id=next(_next_id), **data.model_dump())
    _tasks[task.id] = task
    return task


@app.patch("/tasks/{task_id}/complete", response_model=Task)
def complete_task(task_id: int) -> Task:
    task = _tasks.get(task_id)
    if task is None:
        raise HTTPException(status_code=404, detail="Task not found")
    updated = task.model_copy(update={"status": "done"})
    _tasks[task_id] = updated
    return updated


@app.delete("/tasks/{task_id}", status_code=204)
def delete_task(task_id: int) -> None:
    if task_id not in _tasks:
        raise HTTPException(status_code=404, detail="Task not found")
    del _tasks[task_id]
