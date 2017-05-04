import re
import os
import requests
from bs4 import BeautifulSoup
from flask import Flask, render_template, send_from_directory

app = Flask(__name__)


@app.route('/')
def index():
    response = requests.get('https://www.nytimes.com/section/world/americas')
    soup = BeautifulSoup(response.text, 'html.parser')
    links = []
    for a in soup.find_all('a', { 'class' : 'story-link' }):
        href = a.get('href')
        slug = re.search(r'/([\w+-]+).html$', href).group(1)

        # write file
        if not os.path.isfile('templates/articles/{}.html'.format(slug)):
            with open('templates/articles/{}.html'.format(slug), 'a') as write_file:
                response = requests.get(href)
                page_text = response.text
                write_file.write(page_text.encode('utf-8'))
                print 'wrote file!'

        links.append({
            'href': 'templates/articles/{}.html'.format(slug),
            'slug': slug
        })
    return render_template('index.html', links=links)


@app.route('/templates/articles/<path:path>')
def templates(path):
    return send_from_directory('templates/articles', path)


if __name__ == "__main__":
    # app.run()
    app.run(debug=True)
