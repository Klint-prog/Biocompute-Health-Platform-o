# Security and LGPD Notes

Health data must be treated as sensitive personal data. The platform should be designed with privacy, auditability and least privilege from the first phase.

## Initial Controls

- Use HTTPS in every deployed environment.
- Centralize identity in Keycloak.
- Apply role-based access control.
- Record audit logs for sensitive operations.
- Separate clinical care data from research data.
- Validate consent before research use.
- Pseudonymize research exports.
- Encrypt backups and object storage.
- Avoid storing unnecessary identifiers in analytics datasets.

## Roles

Initial roles:

- administrator
- physician
- nurse
- laboratory_technician
- researcher
- auditor
- patient

## Audit Events

Initial audited operations:

- patient.create
- patient.read
- consent.grant
- consent.revoke
- exam.request
- specimen.collect
- result.publish
- research.export

## Research Boundary

Research datasets must not receive direct personal identifiers by default. The platform should create research subject identifiers and keep the mapping in a restricted registry.
