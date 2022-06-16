from turtle import ScrolledCanvas
from pyrsistent import s
from sqlalchemy import column
import streamlit as st
import streamlit_option_menu as som
from PIL import Image
import src
from datetime import date
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
    order = st.multiselect('Order By',
        ['Obat Cair', 'Obat Kapsul', 'Obat Tablet',
        'Obat Oles', 'Obat Suppositoria', 'Obat Tetes'
        'Obat Inhaler', 'Obat Suntik', 'Obat Implan'], ['Obat Cair', 'Obat Tablet'])
    selBy = src.orderBy(order)
    st.table(selBy)
    
        

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
                        st.error("You only can search a id using a number")
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
            nav1, nav3,nav4,nav5 = st.columns([1,1,1, 0.5])
            with nav1:
                filterBar = st.selectbox(
                    label='Options', options=['price', 'stock'])
            # with nav2:
            #     searchBar = st.text_input(label='Values',value = 'search')
            with nav3:
                starBar = st.text_input(label='Start')
            with nav4:
                endBar = st.text_input(label = 'End')
            with nav5:
                st.text('Search')
                submitBar = st.form_submit_button(label='Do')
        if submitBar == True and (starBar == '' or endBar == ''):
            st.error("There aren't input a data")
        elif submitBar:
            try:
                dfSearch = src.betweenSrcIven(filterBar, starBar, endBar)
            except ValueError:
                if filterBar == "id":
                    try:
                        print(int(starBar))
                    except:
                        st.error("You only can search a id using a number")
            else:
                dfFilter = src.betweenSrcIven(filterBar, starBar, endBar)
                # st.success("Your searched for {} with filter {}".format(
                #     , filterBar))
                st.table(dfFilter)
elif (selInv == "Insert"):
    # st.markdown("<h1 style='text-align: center;'>Inventory</h1>",
    # unsafe_allow_html=True)
    with st.container():
        with st.form(key='insert', clear_on_submit=False):
            # st.markdown("<p style='text-align: left;'>Inventory</p>",
            #             unsafe_allow_html=True)
            nav1, nav2, nav3, nav4, nav5,nav6,nav7,nav8 = st.columns([1,1,1,1,1,1,1,0.5])
            with nav1:
                cateBar = st.selectbox(
                    label='Caetgory', options=['Obat Cair', 'Obat Kapsul'])
            with nav2:
                nameBar = st.text_input(label='Name')
            with nav3:
                priceBar = st.text_input(label='Price')
            with nav4:
                stockBar = st.text_input(label='Stock')
            with nav5:
                yy = st.text_input(label="Exp (Year)")
            with nav6:
                mm = st.text_input(label='Exp (Month)')
            with nav7:
                dd = st.text_input(label='Exp (Date)')
            with nav8:
                st.text('Search')
                submitBar = st.form_submit_button(label='Do')
        if submitBar == True and (cateBar == '' or nameBar == '' or priceBar == '' or stockBar == '' or yy == '' or mm == '' or dd == ''):
            st.error("There aren't input a data")
        elif submitBar:
            # print(type(cateBar))
            # expDate = (int(year),int(month),int(datebar))
            src.insertInv(nameBar, int(yy), int(mm), int(dd), priceBar, stockBar,cateBar)

elif (selInv == "Update"):
    # st.markdown("<h1 style='text-align: center;'>Inventory</h1>",
    # unsafe_allow_html=True)
    selAll = src.selectAllInv()
    st.table(selAll)
    with st.container():
        with st.form(key='insert', clear_on_submit=False):
            nav1, nav2, nav3, nav4, nav5, nav6, nav7, nav8 ,nav9= st.columns(
                [1, 1, 1, 1, 1, 1, 1,1, 0.5])
            with nav1:
                idDrugs = st.text_input(label='Select ID')
            with nav2:
                cateBar = st.selectbox(
                    label='Caetgory', options=['Obat Cair', 'Obat Kapsul','Obat Tablet',
                    'Obat Oles', 'Obat Suppositoria','Obat Tetes'
                    'Obat Inhaler', 'Obat Suntik', 'Obat Implan'])
            with nav3:
                nameBar = st.text_input(label='Name')
            with nav4:
                priceBar = st.text_input(label='Price')
            with nav5:
                stockBar = st.text_input(label='Stock')
            with nav6:
                yy = st.text_input(label="Exp (Year)")
            with nav7:
                mm = st.text_input(label='Exp (Month)')
            with nav8:
                dd = st.text_input(label='Exp (Date)')
            with nav9:
                st.text('Search')
                submitBar = st.form_submit_button(label='Do')
        if submitBar == True and (cateBar == '' or nameBar == '' or priceBar == '' or stockBar == '' or yy == '' or mm == '' or dd == ''):
            st.error("There aren't input a data")
        elif submitBar:
            # print(type(cateBar))
            # expDate = (int(year),int(month),int(datebar))
            src.updateInv(nameBar, int(yy), int(mm), int(dd), priceBar, stockBar,cateBar)

elif (selInv == "Delete"):
    selAll = src.selectAllInv()
    st.table(selAll)
    target = 'drugs'
    with st.container():
        with st.form(key='del-bar-inv', clear_on_submit=True):
            # st.markdown("<p style='text-align: left;'>Inventory</p>",
            #             unsafe_allow_html=True)
            nav1, nav2, nav3 = st.columns([1, 3, 0.5])
            with nav1:
                optionBar = st.selectbox(
                    label='Options', options=['id'])
            with nav2:
                delBar = st.text_input(label='Values')
            with nav3:
                st.text('Delete')
                submitBar = st.form_submit_button(label='Do')
        if submitBar:
            src.delData(target,int(delBar))

