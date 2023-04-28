import streamlit as st


    
def Post():
    # Add code for home page
    st.title('Post Page')
    st.header('Video Post HU Website')
    col1,col2 = st.columns(2)
    with col1:
        st.markdown(f'<iframe width="365" height="425" src="https://www.youtube.com/embed/Ig_f96ji4ig" frameborder="0" allowfullscreen></iframe>', unsafe_allow_html=True)
    with col2:
        col1, col2 = st.columns([1,7])
        with col1: 
            st.image('https://www.hu.nl/static/images/share.png', width=40)
            st.markdown('')
            st.markdown('')
            st.markdown('')
            st.image('https://www.hu.nl/static/images/share.png', width=40)
            st.markdown('')
            st.markdown('')
            st.markdown('')
            st.markdown('')
            st.markdown('')
            st.markdown('')
            st.markdown('')
            st.markdown('')
            st.markdown('')
            st.markdown('')
            st.markdown('')
            st.image('https://pbs.twimg.com/media/FjU2lkcWYAgNG6d.jpg', width=40)
        with col2:
            st.markdown('**hogeschoolutrecht** • :blue[Follow]')
            st.divider()
            st.markdown('**hogeschoolutrecht**&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Kom naar de open dag op 18 maart of 1 april, geen grap.')
            st.markdown('<span style="color: gray">#studiekeuze #studiekeuzeadvies #studiekiezen #opendag #hogeschool #studeren #opleiding #meelopen #proefstuderen #proefcollege #hbo #pov #pointofview</span>', unsafe_allow_html=True)
            st.markdown('')
            st.markdown('')
            st.markdown('**user**&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;:raised_hands: &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;♡')
            st.markdown('<span style="color: gray">Reply</span>', unsafe_allow_html=True)
    st.divider()
    st.write('## 🤍&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 🗨️&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; ✉️' )
    st.write('###### 203 likes &nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 45 comments&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 20 shares')
    st.markdown('<span style="color: gray">MARCH 9</span>', unsafe_allow_html=True)
    st.divider()
    col1, col2 = st.columns([18,1])
    with col1:
        st.text_area('😀',placeholder='Add Comment.....', label_visibility= "hidden")
    with col2:
        st.markdown('')
        st.markdown('')
        st.markdown('')
        st.markdown('')
        st.markdown(':blue[Post]')


# Define app title and favicon
st.set_page_config(page_title="Mett Hackaton", page_icon=":bar_chart:", layout="wide")

def run_app():

    Post()

if __name__ == '__main__':
    run_app()