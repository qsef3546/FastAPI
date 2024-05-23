from fastapi import FastAPI
from model.sqlconnect import myuser,insert,selects,update,delete
app = FastAPI()


@app.get("/hello")
def hello():
    return {"message": "hello world"}


@app.get("/")
def root():
    return {"message": "root tesst"}

@app.post("/user/insert")
def user_insert(u:myuser):
    insert(u)
    return {"message": "insert success!"}

@app.get("/user/list")
def user_select():
    return selects()

@app.patch("/user/put")
def user_put(u:myuser):
    update(u)
    return {"message": "update success!"}

@app.delete("/user/delete")
def delete_user(name:str):
    delete(name)
    return {"message" : f'{name} delete success!'}


