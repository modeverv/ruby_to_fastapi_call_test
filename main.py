from fastapi import FastAPI
from fastapi import BackgroundTasks
from time import sleep
from datetime import datetime

app = FastAPI()

def back_ground_task(foo):
    sleep(3)
    print(f'background task!!! {foo} - {datetime.utcnow()}')

@app.get('/newmail')
async def newmail(foo, background_tasks: BackgroundTasks):
    background_tasks.add_task(back_ground_task, foo)
    return {"text": "hello world!"}

# uvicorn main:app --reload
