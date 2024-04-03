import streamlit as st
import os
from langchain.llms import AzureOpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain

# Set environment variables for AzureOpenAI API configuration
os.environ["OPENAI_API_TYPE"] = ""
os.environ["OPENAI_API_VERSION"] = ""
os.environ["OPENAI_API_BASE"] = "set your azure url"
os.environ["OPENAI_API_KEY"] = "set your azure api key or open api key"

# Create the main title for the web application
st.title("Code Evaluation or Generation")

# Define options for user selection
options_list = ["Evaluate", "Generate"]
model_list = ["text-davinci-003", "code-davinci-002"]

# Create dropdown select boxes for user input
selected_option = st.sidebar.selectbox("Select an option", options=options_list)
model_selection = st.sidebar.selectbox("Select a model", options=model_list)

# Create a text area for the user to input code snippet or prompt
user_input = st.text_area(label="Input area", placeholder="Enter code snippet or prompt here.")

# Handle user input based on selected option
if selected_option == "Evaluate" and model_selection:
    # Define PromptTemplates for different evaluation tasks
    prompt_templates = [
        PromptTemplate(input_variables=['code'], template='Evaluate the following code snippet: "{code}" and provide a response.'),
        PromptTemplate(input_variables=['code'], template='Is the following code complete? If not, what is missing: "{code}"'),
        PromptTemplate(input_variables=['code'], template='How many lines of code are there in the following snippet: "{code}"?')
    ]
    # Create an instance of AzureOpenAI with the selected model
    llm = AzureOpenAI(deployment_name=model_selection, model=model_selection, temperature=0)

    # Process user input and generate responses
    if user_input:
        response = []
        for template in prompt_templates:
            p_chain = LLMChain(llm=llm, prompt=template)
            result = p_chain.run(user_input)
            response.append(result)
        
        # Display evaluation results on the web application
        st.write("Code completion: ", response[1])
        st.write("Report: ", response[0])
        st.write("Number of lines of code: ", response[2])

if selected_option == "Generate" and model_selection:
    prompt_template = PromptTemplate(input_variables=['prompt'], template='{prompt}')
    llm = AzureOpenAI(deployment_name=model_selection, model=model_selection, temperature=0)
    p_chain = LLMChain(llm=llm, prompt=prompt_template)
    if user_input:
        generated_response = p_chain.run(user_input)
        st.write("Generated Response: ", generated_response)
