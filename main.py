from fastapi import FastAPI, Depends
from pydantic import BaseModel
from views.calc import router as calc_router
import uvicorn


app = FastAPI()

app.include_router(calc_router)

@app.get('/hello')
def func_hello():
    return 'Hello'

@app.get("/greeting")
def greeting(say: str):
    return {
        "say": say
    }
@app.get("/hi")
@app.get("/hi/{name}")
def hi(name: str = None):
    return {"name": name}



if __name__ == "__main__":
    uvicorn.run("main:app", port=5001, reload=True)