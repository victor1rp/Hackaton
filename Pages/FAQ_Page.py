import streamlit as st
import pandas as pd
import altair as alt

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

def run_app():

    FAQ()

if __name__ == '__main__':
    run_app()   