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
    # A coluna 'Close' é o preço de fechamento, que usaremos para o cálculo
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
    # Calculamos a diferença diária dos preços de fechamento
    delta = df['Close'].diff()
    
    # Criamos os ganhos (ups) e as perdas (downs)
    gains = delta.where(delta > 0, 0)
    losses = -delta.where(delta < 0, 0)
    
    # Calculamos a média móvel exponencial (EMA) dos ganhos e perdas
    avg_gain = gains.ewm(com=window - 1, min_periods=window).mean()
    avg_loss = losses.ewm(com=window - 1, min_periods=window).mean()
    
    # Calculamos o Índice de Força Relativa (IFR)
    rs = avg_gain / avg_loss
    df['RSI'] = 100 - (100 / (1 + rs))
    
    return df

if __name__ == '__main__':
    # Exemplo de uso para testar o módulo
    # Criamos um DataFrame de exemplo para simular os dados da ação
    sample_data = {
        'Close': [100, 102, 105, 103, 107, 109, 110, 108, 112, 115,
                  113, 118, 120, 119, 125, 122, 128, 130, 127, 135]
    }
    df_sample = pd.DataFrame(sample_data)
    
    # Calculamos a Média Móvel Simples (MMS)
    df_with_mms = calculate_moving_average(df_sample, window=5)
    print("DataFrame com Média Móvel Simples (MMS):")
    print(df_with_mms.tail(10))
    
    # Calculamos o Índice de Força Relativa (IFR)
    df_with_rsi = calculate_rsi(df_sample, window=5)
    print("\nDataFrame com Índice de Força Relativa (IFR):")
    print(df_with_rsi.tail(10))