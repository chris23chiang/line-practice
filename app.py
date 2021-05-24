
#Web APP

from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,
)

app = Flask(__name__)

line_bot_api = LineBotApi('8P5f2qX/mKtrnpiJMrfzO+RiHT7cSJKoJY8I0Sru8Ct7dz3YNdysh9EPQwRokPBLGIxakTAS3vT8o++L/H6569fwkExUangq7jsMmZdmsrCydmjGY5H9ZdLmBfDXPV5Vy4G8EW2jfXcYRGwC5dfDJQdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('e6a347da746c550f95cd2217ef8bfb7a')


@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        print("Invalid signature. Please check your channel access token/channel secret.")
        abort(400)

    return 'OK'


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=event.message.text))


if __name__ == "__main__":
    app.run()