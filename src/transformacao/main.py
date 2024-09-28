import pandas as pd
import sqlite3
from datetime import datetime

#df = pd.read_json('../dados/dados_2.json', lines=True)
#print(df)

df = pd.read_json('C:/Users/Nascimento/Germano/Jornada de Dados/mercado_livre_scraping/dados/dados.json', encoding='utf-8')

df['_source']= "https://lista.mercadolivre.com.br/tenis-corrida-masculino"
df['_data_coleta'] = datetime.now()

print(df)

df['new_price'] = df['new_price'].fillna(0).astype(float)
print(df)

conn=sqlite3.connect('C:/Users/Nascimento/Germano/Jornada de Dados/mercado_livre_scraping/dados/quotes.db')

df.to_sql('mercadolivre_tennis', conn, if_exists='replace', index=False)
conn.close()