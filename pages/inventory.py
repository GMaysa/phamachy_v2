from turtle import ScrolledCanvas
from pyrsistent import s
import streamlit as st
import streamlit_option_menu as som
from PIL import Image
import src

icon = Image.open(
    "C:/Dipung/Kuliah/Semeter_IV\BASAT/Final Project/favicon/box-seam.png")

st.set_page_config(
    page_title='Batin Phamarcy',
    page_icon= icon,
)

st.markdown("<h1 style='text-align: center;'>Inventory</h1>",
            unsafe_allow_html=True)
selInv = som.option_menu(
    menu_title=None,
    options=["All", "Search", "Filter", "Insert",'Update', "Delete"],
    icons=['list', 'search',
            'filter', 'arrow-down-square', 'arrow-up-square','x-square'],
    menu_icon=None,
    default_index=0,
    orientation='horizontal')
if (selInv =="All"):
    selAll = src.selectAll()
    st.table(selAll)

elif (selInv == "Search"):
    # st.markdown("<h1 style='text-align: center;'>Inventory</h1>",
                # unsafe_allow_html=True)
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
        if submitBar == True and searchBar == '':
            st.error("There aren't input a data")
        elif submitBar:
            try:
                dfSearch= src.likeSrcIven(optionBar, searchBar)
            except ValueError:
                if optionBar == "id":
                    try:
                        print(int(searchBar))
                    except:
                        st.error("You only can search a Book ID using a number")
            else:
                dfSearch = src.likeSrcIven(optionBar, searchBar)
                st.success("Your searched for {} in {}".format(searchBar, optionBar))
                st.table(dfSearch)

elif (selInv == "Filter"):
    # st.markdown("<h1 style='text-align: center;'>Inventory</h1>",
    # unsafe_allow_html=True)
    with st.container():
        with st.form(key='search-bar', clear_on_submit=False):
            # st.markdown("<p style='text-align: left;'>Inventory</p>",
            #             unsafe_allow_html=True)
            nav1, nav2, nav3,nav4,nav5 = st.columns([1, 1,1,1, 0.5])
            with nav1:
                optionBar = st.selectbox(
                    label='Options', options=['name', 'category'])
            with nav2:
                searchBar = st.text_input(label='Values', value="search")
            with nav3:
                starBar = st.text_input(label='Start')
            with nav4:
                endBar = st.text_input(label = 'End')
            with nav5:
                st.text('Search')
                submitBar = st.form_submit_button(label='Do')

elif (selInv == "Insert"):
    # st.markdown("<h1 style='text-align: center;'>Inventory</h1>",
    # unsafe_allow_html=True)
    with st.container():
        with st.form(key='Insert', clear_on_submit=False):
            # st.markdown("<p style='text-align: left;'>Inventory</p>",
            #             unsafe_allow_html=True)
            nav1, nav2, nav3, nav4, nav5,nav6 = st.columns([1,1,1,1,1,0.5])
            with nav1:
                optionBar = st.selectbox(
                    label='Caetgory', options=['Obat Pil', 'Obat Kapsul'])
            with nav2:
                nameBar = st.text_input(label='Name')
            with nav3:
                priceBar = st.text_input(label='Price')
            with nav4:
                stcokBar = st.text_input(label='Stock')
            with nav5:
                expBar = st.text_input(label="Exp Date")
            with nav6:
                st.text('Search')
                submitBar = st.form_submit_button(label='Do')

elif (selInv == "Update"):
    # st.markdown("<h1 style='text-align: center;'>Inventory</h1>",
    # unsafe_allow_html=True)
    with st.container():
        with st.form(key='Update', clear_on_submit=False):
            # st.markdown("<p style='text-align: left;'>Inventory</p>",
            #             unsafe_allow_html=True)
            nav1, nav2, nav3, nav4, nav5, nav6 = st.columns(
                [1, 1, 1, 1, 1, 0.5])
            with nav1:
                optionBar = st.selectbox(
                    label='Caetgory', options=['Obat Pil', 'Obat Kapsul'])
            with nav2:
                nameBar = st.text_input(label='Name')
            with nav3:
                priceBar = st.text_input(label='Price')
            with nav4:
                stcokBar = st.text_input(label='Stock')
            with nav5:
                expBar = st.text_input(label="Exp Date")
            with nav6:
                st.text('Search')
                submitBar = st.form_submit_button(label='Do')
elif (selInv == "Delete"):
    selAll = src.selectAll()
    st.table(selAll)
    with st.container():
        with st.form(key='search-bar', clear_on_submit=False):
            # st.markdown("<p style='text-align: left;'>Inventory</p>",
            #             unsafe_allow_html=True)
            nav1, nav2, nav3 = st.columns([1, 3, 0.5])
            with nav1:
                optionBar = st.selectbox(
                    label='Options', options=['name','id'])
            with nav2:
                searchBar = st.text_input(label='Values')
            with nav3:
                st.text('Delete')
                submitBar = st.form_submit_button(label='Do')

