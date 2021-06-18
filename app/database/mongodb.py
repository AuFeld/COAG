import os 
from dotenv import load_dotenv
import motor.motor_asyncio

"""
Parameters for Connecting to MongoDB
"""

# load params from dotenv
load_dotenv()
MONGODB_URI = os.environ.get('mongodb_uri')

# connect to MongoDB cluster
conn = motor.motor_asyncio.AsyncIOMotorClient(MONGODB_URI)

# identify db in the cluster
db = conn.COAG

# identify collection in the db
growjo_collection = db.Growjo1
indeed_collection = db.indeed_data
linkedin_collection = db.linkedin_data