
# **Projeto Python Algodão - Dashboard de Vendas**

## **Descrição**

Este projeto tem como objetivo criar um dashboard interativo para análise de dados de vendas de algodão. Utilizando **Streamlit** para construção da interface web, **Pandas** para manipulação de dados e **Plotly** para gráficos interativos, a aplicação permite visualizar receitas, realizar processamento de dados e analisar a variação de preços ao longo do tempo.

## **Pré-requisitos**

Antes de executar o projeto, é necessário configurar o ambiente de desenvolvimento local. Siga os passos abaixo para garantir que tudo esteja pronto.

## **1. Criação do Ambiente Virtual**

Primeiro, vamos criar e ativar o ambiente virtual para isolar as dependências do projeto.

### Passo 1.1 - Criando o Ambiente Virtual
Abra o terminal e execute o comando abaixo para criar o ambiente virtual:

```bash
python -m venv .venv
```

### Passo 1.2 - Habilitando o Ambiente Virtual
Ative o ambiente virtual para garantir que as dependências sejam instaladas corretamente:

- No Windows:
  ```bash
  .\.venv\Scripts\activate
  ```

- No macOS/Linux:
  ```bash
  source .venv/bin/activate
  ```

## **2. Instalando as Dependências**

Após ativar o ambiente virtual, você precisará instalar as bibliotecas necessárias para rodar o projeto. Use os seguintes comandos no terminal:

### Passo 2.1 - Instalando as Bibliotecas

- **Pandas**: Biblioteca essencial para importar e manipular dados de datasets.
  ```bash
  pip install pandas
  ```

- **Plotly**: Biblioteca para criar gráficos interativos, excelente para visualização de dados no Streamlit.
  ```bash
  pip install plotly
  ```

- **Streamlit**: Framework para criar interfaces web interativas de forma rápida e simples, utilizado para a construção do dashboard.
  ```bash
  pip install streamlit
  ```

### Passo 2.2 - Verificando as Dependências Instaladas

Você pode verificar se as bibliotecas foram instaladas corretamente utilizando o comando:

```bash
pip list
```

Isso irá listar todas as bibliotecas e suas versões instaladas no ambiente virtual.

## **3. Executando o Projeto**

Agora que todas as dependências estão instaladas, você pode iniciar o servidor local do Streamlit para visualizar o dashboard interativo.

### Passo 3.1 - Executando o Streamlit

No terminal, execute o seguinte comando para iniciar o aplicativo:

```bash
streamlit run .\app.py
```

Isso irá abrir automaticamente o seu navegador com o dashboard, geralmente acessível em `http://localhost:8501`.

## **4. Navegação no Dashboard**

- **Aba 1**: Exibe a visualização de vendas com a tabela de dados.
- **Aba 2**: Mostra o processamento de dados, com métricas como receita total e quantidade de vendas.
- **Aba 3**: Exibe gráficos interativos para análise dos preços do algodão ao longo do tempo.

---

### **Atualizando as Dependências do Projeto**

Se você adicionar novas dependências ao seu ambiente ou se outras pessoas precisarem instalar as mesmas dependências, basta atualizar o arquivo `requirements.txt` com o seguinte comando:

1. **Certifique-se de que o ambiente virtual esteja ativado**:
   - No Windows:
     ```bash
     .\.venv\Scripts\activate
     ```
   - No macOS/Linux:
     ```bash
     source .venv/bin/activate
     ```

2. **Instalar novas dependências** com `pip`:
   ```bash
   pip install <nome-da-biblioteca>
   ```

3. **Atualizar o arquivo `requirements.txt`** para refletir as novas dependências:
   ```bash
   pip freeze > requirements.txt
   ```

Isso atualizará o arquivo `requirements.txt` com todas as dependências do ambiente virtual, garantindo que outras pessoas possam instalar as mesmas versões de bibliotecas ao configurar o projeto.

---

### **Tecnologias Utilizadas**
- **Python**: Linguagem utilizada para o desenvolvimento do projeto.
- **Pandas**: Manipulação e análise de dados.
- **Plotly**: Visualização de gráficos interativos.
- **Streamlit**: Criação rápida de interfaces web interativas.
