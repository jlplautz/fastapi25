from fastapi import FastAPI

from fastapi25.schemas import Message

app = FastAPI()


@app.get('/', status_code=200, response_model=Message)
def read_root():
    return {'message': 'Hello World!'}


@app.get('/ola_mundo', status_code=200)
def ola_mundo():
    return {"Ola Mundo!"}
