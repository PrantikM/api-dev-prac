from jose import JWTError, jwt
from datetime import datetime,timedelta


#SECRET_KEY
#Algorithm
#Expiration time

SECRET_KEY = "iwye8927837qw3ted87ut82e0972qye892e0293e89732e82ye78t37ed"
Algorithm = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30


def create_acces_token(data:dict):
    to_encode = data.copy()
    expire = datetime.now() + timedelta(minutes = ACCESS_TOKEN_EXPIRE_MINUTES)

    to_encode.update({"exp": expire})

    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm = Algorithm)

    return encoded_jwt
    