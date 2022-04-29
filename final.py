import streamlit as st
import pandas as pd
countries = []
for i in df:
  countries = countries.append(i)

country_acronym = st.selectbox('Country acronym', countries)
