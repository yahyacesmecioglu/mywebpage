import streamlit as st

st.set_page_config(page_title="My Webpage", page_icon=":computer:", layout="wide")


with st.container():
    st.subheader("Hi, I am Yahya :wave:")
    st.title("A Student From Türkiye")
    st.write("I am learning Python and C# now.")



with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("What I do")
        st.write("##")
        st.write("Actually I did nothing but I will make some projects for soon... ")
        st.write("[My Github Profile >](https://github.com/yahyacesmecioglu)")

 
with st.container():  
    st.write("---")
    st.header("Contact Me!")
    st.write("##") 

    contact_form="""
    <form action="https://formsubmit.co/yahyacesmecioglu@gmail.com" method="POST">
     <input type="hidden" name="_captcha" value="false">
     <input type="text" name="name" placeholder="Yourname" required>
     <input type="email" name="email"placeholder="Your email"  required>
     <textarea name="message placeholder="Your message here" required></textarea>
     <button type="submit">Send</button>
</form>
    """    
left_column, right_column = st.columns(2)
with left_column:
    st.markdown(contact_form, unsafe_allow_html=True)
with right_column:
    st.empty()    

def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
local_css("style/style.css")









