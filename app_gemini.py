import os
import streamlit as st
from langchain.prompts import PromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI

# Set Google API Key
os.environ["GOOGLE_API_KEY"] = "your_api_key"  

## Function To get response from Gemini
def getGeminiResponse(input_text, no_words, blog_style):
    llm = ChatGoogleGenerativeAI(model="models/gemini-1.5-flash", temperature=0.7)

    # Prompt Template
    template = """
        Write a blog in {blog_style} style on the topic "{input_text}" 
        within {no_words} words.
    """
    prompt = PromptTemplate(
        input_variables=["blog_style", "input_text", "no_words"],
        template=template,
    )

    formatted_prompt = prompt.format(
        blog_style=blog_style, input_text=input_text, no_words=no_words
    )

    # Generate response
    response = llm.invoke(formatted_prompt)
    return response.content


# Streamlit UI
st.set_page_config(page_title="Generate Blogs", page_icon='🤖', layout='centered')

st.header("Generate Blogs 🤖")

input_text = st.text_input("Enter the Blog Topic")

col1, col2 = st.columns([5, 5])
with col1:
    no_words = st.text_input('No of Words')
with col2:
    blog_style = st.selectbox(
        'Writing the blog for',
        ('Researchers', 'Data Scientist', 'Common People'),
        index=0
    )

submit = st.button("Generate")

if submit:
    if input_text and no_words:
        with st.spinner("Generating blog..."):
            result = getGeminiResponse(input_text, no_words, blog_style)
            st.write(result)
    else:
        st.warning("Please enter both topic and number of words.")
