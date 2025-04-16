from fastapi import *
from fastapi.security import OAuth2PasswordBearer
from . token import *


oauth2_scheme=OAuth2PasswordBearer(tokenUrl="login")

def get_current_user(token:str=Depends(oauth2_scheme)):
    try:
        # Assuming verify_token decodes the JWT and checks validity
        payload = verify_token(token)
        username = payload.get("sub")
        if username is None:
            raise HTTPException(status_code=401, detail="Could not validate credentials")
        return username
    except Exception:
        raise HTTPException(status_code=401, detail="Could not validate credentials")