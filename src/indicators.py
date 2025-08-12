import pandas as pd

def calculate_moving_average(df, window=20):
    """
    Calcula a Média Móvel Simples (MMS) de uma série de preços.

    Args:
        df (pd.DataFrame): O DataFrame com os dados da ação.
        window (int): O número de períodos (dias) para o cálculo da MMS.

    Returns:
        pd.DataFrame: O DataFrame original com uma nova coluna 'MMS'.
    """
    df['MMS'] = df['Close'].rolling(window=window).mean()
    return df

def calculate_rsi(df, window=14):
    """
    Calcula o Índice de Força Relativa (IFR ou RSI).

    Args:
        df (pd.DataFrame): O DataFrame com os dados da ação.
        window (int): O número de períodos (dias) para o cálculo do IFR.

    Returns:
        pd.DataFrame: O DataFrame original com uma nova coluna 'RSI'.
    """
    delta = df['Close'].diff()
    gains = delta.where(delta > 0, 0)
    losses = -delta.where(delta < 0, 0)
    avg_gain = gains.ewm(com=window - 1, min_periods=window).mean()
    avg_loss = losses.ewm(com=window - 1, min_periods=window).mean()
    rs = avg_gain / avg_loss
    df['RSI'] = 100 - (100 / (1 + rs))
    return df