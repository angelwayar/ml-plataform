import uvicorn
from fastapi import FastAPI

from api.user.routes.user_routes import router
from app.api.pixToPix.routes.pix_to_pix_routes import router_pix_to_pix
from core.database.database import engine
from core.models.base_model import BaseEntity

# BaseEntity.metadata.create_all(bind=engine)

app = FastAPI()
app.include_router(router)
app.include_router(router_pix_to_pix)


@app.get("/")
async def root():
    return {"message": "Hello World"}

# This is for debuging de project
if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
