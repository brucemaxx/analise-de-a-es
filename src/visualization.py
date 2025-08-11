import pandas as pd
import matplotlib.pyplot as plt
import mplfinance as mpf

def plot_stock_analysis(df, ticker):
    """
    Gera um gráfico de velas da ação com Média Móvel e RSI.

    Args:
        df (pd.DataFrame): O DataFrame com os dados da ação e os indicadores.
        ticker (str): O código da ação para o título do gráfico.
    """
    # Cria o subgráfico do RSI
    rsi_panel = mpf.make_addplot(df['RSI'], panel=2, color='purple', title='RSI',
                                 ylabel='Nível', y_on_right=True)

    # Cria o subgráfico da Média Móvel Simples
    mms_panel = mpf.make_addplot(df['MMS'], color='orange', linestyle='--', panel=0,
                                 ylabel='Preço (R$)')
                                 
    # Cria o gráfico completo com velas, MMS e RSI
    mpf.plot(df, type='candle', style='charles', title=f'Análise Técnica - {ticker}',
             ylabel='Preço (R$)',
             volume=True,
             addplot=[mms_panel, rsi_panel],
             figsize=(12, 8))

if __name__ == '__main__':
    # Exemplo de uso para testar o módulo
    # Criamos um DataFrame de exemplo para simular os dados da ação com os indicadores
    # Os dados aqui são fictícios, mas simulam o que esperamos do projeto completo
    sample_data = {
        'Open': [100, 102, 105, 103, 107, 109, 110, 108, 112, 115],
        'High': [103, 106, 108, 107, 110, 112, 113, 112, 115, 118],
        'Low': [99, 101, 104, 102, 106, 108, 109, 107, 111, 114],
        'Close': [102, 105, 103, 107, 109, 110, 108, 112, 115, 113],
        'Volume': [100000, 120000, 90000, 150000, 110000, 130000, 105000, 140000, 160000, 125000],
        'MMS': [100, 101, 102, 103, 104, 105, 106, 107, 108, 109], # Dados fictícios de MMS
        'RSI': [50, 55, 45, 60, 65, 70, 62, 75, 80, 72]           # Dados fictícios de RSI
    }
    sample_index = pd.to_datetime(pd.date_range(start='2024-01-01', periods=10, freq='B'))
    df_sample = pd.DataFrame(sample_data, index=sample_index)
    
    # Geramos o gráfico
    plot_stock_analysis(df_sample, 'VALE3.SA')
    
    # Exibe o gráfico
    plt.show()