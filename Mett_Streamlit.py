
import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd
import datetime
import altair as alt

df = pd.read_csv("C:/Users/victo/Documents/GitHub/Hackaton/MOCK_METT_final.csv")


#Changing type from object to datatime64 to date
df['Date'] = pd.to_datetime(df['Date'])
df['Date'] = df['Date'].dt.date


# Home page section
def Home():
    # Add code for home page
    st.title('Home Page')
    st.header('Blogpost HU Website')
    st.write('Lorem Epsum')
    
    
def Blog():
    # Add code for home page
    st.title('Blog Page')
    st.header('Blogpost HU Website')
    st.write('Lorem Epsum')
    if st.button('Website Admin'):
            Blog_Analytic()
    
def Post():
    # Add code for home page
    st.title('Post Page')
    st.header('Video Post HU Website')
    st.write('Lorem Epsum')
    if st.button('Community Manager'):
            Post_Analytic

def Survey():
    # Add code for home page
    st.title('Survey Page')
    st.header('Survey HU Website')
    st.write('Lorem Epsum')
    if st.button('Co Creation Platform'):
            Survey_Analytic     

    
def Blog_Analytic():
    # Add code for home page
    st.title('Blog Page')
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
    
def Post_Analytic():
    # Add code for home page
    st.title('Post Page')
    st.header('Video Post HU Website')
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


def FAQ():
    # Add code for home page
    st.title('FAQ Page')
    st.header("Helping you understand the KPI's")
    # List of dictionaries containing variables, analytics, and examples
    faq = [
        {
            "variable": "Time on Site",
            "analytics": "Average time a visitor spends on the website",
            "example": pd.DataFrame({"Month": ["Jan", "Feb", "Mar"], "Time on Site": [3.5, 4.2, 3.9]})
        },
        {
            "variable": "Page Views",
            "analytics": "Number of pages viewed by visitors",
            "example": pd.DataFrame({"Month": ["Jan", "Feb", "Mar"], "Page Views": [100, 120, 90]})
        },
        {
            "variable": "Form Submissions",
            "analytics": "Number of forms submitted by visitors",
            "example": pd.DataFrame({"Month": ["Jan", "Feb", "Mar"], "Form Submissions": [10, 15, 20]})
        },
        {
            "variable": "Video Plays",
            "analytics": "Number of times a video is played on the website",
            "example": pd.DataFrame({"Month": ["Jan", "Feb", "Mar"], "Video Plays": [50, 60, 70]})
        },
        {
            "variable": "Social Shares",
            "analytics": "Number of times the website content is shared on social media",
            "example": pd.DataFrame({"Month": ["Jan", "Feb", "Mar"], "Social Shares": [20, 25, 30]})
        },
        {
            "variable": "Social Likes",
            "analytics": "Number of times the website content is liked on social media",
            "example": pd.DataFrame({"Month": ["Jan", "Feb", "Mar"], "Social Likes": [50, 70, 80]})
        },
        {
            "variable": "Social Comments",
            "analytics": "Number of comments made on the website content on social media",
            "example": pd.DataFrame({"Month": ["Jan", "Feb", "Mar"], "Social Comments": [10, 15, 20]})
        },
        {
            "variable": "Email Subscriptions", 
            "analytics": "Number of visitors who subscribe to the email list",
            "example": pd.DataFrame({"Month": ["Jan", "Feb", "Mar"], "Email Subscriptions": [5, 8, 10]})
        },
        {
            "variable": "Bounce Rate",
            "analytics": "Percentage of visitors who navigate away from the site after viewing only one page",
            "example": pd.DataFrame({"Month": ["Jan", "Feb", "Mar"], "Bounce Rate": [0.6, 0.5, 0.7]})
        },
        {
            "variable": "Visitors",
            "analytics": "Total number of visitors to the website",
            "example": pd.DataFrame({"Month": ["Jan", "Feb", "Mar"], "Visitors": [100, 150, 200]})
        },
        {   "variable": "New Visitors",
            "analytics": "Number of first-time visitors to the website",
            "example": pd.DataFrame({"Month": ["Jan", "Feb", "Mar"], "New Visitors": [50, 75, 100]})
        }
    ]


    # Loop through the faq list and create an expander widget for each question and answer pair
    for item in faq:
        with st.expander(f"{item['variable']} - {item['analytics']}"):
            chart = alt.Chart(item['example']).mark_line().encode(
                x='Month',
                y=alt.Y(f'{item["variable"]}', title=f'{item["analytics"]}')
            ).properties(
                width=500,
                height=300
            )
            st.altair_chart(chart)
            st.write("Explanation:")
            st.write(f"This graph shows the trend in {item['variable']} over time. The x-axis shows the time period, while the y-axis shows the value of the variable. In this case, the graph shows the trend in {item['variable']} over a period of time.")
    
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
    'Blog': Blog,
    'Post': Post,
    'Survey': Survey,
    'FAQ': FAQ
}




# Define app title and favicon
st.set_page_config(page_title="Mett Hackaton", page_icon=":bar_chart:", layout="wide")

# Create a function to run the selected page
def run_app():

    # Display the selected page
    page = st.sidebar.selectbox('Select a page', list(pages.keys()))
    pages[page]()

if __name__ == '__main__':
    run_app()