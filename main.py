from typing import Annotated, List

from fastapi import FastAPI, Query
from pydantic import BaseModel, Field, field_validator

app = FastAPI()


class User(BaseModel):
    name: str
    email: str
    age: Annotated[int, Field(ge=18, le=60)]
    role: str

    # pre-validator: run before other validations to check raw input
    @field_validator('email', mode='before')
    def ensure_at_in_email(cls, v):
        if not isinstance(v, str) or '@' not in v:
            raise ValueError("email must contain '@'")
        return v


SAMPLE_USERS = [
    {"name": "Alice", "email": "alice@example.com", "age": 30, "role": "admin"},
    {"name": "Bob", "email": "bob@example.org", "age": 25, "role": "user"},
    {"name": "Carol", "email": "carol@example.com", "age": 40, "role": "user"},
]


@app.get('/')
async def index():
    return {'hello': 'world'}

@app.get("/version")
def get_version():
    return {"version": "1.0.0", "name": "My First FastAPI App"}

@app.get('/about')
async def about():
    return {'about': 'An Exceptional company'}

@app.get('/filter_users', response_model=List[User])
def filter_users(role: str = Query(..., description="Role to filter by")):
    """Return users filtered by the `role` query parameter."""
    users = [User(**data) for data in SAMPLE_USERS]
    filtered = [u for u in users if u.role == role]
    return filtered

