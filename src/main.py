import os
import matplotlib.pyplot as plt
import pandas as pd

from data_handler import download_stock_data, save_data_to_csv, load_data_from_csv
from indicators import calculate_moving_average, calculate_rsi
from visualization import plot_stock_analysis

def main():
    """
    Função principal do projeto de Análise de Ações.
    Orquestra a coleta de dados, cálculo de indicadores e visualização.
    """
    ticker = 'VALE3.SA'
    start_date = '2023-01-01'
    end_date = '2024-01-01'
    filename = f'../data/{ticker}_history.csv'

    if os.path.exists(filename):
        df = load_data_from_csv(filename)
    else:
        df = download_stock_data(ticker, start_date, end_date)
        save_data_to_csv(df, filename)

    if df.empty:
        print("Não foi possível carregar ou baixar os dados. Encerrando o programa.")
        return

    print("\nCalculando indicadores técnicos...")
    df = calculate_moving_average(df, window=20)
    df = calculate_rsi(df, window=14)
    print("Indicadores calculados com sucesso.")

    # --- NOVO: Preparando o DataFrame para o mplfinance ---
    # Garante que o índice seja de tipo de data
    df.index = pd.to_datetime(df.index)
    
    # Remove linhas com valores NaN para o gráfico de velas
    df.dropna(inplace=True)
    
    print("\nGerando o gráfico de análise técnica...")
    plot_stock_analysis(df, ticker)
    plt.show()
    print("Análise concluída. O gráfico foi exibido.")

if __name__ == '__main__':
    main()