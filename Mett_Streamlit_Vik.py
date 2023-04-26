
import requests
import json
import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd
import datetime

df = pd.read_excel("C:/Users/vikto/OneDrive - Stichting Hogeschool Utrecht/Block 2 Learning from data - Hackathon/Hackathon/Hackaton/MOCK_METT_final.xlsx")

#Changing type from object to datatime64 to date
df['Date'] = pd.to_datetime(df['Date'])
df['Date'] = df['Date'].dt.date


# Home page section
def Home():
    # Add code for home page
    st.title('Home Page')
    st.header('Blogpost HU Website')
    st.write('Lorem Epsum')
    st.markdown(
         f"""
         <style>
         .stApp {{
             background-image: url("https://imgur.com/a/W6hSkrZ");
             background-attachment: fixed;
             background-size: cover
         }}
         </style>
         """,
         unsafe_allow_html=True
     )


# Basic Performance section
def Basic():
    # Add code for user page
    st.title('Performance Overview')
    
    #Providing todays date
    datetime.datetime(2022, 11, 25)
    
    user_date = st.date_input("Select your Date",
                            value = datetime.datetime(2022, 11, 25),
                            min_value = datetime.datetime(2022, 2, 1),
                            max_value = datetime.datetime(2022, 12, 31)
                            )
    
    #Provide dropdown menu, showing Today, Last week, Last month
    basic_option = st.selectbox(
        'Option',
        ('Today', 'Last week', 'Last month'))
    
    if basic_option == 'Today':
        basic_compare = 'Your overview of today is:'
    elif basic_option == 'Last week':
        basic_compare = 'Your overview of last week is:'
    elif basic_option == 'Last month':
        basic_compare = 'Your overview of last month is:'
    st.markdown(basic_compare)
        
    
    #Basic Performance Views
    if basic_option == 'Today':
        basic_views = df.loc[df['Date'] == user_date, 'page_views'].iloc[0]
    elif basic_option == 'Last week':
        basic_views = df.loc[(df['Date'] >= user_date - datetime.timedelta(days=7)) & (df['Date'] <= user_date)]['page_views'].sum()
    elif basic_option == 'Last month':
        basic_views = df.loc[(df['Date'] >= user_date - datetime.timedelta(days=31)) & (df['Date'] <= user_date)]['page_views'].sum()
    st.markdown(f'Total views: {basic_views}')
    
    
    #Basic Performance Time Spent on site
    if basic_option == 'Today':
        basic_time = df.loc[df['Date'] == user_date, 'time_on_site'].iloc[0]
    elif basic_option == 'Last week':
        basic_time = df.loc[(df['Date'] >= user_date - datetime.timedelta(days=7)) & (df['Date'] <= user_date)]['time_on_site'].iloc[0].sum()
    elif basic_option == 'Last month':
        basic_time = df.loc[(df['Date'] >= user_date - datetime.timedelta(days=31)) & (df['Date'] <= user_date)]['time_on_site'].iloc[0].sum()
    st.markdown(f'Total Time spent on Site: {basic_time} seconds')
    
    
#Top 5 KPI's for today (or maxbe adjustable time frame)
#1 Page Views
#2 Time spent on site
#3 Engagement-Rate
#4 Visitors
#5 Bounce-Rate

# User Origin section
def Origin():
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
   st.title('Upload Image Page')
#Which day highest engagement rate in the past 7 weeks
#WHich day highest bounce rate?
#Which day highest amount of visitors
# Which day highest amount of new visitors
#Which day highest page views

# Create a dictionary to store the pages
pages = {
    'Home': Home,
    'Basic': Basic,
    'Origin': Origin,
    'Trends': Trends,
    'Analysis': Analysis
}

# Define app title and favicon
#st.set_page_config(page_title="Nudity AI Detector", page_icon=":camera:", layout="wide")

# Create a function to run the selected page
def run_app():

    # Display the selected page
    page = st.sidebar.selectbox('Select a page', list(pages.keys()))
    pages[page]()

if __name__ == '__main__':
    run_app()