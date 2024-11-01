from fastapi import FastAPI,Form
from fastapi.responses import FileResponse

app = FastAPI()


@app.get("/")
async def root():
    return FileResponse("index.html")

@app.post("/calculate")
async def summ(num1: int = Form(ge=0, lt=111), num2: int = Form(ge=0, lt=111)):
    return {"sum": num1 + num2}
    