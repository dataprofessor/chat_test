import streamlit as st

cloud_yes = '✅ Community Cloud'
cloud_no = '❌ Community Cloud'
local_yes = '✅ Local'
local_no = '❌ Local'

# Works on Community Cloud
# Works locally
st.write(cloud_yes, local_yes)
with st.chat_message("assistant", avatar='🤖' ):
    st.write('Testing ... 1, 2, 3')

# Works on Community Cloud
# Works locally
st.write(cloud_yes, local_yes)
with st.chat_message("assistant", avatar='https://streamlit.io/images/brand/streamlit-mark-color.png' ):
    st.write('Testing ... 1, 2, 3')

# Not working on Community Cloud
# Not working locally
st.write(cloud_no, local_no)
image = 'streamlit.png'
with st.chat_message("assistant", avatar=image ):
    st.write('Testing ... 1, 2, 3')

# Not working on Community Cloud
# Works locally
st.write(cloud_no, local_yes)
from PIL import Image
image = Image.open('streamlit.png')
with st.chat_message("assistant", avatar=image ):
    st.write('Testing ... 1, 2, 3')
