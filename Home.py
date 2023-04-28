
import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd
import datetime
import altair as alt

# Home page section
def Home():
    # Add code for home page
    st.title('Measurable Engagement')
    st.header('Hackaton - Mett')
    col1, col2 = st.columns(2)
    with col1:
        st.subheader("Welcome to Mett!") 
        st.markdown("As a SaaS company, we understand the importance of providing our customers with the tools they need to succeed. We're excited to share that we're currently rebuilding our entire product to make it even better than before.")
        st.markdown("One of our top priorities in Mett 4 is to provide our customers with better insights into how their platform is performing. We want to offer performance information in an accessible manner, so our customers can work and think in a result-oriented way.")
    with col2:
        st.markdown('')
        st.markdown('')
        st.markdown('')
        st.markdown('')
        st.image('data:image/png;base64,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')
    st.markdown('In the left side you will find the different :blue[**Content Types,  the New Implementations and Dashboards**].')
    st.divider()
    col1,col2 = st.columns(2)
    with col1:
        st.subheader('&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Design Group')
        st.caption('Albert Kamara | Annette Holst | Joshua Scott')
    with col2:
        st.subheader('&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Tech Group')
        st.caption('Laurens Lilja | Victor Rios Pinto | Viktor van Mun')
    

# Define app title and favicon
st.set_page_config(page_title="Mett Hackaton", page_icon=":bar_chart:", layout="wide")

# Create a function to run the selected page
def run_app():

    # Display the selected page
    Home()

if __name__ == '__main__':
    run_app()