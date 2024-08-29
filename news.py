import streamlit as st
import requests
from langchain.prompts import ChatPromptTemplate
from langchain_ollama.llms import OllamaLLM
from typing import List, Dict
import dotenv
import os

# Load environment variables
dotenv.load_dotenv()
news_api_key = os.getenv("NEWS_API_KEY")


# Function to fetch news articles based on a query
def fetch_news(query: str) -> List[Dict]:
    url = f"https://newsapi.org/v2/everything?q={query}&apiKey={news_api_key}"
    response = requests.get(url)
    data = response.json()
    articles = data.get("articles", [])
    return articles


# Function to summarize text using the LLaMA model
def summarize_text(text: str) -> str:
    template = "Summarize the following text: {text}"
    prompt_template = ChatPromptTemplate.from_template(template=template)
    prompt = prompt_template.format_messages(text=text)
    model = OllamaLLM(model="llama3.1")
    response = model.invoke(prompt)
    return response


# Function to categorize a summary into predefined categories
def categorize_summary(summary: str) -> str:
    categories = ["Technology", "Health", "Finance", "Sports", "Entertainment", "Science"]
    template = "Categorize the following text into one of these categories: {categories}. Text: {text}"
    prompt_template = ChatPromptTemplate.from_template(template=template)
    prompt = prompt_template.format_messages(categories=", ".join(categories), text=summary)
    model = OllamaLLM(model="llama3.1")
    response = model.invoke(prompt)
    return response


# Streamlit Interface
def main():
    st.title("News Summarizer and Categorizer")

    # User input for news query
    query = st.text_input("Enter a topic to search for news:")

    if st.button("Fetch News"):
        if query:
            # Fetch news articles
            articles = fetch_news(query)
            if articles:
                for i, article in enumerate(articles):
                    st.subheader(f"Article {i + 1}: {article['title']}")
                    st.write(f"Source: {article['source']['name']}")
                    st.write(article['description'])

                    if st.button(f"Summarize Article {i + 1}"):
                        with st.spinner('Summarizing...'):
                            summary = summarize_text(article['description'] or article['content'])
                            st.write("Summary:", summary)

                            if st.button(f"Categorize Summary {i + 1}"):
                                with st.spinner('Categorizing...'):
                                    category = categorize_summary(summary)
                                    st.write("Category:", category)
            else:
                st.write("No articles found for the given query.")
        else:
            st.write("Please enter a query to search for news.")


if __name__ == "__main__":
    main()
