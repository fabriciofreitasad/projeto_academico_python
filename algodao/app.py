import streamlit as st
import plotly.express as px  # Adicionando a importação do plotly.express
from dataset import df, df_rec_mensal  # Importa os dados preparados
from utils import format_number  # Função para formatação de números
from graficos import GraficoVendas  # Classe para gerar os gráficos


st.set_page_config(layout='wide')
st.title("Dashboard de Vendas :shopping_trolley:")

aba1, aba2, aba3 = st.tabs(["Ambiente de Visualização de Vendas", "Ambiente de Processamento de Dados", "Ambiente de Análise de Preços"])

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
    # Exemplo de gráfico com Plotly
    fig = px.line(df, x='Data', y='Preco_R$', title="Preço do Algodão ao Longo do Tempo")
    st.plotly_chart(fig)
