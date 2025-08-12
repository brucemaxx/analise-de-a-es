import os
import matplotlib.pyplot as plt

# Importa as funções dos módulos que criamos
from data_handler import download_stock_data, save_data_to_csv, load_data_from_csv
from indicators import calculate_moving_average, calculate_rsi
from visualization import plot_stock_analysis

def main():
    """
    Função principal do projeto de Análise de Ações.
    Orquestra a coleta de dados, cálculo de indicadores e visualização.
    """
    # --- 1. Configurações e Coleta de Dados ---
    ticker = 'VALE3.SA'  # Símbolo da ação que queremos analisar
    start_date = '2023-01-01'
    end_date = '2024-01-01'
    filename = f'../data/{ticker}_history.csv'

    # Se o arquivo de dados já existir, carrega; senão, baixa e salva.
    if os.path.exists(filename):
        df = load_data_from_csv(filename)
    else:
        df = download_stock_data(ticker, start_date, end_date)
        save_data_to_csv(df, filename)

    if df.empty:
        print("Não foi possível carregar ou baixar os dados. Encerrando o programa.")
        return

    # --- 2. Cálculo dos Indicadores ---
    print("\nCalculando indicadores técnicos...")
    df = calculate_moving_average(df, window=20)
    df = calculate_rsi(df, window=14)
    print("Indicadores calculados com sucesso.")

    # --- 3. Geração da Visualização ---
    print("\nGerando o gráfico de análise técnica...")
    plot_stock_analysis(df, ticker)
    plt.show()
    print("Análise concluída. O gráfico foi exibido.")

if __name__ == '__main__':
    main()