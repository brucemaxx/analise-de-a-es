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
    rsi_panel = mpf.make_addplot(df['RSI'], panel=2, color='purple', title='RSI',
                                 ylabel='Nível', y_on_right=True)
    mms_panel = mpf.make_addplot(df['MMS'], color='orange', linestyle='--', panel=0,
                                 ylabel='Preço (R$)')
                                 
    mpf.plot(df, type='candle', style='charles', title=f'Análise Técnica - {ticker}',
             ylabel='Preço (R$)',
             volume=True,
             addplot=[mms_panel, rsi_panel],
             figsize=(12, 8))