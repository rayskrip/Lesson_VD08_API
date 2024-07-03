from flask import Flask, render_template, request
import requests

app = Flask(__name__)


@app.route('/')
def index():
    response = requests.get('https://api.quotable.io/random')
    if response.status_code == 200:
        data = response.json()
        quote = data.get('content', 'No quote found')
        author = data.get('author', 'Unknown')
    else:
        quote = 'Error fetching quote'
        author = 'N/A'

    return render_template('index.html', quote=quote, author=author)


if __name__ == '__main__':
    app.run(debug=True)