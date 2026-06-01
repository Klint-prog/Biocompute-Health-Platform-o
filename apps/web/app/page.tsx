const cards = [
  {
    title: "Pacientes",
    description: "Cadastro longitudinal com vínculo futuro ao OpenMRS e recursos FHIR Patient.",
  },
  {
    title: "Laboratório",
    description: "Solicitações, amostras, resultados e laudos integrados ao OpenELIS Global.",
  },
  {
    title: "Pesquisa",
    description: "Coortes pseudonimizadas, consentimentos e datasets preparados para LabKey.",
  },
  {
    title: "Governança",
    description: "LGPD, auditoria, RBAC, consentimento e separação entre assistência e pesquisa.",
  },
];

export default function Home() {
  return (
    <main style={{ minHeight: "100vh", padding: "48px", fontFamily: "Arial, sans-serif" }}>
      <section style={{ maxWidth: "1120px", margin: "0 auto" }}>
        <p style={{ textTransform: "uppercase", letterSpacing: "0.12em", color: "#2563eb", fontWeight: 700 }}>
          Biocompute Health Platform
        </p>
        <h1 style={{ fontSize: "48px", lineHeight: 1.05, margin: "16px 0" }}>
          Plataforma moderna para saúde, laboratório e pesquisa translacional.
        </h1>
        <p style={{ fontSize: "20px", color: "#475569", maxWidth: "760px" }}>
          Um portal único sobre motores open source especializados: OpenMRS, OpenELIS, LabKey,
          Keycloak, PostgreSQL, MinIO e APIs orientadas a FHIR.
        </p>

        <div style={{ display: "grid", gridTemplateColumns: "repeat(auto-fit, minmax(220px, 1fr))", gap: "20px", marginTop: "40px" }}>
          {cards.map((card) => (
            <article key={card.title} style={{ border: "1px solid #e2e8f0", borderRadius: "20px", padding: "24px", boxShadow: "0 10px 30px rgba(15, 23, 42, 0.06)" }}>
              <h2 style={{ margin: 0, fontSize: "22px" }}>{card.title}</h2>
              <p style={{ color: "#475569", lineHeight: 1.6 }}>{card.description}</p>
            </article>
          ))}
        </div>
      </section>
    </main>
  );
}
