# app2.py
import streamlit as st
import streamlit as st
import pandas as pd
import plotly.express as px
import random, string
import importlib
import os
from codex import code




def app():
    
    #st.balloons()
    df = pd.read_csv("data.csv")
    st.title("Where magic happens 🤖")
    st.markdown('**Example of how to use it, just write a simple sentence to know details about the data**.')
    st.write("Example: show the property with more bedrooms")







    form = st.form(key='my-form')
    sentence = form.text_input('Write a sentence into Natural Language to translate to code')
    submit = form.form_submit_button('Submit')

    st.write('Press submit to generate code')

    if submit:
        content=code(sentence)
        #content=content+"TestStrategy=5"


        strategy_name = ''.join(random.choices(string.ascii_letters + string.digits, k=8)) 
        with open(strategy_name+'.py', 'w') as the_file:
            the_file.write(content)
        TestStrategy = getattr(importlib.import_module(strategy_name), 'TestStrategy')
        if os.path.exists(strategy_name+'.py'):
            os.remove(strategy_name+'.py')
        else:
            print("The file does not exist")