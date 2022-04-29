import sqlite3
import pandas as pd
from sqlite3 import connect

conn = sqlite3.connect('db1.db')
cur = conn.cursor()
cur.execute('SELECT Countries.Country FROM Countries')
df = pd.DataFrame(cur.fetchall(), columns = ['Countries'])


import streamlit as st
import pandas as pd
countries = []
for i in df:
  countries = countries.append(i)

country_acronym = st.selectbox('Country acronym', countries)
