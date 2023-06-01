from langchain.embeddings import HuggingFaceEmbeddings
from transformers import pipeline
from langchain.llms import HuggingFacePipeline
from paperqa import Docs
import streamlit as st

model_name = "MBZUAI/LaMini-Neo-125M" #using an open-source model. 
# You can choose a model of your choice available at https://huggingface.co/models
embeddings = HuggingFaceEmbeddings()
model = pipeline('text2text-generation', model = model_name)
local_llm = HuggingFacePipeline(pipeline=model, model_kwargs={"temperature":0.2})

@st.cache_data
def get_docs(file_loc):
    docs = Docs(llm=local_llm, embeddings=embeddings)
    my_docs = [file_loc] # you can add other document paths based on the documents you are querying
    for d in set(my_docs):
        docs.add(d,chunk_chars = 2000)
    return docs

@st.cache_data
def get_response(_docs,query):     
    answer = _docs.query(query)
    return answer
