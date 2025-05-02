import streamlit as st
import plotly.express as px  # Adicionando a importação do plotly.express
from dataset import df, df_rec_mensal  # Importa os dados preparados
from utils import format_number  # Função para formatação de números
from graficos import GraficoVendas, grafico_re_venda_por_dia # Classe para gerar os gráficos
from modelo_ia import obter_previsao  
from previsoes import previsao_lstm, previsao_mlp, previsao_reg_linear  

st.set_page_config(layout='wide')
st.title("Dashboard de Vendas :shopping_trolley:")

aba1, aba2, aba3, aba4 = st.tabs([
    "Ambiente de Visualização de Vendas",
    "Ambiente de Processamento de Dados",
    "Ambiente de Análise de Preços",
    "Ambiente de Previsão com IA"
])

# Aba 1 - Visualização de vendas
with aba1:
    st.dataframe(df)  # Exibe o DataFrame original

# Aba 2 - Processamento de Dados
with aba2:
    coluna1, coluna2 = st.columns(2)
    with coluna1:
        st.metric('Receita total', format_number(df['Preco_R$'].sum(), 'R$'))
    with coluna2:
        st.metric('Quantidade de vendas', format_number(df['Preco_R$'].shape[0]))

    # Exibe o gráfico de receita mensal
    grafico_vendas = GraficoVendas(df_rec_mensal)
    grafico = grafico_vendas.grafico_receita_mensal()
    st.plotly_chart(grafico)  # Exibe o gráfico interativo no Streamlit

# Aba 3 - Análise de Preços
with aba3:
    # Calcula o preço máximo e mínimo
    preco_max = df.loc[df['Preco_R$'].idxmax()]
    preco_min = df.loc[df['Preco_R$'].idxmin()]

    # Exibe as métricas de Preço Máximo e Mínimo
    col1, col2 = st.columns(2)
    with col1:
        st.metric("Preço Máximo", format_number(preco_max['Preco_R$'], 'R$'), preco_max['Data'].strftime('%d/%m/%Y'))
    with col2:
        st.metric("Preço Mínimo", format_number(preco_min['Preco_R$'], 'R$'), preco_min['Data'].strftime('%d/%m/%Y'))

    # Gráfico de preço do algodão ao longo do tempo
    fig = px.line(df, x='Data', y='Preco_R$', title="Preço do Algodão ao Longo do Tempo")
    st.plotly_chart(fig)

    # Exibe o gráfico Top 7 de vendas por dia
    st.plotly_chart(grafico_re_venda_por_dia, use_container_width=True)

# Nova aba - Previsão com IA
with aba4:
    st.subheader("Previsões de Preço do Algodão com Modelos de IA")

    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("Previsão com Rede Neural LSTM", format_number(previsao_lstm(), 'R$'))
    with col2:
        st.metric("Previsão com Rede Neural MLP", format_number(previsao_mlp(), 'R$'))
    with col3:
        st.metric("Previsão com Regressão Linear", format_number(previsao_reg_linear(), 'R$'))

    with st.expander("📘 O que significam esses modelos?"):
        st.markdown("""
        - **LSTM**: Uma Rede Neural Recorrente que considera o histórico de preços ao longo do tempo. Ideal para prever séries temporais.
        - **MLP**: Rede Neural Perceptron Multicamadas. Funciona bem com padrões gerais e relacionamentos nos dados.
        - **Regressão Linear**: Um modelo estatístico simples, útil como linha de base para comparação.
        """)