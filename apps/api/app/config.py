from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    app_name: str = "Biocompute Health Platform"
    app_env: str = "development"
    openmrs_base_url: str = "http://openmrs:8080/openmrs"
    openelis_base_url: str = "http://openelis:8080"
    labkey_base_url: str = "http://labkey:8080/labkey"

    model_config = SettingsConfigDict(env_file=".env", extra="ignore")


settings = Settings()
