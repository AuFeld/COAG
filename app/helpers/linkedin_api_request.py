import string
import requests
import random
from dotenv import load_dotenv
import os

'''
load dotenv to import secrets from .env file
'''

load_dotenv()

'''
define your parameters
'''

CLIENT_ID = os.environ.get('client_id')
CLIENT_SECRET = os.environ.get('client_secret')
REDIRECT_URI = os.environ.get('redirect_uri')
AUTH_CODE = os.environ.get('auth_code')
ACCESS_TOKEN_URL = 'https://www.linkedin.com/oauth/v2/accessToken'

'''
generate a random string to protect against CSRF (cross-site request forgery)
'''

letters = string.ascii_lowercase
CSRF_TOKEN = ''.join(random.choice(letters) for i in range(24))

'''
request authentication URL
'''

auth_params = {
    'response_type': 'code',
    'client_id': CLIENT_ID,
    'redirect_uri': REDIRECT_URI,
    'state': CSRF_TOKEN,
    'scope': 'r_liteprofile'
}

html = requests.get(
    "https://www.linkedin.com/oauth/v2/authorization", 
    params = auth_params
)

'''
to aquire auth code:
1. uncomment indicated line below
2. run py file in your terminal
3. follow link returned in your terminal to your browser 
4. from your browser, record the authorization code. eg, code=AQQ...

:return: linkedin authorization code
'''

# uncomment line below and run py file in terminal
#print(html.url)

'''
run py file in terminal

:return: your linkedin access token
'''

qd = {
    'grant_type': 'authorization_code',
    'code': AUTH_CODE,
    'redirect_uri': REDIRECT_URI,
    'client_id': CLIENT_ID,
    'client_secret': CLIENT_SECRET
    }

response = requests.post(ACCESS_TOKEN_URL, data=qd, timeout=60)

response = response.json()

access_token = response['access_token']

print ("Access Token:", access_token)
print ("Expires in (seconds):", response['expires_in'])