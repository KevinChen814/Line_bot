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

line_bot_api = LineBotApi('Cpe12iIfX2rlmR+ZTgaE0MIM53OAugSHMRfVba4sxPI9hynfRDiVChU5i6GlkoDi4ZZwpgLdw6e5JIqHsVmU+ll3qdtyhjjJG7siiw9Inm54AS1IG+XDAfuHVGpPWcdChQWeCxtSwCeoj54Xui+uawdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('5d9f18a30543d7a215391e4013ae4306')


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
    mas = event.message.text
    r = '很抱歉 您說什麼？'
    if msg == 'hi':
        r == 'hi'
    elif msg == '你吃飯了嗎':
        r == 'Not yet'
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=r))


if __name__ == "__main__":
    app.run()