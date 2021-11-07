# Quantum Inspired News Suggestions

## Qiskit Fall Fest 2021 at Yale

Our project allows users to specify a country/region for their news and keywords that they want to search for, from which they will recieve an article suggestion. We use a statevector that is in a superposition of possible article outputs, with the probability of being measured increasing if more of the desired keywords are present. The statevector is measured and the cooresponding article title and url is returned. The goal is for users to recieve variation in their news suggestions, inspired by quantum mechanics, while still recieving relevant suggestions with high probability. We hope to inspire an interest in quantum mechanics and quantum computing with a fun suggestion tool that introduces some variation into users' daily news.

## Setup

This project has the a few basic package requirements, which can be installed as follows:

```bash
pip install requests qiskit streamlit
```

Alternately, use the corresponding install commands for your package manager of choice.

To run the `streamlit` server, run the following in the project directory:

```bash
streamlit run news_search.py
```

Then, in your browser, open the webapp on the port specified by `streamlit`, e.g., `http://localhost:8501`.

Follow the web interface to use our project! Alternatively, take a look at our Jupyter notebook (`news_search.ipynb`) for a static demonstration.

## Usage

You can obtain an API key at `newsapi.org` or use the one provided.

Country code may be one of the following:

```
ae ar at au be bg br ca ch cn co cu cz de eg fr gb gr hk hu id ie il in it jp kr lt lv ma mx my ng nl no nz ph pl pt ro rs ru sa se sg si sk th tr tw ua us ve za
```

## Authors

Yasmina Abukhadra, Ben Foxman, Seb Seager
