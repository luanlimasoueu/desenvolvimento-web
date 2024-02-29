import streamlit as st
import numpy as np
import pandas as pd

#map
map_data = pd.DataFrame(
    np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4],
    columns=['lat', 'lon'])

st.map(map_data)

#acesso a determinados valores
import streamlit as st
st.text_input("Your name", key="name")

st.session_state.name
