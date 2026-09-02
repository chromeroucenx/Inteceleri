from flask import Flask, render_template_string

app = Flask(__name__)

dados = [
    {
        "Empresa": "Inteceleri",
        "Setor": "EdTech & VR",
        "Ponto_Forte": "Pioneirismo em VR sustentável regional (MiritiBoard) e gamificação de matemática básica.",
        "Tecnologia_Destaque": "Realidade Virtual + Hardware Ecológico",
        "Oportunidade_Inteceleri": "Empresa central sob proposição de melhorias arquiteturais e estratégicas."
    },
    {
        "Empresa": "NavegAM",
        "Setor": "LogTech Fluvial",
        "Ponto_Forte": "Capacidade de validar e processar dados em áreas isoladas, sincronizando lotes em pontos locais de atracação.",
        "Tecnologia_Destaque": "Offline-First & Sincronização em Borda Local (Edge)",
        "Oportunidade_Inteceleri": "Edge Sync Escolar: Sincronizar o progresso dos alunos no computador da secretaria via rede local sem consumir pacote de dados móveis do estudante."
    },
    {
        "Empresa": "Sallusmed",
        "Setor": "HealthTech",
        "Ponto_Forte": "Interoperabilidade total com bancos de dados federais (e-SUS), gerando indicadores oficiais de impacto municipal.",
        "Tecnologia_Destaque": "APIs Padronizadas & Auditoria de Indicadores Públicos",
        "Oportunidade_Inteceleri": "Módulo SEDUC / IDEB: Integrar as notas de matemática diretamente aos sistemas das secretarias de educação, blindando o contrato de renovação B2G."
    },
    {
        "Empresa": "Amazônia Smart Wood",
        "Setor": "Geotecnologia",
        "Ponto_Forte": "Algoritmos eficientes para compactação e streaming de dados volumosos (LiDAR) e monetização por assinatura contínua.",
        "Tecnologia_Destaque": "Otimização de Geometria 3D & Modelo SaaS Puro",
        "Oportunidade_Inteceleri": "Pipeline 3D Compacto (Draco/glTF): Reduzir o peso gráfico dos apps para celulares de 2GB de RAM e vender o software de forma independente do óculos."
    },
    {
        "Empresa": "Manioca Brasil",
        "Setor": "Bioeconomia",
        "Ponto_Forte": "Forte presença de marca em canais B2C nacionais e parcerias corporativas no atacado privado.",
        "Tecnologia_Destaque": "Distribuição Multicanal & Varejo Direto",
        "Oportunidade_Inteceleri": "Desverticalização B2C: Comercializar licenças diretamente a famílias e fechar acordos white-label com grandes editoras didáticas privadas."
    },
    {
        "Empresa": "Pecege Amazônia",
        "Setor": "EdTech & Extensão",
        "Ponto_Forte": "Trilhas formativas estruturadas em micro-conteúdos assíncronos que não exigem streaming pesado.",
        "Tecnologia_Destaque": "Arquitetura LMS Modular e Leve",
        "Oportunidade_Inteceleri": "Micro-Aulas Gamificadas: Baixar pequenas fases de matemática sob demanda (Lazy Loading), evitando sobrecarga de armazenamento no celular."
    },
    {
        "Empresa": "IdDX Biotecnologia",
        "Setor": "Biotecnologia",
        "Ponto_Forte": "Alto rigor de conformidade e validação junto a órgãos regulatórios públicos nacionais.",
        "Tecnologia_Destaque": "Certificação e Padronização Técnica Oficial",
        "Oportunidade_Inteceleri": "Selo de Tecnologia Educacional MEC: Certificar os módulos imersivos formalmente para facilitar adesão por adesão de atas do FNDE."
    }
]

HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <title>Dashboard de Benchmarking e Oportunidades | PCT Guamá</title>
    <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
    <style>
        :root {
            --primary: #0284c7;
            --bg: #f8fafc;
            --card-bg: #ffffff;
            --text-main: #0f172a;
            --text-sub: #475569;
            --border: #e2e8f0;
            --accent: #10b981;
            --accent-soft: #ecfdf5;
        }
        body { font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif; background: var(--bg); color: var(--text-main); margin: 0; padding: 24px; }
        .container { max-width: 1240px; margin: 0 auto; }
        .header { background: var(--card-bg); padding: 24px; border-radius: 12px; border: 1px solid var(--border); box-shadow: 0 1px 3px rgba(0,0,0,0.05); margin-bottom: 24px; }
        .kpis { display: grid; grid-template-columns: repeat(4, 1fr); gap: 16px; margin-bottom: 24px; }
        .kpi-card { background: var(--card-bg); padding: 20px; border-radius: 12px; border: 1px solid var(--border); text-align: center; }
        .kpi-card h3 { margin: 0; font-size: 32px; color: var(--primary); font-weight: 700; }
        .kpi-card p { margin: 6px 0 0 0; color: var(--text-sub); font-size: 14px; font-weight: 500; }
        .grid-charts { display: grid; grid-template-columns: 1fr 1fr; gap: 24px; margin-bottom: 24px; }
        .chart-card { background: var(--card-bg); padding: 20px; border-radius: 12px; border: 1px solid var(--border); }
        .section-title { font-size: 20px; font-weight: 700; margin: 32px 0 16px 0; color: var(--text-main); }
        table { width: 100%; border-collapse: collapse; background: var(--card-bg); border-radius: 12px; overflow: hidden; border: 1px solid var(--border); margin-bottom: 24px; }
        th, td { padding: 14px 16px; text-align: left; border-bottom: 1px solid var(--border); font-size: 14px; vertical-align: top; }
        th { background: #f1f5f9; color: #334155; font-weight: 600; }
        .badge { display: inline-block; padding: 4px 10px; border-radius: 6px; background: #e0f2fe; color: #0369a1; font-size: 12px; font-weight: 600; }
        .inteceleri-row { background: #f0fdf4; }
        .opportunity-box { background: var(--accent-soft); border-left: 4px solid var(--accent); padding: 10px 12px; border-radius: 4px; font-size: 13px; color: #065f46; font-weight: 500; line-height: 1.4; }
        .stack-section { background: #0f172a; color: #f8fafc; padding: 28px; border-radius: 12px; margin-top: 32px; }
        .stack-section h2 { color: #38bdf8; margin-top: 0; }
        .stack-table { background: #1e293b; border-color: #334155; }
        .stack-table th { background: #334155; color: #94a3b8; }
        .stack-table td { color: #e2e8f0; border-bottom-color: #334155; }
        pre { background: #020617; padding: 20px; border-radius: 8px; overflow-x: auto; color: #38bdf8; font-family: monospace; font-size: 13px; line-height: 1.5; }
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <h1 style="margin:0; font-size: 26px;">🎯 Benchmarking de Pontos Fortes e Oportunidades</h1>
            <p style="margin:8px 0 0 0; color:var(--text-sub);">Polo: PCT Guamá (Belém-PA) | Foco: Melhores Práticas Transferíveis para a Inteceleri Tecnologia</p>
        </div>

        <div class="kpis">
            <div class="kpi-card"><h3>6</h3><p>Práticas Inovadoras Identificadas</p></div>
            <div class="kpi-card"><h3>5</h3><p>Domínios de Engenharia</p></div>
            <div class="kpi-card"><h3>100%</h3><p>Foco em Soluções para a Inteceleri</p></div>
            <div class="kpi-card"><h3 style="color:var(--accent);">Inteceleri</h3><p>Beneficiária Direta da Análise</p></div>
        </div>

        <div class="grid-charts">
            <div class="chart-card">
                <h3 style="margin-top:0; font-size: 16px;">Áreas de Competência Identificadas no Polo</h3>
                <canvas id="setorChart"></canvas>
            </div>
            <div class="chart-card">
                <h3 style="margin-top:0; font-size: 16px;">Vetor de Oportunidades Geradas para a Inteceleri</h3>
                <canvas id="vetoresChart"></canvas>
            </div>
        </div>

        <div class="section-title">💡 Matriz de Transferência de Práticas Vencedoras</div>
        <table>
            <thead>
                <tr>
                    <th style="width: 14%;">Empresa</th>
                    <th style="width: 12%;">Setor</th>
                    <th style="width: 25%;">Ponto Forte Consolidado</th>
                    <th style="width: 18%;">Tecnologia / Prática Chave</th>
                    <th style="width: 31%;">Como a Inteceleri Pode Aproveitar</th>
                </tr>
            </thead>
            <tbody>
                {% for item in dados %}
                <tr class="{% if item.Empresa == 'Inteceleri' %}inteceleri-row{% endif %}">
                    <td>
                        <strong>{{ item.Empresa }}</strong>
                        {% if item.Empresa == 'Inteceleri' %}<span style="color:#16a34a; font-size: 11px; display:block;">(Empresa Foco)</span>{% endif %}
                    </td>
                    <td><span class="badge">{{ item.Setor }}</span></td>
                    <td>{{ item.Ponto_Forte }}</td>
                    <td><span style="font-weight:600; color:#0369a1;">{{ item.Tecnologia_Destaque }}</span></td>
                    <td><div class="opportunity-box">{{ item.Oportunidade_Inteceleri }}</div></td>
                </tr>
                {% endfor %}
            </tbody>
        </table>

        <div class="stack-section">
            <h2>🏗️ Stack Arquitetural Integrando as Melhores Práticas</h2>
            <p style="color:#94a3b8;">Consolidação técnica combinando resiliência offline (inspirada na NavegAM), dados leves (Amazônia Smart Wood) e auditoria relacional (Sallusmed).</p>

            <table class="stack-table">
                <tr>
                    <th>Camada</th>
                    <th>Tecnologia Selecionada</th>
                    <th>Valor Agregado ao Negócio da Inteceleri</th>
                </tr>
                <tr>
                    <td><strong>Cliente Mobile</strong></td>
                    <td><span style="color:#38bdf8;">Flutter + SQLite</span></td>
                    <td>Funciona 100% offline; o aluno não perde nenhuma atividade por oscilação de internet.</td>
                </tr>
                <tr>
                    <td><strong>Borda & Cache</strong></td>
                    <td><span style="color:#38bdf8;">Firebase Storage + CDN</span></td>
                    <td>Distribuição leve de pacotes 3D e texturas compactadas sem gargalo no servidor principal.</td>
                </tr>
                <tr>
                    <td><strong>Back-End API</strong></td>
                    <td><span style="color:#38bdf8;">Node.js (Express)</span></td>
                    <td>Recepção rápida e modular de requisições com baixo custo computacional.</td>
                </tr>
                <tr>
                    <td><strong>Processamento Assíncrono</strong></td>
                    <td><span style="color:#38bdf8;">Redis (BullMQ)</span></td>
                    <td>Enfileira os envios maciços de notas de final de turno sem indisponibilidade de serviço.</td>
                </tr>
                <tr>
                    <td><strong>Banco de Dados</strong></td>
                    <td><span style="color:#38bdf8;">PostgreSQL</span></td>
                    <td>Consolidação dos dados pedagógicos pronta para geração de relatórios oficiais para o IDEB e SEDUC.</td>
                </tr>
            </table>

            <h3 style="color:#38bdf8; margin-top:24px;">Fluxo Operacional Proposto</h3>
            <pre>
[ Aluno / Smartphone (2GB-3GB RAM) ]
       │
       ▼ (1. Registra progresso e notas localmente - Offline-First)
[ SQLite Local ]
       │
       ▼ (2. Conexão restabelecida ou Wi-Fi da secretaria detectado)
[ API Node.js (Express) ]
       │
       ├──► (3. Enfileira lote assíncrono com resposta HTTP 202) ──► [ Fila Redis (BullMQ) ]
       │                                                                   │
       │                                                                   ▼
       ▼                                                           [ Worker Assíncrono ]
[ Firebase CDN ]                                                           │
  (Assets 3D compactados via Draco)                                        ▼
                                                                  [ PostgreSQL Central ]
                                                            (Relatórios prontos para a SEDUC)
            </pre>
        </div>
    </div>

    <script>
        const ctx1 = document.getElementById('setorChart');
        new Chart(ctx1, {
            type: 'doughnut',
            data: {
                labels: ['EdTech & VR', 'LogTech Fluvial', 'HealthTech', 'Geotecnologia', 'Bioeconomia'],
                datasets: [{
                    data: [2, 1, 2, 1, 1],
                    backgroundColor: ['#0284c7', '#f59e0b', '#ef4444', '#8b5cf6', '#10b981']
                }]
            },
            options: { plugins: { legend: { position: 'bottom' } } }
        });

        const ctx2 = document.getElementById('vetoresChart');
        new Chart(ctx2, {
            type: 'bar',
            data: {
                labels: ['Sincronização Edge', 'Interoperabilidade B2G', 'Compressão 3D', 'Diversificação B2C', 'Modularização de Conteúdo'],
                datasets: [{
                    label: 'Impacto Estratégico',
                    data: [5, 5, 4, 4, 3],
                    backgroundColor: '#10b981'
                }]
            },
            options: { scales: { y: { beginAtZero: true, max: 5 } }, plugins: { legend: { display: false } } }
        });
    </script>
</body>
</html>
"""

@app.route("/")
def index():
    return render_template_string(HTML_TEMPLATE, dados=dados)

print("=" * 65, flush=True)
print(">>> SERVIDOR DE BENCHMARKING ATIVO!", flush=True)
print(">>> Acesse no seu navegador: http://127.0.0.1:5000", flush=True)
print("=" * 65, flush=True)

app.run(host="127.0.0.1", port=5000, debug=False)