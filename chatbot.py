import langchain
import os
from langchain.chat_models import ChatOpenAI
from langchain.llms import openai,AzureOpenAI
from langchain.memory import ConversationBufferMemory
import streamlit as st

 

os.environ["OPENAI_API_TYPE"]=""
os.environ["OPENAI_API_VERSION"]=""
os.environ["OPENAI_API_BASE"]=""
os.environ["OPENAI_API_KEY"]=""

 

# Create a Langchain chat model

llm = AzureOpenAI(deployment_name="text-davinci-003")

 

# Create a prompt template for the chatbot

prompt_template = """

Hi, I'm a chatbot that can remember our conversation. What can I help you with today?

"""

 

# Create a ConversationBufferMemory to store the chatbot's conversation history

memory = ConversationBufferMemory()

 

from langchain.chains import ConversationChain,LLMChain

 

conversation = ConversationChain(

   llm=llm,

   memory=memory,

   # verbose=True

)

st.title("Chatbot")

user_input = st.text_input("What do you want to ask the chatbot?")

response = conversation.predict(input=user_input)

# conversation.predict(input="Hello, my name is Andrea")

st.write(response)