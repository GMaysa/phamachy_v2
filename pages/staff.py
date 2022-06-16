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
    page_icon=icon,
)

st.markdown("<h1 style='text-align: center;'>Staff Data</h1>",
            unsafe_allow_html=True)
selStaff = som.option_menu(
    menu_title=None,
    options=["All", "Search", "Insert", "Update","Delete"],
    icons=['list', 'search','arrow-down-square','arrow-up-square', 'x-square'],
    menu_icon=None,
    default_index=0,
    orientation='horizontal')

if (selStaff == "All"):
    order = st.multiselect('Order By',
                           ['admin','staff frontline','staff warehouse'],['admin','staff frontline'])
    selBy = src.orderByStaff(order)
    st.table(selBy)

elif (selStaff == "Search"):
    # st.markdown("<h1 style='text-align: center;'>Inventory</h1>",
    # unsafe_allow_html=True)
    with st.container():
        with st.form(key='search-bar-staff', clear_on_submit=False):
            # st.markdown("<p style='text-align: left;'>Inventory</p>",
            #             unsafe_allow_html=True)
            nav1, nav2, nav3 = st.columns([1, 3, 0.5])
            with nav1:
                optionBar = st.selectbox(
                    label='Options', options=['username','position'])
            with nav2:
                searchBar = st.text_input(label='Values', value="search")
            with nav3:
                st.text('Search')
                submitBar = st.form_submit_button(label='Do')
        if submitBar == True and searchBar == '':
            st.error("There aren't input a data")
        elif submitBar:
            try:
                dfSearch = src.likeSrcStaff(optionBar, searchBar)
            except ValueError:
                if optionBar == "id":
                    try:
                        print(int(searchBar))
                    except:
                        st.error("You only can search a Book ID using a number")
            else:
                dfSearch = src.likeSrcStaff(optionBar, searchBar)
                st.success("Your searched for {} in {}".format(
                    searchBar, optionBar))
                st.table(dfSearch)

elif (selStaff == "Insert"):
    # st.markdown("<h1 style='text-align: center;'>Inventory</h1>",
    # unsafe_allow_html=True)
    with st.container():
        with st.form(key='insert-bar-staff', clear_on_submit=False):
            # st.markdown("<p style='text-align: left;'>Inventory</p>",
            #             unsafe_allow_html=True)
            nav1, nav2, nav3 ,nav4,nav5,nav6= st.columns([1, 1, 1,1,1,0.5])
            with nav1:
                occBar = st.selectbox(label='Position', options=['admin','staff warehouse','staff frontline'])
            with nav2:
                nameBar = st.text_input(label='Username')
            with nav3:
                genBar = st.selectbox(label='Gender', options=['L','P'])
            with nav4:
                emailBar = st.text_input(label='Email',value='@gmail.com')
            with nav5:
                passBar = st.text_input(label='Password')
            with nav6:
                st.text('Submit')
                submitBar = st.form_submit_button(label='Do')
                src.insertStaff(nameBar,genBar,emailBar,passBar,occBar)
elif (selStaff == "Update"):
    # st.markdown("<h1 style='text-align: center;'>Inventory</h1>",
    # unsafe_allow_html=True)
    with st.container():
        with st.form(key='insert-bar-staff', clear_on_submit=False):
            # st.markdown("<p style='text-align: left;'>Inventory</p>",
            #             unsafe_allow_html=True)
            nav1, nav2, nav3, nav4, nav5, nav6, nav7 = st.columns(
                [1, 1, 1, 1, 1, 1,0.5])
            with nav1:
                idBar = st.text_input(label='Id Staff')
            with nav2:
                occBar = st.selectbox(label='Position', options=[
                                      'admin', 'staff warehouse', 'staff frontline'])
            with nav3:
                nameBar = st.text_input(label='Username')
            with nav4:
                genBar = st.selectbox(label='Gender', options=['L', 'P'])
            with nav5:
                emailBar = st.text_input(label='Email', value='@gmail.com')
            with nav6:
                passBar = st.text_input(label='Password')
            with nav7:
                st.text('Submit')
                submitBar = st.form_submit_button(label='Do')
        if submitBar:
            src.updateStaff(nameBar,genBar,emailBar,passBar,occBar,idBar)

elif (selStaff == 'Delete'):
    selAll = src.selectAllStaff()
    st.table(selAll)
    target = 'staff'
    with st.container():
        with st.form(key='del-bar-staff', clear_on_submit=False):
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
            src.delData(target, int(delBar))
