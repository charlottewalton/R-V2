import streamlit as st
import streamlit_nested_layout

st.set_page_config(page_title='Image Recognition Validation Application',
                   page_icon=None, layout="wide", initial_sidebar_state="auto", menu_items=None)

left_side_col, right_side_col = st.columns(2)

with left_side_col:
    with st.container():
        col1, col2, col3 = st.columns(3)

        with col1:
            option1 = st.selectbox('Product1',
                                   ['Coin Cell 2CT', 'Optimum AA 4CT', 'Optimum AAA 8CT', 'Power Boost AA 8CT',
                                    'Power Boost AA 16CT', 'Power Boost AAA 8CT', 'Power Boost AAA 16CT',
                                    'Power Boost D 4CT', 'Power Boost C 4CT', 'Power Boost 9V 2CT', 'Out of Stock'],
                                   index=0, label_visibility="visible")

        with col2:
            option2 = st.text_input('Product2', value="Optimum AA 4CT", placeholder='Product Name')

        with col3:
            option3 = st.text_input('Product3', value="Optimum AAA 8CT", placeholder='Product Name')
    with st.container():
        col1, col2, col3 = st.columns(3)

        with col1:
            option4 = st.text_input('Product4', value="Coin Cell 2CT", placeholder='Product Name')

        with col2:
            option5 = st.text_input('Product5', value="Optimum AA 4CT", placeholder='Product Name')

        with col3:
            option6 = st.text_input('Product6', value="Optimum AAA 8CT", placeholder='Product Name')
    with st.container():
        col1, col2 = st.columns([1, 2])

        with col1:
            option7 = st.text_input('Product7', value="Power Boost AA 8CT", placeholder='Product Name')

        with col2:
            option8 = st.text_input('Product8', value="Power Boost AA 16CT", placeholder='Product Name')
    with st.container():
        col1, col2 = st.columns([1, 2])

        with col1:
            option9 = st.text_input('Product9', value="Power Boost AA 8CT", placeholder='Product Name')

        with col2:
            option10 = st.text_input('Product10', value="Power Boost AA 16CT", placeholder='Product Name')
    with st.container():
        col1, col2, col3 = st.columns(3)

        with col1:
            option11 = st.text_input('Product11', value="Power Boost AA 8CT", placeholder='Product Name')

        with col2:
            option12 = st.text_input('Product12', value="Power Boost AA 8CT", placeholder='Product Name')

        with col3:
            option13 = st.text_input('Product13', value="Power Boost AA 8CT", placeholder='Product Name')
    with st.container():
        col1, col2 = st.columns([1, 2])

        with col1:
            option14 = st.text_input('Product14', value="Power Boost AAA 8CT", placeholder='Product Name')

        with col2:
            option15 = st.text_input('Product15', value="Power Boost AAA 16CT", placeholder='Product Name')
    with st.container():
        col1, col2 = st.columns([1, 2])

        with col1:
            option16 = st.text_input('Product16', value="Power Boost AAA 8CT", placeholder='Product Name')

        with col2:
            option17 = st.text_input('Product17', value="Power Boost AAA 16CT", placeholder='Product Name')
    with st.container():
        col1, col2 = st.columns([1, 2])

        with col1:
            option18 = st.text_input('Product18', value="Power Boost AAA 8CT", placeholder='Product Name')

        with col2:
            option19 = st.text_input('Product19', value="Power Boost AAA 16CT", placeholder='Product Name')
    with st.container():
        col1, col2, col3 = st.columns(3)

        with col1:
            option20 = st.text_input('Product20', value="Power Boost 9V 2CT", placeholder='Product Name')

        with col2:
            option21 = st.text_input('Product21', value="Power Boost C 4CT", placeholder='Product Name')

        with col3:
            option22 = st.text_input('Product22', value="Power Boost D 4CT", placeholder='Product Name')

with right_side_col:
    st.image('https://www.qtraxweb.com/p/67974-331778-us/AR/50220337_85894922.JPG', caption=None, width=None,
             use_column_width=None, clamp=False, channels="RGB", output_format="auto")

# 'https://www.qtraxweb.com/p/67974-331778-us/AR/50220337_85894994.JPG'
