import os
import requests

from flask import Flask, render_template, request

NEWS_API_KEY = os.environ.get('NEWS_API_KEY')

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

@app.route('/fireworks')
def get_fireworks():
    return render_template('fireworks.html')

@app.route('/birthday')
def get_birthday():
    return render_template('birthday.html')

@app.route('/baby')
def get_baby():
    return render_template('baby-wants-milk.html')

@app.route('/clock')
def get_clock():
    return render_template('clock.html')

@app.route('/organs')
def get_organs():
    return render_template('organs.html')

@app.route('/wand')
def get_wand():
    return render_template('magic-wand.html')

@app.route('/color')
def get_color():
    return render_template('random-color.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
