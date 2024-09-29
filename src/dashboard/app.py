import streamlit as st
import pandas as pd
import sqlite3

conn=sqlite3.connect('C:/Users/Nascimento/Germano/Jornada de Dados/mercado_livre_scraping/dados/quotes.db')

df = pd.read_sql_query("SELECT * FROM mercadolivre_tennis", conn)

conn.close()

st.title('Tenis Esportivo - Mercado Livre')
st.write(df)

col1,col2 = st.columns(2)

total_itens = df.shape[0]
col1.metric(label="Quantidade de Itens", value=total_itens)

unique_brands=df['brand'].nunique()
col2.metric(label='Marcas Unicas', value=unique_brands)

st.subheader('Marcas mais encontradas')
col1, col2 = st.columns([4,2])
top_brands=df['brand'].value_counts().sort_values(ascending=False)
col1.bar_chart(top_brands)
col2.write(top_brands)

