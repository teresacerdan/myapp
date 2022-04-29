import sqlite3
import pandas as pd
from sqlite3 import connect

conn = sqlite3.connect('db1.db')
cur = conn.cursor()
cur.execute('SELECT Countries.Country FROM Countries')
df = pd.DataFrame(cur.fetchall(), columns = ['Countries'])


import streamlit as st
import pandas as pd
acronym = df['Acronym']
countries = []
for i in acronym:
  countries.append(i)

country_acronym = st.radio('Country acronym', countries)
