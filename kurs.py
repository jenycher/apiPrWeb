#выводит курсы валют с биржи coinex

from flask import Flask, jsonify

import requests

app = Flask(__name__)

# Новый URL для запроса котировок
API_URL = 'https://api.coinex.com/v2/spot/ticker?market=BTCUSDT,LTCUSDT,BELlSCOINUSDT,DOGEUSDT'


@app.route('/', methods=['GET'])
def get_ticker():
    try:
        # Отправляем запрос к API
        response = requests.get(API_URL)
        response.raise_for_status()  # проверка на наличие ошибок

        # Получаем JSON ответ от API
        data = response.json()

        # Проверяем успешность ответа
        if data.get("code") == 0:
            # Извлекаем данные о рынках
            markets_data = []
            for market in data["data"]:
                markets_data.append({
                    "market": market["market"],
                    "last_price": market["last"],
                    "open_price": market["open"],
                    "close_price": market["close"],
                    "high_price": market["high"],
                    "low_price": market["low"]
                  #  "volume": market["volume"],
                  #  "volume_sell": market["volume_sell"],
                  #  "volume_buy": market["volume_buy"],
                  #  "value": market["value"],
                  #  "period": market["period"]
                })

            # Возвращаем данные
            return jsonify({
                "status": "success",
                "markets": markets_data,
                "message": data["message"]
            })
        else:
            return jsonify({
                "status": "error",
                "message": "Failed to retrieve data"
            })
    except requests.exceptions.RequestException as e:
        # Обрабатываем ошибки запросов
        return jsonify({
            "status": "error",
            "message": str(e)
        })


if __name__ == '__main__':
    app.run(debug=True)
