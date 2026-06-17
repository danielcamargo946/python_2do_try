from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def inicio():
    return{"hola estoy aprendiendo fastapi"}