#https://api.quotable.io/random
#Создайте простое веб-приложение, которое будет запрашивать случайные цитаты
# с публичного API и отображать их на странице

from flask import Flask, render_template, request
import requests

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    quote = get_random_quote()
    return render_template("index_dz.html", quote=quote)

def get_random_quote():
    url = "https://api.quotable.io/random"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return {"content": "Ошибка получения цитаты", "author": "Неизвестный"}

if __name__ == '__main__':
    app.run(debug=True)