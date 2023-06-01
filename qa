import streamlit as st
import io
from tempfile import NamedTemporaryFile
import utils

with open('favicon.png', 'rb') as f:
    favicon = io.BytesIO(f.read())

st.set_page_config(page_title='Ask your pdf',
                   page_icon=favicon, 
                   initial_sidebar_state='expanded',layout='wide')
st.sidebar.image("./siemens_logo.png", width = 150)

st.sidebar.title("Please upload pdf file")
temp = st.sidebar.file_uploader(label='', type=['pdf'])

st.title('Ask your PDF')

if temp:
    text = st.text_input('Please enter your query')
    st.write('Your query is:', text)

    with NamedTemporaryFile(delete=False) as tmp_file:
        tmp_file.write(temp.read())
        # st.write("File saved to:", tmp_file.name)
    file_loc = tmp_file.name

    if st.button('Get response'):
        answer = utils.get_response(file_loc,text)
        st.write(answer.formatted_answer)
    
        



