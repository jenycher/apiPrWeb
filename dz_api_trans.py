from flask import Flask, render_template, request
import requests
from googletrans import Translator

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    quote = get_random_quote()
    translated_quote = translate_quote(quote['content'], 'en', 'ru')
    return render_template("index_dz_trans.html", quote=quote, translated_quote=translated_quote)

def get_random_quote():
    url = "https://api.quotable.io/random"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return {"content": "Ошибка получения цитаты", "author": "Неизвестный"}

def translate_quote(text, src_lang, tgt_lang):
    translator = Translator()
    translation = translator.translate(text, src=src_lang, dest=tgt_lang)

    #word_definition_ru = translator.translate(word_definition, dest="ru").text
    return translation.text

if __name__ == '__main__':
    app.run(debug=True)
