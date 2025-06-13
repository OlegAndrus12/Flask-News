import os
import requests

from flask import Flask, render_template, request

NEWS_API_KEY = os.environ.get('DATABASE_URL')

app = Flask(__name__)

@app.route('/')
def index():
    query = request.args.get('query', 'latest')
    url = f'https://newsapi.org/v2/everything?q={query}&apiKey={NEWS_API_KEY}'
    response = requests.get(url)
    response.raise_for_status()
    news_data = response.json()
    articles = news_data.get('articles', [])

    # Filter out Yahoo articles and articles with "removed" in the title
    filtered_articles = [
        article for article in articles 
        if 'Yahoo' not in article['source']['name'] and 'removed' not in article['title'].lower()
    ]

    return render_template('index.html', articles=filtered_articles, query=query)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
