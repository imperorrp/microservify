#streamlit entry point

#importing dependencies
import streamlit as st
from langchain.llms import Cohere
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain

#setting main page title
st.title("🦜🔗 Microservify - Microservice Code Generator ")

#provide llm provider options (OpenAI, Anthropic, Cohere, etc.)
#currently just a Cohere model
cohere_api_key = st.sidebar.text_input("Cohere API Key", type="password")

#first step of logic, generating microservice outline from user prompt
def microservice_outline(concept):
    #instantiate LLM model
    llm = Cohere(model_name="command-nightly", cohere_api_key=cohere_api_key)
    #prompt
    template = "You are an expert programmer well versed with multiple programming languages and coding paradigms. You are very proficient at planning and creating microservices with code. You have been granted the task of generating a comprehensive outline for a microservice, which will include all the flows and top level architectural design describing it. The required microservice is described as follows: {concept}."
    prompt = PromptTemplate(input_variables=["topic"], template=template)
    prompt_query = prompt.format(concept=concept)
    #run llm model
    response = llm(prompt_query)
    #print results
    return st.info(response)

#todo: rest of the logic chain (generation + review)

with st.form("form1"):
    topic_text = st.text_input("Describe the concept/idea of the microservice you want generated:", "")
    submitted = st.form_submit_button("Submit")
    if not cohere_api_key:
        st.info("Please enter your Cohere API key to continue.")
    elif submitted:
        microservice_outline(topic_text)

