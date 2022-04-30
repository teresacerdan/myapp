import sqlite3
import pandas as pd
from sqlite3 import connect

conn = sqlite3.connect('db1.db')
cur = conn.cursor()
cur.execute('SELECT Country, Acronym FROM Countries')
df = pd.DataFrame(cur.fetchall(), columns = ['Countries', 'Acronym'])


import streamlit as st
import pandas as pd
acronym = df['Countries']
countries = []
for i in acronym:
  countries.append(i)
country_selected = st.selectbox('Country name', countries)


cur.execute('SELECT ecContribution, name, shortName, activityType, organizationURL FROM Participants GROUP BY organizationURL')
df_participants = pd.DataFrame(cur.fetchall(), columns= ['shortName', 'name', 'activityType', 'Sum', 'count_project'])
st.dataframe(df_participants)
