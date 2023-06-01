import streamlit as st
import io
import utils

with open('favicon.png', 'rb') as f:
    favicon = io.BytesIO(f.read())

st.set_page_config(page_title='Ask your pdf',
                   page_icon=favicon, 
                   initial_sidebar_state='expanded',layout='wide')
# st.sidebar.image("./siemens_logo.png", width = 150)

st.sidebar.title("Please upload pdf file")
temp = st.sidebar.file_uploader(label='', type=['pdf'])

st.title('Ask your PDF')

if temp:
    text = st.text_input('Please input your query and hit enter')
    st.write('Your query is:', text)

    file_contents = temp.getvalue()
    file_loc = 'sample.pdf' #tmp_file.name
    # Write the contents of the file to a specific location
    with open(file_loc, 'wb') as f:
        f.write(file_contents)   

    if st.button('Get response'):
        model_name = 'MBZUAI/LaMini-Flan-T5-783M'
        st.write(f'Model - {model_name}')
        utils.load_model(model_name)
        utils.get_docs(file_loc)
        answer = utils.get_response(text)
        st.write(answer.formatted_answer)
    
        



