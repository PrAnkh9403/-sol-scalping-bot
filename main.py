# main.py
from telegram_sender import send_telegram_message
from bybit_client import place_order
from flask import Flask, request

app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.json
    if not data:
        return "No data received", 400

    direction = data.get("direction", "LONG")
    entry = data.get("entry")
    sl = data.get("sl")
    tp1 = data.get("tp1")

    message = f"""📡 SEMNAL {direction.upper()} – SOL/USDT (1D)
🎯 Entry: {entry}
🛑 SL: {sl}
✅ TP1: {tp1}
#solana #scalping
"""
    send_telegram_message(message)
    place_order(direction, entry, sl, tp1)
    return "OK", 200

@app.route('/test', methods=['GET'])
def test():
    send_telegram_message("🔔 Test mesaj trimis cu succes din bot!")
    return "Test trimis în Telegram!", 200

if __name__ == "__main__":
    app.run()
