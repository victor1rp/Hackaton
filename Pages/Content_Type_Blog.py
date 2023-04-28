import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd
import datetime
import altair as alt


def Blog():
    col1, col2 = st.columns([1,20])
    with col1: 
        st.image('https://www.hu.nl/static/images/share.png', width=30)
    with col2:
        st.markdown(' **:blue[HU MINORS]**')
    # Add code for home page
    st.header('BIG DATA & DESIGN - ENGLISH')
    st.divider()
    col1, col2 = st.columns([4,1])
    with col1:
        st.markdown('We believe that you, as a future specialist in any field, need to acquire the necessary skills to work with data. Employers are not only desperately looking for specialists with practical knowledge of data, but also to people who can translate insights into creative data-driven designs.')
        st.markdown('In the minor Big Data & Design, you learn to work on projects and relevant topics during in-depth classes. During 1-week design crunches you will work on assignments for real clients and develop your own start-up ideas. We will work from your background and motivation to use data in your context and focus on current technologies, look at future possibilities from a design, technical, business, and ethical point of view. You will learn basic programming in python, which will help you feel comfortable when working with data and prototyping your concepts, but you do not need to be a hardcore computer scientist to do this!')
        st.markdown('Companies in all domains are looking for go-getters with practical knowledge of data and skills to translate insights into solutions. What are you waiting for!?')
        st.subheader('Learning Objectives')
        st.markdown("After this minor you can: ")
        st.markdown("""
        1. Critically examine the impact of big data on our society.
        2. Use design research to create innovative data-driven concepts.
        3. Collect, clean, analyse and visualise data from various sources through tools and basic programming. 
        4. Create and communicate insights, predictions and actions from data using basic machine learning techniques and statistics. 
        5. Learn new skills and methods within design research and data science using a self-directed, experimental, inquisitive learning style. 
        """)
    with col2:
        st.subheader('Practical')
        st.markdown('**Part of Institute**')
        st.caption('Institute of Media')
        st.markdown("**Part of Bachelor's Degree**")
        st.caption('Communication and Multimedia Design')
        st.markdown('**Osiriscode**')
        st.caption('JM-BDD-22')
        st.markdown('**Period and participants**')
        st.caption('AB: 28 maximum')
        st.markdown('**Lesson days**')
        st.caption('Class days are not yet known')
        st.markdown('**Questions about this minor?**')
        st.caption('Contact: :blue[Lars Heemskerk]')
    st.markdown('')
    st.divider()
    st.subheader('Like this page? Share it with your friends')
    st.markdown('')    
    st.markdown('')
    st.markdown('')

    #Share This Section

    # Current URL to share
    url = "http://localhost:8512/Content_Type_Blog"

    # Social Media Share PAge
    twitter_url = f"https://twitter.com/intent/tweet?url={url}"
    facebook_url = f"https://www.facebook.com/sharer/sharer.php?u={url}"
    linkedin_url = f"https://www.linkedin.com/shareArticle?url={url}"
    reddit_url = f"https://www.reddit.com/submit?url={url}"
    whatsapp_url = f"https://wa.me/?text={url}"
    pinterest_url = f"https://pinterest.com/pin/create/button/?url={url}"

    instagram_url = f"https://www.instagram.com/?url={url}"

    # Social Media Logo
    icons = {
        "twitter": "https://img.icons8.com/color/48/000000/twitter--v1.png",
        "facebook": "https://img.icons8.com/color/48/000000/facebook-new--v1.png",
        "linkedin": "https://img.icons8.com/color/48/000000/linkedin.png",
        "reddit": "https://img.icons8.com/color/48/000000/reddit.png",
        "whatsapp": "https://img.icons8.com/color/48/000000/whatsapp--v1.png",
        "pinterest": "https://img.icons8.com/color/48/000000/pinterest--v1.png",
        "instagram": "https://img.icons8.com/color/48/000000/instagram-new--v1.png"
    }

    # Social Media Button
    col1, col2, col3, col4, col5, col6, col7 = st.columns(7)

    with col1:
        st.markdown(f"[![Twitter]({icons['twitter']})]({twitter_url})")

    with col2:
        st.markdown(f"[![Facebook]({icons['facebook']})]({facebook_url})")

    with col3:
        st.markdown(f"[![Linkedin]({icons['linkedin']})]({linkedin_url})")

    with col4:
        st.markdown(f"[![Reddit]({icons['reddit']})]({reddit_url})")

    with col5:
        st.markdown(f"[![WhatsApp]({icons['whatsapp']})]({whatsapp_url})")

    with col6:
        st.markdown(f"[![Pinterest]({icons['pinterest']})]({pinterest_url})")

    with col7:
        st.markdown(f"[![Instagram]({icons['instagram']})]({instagram_url})") 

    #Amount of Share in Each Social
    col1, col2, col3, col4, col5, col6, col7 = st.columns(7)

    with col1:
        st.markdown('&nbsp;&nbsp;&nbsp;454')

    with col2:
        st.markdown('&nbsp;&nbsp;&nbsp;454')

    with col3:
        st.markdown('&nbsp;&nbsp;&nbsp;454')

    with col4:
        st.markdown('&nbsp;&nbsp;&nbsp;454')

    with col5:
        st.markdown('&nbsp;&nbsp;&nbsp;454')

    with col6:
        st.markdown('&nbsp;&nbsp;&nbsp;454')

    with col7:
        st.markdown('&nbsp;&nbsp;&nbsp;454')       

# Define app title and favicon
st.set_page_config(page_title="Mett Hackaton", page_icon=":bar_chart:", layout="wide")

def run_app():

    Blog()

if __name__ == '__main__':
    run_app()