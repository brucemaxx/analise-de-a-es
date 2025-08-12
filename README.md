# Análise de Ações: Ferramenta de Análise Técnica com Python

Este projeto é uma ferramenta de linha de comando para realizar análises técnicas de ações da B3. Ele automatiza a coleta de dados, o cálculo de indicadores e a visualização de gráficos, proporcionando uma base sólida para quem deseja explorar o mercado financeiro com programação.

## Funcionalidades

- **Coleta de Dados:** Baixa dados históricos de ações do Yahoo Finance (`yfinance`).
- **Análise Técnica:** Calcula a **Média Móvel Simples (MMS)** e o **Índice de Força Relativa (RSI)**.
- **Visualização:** Gera um gráfico de velas profissional, incluindo volume, MMS e RSI.

## Tecnologias Utilizadas

- **Python 3.x**
- **Pandas:** Manipulação de dados
- **yfinance:** Coleta de dados
- **matplotlib & mplfinance:** Visualização de gráficos

## Como Usar o Projeto

Siga estes passos para configurar e rodar a aplicação em sua máquina.

1.  **Clonar o Repositório:**
    ```bash
    git clone https://github.com/brucemaxx/analise-de-a-es.git
    cd analise-de-acoes
    ```
2.  **Configurar o Ambiente:**
    ```bash
    python -m venv .venv
    # Ative o ambiente virtual
    # No Windows: .venv\Scripts\activate
    # No macOS/Linux: source .venv/bin/activate
    pip install -r requirements.txt
    ```
3.  **Executar a Análise:**
    ```bash
    python src/main.py
    ```

## Estrutura do Projeto

O código é organizado em módulos com responsabilidades claras para facilitar a leitura e a manutenção.

-   `src/`: Contém todo o código-fonte.
    -   `main.py`: O ponto de entrada que orquestra a análise.
    -   `data_handler.py`: Gerencia a obtenção e armazenamento dos dados.
    -   `indicators.py`: Responsável pelo cálculo dos indicadores técnicos.
    -   `visualization.py`: Gera os gráficos da análise.
-   `data/`: Pasta onde os dados brutos são armazenados.
-   `docs/`: Contém a imagem de exemplo do gráfico.

## Exemplo de Saída

![Gráfico de Análise Técnica](docs/chart_example.png)
_Nota: O gráfico gerado pode variar com base nos dados mais recentes._