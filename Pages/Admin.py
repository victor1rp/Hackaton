
import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd
import datetime
import altair as alt

df = pd.read_csv("C:/Users/victo/Documents/GitHub/Hackaton/MOCK_METT_final.csv")


#Changing type from object to datatime64 to date
df['Date'] = pd.to_datetime(df['Date'])
df['Date'] = df['Date'].dt.date
  

    
def Blog_Analytic():
    # Add code for home page
    st.title('Blog Page')
    st.header('Blogpost HU Website')
         
    
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
    
def Post_Analytic():
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
    st.markdown(f'Total post views: {basic_views}')
    
    
    #Basic Performance Time Spent on site
    if basic_option == 'Today':
        basic_time = df.loc[df['Date'] == user_date, 'time_on_site'].iloc[0]
    elif basic_option == 'Last week':
        basic_time = df.loc[(df['Date'] >= user_date - datetime.timedelta(days=7)) & (df['Date'] <= user_date)]['time_on_site'].iloc[0].sum()
    elif basic_option == 'Last month':
        basic_time = df.loc[(df['Date'] >= user_date - datetime.timedelta(days=31)) & (df['Date'] <= user_date)]['time_on_site'].iloc[0].sum()
    st.markdown(f'Total Time spent on Site: {basic_time} seconds')

def Survey_Analytic():
    # Add code for home page
    st.title('Survey Page')
    st.header('Survey HU Website')
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


    

# Create a dictionary to store the pages
pages = {
    "Visitor Engagement Insights?": Blog_Analytic,
    "Measure Community Engagement and Growth?": Post_Analytic,
    "Foster User Engagement and Co-Creation?": Survey_Analytic
}



# Define app title and favicon
st.set_page_config(page_title="Mett Hackaton", page_icon=":bar_chart:", layout="wide")

# Create a function to run the selected page
def run_app():

    # Display the selected page
    page = st.sidebar.selectbox('Choose Your Engagement Metrics', list(pages.keys()))
    pages[page]()

if __name__ == '__main__':
    run_app()