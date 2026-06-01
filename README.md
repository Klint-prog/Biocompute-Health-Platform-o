# Biocompute Health Platform

Composable open-source health and research platform integrating clinical records, laboratory workflows and translational research.

## Vision

Biocompute Health Platform is designed as a modern user-facing layer over specialized open-source engines:

- OpenMRS for clinical records and encounters.
- OpenELIS Global for laboratory workflows.
- LabKey Server for research datasets and longitudinal studies.
- Keycloak for identity and role-based access control.
- PostgreSQL for the platform registry and operational metadata.
- MinIO for documents, consent forms, reports and scientific files.
- Redis/RabbitMQ-ready event-driven integration.

The platform does not try to replace these systems. It provides a simple portal, a central API and integration contracts so healthcare, laboratory and research teams can work through a unified experience.

## Initial MVP Scope

This repository currently contains the first scaffold for the platform:

- Architecture documentation.
- Docker Compose development environment.
- Backend API scaffold using FastAPI.
- Frontend portal scaffold using Next.js.
- FHIR-oriented integration contracts.
- Security and LGPD-oriented design notes.
- GitHub Actions CI workflow.

## Repository Structure

```text
apps/
  api/       FastAPI backend gateway and integration service
  web/       Next.js frontend portal
infra/
  docker/    Development compose stack and service configuration
docs/        Architecture, roadmap, security and integration documents
.github/     CI workflows
```

## Quick Start

```bash
cp .env.example .env
docker compose -f infra/docker/docker-compose.yml up --build
```

Services planned for local development:

- Web portal: http://localhost:3000
- API gateway: http://localhost:8000
- API docs: http://localhost:8000/docs
- Keycloak: http://localhost:8080
- MinIO console: http://localhost:9001

## License

AGPL-3.0-or-later.
