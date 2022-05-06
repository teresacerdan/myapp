import sqlite3
import pandas as pd
from sqlite3 import connect

conn = sqlite3.connect('db1.db')
cur = conn.cursor()
cur.execute('SELECT Country, Acronym FROM Countries')
df = pd.DataFrame(cur.fetchall(), columns = ['Countries', 'Acronym'])


import streamlit as st
import pandas as pd
countries_column = df['Countries']
countries = []
for i in countries_column:
  countries.append(i)
country_selected = st.selectbox('Country name', countries)
st.write('You selected:', country_selected)

acronym_selected=pd.read_sql("SELECT Acronym FROM Countries WHERE Country='country_selected'", conn) 
                             
cur.execute("SELECT country, shortName, name, activityType, ecContribution, organizationURL, COUNT(organizationURL) FROM Participants")
df_participants = pd.DataFrame(cur.fetchall(), columns= ['country', 'shortName', 'name', 'activityType', 'Sum','organizationURL', 'count_project'])
conn.close()
st.dataframe(df_participants)
