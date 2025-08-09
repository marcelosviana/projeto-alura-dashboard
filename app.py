import streamlit as st
import pandas as pd
import plotly.express as px

# --- Configuração da Página ---
# Define o título da página, o ícone e o layout para ocupar a largura inteira.
st.set_page_config(
    page_title="Dashboard de Salários na Área de Dados",
    page_icon="📊",
    layout="wide",
)

# --- CSS Customizado para o tema azul escuro ---
# Adiciona estilos personalizados para o tema azul escuro, alterando cores de fundo, texto e hover.
st.markdown("""
<style>
    /* Filtros selecionados na sidebar */
    .stMultiSelect [data-baseweb="select"] span[aria-selected="true"] {
        background-color: #1a3d5d !important;
        color: white !important;
    }
    
    /* Botões e controles ativos */
    .st-bb, .st-at, .st-ag {
        background-color: #1a3d5d !important;
    }
    
    /* Hover nos filtros */
    .stMultiSelect [data-baseweb="select"] span:hover {
        background-color: #2a4d6d !important;
    }
    
    /* Borda dos filtros quando focados */
    .stMultiSelect [data-baseweb="select"]:focus-within {
        border-color: #1a3d5d !important;
        box-shadow: 0 0 0 2px rgba(26, 61, 93, 0.2) !important;
    }
    
    /* Sliders */
    .stSlider .st-ae {
        background-color: #1a3d5d !important;
    }
    
    /* Checkbox selecionado */
    .stCheckbox [aria-checked="true"]+div {
        background: #1a3d5d url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='16' height='16' viewBox='0 0 24 24' fill='none' stroke='white' stroke-width='3' stroke-linecap='round' stroke-linejoin='round'%3E%3Cpolyline points='20 6 9 17 4 12'%3E%3C/polyline%3E%3C/svg%3E") no-repeat center !important;
        border-color: #1a3d5d !important;
    }
    
    /* Radio button selecionado */
    .stRadio [role="radiogroup"] [aria-checked="true"]+div {
        background-color: #1a3d5d !important;
        border-color: #1a3d5d !important;
    }
</style>
""", unsafe_allow_html=True)

# --- Carregamento dos dados ---
df = pd.read_csv("dados-imersao-final.csv")

# --- Barra Lateral (Filtros) ---
st.sidebar.header("🔍 Filtros")

# Filtro de Ano
anos_disponiveis = sorted(df['ano'].unique())
anos_selecionados = st.sidebar.multiselect("Ano", anos_disponiveis, default=anos_disponiveis)

# Filtro de Senioridade
senioridades_disponiveis = sorted(df['senioridade'].unique())
senioridades_selecionadas = st.sidebar.multiselect("Senioridade", senioridades_disponiveis, default=senioridades_disponiveis)

# Filtro por Tipo de Contrato
contratos_disponiveis = sorted(df['contrato'].unique())
contratos_selecionados = st.sidebar.multiselect("Tipo de Contrato", contratos_disponiveis, default=contratos_disponiveis)

# Filtro por Tamanho da Empresa
tamanhos_disponiveis = sorted(df['tamanho_empresa'].unique())
tamanhos_selecionados = st.sidebar.multiselect("Tamanho da Empresa", tamanhos_disponiveis, default=tamanhos_disponiveis)

# --- Filtragem do DataFrame ---
# O dataframe principal é filtrado com base nas seleções feitas na barra lateral.
df_filtrado = df[
    (df['ano'].isin(anos_selecionados)) &
    (df['senioridade'].isin(senioridades_selecionadas)) &
    (df['contrato'].isin(contratos_selecionados)) &
    (df['tamanho_empresa'].isin(tamanhos_selecionados))
]

# --- Conteúdo Principal ---
st.title("🎲 Dashboard de Análise de Salários na Área de Dados")
st.markdown("Explore os dados salariais na área de dados nos últimos anos. Utilize os filtros à esquerda para refinar sua análise.")

# --- Métricas Principais (KPIs) ---
st.subheader("Métricas gerais (Salário anual em USD)")

if not df_filtrado.empty:
    salario_medio = df_filtrado['usd'].mean()
    salario_maximo = df_filtrado['usd'].max()
    total_registros = df_filtrado.shape[0]
    cargo_mais_frequente = df_filtrado["cargo"].mode()[0]
else:
    salario_medio, salario_mediano, salario_maximo, total_registros, cargo_mais_comum = 0, 0, 0, ""

col1, col2, col3, col4 = st.columns(4)
col1.metric("Salário médio", f"${salario_medio:,.0f}")
col2.metric("Salário máximo", f"${salario_maximo:,.0f}")
col3.metric("Total de registros", f"{total_registros:,}")
col4.metric("Cargo mais frequente", cargo_mais_frequente)

st.markdown("---")

# --- Análises Visuais com Plotly ---
st.subheader("Gráficos")

col_graf1, col_graf2 = st.columns(2)


with col_graf1:
    if not df_filtrado.empty:
        top_cargos = df_filtrado.groupby('cargo')['usd'].mean().nlargest(10).sort_values(ascending=True).reset_index()
        grafico_cargos = px.bar(
        top_cargos,
        x='usd',
        y='cargo',
        orientation='h',
        title="🔝 Top 10 cargos por salário médio",
        color='usd',  # Adiciona gradiente de cor
        color_continuous_scale='tealrose',
        labels={'usd': '💰 Média salarial anual (USD)', 'cargo': ''}
        )
        grafico_cargos.update_layout(title_x=0.1, yaxis={'categoryorder':'total ascending'})
        st.plotly_chart(grafico_cargos, use_container_width=True)
    else:
        st.warning("Nenhum dado para exibir no gráfico de cargos.")

with col_graf2:
    if not df_filtrado.empty:
        grafico_hist = px.histogram(
            df_filtrado,
            x='usd',
            nbins=30,
            title="Distribuição de salários anuais",
            labels={'usd': 'Faixa salarial (USD)', 'count': ''}
        )
        grafico_hist.update_layout(title_x=0.1)
        st.plotly_chart(grafico_hist, use_container_width=True)
    else:
        st.warning("Nenhum dado para exibir no gráfico de distribuição.")

col_graf3, col_graf4 = st.columns(2)

with col_graf3:
    if not df_filtrado.empty:
        remoto_contagem = df_filtrado['remoto'].value_counts().reset_index()
        remoto_contagem.columns = ['tipo_trabalho', 'quantidade']
        grafico_remoto = px.pie(
            remoto_contagem,
            names='tipo_trabalho',
            values='quantidade',
            title='Proporção dos tipos de trabalho',
            hole=0.5
        )
        grafico_remoto.update_traces(textinfo='percent+label')
        grafico_remoto.update_layout(title_x=0.1)
        st.plotly_chart(grafico_remoto, use_container_width=True)
    else:
        st.warning("Nenhum dado para exibir no gráfico dos tipos de trabalho.")

with col_graf4:
    if not df_filtrado.empty:
        df_ds = df_filtrado[df_filtrado['cargo'] == 'Data Scientist']
        media_ds_pais = df_ds.groupby('residencia_iso3')['usd'].mean().reset_index()
        grafico_paises = px.choropleth(media_ds_pais,
            locations='residencia_iso3',
            color='usd',
            color_continuous_scale='rdylgn',
            title='Salário médio de Cientista de Dados por país',
            labels={'usd': 'Salário médio (USD)', 'residencia_iso3': 'País'})
        grafico_paises.update_layout(title_x=0.1)
        st.plotly_chart(grafico_paises, use_container_width=True)
    else:
        st.warning("Nenhum dado para exibir no gráfico de países.")

# --- Tabela de Dados Detalhados ---
st.subheader("Dados Detalhados")
st.dataframe(df_filtrado)

# --- Seção "Sobre este painel" ---
st.markdown("---")
with st.expander("📌 Sobre este painel"):
    st.markdown("""
    **✨ Painel criado por Marcelo Viana durante a Imersão Dados Com Python(2025) da Alura**  
    
    Este dashboard interativo permite explorar os salários na área de dados com filtros dinâmicos e visualizações ricas.
    
    **📊 Dados:**  
    - Período: {}-{}  
    - Total de registros: {}  

    
    **🛠️ Tecnologias utilizadas:**  
    - Python • Streamlit • Plotly • Pandas
    
    **📌 Como usar:**  
    1. Ajuste os filtros na barra lateral  
    2. Explore as métricas automáticas  
    3. Interaja com os gráficos
    
    **📧 Contato:** marceloviana836@gmail.com | [LinkedIn](https://linkedin.com/in/marcelo-sviana) 
    """.format(df['ano'].min(), df['ano'].max(), len(df)))
    
if st.checkbox("📱 Modo Mobile"):
    st.write("""
    <style>
        [data-testid="column"] {
            width: 100% !important;
        }
    </style>
    """, unsafe_allow_html=True)