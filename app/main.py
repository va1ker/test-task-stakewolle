from fastapi import FastAPI
from app import core, api
from app.core.config import config
import uvicorn


app = FastAPI()

app.include_router(api.api_v1_router)

if __name__ == "__main__":
    uvicorn.run(
        host="0.0.0.0",
        app="core.server:app",
        port=7777,
        reload=True if config.ENVIRONMENT != "production" else False,
        workers=1,
    )
