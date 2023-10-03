#streamlit entry point

#importing dependencies
import streamlit as st
from langchain.llms import Cohere
from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain

#setting main page title
st.title("Microservify 💻🚀")
st.divider()
st.header("Microservice Code Generator")

#provide llm provider options (OpenAI, Anthropic, Cohere, etc.)
with st.sidebar:
    selected_provider = st.selectbox("Pick an LLM provider", ["OpenAI", "Cohere"])
    api_key = st.text_input(f"Enter your {selected_provider} API Key", type="password")
    st.divider()
    st.subheader("About")
    st.write("Microservify is a microservice code generation tool, powered by the magic of generative large language models and prompt chaining. Enter an LLM provider API key, mention the microservice concept and functionality you require, and pick a programming language. Hit submit and let Microservify generate it for you!")
    st.write("Hint: be specific and provide context in the prompt, and get a human to review/edit the code after generation")
    

#first step of logic, generating microservice outline from user prompt
def microservice_outline(concept, llm):
    #prompt
    template = "You are an expert programmer well versed with multiple programming languages and coding paradigms. You are very proficient at planning and creating microservices with code. You have been granted the task of generating a comprehensive outline for a microservice, which will include all the flows and top level architectural design describing it. The required microservice is described as follows: {concept}."
    prompt = PromptTemplate(input_variables=["topic"], template=template)
    prompt_query = prompt.format(concept=concept)
    #run llm model
    response = llm(prompt_query)
    return st.info(response)

#second step of logic, generating the actual code from user prompt
def microservice_code_generation(outline, llm, code_language):
    #prompt 
    template = "You are an expert programmer well versed with multiple programming languages and coding paradigms. You are very proficient at creating the microservice code from a given outline given to you that you have to follow, and you have to do this now. Here is the outline: {outline}. Generate the code."
    prompt = PromptTemplate(input_variables=["topic"], template=template)
    prompt_query = prompt.format(outline=outline)
    #run llm model and display loading spinner during generation
    with st.spinner("Generating code..."):
        response = llm(prompt_query)
    return st.code(response, language=code_language)

#third step of logic: preemptively fixing bugs or styling issues and conventions
def microservice_code_checker(gen_code, llm, code_language):
    template = "You are an expert programmer well versed with multiple programming languages and coding paradigms. You are a very efficient debugger and code optimizer as well, and have good knowledge of best code structuring and formatting paradigms. You can can catch potential errors or bugs and fix them when given some code. You will be given some code now. Apply your review skills and go over the code to see if there are any mistakes and fix them. If there any improvements to be made, make the improvements. Here is the code: {gen_code}"
    prompt = PromptTemplate(input_variables=["topic"], template=template)
    prompt_query = prompt.format(gen_code=gen_code)
    #run llm model and display loading spinner during generation
    with st.spinner("Generating code..."):
        response = llm(prompt_query)
    return st.code(response, language=code_language)

def llm_instance(api_key, selected_provider):
    if selected_provider=="Cohere":
        llm = Cohere(model_name="command-nightly", cohere_api_key=api_key)
    elif selected_provider=="OpenAI":
        llm=OpenAI(openai_api_key=api_key)
    return llm

with st.form("form1"):
    topic_text = st.text_input("Describe the concept/idea of the microservice you want generated:", "")
    submitted = st.form_submit_button("Submit")
    if not api_key:
        st.info(f"Please enter your {selected_provider} API key first!")
    elif submitted:
        #setup instance of llm provider
        llm = llm_instance(api_key, selected_provider)
        outline = microservice_outline(topic_text, llm)
        #send outline response to next step
        generated_code = microservice_code_generation(outline, llm)
        reviewed_code = microservice_code_checker(generated_code, llm)




