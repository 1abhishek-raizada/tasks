
from blog import schemas,database
from fastapi import *
from typing import List
from sqlalchemy.orm import Session
from .. repository import blog
from .. oauth2 import get_current_user
router=APIRouter(
    prefix='/blog',
    tags=["Blogs"]
)

@router.get('/',response_model=List[schemas.ShowBlog])
def all(db:Session=Depends(database.get_db),current_user:schemas.User=Depends(get_current_user)):
     return blog.get_all(db)


#FOR CREATING AN ENTRY
@router.post('/',status_code=status.HTTP_201_CREATED)
def create(request:schemas.Blog,db:Session=Depends(database.get_db),current_user:schemas.User=Depends(get_current_user)):
    return blog.create(request,db)

#FOR PARTICULAR ID
@router.get('/{id}',status_code=200,response_model=schemas.ShowBlog)
def show(id,db:Session=Depends(database.get_db),current_user:schemas.User=Depends(get_current_user)):
    return blog.show(id,db)


#FOR UPDATING
@router.put('/{id}',status_code=status.HTTP_202_ACCEPTED)
def update(id,request:schemas.Blog,db:Session=Depends(database.get_db),current_user:schemas.User=Depends(get_current_user)):
    return blog.update(id,request,db)



#FOR DELETING
@router.delete('/{id}',status_code=status.HTTP_204_NO_CONTENT)
def destroy(id,db:Session=Depends(database.get_db),current_user:schemas.User=Depends(get_current_user)):
    return blog.destroy(id,db)
   





