import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image
chart_data = pd.DataFrame(np.random.randn(20, 3), columns=['a', 'b', 'c'])

st.title("My first web app")
image = Image.open('KDT-JU.png')
st.image(image)
