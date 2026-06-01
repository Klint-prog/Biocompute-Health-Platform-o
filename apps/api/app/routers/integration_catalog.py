from fastapi import APIRouter
from pydantic import BaseModel

from app.config import settings

router = APIRouter()


class IntegrationEndpoint(BaseModel):
    name: str
    base_url: str
    role: str
    status: str = "configured"
    integration_pattern: str


@router.get("", response_model=list[IntegrationEndpoint])
def list_integrations() -> list[IntegrationEndpoint]:
    """Return the external engines configured behind the platform API."""
    return [
        IntegrationEndpoint(
            name="OpenMRS",
            base_url=settings.openmrs_base_url,
            role="clinical-records",
            integration_pattern="FHIR Patient, Encounter, Observation and Condition mapping",
        ),
        IntegrationEndpoint(
            name="OpenELIS Global",
            base_url=settings.openelis_base_url,
            role="laboratory-information-system",
            integration_pattern="Specimen, ServiceRequest, Observation and DiagnosticReport mapping",
        ),
        IntegrationEndpoint(
            name="LabKey Server",
            base_url=settings.labkey_base_url,
            role="research-data-platform",
            integration_pattern="pseudonymized cohorts, datasets and study exports",
        ),
    ]
