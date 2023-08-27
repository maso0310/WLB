from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import *

#======python的函數庫==========
import re
import tempfile, os
import datetime
import time

app = Flask(__name__)
static_tmp_path = os.path.join(os.path.dirname(__file__), 'static', 'tmp')
# Channel Access Token
line_bot_api = LineBotApi(os.getenv('CHANNEL_ACCESS_TOKEN'))
# Channel Secret
handler = WebhookHandler(os.getenv('CHANNEL_SECRET'))



# 監聽所有來自 /callback 的 Post Request
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

# 處理訊息
@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    message = text=event.message.text
    #文字表達
    if re.match('1451264564152156446',message):
        line_bot_api.reply_message(event.reply_token,TextSendMessage('error'))
    else:
        #大圖片(內容包含:颱風情報、南台選課、 BMI值計算、食物熱量查詢)
            carousel_template_message = ImagemapSendMessage(
                base_url ="https://i.imgur.com/I9baIpi.jpg",
                alt_text='需要什麼服務嗎?',
                base_size=BaseSize(height=2000, width=2000),
                actions=[
                    URIImagemapAction(
                        #颱風
                        link_uri="https://www.cwb.gov.tw/V8/C/P/Typhoon/TY_NEWS.html",
                        area=ImagemapArea(
                            x=0, y=0, width=1000, height=1000
                        )
                    ),
                    URIImagemapAction(
                        #熱量
                        link_uri="http://211.21.168.52/FOOD/%A5D%AD%B9%C3%FE.htm",
                        area=ImagemapArea(
                            x=1000, y=0, width=1000, height=1000
                        )
                    ),
                    URIImagemapAction(
                        #BMI
                        link_uri="https://depart.femh.org.tw/dietary/3OPD/BMI.htm",
                        area=ImagemapArea(
                            x=0, y=1000, width=1000, height=1000
                        )
                    ),
                    URIImagemapAction(
                        #南台選課
                        link_uri="https://course.stust.edu.tw/CourSel/Pages/QueryAndSelect.aspx",
                        area=ImagemapArea(
                            x=1000, y=1000, width=1000, height=1000
                        )
                    )
                ]
            )
            line_bot_api.reply_message(event.reply_token,carousel_template_message)
       
       

import os
if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
    
    