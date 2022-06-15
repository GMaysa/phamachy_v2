# %matplotlib
from sqlalchemy import column
import streamlit as st
from streamlit.elements import image
import streamlit_option_menu as som
import pandas as pd
import matplotlib as plt
import numpy as np
# from PIL import Image
# img = Image.open("")
# st.markdown("# Report")
st.sidebar.markdown("<h1>Dashboard</h1>",unsafe_allow_html=True)
selected = som.option_menu(
    menu_title=None,
    options=["Report", "Inventory", "Cashier", "Staff", "Search"],
    icons=['bar-chart-line-fill', 'box-seam',
        'cash', 'person-lines-fill', 'house'],
    menu_icon=None,
    default_index=0,
    orientation='horizontal')

if (selected=="Report"):
    st.markdown("<h1>Dashboard</h1>", unsafe_allow_html=True)
    st.write("asu")
    # # d ={
    # #     'Month':[
    # #         'January',
    # #         'February',
    # #         'March',
    # #         'April',
    # #         'May',
    # #         'June',
    # #         'July',
    # #         'August',
    # #         'September',
    # #         'October',
    # #         'November',
    # #         'December'],
    # #     'Count':[100,200,150,75,78,19,203,465,267,183,52,321]
    # #     }
    # y = np.array = [100, 200, 150, 75, 78, 19, 203, 465, 267, 183, 52, 321]
    # # df = pd.DataFrame(data = d, columns=['Month', 'Income'])
    # # fig, ax = df.plot(x ='Month', y='Income', kind = 'line')
    # # print(df)
    # with st.container():
    #     nav1, nav2, nav3 = st.columns([1,1,1])
    #     with nav1:
    #         income = pd.DataFrame
    #         # st.pyplot(fig)
    #         # df = pd.DataFrame(data=d, columns=['Month', 'Income'])
    #         # df.plot(x='Month', y='Income', kind='line')
    #         plt.show()

elif (selected == "Inventory"):
    st.markdown("<h1 style='text-align: center;'>Inventory</h1>",
    unsafe_allow_html=True)
    with st.container():
        with st.form(key='search-bar', clear_on_submit=False):
            # st.markdown("<p style='text-align: left;'>Inventory</p>",
            #             unsafe_allow_html=True)
            nav1,nav2,nav3 = st.columns([1,3,0.5])
            with nav1:
                optionBar = st.selectbox(label='Options',options=['name','category'])
            with nav2:
                searchBar = st.text_input(label='Values',value="search")
            with nav3:
                st.text('Search')
                submitBar = st.form_submit_button(label='Do')


elif (selected == "Cashier"):
    st.markdown("<h1 style='text-align: center;'>Cashier</h1>",
                unsafe_allow_html=True)
    with st.container():
        with st.form(key='search-bar', clear_on_submit=False):
            # st.markdown("<p style='text-align: left;'>Inventory</p>",
            #             unsafe_allow_html=True)
            nav1, nav2, nav3 = st.columns([1, 3, 0.5])
            with nav1:
                optionBar = st.selectbox(
                    label='Options', options=['name', 'category'])
            with nav2:
                searchBar = st.text_input(label='Values', value="search")
            with nav3:
                st.text('Search')
                submitBar = st.form_submit_button(label='Do')


elif (selected == "Staff"):
    st.markdown("<h1 style='text-align: center;'>Staff</h1>",
                 unsafe_allow_html=True)
    with st.container():
        with st.form(key='search-bar', clear_on_submit=False):
            # st.markdown("<p style='text-align: left;'>Inventory</p>",
            #             unsafe_allow_html=True)
            nav1, nav2, nav3 = st.columns([1, 3, 0.5])
            with nav1:
                optionBar = st.selectbox(
                    label='Options', options=['name', 'category'])
            with nav2:
                searchBar = st.text_input(label='Values', value="search")
            with nav3:
                st.text('Search')
                submitBar = st.form_submit_button(label='Do')
