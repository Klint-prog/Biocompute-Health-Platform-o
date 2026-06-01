from fastapi import FastAPI

from app.config import settings
from app.routers import health_status, integration_catalog, patients

app = FastAPI(
    title=settings.app_name,
    version="0.1.0",
    description="API gateway for clinical, laboratory and research integrations.",
)

app.include_router(health_status.router, tags=["health"])
app.include_router(patients.router, prefix="/v1/patients", tags=["patients"])
app.include_router(
    integration_catalog.router,
    prefix="/v1/integrations",
    tags=["integrations"],
)


@app.get("/")
def root() -> dict[str, str]:
    return {
        "name": settings.app_name,
        "environment": settings.app_env,
        "status": "running",
    }
