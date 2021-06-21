# need to refactor code != indeed libray
from app.database.crud import retrieve_companies
from fastapi import APIRouter, Body
import json
# from app.database.crud import add_indeed_data
from app.models.indeed_model import (
    ErrorResponseModel, 
    ResponseModel,
    IndeedModel,
)


Indeed = APIRouter()

client = IndeedClient(publisher= 'YOUR_PUBLISHER_NUMBER')

# define search and params
params = {
    'pushlisher': '',
    'userip': '2601:581:4300:b4c0:3f1:4095:11b9:527f',
    'useragent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:89.0) Gecko/20100101 Firefox/89.0',    
    'jobkeys': '',
    'v': '2',
    'format': 'json',
    'q': 'Data Engineer',
    'employer': str(retrieve_companies), 
    'jt': 'fulltime',
    'limit': '25',
    'filter': '1', 
    'fromage': '14',
}

search_response = client.search(**params)

# retrieve jobs
indeed_response = client.jobs(jobkeys = ("job_key1", "job_key2"))
indeed_response = json.load(indeed_response)

