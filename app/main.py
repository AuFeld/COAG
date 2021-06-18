from fastapi import FastAPI
from app.routes.company_routes import GrowjoAPI as GrowjoAPIRouter
#from app.oauth import OAuth as OAuthRouter
from mangum import Mangum

tags_metadata = [
    {
        "name": "Growjo",
        "description": "Router for Growjo data",
        "externalDocs": {
            "description": "Growjo URL",
            "url": "https://wwww.growjo.com/",
        },
    },
        {
            "name": "Root",
            "description": "Base API",
        },
]

app = FastAPI(
    openapi_tags=tags_metadata,
    title="COAG",
    description="An application for career opportunities and growth"
)
# router for growjo data
app.include_router(GrowjoAPIRouter, tags=["Growjo"], prefix="/growjo")

# router for oauth
#app.include_router(OAuthRouter)

@app.get("/", tags=["Root"])
async def root():
    return {"message": "Welcome to COAG!"}


handler = Mangum(app)