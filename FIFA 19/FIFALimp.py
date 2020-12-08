# -*- coding: utf-8 -*-
"""
Created on Tue Dec  8 11:00:54 2020

@author: André
"""


def f(x):
    '''
    Função removedora de cifrões e unidades
    Transforma "$5K" em '5'

    Parameters
    ----------
    x : A string a ser transformada em número

    Returns
    -------
    Retorna o float do valor inserido, em milhares

    '''
    unit = x[len(x)-1:]
    x = x[1:len(x)-1]
    if unit == 'M':
        return float(x)*1000
    elif unit == 'K':
        return float(x)*1

def limpeza():
    import FIFAConn
    df = FIFAConn.readFIFA()
    '''
    Limpa e organiza a base de dados para facilitar a modelagem estatistíca dela
    A descrição das mudanças feitas pode ser encontrada no relatório
    
    Parameters
    ----------
    df : O dataframe da base de dados suja
    Returns
    -------
    df : O dataframe da base de dados limpa

    '''
    df['Club'] = df['Club'].fillna("No Club")
    df.loc[df['Club'] == 'No Club']
    df['Loaned_From'] = df['Loaned_From'].fillna("Not Loaned")
    df.loc[df['Loaned_From'] == 'Not Loaned']
    df['Release_Clause'] = df['Release_Clause'].fillna("0")
    df.loc[df['Release_Clause'] == '0']
    df = df[df.Preferred_Foot.notnull()]
    df = df.drop(['Photo','Club_Logo','Flag','Joined','Contract_Valid_Until','ID','Counter'], axis = 1)
    df = df.drop(["LS","ST","RS","LW","LF","CF","RF","RW","LAM","CAM","RAM","LM","LCM","CM","RCM","RM","LWB","LDM","CDM","RDM","RWB","LB","LCB","CB","RCB","RB"], axis = 1)
    df['Wage'] = df['Wage'].replace(['€','K'],"", regex = True)
    lista = []
    for a in df["Value"]:
        lista.append(f(a))
    df['Value'] = lista
    lista = []
    for a in df["Release_Clause"]:
        lista.append(f(a))
    df['Release_Clause'] = lista
    df = df[df.Position.notnull()]
    df['PosicionamentoCampo'] = df['Position']
    df['PosicionamentoCampo'] = df['PosicionamentoCampo'].replace(['GK'],"GOL")
    df['PosicionamentoCampo'] = df['PosicionamentoCampo'].replace(["RB","RWB","CB","LWB","LB","LCB","RCB"],"DEF")
    df['PosicionamentoCampo'] = df['PosicionamentoCampo'].replace(["CM","CDM","CAM","RM","LM","LAM","RAM","LCM","RCM","LDM","RDM","LW","RW"],"MEC")
    df['PosicionamentoCampo'] = df['PosicionamentoCampo'].replace(["CF","LF","RF","ST","LS","RS"],"ATQ")
    return df

limpeza()
print(limpeza())
