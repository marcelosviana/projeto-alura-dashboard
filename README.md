# 📊 Dashboard de Salários na Área de Dados

 [![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://projetoaluradashboard.streamlit.app)

> Dashboard interativo para análise exploratória de remunerações em tecnologia, desenvolvido com Python e Streamlit.

## 📌 Descrição

Este projeto oferece uma visualização completa do mercado de trabalho na área de dados, permitindo filtrar informações por:
- **Período temporal** (anos disponíveis)
- **Nível de senioridade**
- **Tipo de contrato**
- **Tamanho da empresa**

Destaques:
- Visualizações dinâmicas com interatividade total
- Geoprocessamento de salários por país
- Cálculo automático de métricas-chave

---

## 💡 Principais Funcionalidades

### 🔸 **Filtros Interativos**
- Controles na sidebar para seleção multidimensional
- Persistência de estado entre sessões
- Valores padrão baseados na distribuição dos dados

✔️ *Tecnologias:* Streamlit widgets, Pandas filtering

---

### 🔸 **Visualizações Dinâmicas**
1. **Top 10 Cargos por Salário**  
   - Gráfico de barras horizontais classificadas
   - Tooltips com valores exatos

2. **Distribuição Salarial**  
   - Histograma com bins ajustáveis
   - Identificação de outliers

3. **Mapa de Calor por País**  
   - Choropleth com escala de cores
   - Projeção Mercator

✔️ *Tecnologias:* Plotly Express, GeoPandas

---

### 🔸 **KPIs Automáticos**
- Cálculo em tempo real de:
  - 📈 Salário médio
  - 🚀 Salário máximo
  - 🧮 Total de registros
  - 🏆 Cargo mais frequente

✔️ *Tecnologias:* Pandas aggregations, Streamlit metrics

---

### 🔸 **Tema Customizado**
- Estilo dark mode com azul escuro
- CSS personalizado para componentes
- Layout responsivo (wide mode)

✔️ *Tecnologias:* Streamlit CSS injection, HTML components

---

## 🛠️ Stack Tecnológica

- **Deploy:** [Streamlit Cloud](https://projetoaluradashboard.streamlit.app)  
- **Linguagem:** Python 3.10+
- **Bibliotecas Principais:**
  - Streamlit (frontend)
  - Plotly (visualizações)
  - Pandas (processamento)
- **Dados:** CSV otimizado (encoding UTF-8)

## ▶️ Como Executar
```bash
pip install -r requirements.txt
streamlit run app.py
```
## 🌐 **Explore interativamente:** [projetoaluradashboard.streamlit.app](https://projetoaluradashboard.streamlit.app)  
📧 **Contato:** marceloviana836@gmail.com | [LinkedIn](https://linkedin.com/in/marcelo-sviana) 


<br>

<br>

---



> *"O mundo é um livro, e quem não analisa seus dados lê apenas uma página."*  
> **—  Santo Agostinho** | Filósofo e teólogo  
 
