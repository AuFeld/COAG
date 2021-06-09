from fastapi.encoders import jsonable_encoder
from fastapi import APIRouter, Body

from app.database.mongo_db import (
    add_company,
    delete_company,
    retrieve_company,
    retrieve_companies,
    update_company,
)

from app.models.company_model import (
    ErrorResponseModel,
    ResponseModel,
    GrowjoSchema,
    UpdateGrowjoModel,
)

GrowjoAPI = APIRouter()

@GrowjoAPI.post("/", response_description="Company data added into the database")
async def add_company_data(company: GrowjoSchema = Body(...)):
    company = jsonable_encoder(company)
    new_company = await add_company(company)
    return ResponseModel(new_company, "Company added successfully!")

@GrowjoAPI.get("/", response_description="Companies retrieved")
async def get_companies():
    companies = await retrieve_companies()
    if companies:
        return ResponseModel(companies, "Companies data retrieved successfully!")
    return ResponseModel(companies, "Empty list returned")

@GrowjoAPI.get("/{id}", response_description="Company data retrieved")
async def get_company_data(id):
    company = await retrieve_company(id)
    if company: 
        return ResponseModel(company, "Company data retrieved successfully")
    return ErrorResponseModel("An error occured.", 404, "Company doesn't exist.")

@GrowjoAPI.put("/{id}")
async def update_company_data(id: str, req: UpdateGrowjoModel = Body(...)):
    req = {k: v for k, v in req.dict().items() if v is not None}
    updated_company = await update_company(id, req)
    if updated_company: 
        return ResponseModel(
            "Company with ID: {} name update is successful".format(id),
            "Company name updated successfully",
        )
    return ErrorResponseModel(
        "An error occurred",
        404,
        "There was an error updating the company data.",
    )

@GrowjoAPI.delete("/{id}", 
    response_description="Company data deleted from the database")
async def delete_company_data(id: str):
    deleted_company = await delete_company(id)
    if deleted_company: 
        return ResponseModel(
            "Company with ID: {} removed".format(id), 
            "Company deleted successfully"
        )
    return ErrorResponseModel(
        "An error occurred", 404, 
        "Company with id {0} does not exist".format(id)
    )


