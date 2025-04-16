from blog import schemas,database,models
from fastapi import *
from sqlalchemy.orm import Session
from .. hashing import Hash
from .. repository import user

router=APIRouter(
    prefix='/user',
    tags=["Users"]
)
@router.post('/',response_model=schemas.ShowUser)
def createUser(request:schemas.User,db:Session=Depends(database.get_db)):
    return user.create(request,db)


@router.get('/{id}',response_model=schemas.ShowUser)
def getUser(id:int,db:Session=Depends(database.get_db)):
    return user.show(id,db)