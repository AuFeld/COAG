import os 
from dotenv import load_dotenv
import motor.motor_asyncio
from bson.objectid import ObjectId

"""
Parameters for Connecting to MongoDB
"""
# load params from dotenv
load_dotenv()
MONGODB_URI = os.environ['mongodb_uri']

# connect to MongoDB cluster
conn = motor.motor_asyncio.AsyncIOMotorClient(MONGODB_URI)

# identify db in the cluster
db = conn.COAG

# identify collection in the db
growjo_collection = db.Growjo

"""
Helpers
"""

def growjo_helper(entity) -> dict:
    return {
        "_id": str(entity["_id"]),
        "company_name": str(entity["company_name"]),
        "url": str(entity["url"]), 
        "city": str(entity["city"]),
        "country": str(entity["country"]), 
        "employess": str(entity["employees"]),
        "linkedin_url": str(entity["linkedin_url"]),
        "founded": str(entity["founded"]), 
        "industry": str(entity["industry"]),
        "growjo_ranking": str(entity["growjo_ranking"]), 
        "previous_ranking": str(entity["previous_ranking"]), 
        "estimated_revenues": str(entity["estimated_revenues"]),
        "job_openings": str(entity["job_openings"]),
        "keywords": str(entity["keywords"]),
        "lead_investors": str(entity["lead_investors"]),
        "accelerator": str(entity["accelerator"]),
        "btype": str(entity["btype"]), 
        "valuation": str(entity["valuation"]), 
        "total_funding": str(entity["total_funding"]),
        "product_url": str(entity["product_url"]),
        "indeed_url": str(entity["indeed_url"]),
        "growth_percentage": str(entity["growth_percentage"]),
    }

"""
CRUD Operations
"""

# retrieve all companies in the database
async def retrieve_companies():
    companies = []
    async for entity in growjo_collection.find():
        companies.append(growjo_helper(entity))
    return companies

# add a new company into the database
async def add_company(company_data: dict) -> dict:
    entity = await growjo_collection.insert_one(company_data)
    new_company = await growjo_collection.find_one({"_id": entity.inserted_id})
    return growjo_helper(new_company)

# retrieve a company with a matching ID
async def retrieve_company(id: str) -> dict:
    entity = await growjo_collection.find_one({"_id": ObjectId(id)})
    if entity:
        return growjo_helper(entity)

# update a company with a matching ID
async def update_company(id: str, data: dict):
    # return false if any empty request body is sent
    if len(data) < 1:
        return False
    entity = await growjo_collection.find_one({"_id": ObjectId(id)})
    if entity: 
        updated_company = await growjo_collection.update_one(
                            {"_id": ObjectId(id)}, {"$set": data})
        if updated_company:
            return True
        return False

# delete a company from the database
async def delete_company(id: str):
    entity = await growjo_collection.find_one({"_id": ObjectId(id)})
    if entity: 
        await growjo_collection.delete_one({"_id": ObjectId(id)})
        return True


