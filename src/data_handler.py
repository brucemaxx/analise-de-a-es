import yfinance as yf
import pandas as pd

def download_stock_data(ticker, start_date, end_date):
    """
    Baixa dados históricos de uma ação usando a biblioteca yfinance.

    Args:
        ticker (str): O código (ticker) da ação, por exemplo, 'PETR4.SA'.
        start_date (str): A data de início no formato 'YYYY-MM-DD'.
        end_date (str): A data de fim no formato 'YYYY-MM-DD'.

    Returns:
        pd.DataFrame: Um DataFrame do pandas contendo os dados da ação.
                      Retorna um DataFrame vazio se houver um erro.
    """
    try:
        print(f"Baixando dados para {ticker} de {start_date} até {end_date}...")
        data = yf.download(ticker, start=start_date, end=end_date)
        if data.empty:
            print(f"Aviso: Nenhum dado encontrado para {ticker}.")
        else:
            print(f"Dados baixados com sucesso para {ticker}.")
        return data
    except Exception as e:
        print(f"Erro ao baixar dados para {ticker}: {e}")
        return pd.DataFrame()

def save_data_to_csv(data, filename):
    """
    Salva um DataFrame em um arquivo CSV.

    Args:
        data (pd.DataFrame): O DataFrame a ser salvo.
        filename (str): O nome do arquivo, por exemplo, 'PETR4_history.csv'.
    """
    if not data.empty:
        try:
            data.to_csv(filename)
            print(f"Dados salvos em {filename}.")
        except Exception as e:
            print(f"Erro ao salvar dados em {filename}: {e}")

def load_data_from_csv(filename):
    """
    Carrega dados de um arquivo CSV para um DataFrame.

    Args:
        filename (str): O nome do arquivo CSV a ser carregado.

    Returns:
        pd.DataFrame: O DataFrame carregado. Retorna um DataFrame vazio se houver um erro.
    """
    try:
        print(f"Carregando dados de {filename}...")
        data = pd.read_csv(filename, index_col='Date', parse_dates=True)
        print("Dados carregados com sucesso.")
        return data
    except FileNotFoundError:
        print(f"Erro: O arquivo {filename} não foi encontrado.")
        return pd.DataFrame()
    except Exception as e:
        print(f"Erro ao carregar dados de {filename}: {e}")
        return pd.DataFrame()

if __name__ == '__main__':
    # Exemplo de uso para testar o módulo
    ticker = 'VALE3.SA' # Exemplo de ticker da B3
    start_date = '2023-01-01'
    end_date = '2024-01-01'
    filename = '../data/VALE3_history.csv'

    # Baixa e salva os dados
    stock_data = download_stock_data(ticker, start_date, end_date)
    save_data_to_csv(stock_data, filename)

    # Carrega os dados salvos
    loaded_data = load_data_from_csv(filename)
    print("\nDataFrame carregado:")
    print(loaded_data.head())