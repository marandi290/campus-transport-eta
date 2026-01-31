from fastapi import FastAPI
from app.api import routes, staff

app = FastAPI(title="Campus Transport ETA Service")

app.include_router(staff.router, prefix="/staff", tags=["Staff"])
app.include_router(routes.router, prefix="/routes", tags=["Users"])
