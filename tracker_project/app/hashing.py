from passlib.context import CryptContext

pwd_cxt=CryptContext(schemes=['bcrypt'],deprecated="auto")

class Hash():
    def bcrypt(password:str):
        hashed_pass=pwd_cxt.hash(password)

        return hashed_pass
    
    def verify(hashed_password,plain_password):
        return pwd_cxt.verify(plain_password,hashed_password)
