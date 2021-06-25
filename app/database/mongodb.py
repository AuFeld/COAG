import os 
from dotenv import load_dotenv
from motor.motor_asyncio import AsyncIOMotorClient

'''
parameters for connecting to MongoDB Compass (local)
'''

# load params from dotenv
load_dotenv()
MONGODB_URI = os.environ.get('mongodb_uri')

# connect to MongoDB cluster
conn = AsyncIOMotorClient(MONGODB_URI)

'''
parameters for connecting to MongoDB Atlas (cloud)
'''

# connect to Atlas
atlas_uri = os.environ.get('ATLAS_URI')
client = AsyncIOMotorClient(atlas_uri, serverSelectionTimeoutMS=5000)

# identify db in atlas
db = client.COAG

# identify collection vars in the db
growjo_collection = db.Growjo1
indeed_collection = db.indeed_data
linkedin_collection = db.linkedin_data

# conn to data lake

mongo_data_lake = os.environ.get("mongo_data_lake")