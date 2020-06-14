from flask import Flask, request, abort
import os

# for image#########
from io import BytesIO
import urllib.request
from PIL import Image
#####################


from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,ImageMessage,
)

import datetime#######実験用

app = Flask(__name__)

#環境変数取得
YOUR_CHANNEL_ACCESS_TOKEN = os.environ["YOUR_CHANNEL_ACCESS_TOKEN"]
YOUR_CHANNEL_SECRET = os.environ["YOUR_CHANNEL_SECRET"]

line_bot_api = LineBotApi(YOUR_CHANNEL_ACCESS_TOKEN)
handler = WebhookHandler(YOUR_CHANNEL_SECRET)

@app.route("/")
def hello_world():
    return "hello world!"

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
        abort(400)

    return 'OK'
######################################################
####respons

import respons
@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    # output text
    line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text=respons.talk(event.message.text))
            
        )

import LINE_predict
@handler.add(MessageEvent, message=ImageMessage)
def handle_image(event):

    message_id = event.message.id
    # message_idから画像のバイナリデータを取得
    message_content = line_bot_api.get_message_content(message_id)

    image = BytesIO(message_content.content)#メモリに保持してディレクトリ偽装みたいなことする
    
    #pil_img = Image.open(image)#PILで読み込む
    #img=BytesIO()#空のインスタンスを作る
    #pil_img.save(img,'jpeg')#さっきのインスタンスに保存

    '''
    line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text='ちょま')
        )
    '''
    line_bot_api.reply_message(
            event.reply_token,
            #TextSendMessage(text=LINE_predict.predict(pil_img))
            TextSendMessage(text=LINE_predict.predict(image))
        )

#########################################################

if __name__ == "__main__":
#    app.run()
    port = int(os.getenv("PORT"))
    app.run(host="0.0.0.0", port=port)