from typing import Annotated

from fastapi import Depends, FastAPI, HTTPException
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm

app = FastAPI()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


@app.get("/items/")
async def read_items(token: Annotated[str, Depends(oauth2_scheme)]):
    return {"token": token}


# Giả sử dang sách username/password có sẵn
users = {
    "admin": {"username": "admin", "password": "123456"},
    "client1": {"username": "user1", "password": "123456"},
}


@app.post("/token")
async def login(form_data: OAuth2PasswordRequestForm = Depends()):
    username = form_data.username
    for user_id, user in users.items():
        if username == user["username"]:
            if not form_data.password == user["password"]:
                raise HTTPException(
                    status_code=400, detail="Incorrect username or password"
                )
            break
    else:  # run all users
        raise HTTPException(
            status_code=400, detail="Incorrect username or password"
        )
    return {"access_token": user["username"], "token_type": "bearer"}
