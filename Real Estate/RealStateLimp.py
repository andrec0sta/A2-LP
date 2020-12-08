# -*- coding: utf-8 -*-
"""
Created on Tue Dec  8 11:32:11 2020

@author: André
"""

def limpeza():
    '''
    Limpa o banco de dados, tornando mais fácil a modelagem estatistica
    Explicação detalhada da limpeza no relatório

    Returns
    -------
    df : Retorna um dataframe da base de dados limpa

    '''
    import RealStateConn
    df = RealStateConn.readBD()
    df = df.dropna()
    df['CHAS'] = df['CHAS'].astype('int')
    return df

limpeza()
print(limpeza())
