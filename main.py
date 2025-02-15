from langchain_google_genai import ChatGoogleGenerativeAI
from langchain import LLMChain
from langchain import PromptTemplate

import streamlit as st
import os

os.environ['GOOGLE_API_KEY'] = st.secrets['GOOGLE_API_KEY']

# Create prompt template for generating tweets

tweet_template = "Give me {number} tweets on {topic}"

tweet_prompt = PromptTemplate(template = tweet_template, input_variables = ['number', 'topic'])

# Initialize Google's Gemini model
gemini_model = ChatGoogleGenerativeAI(model = "gemini-1.5-flash-latest")


# Create LLM chain using the prompt template and model
tweet_chain = tweet_prompt | gemini_model


Recipe_template = "Give me {number} {type} recipes of {topic}"
Recipe_prompt = PromptTemplate(template = Recipe_template, input_variables = ['number','topic','type'])
recipe_chain = Recipe_prompt | gemini_model


st.markdown(
    """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@300;400;600&display=swap');

    .stApp {
        background: linear-gradient(to right, #ff7e5f, #feb47b);
        color: #ffffff;  /* White text color */
        font-family: 'Montserrat', sans-serif;
    }

    /* Ensures all text inside the app uses Montserrat */
   .stTitle, .stHeader, .stSubheader {
        font-family: 'Montserrat', sans-serif !important;
    }
    </style>
    """,
    unsafe_allow_html=True
)


st.header("Recipe Generator 🍔")

st.subheader("Generate recipes using Generative AI")

topic = st.text_input("Topic")

number = st.number_input("Number of recipes", min_value = 1, max_value = 10, value = 1, step = 1)

type = st.pills("Tags", ["Vegan", "Vegetarian", "Non-Vegetarian"])

if st.button("Generate"):
    recipes = recipe_chain.invoke({"number" : number, "topic" : topic, "type" : type})
    st.write(recipes.content)
    

