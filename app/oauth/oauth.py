'''
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from fastapi import Depends, APIRouter

OAuth = APIRouter()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl='token')

@OAuth.post('/token')
async def token(form_data: OAuth2PasswordRequestForm = Depends()):
    return {'access_token' : form_data.username + 'token'}

@OAuth.get('/')
async def index(token: str = Depends(oauth2_scheme)):
    return {'the_token' : token}
'''