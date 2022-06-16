# %matplotlib
from sqlalchemy import column
import streamlit as st
from streamlit.elements import image
import streamlit_option_menu as som
import pandas as pd
import matplotlib as plt
import numpy as np
import src
# from PIL import Image
# img = Image.open("")
# st.markdown("# Report")
st.sidebar.markdown("<h1>Dashboard</h1>",unsafe_allow_html=True)
with st.container():
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric(label = 'Amount', value = src.sumAmount(),delta = 0)
    with col2:
        st.metric(label = 'Buy Drugs',value = src.sumDrugs(), delta = 0 )
    with col3:
        st.metric(label=" Stock Drugs ", value = src.countDrugs(), delta = 0)
with st.container():
    st.table(src.viewTransaction())
with st.container():
    nav1,nav2= st.columns(2)
    with nav1:
        st.metric(label='Suplied Drugs', value=src.countQuantity(), delta=0)
    with nav2:
        st.metric(label='Expired Drugs', value=src.countExp(), delta=0)

# selected = som.option_menu(
#     menu_title=None,
#     options=["Report", "Inventory", "Cashier", "Staff", "Search"],
#     icons=['bar-chart-line-fill', 'box-seam',
#         'cash', 'person-lines-fill', 'house'],
#     menu_icon=None,
#     default_index=0,
#     orientation='horizontal')
