from fastapi import APIRouter

router = APIRouter()


@router.get("/healthz")
def healthz() -> dict[str, str]:
    """Liveness probe used by containers and CI smoke checks."""
    return {"status": "ok", "component": "api"}


@router.get("/readyz")
def readyz() -> dict[str, str]:
    """Readiness probe placeholder for future database and broker checks."""
    return {"status": "ready", "component": "api"}
