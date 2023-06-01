from langchain.embeddings import HuggingFaceEmbeddings
from transformers import pipeline
from langchain.llms import HuggingFacePipeline
from paperqa import Docs
import streamlit as st

model_name = "MBZUAI/LaMini-Flan-T5-783M" #using an open-source model. 
# You can choose a model of your choice available at https://huggingface.co/models
embeddings = HuggingFaceEmbeddings()
model = pipeline('text2text-generation', model = model_name)
local_llm = HuggingFacePipeline(pipeline=model, model_kwargs={"temperature":0.2})
docs = Docs(llm=local_llm, embeddings=embeddings)

@st.cache_resource
def get_docs(file_loc):    
    my_docs = [file_loc] # you can add other document paths based on the documents you are querying
    for d in set(my_docs):
        docs.add(d,chunk_chars = 3000)

def get_response(query):     
    answer = docs.query(query)
    return answer
