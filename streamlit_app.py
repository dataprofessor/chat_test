import streamlit as st

# Works on Community Cloud
# Works locally
with st.chat_message("assistant", avatar='🤖' ):
    st.write('Testing ... 1, 2, 3')

# Works on Community Cloud
# Works locally
with st.chat_message("assistant", avatar='https://streamlit.io/images/brand/streamlit-mark-color.png' ):
    st.write('Testing ... 1, 2, 3')

# Not working on Community Cloud
# Not working locally
image = 'streamlit.png'
with st.chat_message("assistant", avatar=image ):
    st.write('Testing ... 1, 2, 3')

# Not working on Community Cloud
# Works locally
from PIL import Image
image = Image.open('streamlit.png')
with st.chat_message("assistant", avatar=image ):
    st.write('Testing ... 1, 2, 3')
