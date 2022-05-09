import sqlite3
import pandas as pd
from sqlite3 import connect

conn = sqlite3.connect('db1.db')
cur = conn.cursor()
cur.execute('SELECT Country, Acronym FROM Countries')
df = pd.DataFrame(cur.fetchall(), columns = ['Countries', 'Acronym'])


import streamlit as st
import pandas as pd
from PIL import Image
countries_column = df['Countries']
countries = []

image=Image.open('KDT-JU.png')
st.image(image)
st.header('Partner search tool')
for i in countries_column:
  countries.append(i)
country_selected = st.selectbox('Country name', countries)

for i in range(len(countries)):
  if countries[i]==country_selected:
    position=i
  
acronym_column = df['Acronym']
acronym=[]
for i in acronym_column:
  acronym.append(i)
my_acronym=acronym[position]


st.write('You selected:', country_selected,',',my_acronym)



st.write('Participants of', country_selected)
participants=pd.read_sql("SELECT country, shortName, name, activityType, ecContribution, organizationURL, SUM(ecContribution) AS sum, COUNT(organizationURL) FROM participants WHERE role='participant' AND country='{}' GROUP BY organizationURL ORDER BY sum DESC".format(my_acronym),conn)
df_participants = pd.DataFrame(participants, columns= ['country', 'shortName', 'name', 'activityType','organizationURL', 'Sum', 'count'])  
st.dataframe(df_participants)

st.write('Coordinators of', country_selected)
coordinators=pd.read_sql("SELECT shortName, name, ActivityType, projectAcronym FROM participants WHERE role='coordinator' AND country='{}'ORDER BY shortName".format(my_acronym),conn)
df_coordinators = pd.DataFrame(coordinators, columns= ['Short Name', 'Name', 'Activity Type', 'Project Acronym'])  
st.dataframe(df_coordinators)



