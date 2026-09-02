import streamlit as st
import pandas as pd
import plotly.express as px

# Configuração da Página
st.set_page_config(
    page_title="Dashboard de Oportunidades | PCT Guamá",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ---------------------------------------------------------
# BASE DE DADOS DO POLO PCT GUAMÁ / ECOSSISTEMA NORTE
# ---------------------------------------------------------
@st.cache_data
def carregar_dados():
    dados = [
        {"Empresa": "Inteceleri", "Setor": "EdTech & VR", "Modelo": "B2G / B2B", "Maturidade": "Tração / Escala", "Gargalo_Principal": "Conectividade instável e hardware mobile modesto", "Foco_Solucao": "Educação Imersiva & Matemática Básica"},
        {"Empresa": "Manioca", "Setor": "Bioeconomia & Alimentos", "Modelo": "B2B / B2C", "Maturidade": "Escala", "Gargalo_Principal": "Rastreabilidade de cadeia extrativista remota", "Foco_Solucao": "Ingredientes da sociobiodiversidade amazônica"},
        {"Empresa": "Pecege Amazônia", "Setor": "EdTech & Treinamento", "Modelo": "B2B / B2G", "Maturidade": "Validação", "Gargalo_Principal": "Evasão de cursos EAD por instabilidade de rede", "Foco_Solucao": "Capacitação profissional e extensão"},
        {"Empresa": "Sallusmed", "Setor": "HealthTech", "Modelo": "B2G", "Maturidade": "Operação", "Gargalo_Principal": "Prontuários eletrônicos fragmentados em postos isolados", "Foco_Solucao": "Gestão de Atenção Primária à Saúde (APS)"},
        {"Empresa": "NavegAM", "Setor": "LogTech Fluvial", "Modelo": "B2B / Marketplace", "Maturidade": "Tração", "Gargalo_Principal": "Telemetria e cálculo de rotas fluviais sem 4G", "Foco_Solucao": "Passagens e fretes de barcos na Amazônia"},
        {"Empresa": "Amazônia Smart Wood", "Setor": "Geotecnologia & Madeira", "Modelo": "B2B", "Maturidade": "Operação", "Gargalo_Principal": "Volume de dados brutos de LiDAR e satélites", "Foco_Solucao": "Rastreabilidade de madeira e inventário florestal"},
        {"Empresa": "Biobureau Amazônia", "Setor": "Biotecnologia", "Modelo": "B2B / P&D", "Maturidade": "Validação", "Gargalo_Principal": "Processamento bioinformático de genomas da floresta", "Foco_Solucao": "Biotecnologia molecular e catálogo genético"},
        {"Empresa": "IdDX Biotecnologia", "Setor": "HealthTech", "Modelo": "B2B / B2G", "Maturidade": "Operação", "Gargalo_Principal": "Integração de testes diagnósticos rápidos a hospitais", "Foco_Solucao": "Diagnósticos moleculares para doenças tropicais"},
        {"Empresa": "Sensix Norte", "Setor": "AgroTech", "Modelo": "B2B (SaaS)", "Maturidade": "Tração", "Gargalo_Principal": "Upload de ortomosaicos e mapas de drones no campo", "Foco_Solucao": "Fertilidade de solo e análise de lavouras"},
        {"Empresa": "Tucum Tech", "Setor": "Bioeconomia & Artesanato", "Modelo": "Marketplace", "Maturidade": "Tração", "Gargalo_Principal": "Logística reversa e inclusão financeira de ribeirinhos", "Foco_Solucao": "Comércio digital para povos originários"},
        {"Empresa": "Belém GeoSolutions", "Setor": "Geotecnologia & Madeira", "Modelo": "B2G / B2B", "Maturidade": "Operação", "Gargalo_Principal": "Latência no processamento de imagens de satélite radar", "Foco_Solucao": "Monitoramento de desmatamento e CAR"},
        {"Empresa": "Açaí DataTrack", "Setor": "AgroTech", "Modelo": "B2B", "Maturidade": "Validação", "Gargalo_Principal": "Sensores IoT de temperatura com bateria em transporte fluvial", "Foco_Solucao": "Cadeia de frio e qualidade do fruto do açaí"},
        {"Empresa": "GovTech Belém Sistemas", "Setor": "GovTech", "Modelo": "B2G", "Maturidade": "Tração", "Gargalo_Principal": "Sistemas municipais legados sem APIs padronizadas", "Foco_Solucao": "Arrecadação e processos administrativos municipais"},
        {"Empresa": "LearnAmazon", "Setor": "EdTech & VR", "Modelo": "B2B / B2G", "Maturidade": "Ideação / Validação", "Gargalo_Principal": "Renderização 3D em chromebooks e tablets escolares", "Foco_Solucao": "Museus virtuais e fauna amazônica interativa"},
        {"Empresa": "FitoTech Farma", "Setor": "Biotecnologia", "Modelo": "B2B", "Maturidade": "Operação", "Gargalo_Principal": "Controle de qualidade de óleos vegetais em campo", "Foco_Solucao": "Fitocosméticos e bioativos farmacêuticos"},
        {"Empresa": "Fluvial Express", "Setor": "LogTech Fluvial", "Modelo": "B2B", "Maturidade": "Operação", "Gargalo_Principal": "Conflito de reservas durante janelas sem conectividade", "Foco_Solucao": "Despacho e desembaraço de encomendas ribeirinhas"},
        {"Empresa": "Guamá Waste Management", "Setor": "GovTech", "Modelo": "B2G / B2B", "Maturidade": "Validação", "Gargalo_Principal": "Roteamento dinâmico de frotas com baixa sinalização GPS", "Foco_Solucao": "Otimização de rotas de coleta seletiva urbana"},
        {"Empresa": "MapForest Tech", "Setor": "Geotecnologia & Madeira", "Modelo": "B2B (SaaS)", "Maturidade": "Tração", "Gargalo_Principal": "Custo de armazenamento em nuvem de nuvens de pontos 3D", "Foco_Solucao": "Cubagem volumétrica de árvores em pé"},
        {"Empresa": "BioAmazon Óleos", "Setor": "Bioeconomia & Alimentos", "Modelo": "B2B", "Maturidade": "Escala", "Gargalo_Principal": "Padronização de lote com produtores cooperados", "Foco_Solucao": "Manteigas e óleos de andiroba, murumuru e cupuaçu"},
        {"Empresa": "Telemed Amazônia", "Setor": "HealthTech", "Modelo": "B2G / B2B", "Maturidade": "Tração", "Gargalo_Principal": "Streaming de vídeo/voz em conexões de baixíssima largura de banda", "Foco_Solucao": "Consultas remotas para comunidades isoladas"},
        {"Empresa": "CampoConectado", "Setor": "AgroTech", "Modelo": "B2B", "Maturidade": "Validação", "Gargalo_Principal": "Alcance de antenas LoRa em vegetação densa", "Foco_Solucao": "Estações agroclimáticas de baixo custo"},
        {"Empresa": "EducaTapajós", "Setor": "EdTech & VR", "Modelo": "B2G", "Maturidade": "Ideação / Validação", "Gargalo_Principal": "Falta de infraestrutura elétrica contínua para recarga de aparelhos", "Foco_Solucao": "Alfabetização bilíngue em línguas indígenas"},
        {"Empresa": "CidadesInteligentes Norte", "Setor": "GovTech", "Modelo": "B2G", "Maturidade": "Operação", "Gargalo_Principal": "Falta de capacitação dos operadores do serviço público", "Foco_Solucao": "Portais de transparência e protocolo eletrônico"},
        {"Empresa": "AmazonLog Cargas", "Setor": "LogTech Fluvial", "Modelo": "B2B", "Maturidade": "Tração", "Gargalo_Principal": "Variação severa de nível de rios afetando previsões de ETA", "Foco_Solucao": "Gestão de atracação portuária de balsas"}
    ]
    return pd.DataFrame(dados)

df = carregar_dados()

# ---------------------------------------------------------
# SIDEBAR
# ---------------------------------------------------------
st.sidebar.title("🌲 PCT Guamá")
st.sidebar.markdown("**Hub de Inovação Belém-PA**")
st.sidebar.markdown("---")

st.sidebar.subheader("Filtros de Pesquisa")
setores_disponiveis = ["Todos"] + sorted(df["Setor"].unique().tolist())
setor_selecionado = st.sidebar.selectbox("Filtrar por Domínio / Setor:", setores_disponiveis)

modelos_disponiveis = ["Todos"] + sorted(df["Modelo"].unique().tolist())
modelo_selecionado = st.sidebar.selectbox("Filtrar por Modelo de Negócio:", modelos_disponiveis)

# Aplicar filtros
df_filtrado = df.copy()
if setor_selecionado != "Todos":
    df_filtrado = df_filtrado[df_filtrado["Setor"] == setor_selecionado]
if modelo_selecionado != "Todos":
    df_filtrado = df_filtrado[df_filtrado["Modelo"] == modelo_selecionado]

st.sidebar.markdown("---")
st.sidebar.caption("ADS IFRO Calama | Tópicos Especiais")

# ---------------------------------------------------------
# CABEÇALHO
# ---------------------------------------------------------
st.title("📊 Dashboard de Oportunidades Tecnológicas")
st.markdown("**Diagnóstico Setorial do Polo PCT Guamá e Proposição de Arquitetura de Referência**")

# Métricas
kpi1, kpi2, kpi3, kpi4 = st.columns(4)
kpi1.metric("Startups Filtradas", len(df_filtrado))
kpi2.metric("Setores Presentes", df_filtrado["Setor"].nunique())
kpi3.metric("Soluções B2G / Gov", len(df_filtrado[df_filtrado["Modelo"].str.contains("B2G")]))
kpi4.metric("Estudo Central", "Inteceleri")

st.markdown("---")

# ---------------------------------------------------------
# ABAS
# ---------------------------------------------------------
tab1, tab2, tab3 = st.tabs(["📈 Mapeamento Estatístico", "🔍 Análise de Similares", "🏗️ Arquitetura Proposta"])

with tab1:
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("### Distribuição por Domínio / Setor")
        setor_counts = df_filtrado["Setor"].value_counts().reset_index()
        setor_counts.columns = ["Setor", "Quantidade"]
        fig_pizza = px.pie(setor_counts, values="Quantidade", names="Setor", hole=0.4)
        st.plotly_chart(fig_pizza)
        
    with col2:
        st.markdown("### Distribuição por Modelo de Negócio")
        modelo_counts = df_filtrado["Modelo"].value_counts().reset_index()
        modelo_counts.columns = ["Modelo", "Quantidade"]
        fig_barra = px.bar(modelo_counts, x="Modelo", y="Quantidade", color="Modelo")
        fig_barra.update_layout(showlegend=False)
        st.plotly_chart(fig_barra)

    st.markdown("### Maturidade das Soluções no Ecossistema")
    mat_counts = df_filtrado["Maturidade"].value_counts().reset_index()
    mat_counts.columns = ["Maturidade", "Quantidade"]
    fig_mat = px.bar(mat_counts, x="Quantidade", y="Maturidade", orientation="h", color="Maturidade")
    fig_mat.update_layout(showlegend=False)
    st.plotly_chart(fig_mat)

with tab2:
    st.markdown("### Catálogo de Empresas e Gargalos Operacionais Identificados")
    st.dataframe(df_filtrado[["Empresa", "Setor", "Modelo", "Gargalo_Principal", "Foco_Solucao"]])

    st.markdown("---")
    st.markdown("### Casos de EdTech & Tecnologias Imersivas")
    edtech_df = df[df["Setor"] == "EdTech & VR"]
    for _, row in edtech_df.iterrows():
        st.info(f"**{row['Empresa']}** — {row['Foco_Solucao']}\n\n*Gargalo Operacional:* {row['Gargalo_Principal']}")

with tab3:
    st.markdown("### Stack de Referência Proposta (Caso Inteceleri)")
    st.markdown("Solução focada em baixo custo, tecnologias consagradas de mercado e operação em áreas com conectividade precária.")

    stack_dados = {
        "Camada": ["Cliente Mobile", "Hospedagem & Storage", "Back-End API", "Processamento Assíncrono", "Banco de Dados"],
        "Tecnologia": ["Flutter + SQLite", "Firebase Storage + CDN", "Node.js (Express)", "Redis (BullMQ)", "PostgreSQL"],
        "Justificativa": [
            "Execução nativa leve e persistência local obrigatória (Offline-First).",
            "Entrega de assets 3D e texturas otimizadas sem custo de servidor próprio.",
            "API REST simples, leve e com menor consumo de memória computacional.",
            "Enfileiramento para amortecer picos de sincronização no final dos turnos escolares.",
            "Integridade transacional para notas, matrículas e turmas escolares."
        ]
    }
    st.table(pd.DataFrame(stack_dados))

    st.markdown("### Fluxo de Comunicação dos Dados")
    st.code("""
[ App Aluno (Flutter) ]
       │
       ▼ (1. Grava no banco local SQLite - Offline-First)
[ SQLite Local ]
       │
       ▼ (2. Detecta sinal de internet e envia lote JSON)
[ API Node.js Express ]
       │
       ├──► (3. Envia lote para fila sem travar resposta HTTP 202) ──► [ Fila Redis ]
       │                                                                  │
       │                                                                  ▼
       ▼                                                          [ Worker em Background ]
[ Firebase CDN ]                                                          │
 (Entrega pacotes 3D cacheados)                                           ▼
                                                                  [ PostgreSQL ]
                                                            (Notas e relatórios consolidados)
    """, language="text")