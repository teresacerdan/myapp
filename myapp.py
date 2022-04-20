import streamlit as st
import panda as pd
import numpy as np
chart_data = pd.DataFrame(np.random.randn(20, 3), columns=['a', 'b', 'c'])

image = Image.open('KDT-JU.png')
st.image(image)
st.title("My first web app")
