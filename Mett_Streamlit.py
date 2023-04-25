# -*- coding: utf-8 -*-
"""
Created on Thu Apr 13 15:32:47 2023
Updated on Fri Apr 14 18:33:33 2023
Updated on Sat Apr 15 11:15:00 2023
Updated on Sun Apr 16 16:45:25 2023
Updated on Tue Apr 18 10:21:54 2023
@author: Victor
"""

import requests
import json
import streamlit as st
import matplotlib.pyplot as plt

# Home page section
def home():
    # Add code for home page
    st.title('Home Page')
    st.header('Blogpost HU Website')
    st.write('Lorem Epsum')

# Basic Performance section
def Basic():
    # Add code for user page
    st.title('Performance Overview')
#Top 5 KPI's for today (or maxbe adjustable time frame)
#1 Page Views
#2 Time spent on site
#3 Engagement-Rate
#4 Visitors
#5 Bounce-Rate

# User Origin section
def Orgin():
    # Add code for user page
    st.title('Where You get your users from')
    st.header('Nudity Classes and sub-classes')
    st.write('There are 5 main Nudity Classes, each subdivided into further sub-classes. The classes are presented here in descending order of expliciteness, from the most explicit (sexual activity) down to the safest.')
 

# Understanding Trends
def Trends():
    # Add code for uploading image page
    st.title('Upload Image Page')
    st.subheader('Prototype Nudity AI Detector')

#Comparisons with past day/month
#1 New visitors development
#2 Engagement-Rate
#3 Page Views
#4 Returning visitors
#5 average time spent on site (absolute or per visitor)

#Content Analysis
def Analysis():

#Which day highest engagement rate in the past 7 weeks
#WHich day highest bounce rate?
#Which day highest amount of visitors
# Which day highest amount of new visitors
#Which day highest page views

# Create a dictionary to store the pages
pages = {
    'Home': home,
    'Basic': Basic,
    'Origin': Origin,
    'Trends': Trends
    'Analysis': Analysis,
}

# Define app title and favicon
st.set_page_config(page_title="Nudity AI Detector", page_icon=":camera:", layout="wide")

# Create a function to run the selected page
def run_app():

    # Display the selected page
    page = st.sidebar.selectbox('Select a page', list(pages.keys()))
    pages[page]()

if __name__ == '__main__':
    run_app()