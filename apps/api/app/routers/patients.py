from typing import Literal

from fastapi import APIRouter
from pydantic import BaseModel, Field

router = APIRouter()


class PatientCreate(BaseModel):
    given_name: str = Field(..., examples=["Maria"])
    family_name: str = Field(..., examples=["Souza"])
    birth_date: str | None = Field(default=None, examples=["1985-04-12"])
    sex: Literal["female", "male", "other", "unknown"] = "unknown"
    consent_for_research: bool = False


class PatientSummary(BaseModel):
    platform_patient_id: str
    display_name: str
    fhir_resource_type: str = "Patient"
    openmrs_sync_status: Literal["pending", "synced", "failed"] = "pending"
    research_eligible: bool = False


@router.post("", response_model=PatientSummary, status_code=201)
def create_patient(payload: PatientCreate) -> PatientSummary:
    """Create a platform patient record and prepare downstream synchronization.

    This MVP route intentionally returns a deterministic mock response. The next
    implementation step is to persist the registry row, publish patient.created,
    and synchronize with OpenMRS through a dedicated adapter.
    """
    display_name = f"{payload.given_name} {payload.family_name}".strip()
    slug = display_name.lower().replace(" ", "-")
    return PatientSummary(
        platform_patient_id=f"pt-{slug}",
        display_name=display_name,
        research_eligible=payload.consent_for_research,
    )


@router.get("/{platform_patient_id}", response_model=PatientSummary)
def get_patient(platform_patient_id: str) -> PatientSummary:
    return PatientSummary(
        platform_patient_id=platform_patient_id,
        display_name="Example Patient",
        openmrs_sync_status="pending",
    )
