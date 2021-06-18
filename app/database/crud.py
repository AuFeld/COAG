from bson.objectid import ObjectId
#from app.api.indeed import indeed_response
from app.database.mongodb import (
    growjo_collection, 
#    indeed_collection, 
#    linkedin_collection
)
from app.database.mongodb_helper import (
    growjo_helper,
#    indeed_helper,
#    linkedin_helper,    
)
"""
CRUD Operations
"""

# top10 fastest growing companies in the US vars 
filter={
    'country': {
        '$exists': True
    }, 
    'country': 'United States'
}
sort=list({
    'growjo_ranking': {
        '$exists': True
    }, 
    'growjo_ranking': 1
}.items())
limit=10

# retrieve top 10 fastest growing US companies in the database
async def retrieve_companies():
    companies = []
    async for entity in growjo_collection.find(
        filter=filter,
        sort=sort,
        limit=limit,
    ):
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

# add indeed jobs to the database
#async def add_indeed_data(indeed_data: dict) -> dict:
#    entity = await indeed_collection.insertMany(
#        [{'i': i} for i in range(len(indeed_response))]
#    )
#    indeed_data = await indeed_collection.find_one({"id": entity.inserted_id})
#    return indeed_helper(indeed_data)

# add linkedin jobs to the database
# async def add_linkedin_data(linkedin_data: dict) -> dict:
#    entity = await linkedin_collection.insertMany(
#        [{'i': i} for i in range(len(linkedin_response))]
#    )
#    linkedin_data = await linkedin_collection.find_one(
#        {"id": entity.inserted_id})
#    return linkedin_helper(linkedin_data)
    