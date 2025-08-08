# analise-de-a-es
Criando um programa que análise ações do mercado financeiro

análise-de-ações/
├── src/
│   ├── data_handler.py     # Lida com a coleta e armazenamento dos dados.
│   ├── indicators.py       # Calcula os indicadores técnicos.
│   ├── visualization.py    # Gera os gráficos.
│   └── main.py             # Arquivo principal para rodar a análise.
├── tests/
│   ├── test_data_handler.py
│   ├── test_indicators.py
│   └── test_visualization.py
├── data/
│   └── b3_stock_prices.csv # Onde os dados brutos serão salvos.
├── .gitignore              # Ignora arquivos desnecessários no Git.
└── requirements.txt        # Lista as bibliotecas do projeto.