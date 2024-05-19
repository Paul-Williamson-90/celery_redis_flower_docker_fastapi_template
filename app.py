from fastapi import FastAPI
import tasks

app = FastAPI()

@app.get("/ping")
async def read_root():
    return {"message": "pong"}

@app.get("/add")
async def add(x: int, y: int):
    result = tasks.task_add.delay(x, y)
    return {
        "task_id": result.id,
        "result": "processing"
    }

@app.get("/result/{task_id}")
async def get_result(task_id: str):
    result = tasks.app.AsyncResult(task_id)
    if result.ready():
        return {
            "task_id": task_id,
            "result": result.get()
        }
    else:
        return {
            "task_id": task_id,
            "result": "processing"
        }