#app.py
import app1
import app2
import app3
import streamlit as st
from PIL import Image

st.set_page_config(
        page_title="IBA Proof of concept",
        page_icon="chart_with_upwards_trend",
    
    )


image = Image.open('IBA.png')
st.title('Trascender Global Intelligent business analyst IBA')

#st.image(image)


PAGES = {
    "1. Main": app1,
    "2. Dataset conceps and explanation": app2,
    "3. Where magic happens": app3
}
st.sidebar.title('Steps selection')
selection = st.sidebar.radio("Go to", list(PAGES.keys()))
page = PAGES[selection]
page.app()