from flask import Flask, redirect, url_for
from flask import templating
import requests
import json

app = Flask(__name__)

TOKEN = "Bearer b0ab3b7c240759687eaac840a07b8ad7b56ad475d8c7ecd995647a3c33cb6065a2991b03034e167110d60ce54a96e48f32889a5502cbc196247d10208d4c703a1b68b4b2ea9e4db97ceb447b389eac8f20cb2ecf7a499763d963f0fa84c5f787458bfb64f52cc1765c37d8ef56ab5c632a933dcb145a3bfc2d5765b6dfaa821b"


def get_articles():
    response = requests.get("http://192.168.0.174:1337/api/articles", headers={
        "Authorization": TOKEN})
    return json.loads(response.content)


@app.route('/')
def index():  # put application's code here
    return redirect(url_for('article_list'))


@app.route('/list')
def article_list():
    articles = get_articles()
    return templating.render_template('article_list.html', articles=articles['data'])


@app.route('/article/<id>')
def article(id):
    response = requests.get("http://192.168.0.174:1337/api/articles/" + id, headers={"Authorization": TOKEN})
    article = json.loads(response.content)
    attrs = article['data']['attributes']
    return templating.render_template('index.html', attrs=attrs)


if __name__ == '__main__':
    app.run(host='0.0.0.0')
