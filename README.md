# Microservify
AI powered microservice code generator (brought to you by prompt chain magic)

## About 

Microservify is a simple Streamlit web app built around the core functionality of automating microservice code creation. Langchain is used for prompt templating and chaining, and Cohere's LLM models used as the generator. 

As with existing LLM based tools, producing perfect code that does exactly what it needs to is hard for generative AI. The creativity and uniqueness of requirements is proportional to the amount of bugs and flawed logic for generated code- meaning humans are still needed to look over and edit code before pushing into service. The bulk initial work, though, can be automated to a fairly good degree.

What makes the microservices architecture kind of code components especially suited for AI generation? Typically small code sizes falling well within token limits for most LLM models, lack of requirement to understand the entirety of a more monolithic codebase sprawl, and a user can just include relevant information in the initial prompt. 

Microservify leverages these benefits, making use of Langchain for prompt chaining to get step by step logic- first planning, then generating, and finally reviewing to pre-empt the human bug fixing process after generation. 

## Setup and Usage

1. Clone this repository 

`git clone https://github.com/imperorrp/microservify.git`

2. Install dependencies

`pip install -r requirements.txt`

3. Run with

`streamlit run streamlit_app.py` 

A local instance should then be up on localhost
## Coming Soon 

Support for more LLM providers and models.

