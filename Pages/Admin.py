
import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd
import datetime
import altair as alt

df = pd.read_csv("C:/Users/victo/Documents/GitHub/Hackaton/MOCK_METT_final.csv")


df['Date'] = pd.to_datetime(df['Date'])
df['Date'] = df['Date'].dt.date
df.drop('Unnamed: 0', axis=1, inplace=True)
df = df.sort_values(by = 'Date')
  

    
def Blog_Analytic():
    # Add code for blog page
    col1, col2 = st.columns([4,1])
    with col1:
        st.title('Blog Analytic')
    with col2:
        st.button('Export Data')
    #Create and define columns, info left column, graphs right column
    col1, col2 = st.columns(2)
    with col1:
    
    
        # Add code for user page
        st.header('Visitor Engagement')
    
        
        #Providing todays date
        ##Copy/Paste from line 43 through 72
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
            basic_compare = 'Your overview of Past week is:'
        elif basic_option == 'Last month':
            basic_compare = 'Your overview of Past month is:'
        st.subheader(basic_compare)
            
        
        #Basic Performance Views
        if basic_option == 'Today':
            basic_views = df.loc[df['Date'] == user_date, 'page_views'].iloc[0] #change basic_views variable and adjust 'page_views' column to one of your liking, same for other 2 basic_views variables
        elif basic_option == 'Last week':
            basic_views = df.loc[(df['Date'] >= user_date - datetime.timedelta(weeks=1)) & (df['Date'] <= user_date)]['page_views'].sum()
            with col2:
                fig, ax = plt.subplots(figsize=(4,4))
                ax.plot(df.loc[(df['Date'] >= user_date - datetime.timedelta(weeks=1)) & (df['Date'] <= user_date)]['Date'], df.loc[(df['Date'] >= user_date - datetime.timedelta(weeks=1)) & (df['Date'] <= user_date)]['page_views'])
                plt.title('Viewcount of past week')
                plt.ylabel('Viewcount')
                plt.xticks(rotation = 45)
                st.pyplot(fig)
        elif basic_option == 'Last month':
            basic_views = df.loc[(df['Date'] >= user_date - datetime.timedelta(weeks=4)) & (df['Date'] <= user_date)]['page_views'].sum()
            with col2:
                fig, ax = plt.subplots(figsize=(4,4))
                ax.plot(df[(df['Date'] >= user_date - datetime.timedelta(weeks=4)) & (df['Date'] <= user_date)]['Date'], df[(df['Date'] >= user_date - datetime.timedelta(weeks=4)) & (df['Date'] <= user_date)]['page_views'])
                plt.title('Viewcount of past month')
                plt.ylabel('Viewcount')
                plt.xticks(rotation = 45)
                st.pyplot(fig)
        st.markdown(f'Total page views: {basic_views}') #what is in between brackets is the variable, rest is text you want to show
        
        #Basic Performance Time Spent on post
        if basic_option == 'Today':
            basic_time = round(df.loc[df['Date'] == user_date, 'time_on_site'].iloc[0]/basic_views)
        elif basic_option == 'Last week':
            basic_time = round(df.loc[(df['Date'] >= user_date - datetime.timedelta(weeks=1)) & (df['Date'] <= user_date)]['time_on_site'].sum()/basic_views)
        elif basic_option == 'Last month':
            basic_time = round(df.loc[(df['Date'] >= user_date - datetime.timedelta(weeks=4)) & (df['Date'] <= user_date)]['time_on_site'].sum()/basic_views)
        st.markdown(f'Average time spent on Blog: {basic_time} seconds')

        #Basic Performance Bounce Rate
        if basic_option == 'Today':
            basic_bounce = round(df.loc[df['Date'] == user_date, 'bounce_rate'].iloc[0], 2)
        elif basic_option == 'Last week':
            basic_bounce = round((df.loc[(df['Date'] >= user_date - datetime.timedelta(weeks=1)) & (df['Date'] <= user_date)]['bounce_rate'].mean()), 2)
            with col2:
                fig, ax = plt.subplots(figsize=(4,4))
                ax.plot(df.loc[(df['Date'] >= user_date - datetime.timedelta(weeks=1)) & (df['Date'] <= user_date)]['Date'], df.loc[(df['Date'] >= user_date - datetime.timedelta(weeks=1)) & (df['Date'] <= user_date)]['bounce_rate'])
                plt.title('Bounce rate of past week')
                plt.ylabel('Bounce rate in %')
                plt.xticks(rotation = 45)
                st.pyplot(fig)
        elif basic_option == 'Last month':
            basic_bounce = round((df.loc[(df['Date'] >= user_date - datetime.timedelta(weeks=4)) & (df['Date'] <= user_date)]['bounce_rate'].mean()), 2)
            with col2:
                fig, ax = plt.subplots(figsize=(4,4))
                ax.plot(df[(df['Date'] >= user_date - datetime.timedelta(weeks=4)) & (df['Date'] <= user_date)]['Date'], df[(df['Date'] >= user_date - datetime.timedelta(weeks=4)) & (df['Date'] <= user_date)]['bounce_rate'])
                plt.title('Bounce rate of past month')
                plt.ylabel('Bounce rate in %')
                plt.xticks(rotation = 45)
                st.pyplot(fig)
        st.markdown(f'Average Bounce Rate: {basic_bounce} %')

        
        #Basic Performance Total Shares
        if basic_option == 'Today':
            basic_shares = df.loc[df['Date'] == user_date, 'social_shares'].iloc[0]
        elif basic_option == 'Last week':
            basic_shares = df.loc[(df['Date'] >= user_date - datetime.timedelta(weeks=1)) & (df['Date'] <= user_date)]['social_shares'].sum()
            with col2:
                fig, ax = plt.subplots(figsize=(4,4))
                ax.plot(df.loc[(df['Date'] >= user_date - datetime.timedelta(weeks=1)) & (df['Date'] <= user_date)]['Date'], df.loc[(df['Date'] >= user_date - datetime.timedelta(weeks=1)) & (df['Date'] <= user_date)]['social_shares'])
                plt.title('Share count of past week')
                plt.ylabel('Share count')
                plt.xticks(rotation = 45)
                st.pyplot(fig)
        elif basic_option == 'Last month':
            basic_shares = df.loc[(df['Date'] >= user_date - datetime.timedelta(weeks=4)) & (df['Date'] <= user_date)]['social_shares'].sum()
            with col2:
                fig, ax = plt.subplots(figsize=(4,4))
                ax.plot(df[(df['Date'] >= user_date - datetime.timedelta(weeks=4)) & (df['Date'] <= user_date)]['Date'], df[(df['Date'] >= user_date - datetime.timedelta(weeks=4)) & (df['Date'] <= user_date)]['social_shares'])
                plt.title('Share count of past month')
                plt.ylabel('Share count')
                plt.xticks(rotation = 45)
                st.pyplot(fig)
        st.markdown(f'Total Shares: {basic_shares}') 
        
        # Implementing Bar chart overview for Today
        with col2:
            if basic_option == 'Today':
                fig, ax = plt.subplots(figsize=(4,4))
                x = ['Total views', 'Total shares']
                y = [basic_views, basic_shares]
                ax.bar(x, y)
                st.pyplot(fig)
        
        # Summary overview
        with col1:
            if basic_option == 'Today':
                st.title('Summary')
                #Engagement rate below by weighting the share more
                basic_engage = round((basic_shares/basic_views)*100)
                st.markdown(f'In summary today your Engagement rate is {basic_engage}%. Given your **Blog Content Type** any rate above 10% is considered above average.')
                st.markdown('Wish to boost a specific KPI or get to understand how Engagement rate is calculated?')
                st.markdown(':blue[Contact] us to book an appointment!')
                #Improvements, perhaps do a scale of 1-5 of how good engagement is?
    
def Post_Analytic():
    # Add code for home page
    col1, col2 = st.columns([4,1])
    with col1:   
        st.title('Post Analytic')
    with col2:
        st.button('Export Data')
    #Create and define columns, info left column, graphs right column
    col1, col2 = st.columns(2)
    with col1:
    
    
        # Add code for user page
        st.header('Community Engagement')
    
        
        #Providing todays date
        ##Copy/Paste from line 43 through 72
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
            basic_compare = 'Your overview of Past week is:'
        elif basic_option == 'Last month':
            basic_compare = 'Your overview of Past month is:'
        st.markdown(basic_compare)
            
        
        #Basic Performance Views
        if basic_option == 'Today':
            basic_views = df.loc[df['Date'] == user_date, 'page_views'].iloc[0] #change basic_views variable and adjust 'page_views' column to one of your liking, same for other 2 basic_views variables
        elif basic_option == 'Last week':
            basic_views = df.loc[(df['Date'] >= user_date - datetime.timedelta(weeks=1)) & (df['Date'] <= user_date)]['page_views'].sum()
            with col2:
                fig, ax = plt.subplots(figsize=(4,4))
                ax.plot(df.loc[(df['Date'] >= user_date - datetime.timedelta(weeks=1)) & (df['Date'] <= user_date)]['Date'], df.loc[(df['Date'] >= user_date - datetime.timedelta(weeks=1)) & (df['Date'] <= user_date)]['page_views'])
                plt.title('Viewcount of past week')
                plt.ylabel('Viewcount')
                plt.xticks(rotation = 45)
                st.pyplot(fig)
        elif basic_option == 'Last month':
            basic_views = df.loc[(df['Date'] >= user_date - datetime.timedelta(weeks=4)) & (df['Date'] <= user_date)]['page_views'].sum()
            with col2:
                fig, ax = plt.subplots(figsize=(4,4))
                ax.plot(df[(df['Date'] >= user_date - datetime.timedelta(weeks=4)) & (df['Date'] <= user_date)]['Date'], df[(df['Date'] >= user_date - datetime.timedelta(weeks=4)) & (df['Date'] <= user_date)]['page_views'])
                plt.title('Viewcount of past month')
                plt.ylabel('Viewcount')
                plt.xticks(rotation = 45)
                st.pyplot(fig)
        st.markdown(f'Total post views: {basic_views}') #what is in between brackets is the variable, rest is text you want to show
        
        #Basic Performance Time Spent on post
        if basic_option == 'Today':
            basic_time = round(df.loc[df['Date'] == user_date, 'time_on_site'].iloc[0]/basic_views)
        elif basic_option == 'Last week':
            basic_time = round(df.loc[(df['Date'] >= user_date - datetime.timedelta(weeks=1)) & (df['Date'] <= user_date)]['time_on_site'].sum()/basic_views)
        elif basic_option == 'Last month':
            basic_time = round(df.loc[(df['Date'] >= user_date - datetime.timedelta(weeks=4)) & (df['Date'] <= user_date)]['time_on_site'].sum()/basic_views)
        st.markdown(f'Average time spent on Post: {basic_time} seconds')
        
        #Basic Performance Bounce Rate
        if basic_option == 'Today':
            basic_bounce = round(df.loc[df['Date'] == user_date, 'bounce_rate'].iloc[0], 2)
        elif basic_option == 'Last week':
            basic_bounce = round((df.loc[(df['Date'] >= user_date - datetime.timedelta(weeks=1)) & (df['Date'] <= user_date)]['bounce_rate'].mean()), 2)
            with col2:
                fig, ax = plt.subplots(figsize=(4,4))
                ax.plot(df.loc[(df['Date'] >= user_date - datetime.timedelta(weeks=1)) & (df['Date'] <= user_date)]['Date'], df.loc[(df['Date'] >= user_date - datetime.timedelta(weeks=1)) & (df['Date'] <= user_date)]['bounce_rate'])
                plt.title('Bounce rate of past week')
                plt.ylabel('Bounce rate in %')
                plt.xticks(rotation = 45)
                st.pyplot(fig)
        elif basic_option == 'Last month':
            basic_bounce = round((df.loc[(df['Date'] >= user_date - datetime.timedelta(weeks=4)) & (df['Date'] <= user_date)]['bounce_rate'].mean()), 2)
            with col2:
                fig, ax = plt.subplots(figsize=(4,4))
                ax.plot(df[(df['Date'] >= user_date - datetime.timedelta(weeks=4)) & (df['Date'] <= user_date)]['Date'], df[(df['Date'] >= user_date - datetime.timedelta(weeks=4)) & (df['Date'] <= user_date)]['bounce_rate'])
                plt.title('Bounce rate of past month')
                plt.ylabel('Bounce rate in %')
                plt.xticks(rotation = 45)
                st.pyplot(fig)
        st.markdown(f'Average Bounce Rate: {basic_bounce} %')
        
        #Basic Performance Total Shares
        if basic_option == 'Today':
            basic_shares = df.loc[df['Date'] == user_date, 'social_shares'].iloc[0]
        elif basic_option == 'Last week':
            basic_shares = df.loc[(df['Date'] >= user_date - datetime.timedelta(weeks=1)) & (df['Date'] <= user_date)]['social_shares'].sum()
            with col2:
                fig, ax = plt.subplots(figsize=(4,4))
                ax.plot(df.loc[(df['Date'] >= user_date - datetime.timedelta(weeks=1)) & (df['Date'] <= user_date)]['Date'], df.loc[(df['Date'] >= user_date - datetime.timedelta(weeks=1)) & (df['Date'] <= user_date)]['social_shares'])
                plt.title('Share count of past week')
                plt.ylabel('Share count')
                plt.xticks(rotation = 45)
                st.pyplot(fig)
        elif basic_option == 'Last month':
            basic_shares = df.loc[(df['Date'] >= user_date - datetime.timedelta(weeks=4)) & (df['Date'] <= user_date)]['social_shares'].sum()
            with col2:
                fig, ax = plt.subplots(figsize=(4,4))
                ax.plot(df[(df['Date'] >= user_date - datetime.timedelta(weeks=4)) & (df['Date'] <= user_date)]['Date'], df[(df['Date'] >= user_date - datetime.timedelta(weeks=4)) & (df['Date'] <= user_date)]['social_shares'])
                plt.title('Share count of past month')
                plt.ylabel('Share count')
                plt.xticks(rotation = 45)
                st.pyplot(fig)
        st.markdown(f'Total Shares: {basic_shares}') 
        
        #Basic Performance Total Comments
        if basic_option == 'Today':
            basic_comments = df.loc[df['Date'] == user_date, 'social_comments'].iloc[0]
        elif basic_option == 'Last week':
            basic_comments = df.loc[(df['Date'] >= user_date - datetime.timedelta(weeks=1)) & (df['Date'] <= user_date)]['social_comments'].sum()
            with col2:
                fig, ax = plt.subplots(figsize=(4,4))
                ax.plot(df.loc[(df['Date'] >= user_date - datetime.timedelta(weeks=1)) & (df['Date'] <= user_date)]['Date'], df.loc[(df['Date'] >= user_date - datetime.timedelta(weeks=1)) & (df['Date'] <= user_date)]['social_comments'])
                plt.title('Comments count of past week')
                plt.ylabel('Comments count')
                plt.xticks(rotation = 45)
                st.pyplot(fig)
        elif basic_option == 'Last month':
            basic_comments = df.loc[(df['Date'] >= user_date - datetime.timedelta(weeks=4)) & (df['Date'] <= user_date)]['social_comments'].sum()
            with col2:
                fig, ax = plt.subplots(figsize=(4,4))
                ax.plot(df[(df['Date'] >= user_date - datetime.timedelta(weeks=4)) & (df['Date'] <= user_date)]['Date'], df[(df['Date'] >= user_date - datetime.timedelta(weeks=4)) & (df['Date'] <= user_date)]['social_comments'])
                plt.title('Comments count of past month')
                plt.ylabel('Comments count')
                plt.xticks(rotation = 45)
                st.pyplot(fig)
        st.markdown(f'Total Comments: {basic_comments}') 
        
        #Basic Performance Total Like
        if basic_option == 'Today':
            basic_likes = df.loc[df['Date'] == user_date, 'social_likes'].iloc[0]
        elif basic_option == 'Last week':
            basic_likes = df.loc[(df['Date'] >= user_date - datetime.timedelta(weeks=1)) & (df['Date'] <= user_date)]['social_likes'].sum()
            with col2:
                fig, ax = plt.subplots(figsize=(4,4))
                ax.plot(df.loc[(df['Date'] >= user_date - datetime.timedelta(weeks=1)) & (df['Date'] <= user_date)]['Date'], df.loc[(df['Date'] >= user_date - datetime.timedelta(weeks=1)) & (df['Date'] <= user_date)]['social_shares'])
                plt.title('Likes count of past week')
                plt.ylabel('Likes count')
                plt.xticks(rotation = 45)
                st.pyplot(fig)
        elif basic_option == 'Last month':
            basic_likes = df.loc[(df['Date'] >= user_date - datetime.timedelta(weeks=4)) & (df['Date'] <= user_date)]['social_likes'].sum()
            with col2:
                fig, ax = plt.subplots(figsize=(4,4))
                ax.plot(df[(df['Date'] >= user_date - datetime.timedelta(weeks=4)) & (df['Date'] <= user_date)]['Date'], df[(df['Date'] >= user_date - datetime.timedelta(weeks=4)) & (df['Date'] <= user_date)]['social_likes'])
                plt.title('Likes count of past month')
                plt.ylabel('Like count')
                plt.xticks(rotation = 45)
                st.pyplot(fig)
        st.markdown(f'Total Likes: {basic_likes}') 
        
        # Implementing Bar chart overview for Today
        with col2:
            if basic_option == 'Today':
                fig, ax = plt.subplots(figsize=(4,4))
                x = ['Total views', 'Total shares']
                y = [basic_views, basic_shares]
                ax.bar(x, y)
                st.pyplot(fig)
        
        # Summary overview
        with col1:
            if basic_option == 'Today':
                st.title('Summary')
                #Engagement rate below is calculated by by weighing likes more than shares and comments 
                basic_engage = ((basic_shares) + (basic_likes * 2) + (basic_comments)) /4
                st.markdown(f'In summary today your **Community Engagement** rate is {basic_engage}%. Given your **Post Content Type** any rate above 50% is considered above average.')
                st.markdown('Wish to boost a specific KPI or get to understand how Engagement rate is calculated?')
                st.markdown(':blue[Contact] us to book an appointment!')
                #Improvements, perhaps do a scale of 1-5 of how good engagement is?


def Survey_Analytic():
    # Add code for home page
    col1, col2 = st.columns([4,1])
    with col1:   
        st.title('User Engagment')
    with col2:
        st.button('Export Data')
    
    #Create and define columns, info left column, graphs right column
    col1, col2 = st.columns(2)
    with col1:
    
        st.header('Performance Overview')
        
        #Providing todays date
        ##Copy/Paste from line 43 through 72
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
            basic_compare = 'Your overview of Past week is:'
        elif basic_option == 'Last month':
            basic_compare = 'Your overview of Past month is:'
        st.markdown(basic_compare)
    
        #Form submissions, column = form_submissions
            #for 1 week and 4 weeks do the same as above
        if basic_option == 'Today':
            form_subm = df.loc[df['Date'] == user_date, 'form_submissions'].iloc[0]
        elif basic_option == 'Last week':
            form_subm = df.loc[(df['Date'] >= user_date - datetime.timedelta(weeks=1)) & (df['Date'] <= user_date)]['form_submissions'].sum()
            with col2:
                fig, ax = plt.subplots(figsize=(4,4))
                ax.plot(df.loc[(df['Date'] >= user_date - datetime.timedelta(weeks=1)) & (df['Date'] <= user_date)]['Date'], df.loc[(df['Date'] >= user_date - datetime.timedelta(weeks=1)) & (df['Date'] <= user_date)]['form_submissions'])
                plt.title('Form submissions of past week')
                plt.ylabel('Form submissions')
                plt.xticks(rotation = 45)
                st.pyplot(fig)
        elif basic_option == 'Last month':
            form_subm = df.loc[(df['Date'] >= user_date - datetime.timedelta(weeks=4)) & (df['Date'] <= user_date)]['form_submissions'].sum()
            with col2:
                fig, ax = plt.subplots(figsize=(4,4))
                ax.plot(df[(df['Date'] >= user_date - datetime.timedelta(weeks=4)) & (df['Date'] <= user_date)]['Date'], df[(df['Date'] >= user_date - datetime.timedelta(weeks=4)) & (df['Date'] <= user_date)]['form_submissions'])
                plt.title('Form submissions of past month')
                plt.ylabel('Form submissions')
                plt.xticks(rotation = 45)
                st.pyplot(fig)
        st.markdown(f'Total Form submissions: {form_subm}')
        

        #Average time per form submission, = time_on_site/form_submissions
            #keep this as a one liner
        if basic_option == 'Today':
            basic_time = round(df.loc[df['Date'] == user_date, 'time_on_site'].iloc[0]/form_subm/60)
        elif basic_option == 'Last week':
            basic_time = round(df.loc[(df['Date'] >= user_date - datetime.timedelta(weeks=1)) & (df['Date'] <= user_date)]['time_on_site'].sum()/form_subm/60)
        elif basic_option == 'Last month':
            basic_time = round(df.loc[(df['Date'] >= user_date - datetime.timedelta(weeks=4)) & (df['Date'] <= user_date)]['time_on_site'].sum()/form_subm/60)
        st.markdown(f'Average time spent per form: {basic_time} minutes')
                
        
        #Share amount, column = social_shares
            #for 1 week and 4 weeks do the same as above
        if basic_option == 'Today':
            form_share = df.loc[df['Date'] == user_date, 'social_shares'].iloc[0]
        elif basic_option == 'Last week':
            form_share = df.loc[(df['Date'] >= user_date - datetime.timedelta(weeks=1)) & (df['Date'] <= user_date)]['social_shares'].sum()
            with col2:
                fig, ax = plt.subplots(figsize=(4,4))
                ax.plot(df.loc[(df['Date'] >= user_date - datetime.timedelta(weeks=1)) & (df['Date'] <= user_date)]['Date'], df.loc[(df['Date'] >= user_date - datetime.timedelta(weeks=1)) & (df['Date'] <= user_date)]['social_shares'])
                plt.title('Form shares past week')
                plt.ylabel('Form shares')
                plt.xticks(rotation = 45)
                st.pyplot(fig)
        elif basic_option == 'Last month':
            form_share = df.loc[(df['Date'] >= user_date - datetime.timedelta(weeks=4)) & (df['Date'] <= user_date)]['social_shares'].sum()
            with col2:
                fig, ax = plt.subplots(figsize=(4,4))
                ax.plot(df[(df['Date'] >= user_date - datetime.timedelta(weeks=4)) & (df['Date'] <= user_date)]['Date'], df[(df['Date'] >= user_date - datetime.timedelta(weeks=4)) & (df['Date'] <= user_date)]['social_shares'])
                plt.title('Form shares past month')
                plt.ylabel('Form shares')
                plt.xticks(rotation = 45)
                st.pyplot(fig)
        st.markdown(f'Total Form shares: {form_share}')
        
        #Subscription amount, column = email_subscriptions
            #for 1 week and 4 weeks do the same as above
        if basic_option == 'Today':
            form_sub = df.loc[df['Date'] == user_date, 'email_subscriptions'].iloc[0]
        elif basic_option == 'Last week':
            form_sub = df.loc[(df['Date'] >= user_date - datetime.timedelta(weeks=1)) & (df['Date'] <= user_date)]['email_subscriptions'].sum()
            with col2:
                fig, ax = plt.subplots(figsize=(4,4))
                ax.plot(df.loc[(df['Date'] >= user_date - datetime.timedelta(weeks=1)) & (df['Date'] <= user_date)]['Date'], df.loc[(df['Date'] >= user_date - datetime.timedelta(weeks=1)) & (df['Date'] <= user_date)]['email_subscriptions'])
                plt.title('E-mail subscriptions past week')
                plt.ylabel('E-mail subscriptions')
                plt.xticks(rotation = 45)
                st.pyplot(fig)
        elif basic_option == 'Last month':
            form_sub = df.loc[(df['Date'] >= user_date - datetime.timedelta(weeks=4)) & (df['Date'] <= user_date)]['email_subscriptions'].sum()
            with col2:
                fig, ax = plt.subplots(figsize=(4,4))
                ax.plot(df[(df['Date'] >= user_date - datetime.timedelta(weeks=4)) & (df['Date'] <= user_date)]['Date'], df[(df['Date'] >= user_date - datetime.timedelta(weeks=4)) & (df['Date'] <= user_date)]['email_subscriptions'])
                plt.title('E-mail subscriptions past month')
                plt.ylabel('E-mail subscriptions')
                plt.xticks(rotation = 45)
                st.pyplot(fig)
        st.markdown(f'Total e-mail subscriptions: {form_sub}')
        
        #Make bar chart for today only with form submissions, share amount and subscription amount
        # Implementing Bar chart overview for Today
        with col2:
            if basic_option == 'Today':
                fig, ax = plt.subplots(figsize=(4,4))
                x = ['Form submissions', 'Forms shared', 'E-mail subscriptions']
                y = [form_subm, form_share, form_sub]
                ax.bar(x, y)
                plt.xticks(rotation = 15)
                st.pyplot(fig)        
        
        # Summary
        with col1:
            if basic_option == 'Today':
                st.title('Summary')
                #Weighing the forms submission and shares more
                form_engage = ((form_sub) + (form_subm * 2) + (form_share * 2))/5
                st.markdown(f'In summary today your Engagement rate is {form_engage}%.')
                if form_engage >= 5:
                    st.markdown('Your engagement rate is above 5%, this is considered above average!')
                    st.markdown('Unsatisfied with the results?')
                elif form_engage < 5:
                    st.markdown('Your engagement rate is below 5%, this is considered below average.')
                    st.markdown('Wish to boost a specific KPI or get to understand how Engagement rate is calculated?')
                st.markdown(':blue[Contact] us to book an appointment!')


    

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