# Import necessary libraries
import streamlit as st  # For creating interactive web applications
from langchain.llms import AzureOpenAI  # LangChain library for interacting with Azure OpenAI
from langchain import PromptTemplate  # LangChain library for creating prompt templates
import os  # For setting environment variables

# Set environment variables for Azure OpenAI
os.environ["OPENAI_API_TYPE"] = ""
os.environ["OPENAI_API_VERSION"] = ""
os.environ["OPENAI_API_BASE"] = ""
os.environ["OPENAI_API_KEY"] = ""

# Initialize an instance of AzureOpenAI with specific settings
llm = AzureOpenAI(temperature=0, deployment_name='text-davinci-003')

# Define a template for prompts using LangChain
template = """
%INSTRUCTIONS:
Please summarize the following piece of text.
Respond in a manner that a 20-year-old would understand.
%TEXT:
{text}
"""

# Create a PromptTemplate using the defined template
prompt = PromptTemplate(
    input_variables=["text"],  # Specify input variables used in the template
    template=template,
)

# Define the main Streamlit app function
def main():
    st.title("Text Summarizer")  # Set the title for the Streamlit app

    # Create a text input area for user to enter confusing text
    confusing_text = st.text_area("Enter the text:", "")  

    if st.button("Summarize"):  # Create a button that triggers summarization

        # Fill in the prompt template with user input and store it in final_prompt
        final_prompt = prompt.format(text=confusing_text)

        st.write("Below you can find the summary")  # Display a message

        # Use the AzureOpenAI instance to generate a summary based on the final_prompt
        output = llm(final_prompt)
        st.write(output)  # Display the generated summary

# Run the Streamlit app if this script is being executed directly
if __name__ == "__main__":
    main()
