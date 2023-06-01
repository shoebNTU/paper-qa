from langchain.embeddings import HuggingFaceEmbeddings
from transformers import pipeline
from langchain.llms import HuggingFacePipeline
from paperqa import Docs

model_name = "MBZUAI/LaMini-Flan-T5-783M" #using an open-source model. 
# You can choose a model of your choice available at https://huggingface.co/models
embeddings = HuggingFaceEmbeddings()
model = pipeline('text2text-generation', model = model_name)
local_llm = HuggingFacePipeline(pipeline=model, model_kwargs={"temperature":0.2})
docs = Docs(llm=local_llm, embeddings=embeddings)

def get_response(file_loc,query):
    my_docs = [file_loc] # you can add other document paths based on the documents you are querying
    for d in my_docs:
        docs.add(d,chunk_chars = 2000)  
    answer = docs.query(query)
    return answer