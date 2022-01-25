from typing import Optional
from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = [
    "http://localhost:3000"
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.post("/hello")
async def getInformation(info : Request):
    req_info = await info.json()
    print(req_info)
    return {
        "status" : "SUCCESS",
        "StatusCode" : 404,
        "value":"hi"
    }

@app.post("/sendFile")
async def getInfo(info : Request):
    req_info = await info.json()
    print(req_info)
    return {
        "status" : "SUCCESS",
        "StatusCode" : 404,
        "value":"hi"
    }


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}
