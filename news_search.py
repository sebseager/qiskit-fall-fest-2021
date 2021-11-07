import requests
import numpy as np
import qiskit
from qiskit.quantum_info import Statevector
import streamlit as st


def keywords_satisfied(text, keywords):
    ans = [0] * len(keywords)
    for j in range(len(text)):
        for i in range(len(keywords)):
            if keywords[i] == text[j]:
                ans[i] = 1
    return sum(ans)


def oracle(article, keywords):
    n = keywords_satisfied(article, keywords)
    return 1 / (2 ** (len(keywords) - n))


# change article.text to whatever the API defines
def encode_articles(articles, keywords):
    sum = 0
    results = []
    for i in range(len(articles)):
        results.append(oracle(articles[i], keywords))
        sum += results[i] ** 2
    for i in range(len(articles)):
        results[i] = (1 / (sum ** (1 / 2))) * results[i]
    return results


# encoding step
def find_article(articles, keywords):
    encoded_vector = list(encode_articles([x[1] for x in articles], keywords))
    encoded_vector = np.array(encoded_vector)
    state_vector = Statevector(data=encoded_vector)
    chosen_article = articles[int(state_vector.measure()[0], 2)]
    return chosen_article[0], chosen_article[2]


@st.cache()
def pull_articles(news_country, api_key):
    # api call
    base_url = "https://newsapi.org/v2/top-headlines"
    country = f"country={news_country}&" if len(news_country) else ""
    x = requests.get(f"{base_url}?{country}apiKey={api_key}")
    try:
        articles = dict(x.json())["articles"]
    except KeyError:
        st.error("Invalid API call")
        return

    # process articles from api
    processed_articles = []
    for a in articles:
        if a["content"]:
            new_content = a["content"].lower().replace(".,![]{}-—_;':?", "").split()
            new_title = a["title"]
            new_url = a["url"]
            processed_articles.append((new_title, new_content, new_url))

    return processed_articles


def main():
    st.title("<@YAS ADD A GOOD TITLE HERE>")
    st.header("1. Pull articles from NewsAPI")

    api_key = st.text_input("NewsAPI key", value="b72aad9271604a1b888e9479c9de4fb7")
    news_country = st.text_input("News country/region to search", value="us")

    # keywords to check for
    st.header("2. Perform search")
    search_input = st.text_input("Keywords to search for (separated by spaces)")

    if st.button("Run"):
        all_articles = pull_articles(news_country, api_key)
        article_summary = st.text(f"Articles found: {len(all_articles)}")

        # grab article
        search_keywords = search_input.split(" ")
        print(search_keywords)
        print("BREAK")
        print(all_articles)
        received_article = find_article(all_articles, search_keywords)
        try:
            st.text(f"Article: {received_article[0]}")
            st.text(f"URL: {received_article[1]}")
        except IndexError:
            st.error("No articles found")


if __name__ == "__main__":

    main()
