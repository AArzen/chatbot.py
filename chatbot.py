from flask import Flask, render_template, request, jsonify
import openai
import configparser


app = Flask(__name__)

# Kreirajte datoteko config.ini - z vsebino:
"""
[OpenAI]
api_key = YOUR_API_KEY

"""
config = configparser.ConfigParser()
config.read('config.ini')
api_key = config['OpenAI']['api_key']
openai.api_key = api_key


# @app.route('/ask', methods=['POST'])
# def ask():
#     user_message = request.form['user_message']
#
#     # Tukaj bi uporabili OpenAI API, da bi dobili odgovor na uporabnikovo sporočilo
#     # Nadomestite spodnjo vrstico z dejanskim klicem API-ja
#     bot_response = "To je vzorec odgovora od chatbota."
#
#     return jsonify({'response': bot_response})


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/ask', methods=['POST'])
def ask():
    user_message = request.form['user_message']

    # Uporaba OpenAI API za pridobivanje odgovora
    response = openai.Completion.create(
        engine="davinci",
        prompt=user_message,
        max_tokens=50  # Omejimo dolžino odgovora
    )

    bot_response = response.choices[0].text.strip()

    return jsonify({'response': bot_response})


if __name__ == '__main__':
    if api_key:
        app.run(debug=True)
    else:
        print('API ključ ni nastavljen v konfiguracijski datoteki.')
