export const metadata = {
  title: "Biocompute Health Platform",
  description: "Composable open-source platform for clinical records, laboratory workflows and research.",
};

export default function RootLayout({ children }: { children: React.ReactNode }) {
  return (
    <html lang="pt-BR">
      <body>{children}</body>
    </html>
  );
}
