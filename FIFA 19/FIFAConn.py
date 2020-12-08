# -*- coding: utf-8 -*-
"""
Created on Tue Dec  8 10:59:41 2020

@author: André
"""


def readFIFA():
    '''
    Realiza a conexão com o banco de dados do SQL

    Returns
    -------
    df : Retorna um dataframe da base de dados

    '''
    import pandas as pd
    import pyodbc 
    conn = pyodbc.connect('''DRIVER={ODBC Driver 17 for SQL Server};
                          Server=tcp:fgv-db-server.database.windows.net,1433;Initial Catalog=fgv-db;Persist Security Info=False;User ID=student;Password={your_password};MultipleActiveResultSets=False;Connection Timeout=30;
                          DATABASE=fgv-db;
                          UID=student;
                          PWD=@dsInf123''')
                          
                          
    df = pd.read_sql('SELECT * FROM fifa.fifa_players',conn)
    return df