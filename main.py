from fastapi import FastAPI

app = FastAPI()

@app.get('/')
async def index():
    return {'hello':'world'}


@app.get("/version")
def get_version():
    return {"version": "1.0.0", "name": "My First FastAPI App"}

@app.get('/about')
async def about():
    return {'about':'An Exceptional company'}