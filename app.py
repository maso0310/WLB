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
    if re.match('呼叫機器人',message):
        flex_message = TextSendMessage(text='需要什麼幫忙嗎???',
                            quick_reply=QuickReply(items=[
                                QuickReplyButton(action=MessageAction(label="颱風情報", text="颱風情報")),
                                QuickReplyButton(action=MessageAction(label="南台選課", text="南台選課")),
                                QuickReplyButton(action=MessageAction(label="BMI值計算", text="BMI值計算")),
                                QuickReplyButton(action=MessageAction(label="食物熱量查詢", text="食物熱量查詢")),
                                QuickReplyButton(action=MessageAction(label="查看影片", text="查看影片")),
                                QuickReplyButton(action=MessageAction(label="其他選項", text="其他選項")),
                                QuickReplyButton(action=MessageAction(label="按我", text="按！")),
                                QuickReplyButton(action=MessageAction(label="按我", text="按！")),
                                QuickReplyButton(action=MessageAction(label="按我", text="按！"))
                            ]))
        line_bot_api.reply_message(event.reply_token, flex_message)
        #line_bot_api.reply_message(event.reply_token,TextSendMessage('error'))
    elif re.match('颱風情報',message):
        #大圖片(內容包含:颱風情報、南台選課、 BMI值計算、食物熱量查詢)
            carousel_template_message1 = ImagemapSendMessage(
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
            line_bot_api.reply_message(event.reply_token, carousel_template_message1)
    elif re.match('南台選課',message):
        #大圖片(內容包含:颱風情報、南台選課、 BMI值計算、食物熱量查詢)
            carousel_template_message1 = ImagemapSendMessage(
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
            line_bot_api.reply_message(event.reply_token, carousel_template_message1)
    elif re.match('BMI值計算',message):
        #大圖片(內容包含:颱風情報、南台選課、 BMI值計算、食物熱量查詢)
            carousel_template_message1 = ImagemapSendMessage(
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
            line_bot_api.reply_message(event.reply_token, carousel_template_message1)
    elif re.match('食物熱量查詢',message):
        #大圖片(內容包含:颱風情報、南台選課、 BMI值計算、食物熱量查詢)
            carousel_template_message1 = ImagemapSendMessage(
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
            line_bot_api.reply_message(event.reply_token, carousel_template_message1)
    elif re.match('查看影片',message):
        #多樣版組合按鈕
       carousel_template_message = TemplateSendMessage(
            alt_text='免費教學影片',
            template=CarouselTemplate(
                columns=[
                    CarouselColumn(
                        #thumbnailImageUrl:縮圖連結，支援 jpg 和 png，最大寬度 1024px。
                        thumbnail_image_url='https://shoplineimg.com/541acb0db32b41988d00001c/541e8aa3f577fe121e000049/800x.png?',
                        #title:樣板標題。
                        title='微積分教學youtube頻道',
                        #樣板說明文字。
                        text='萬丈高樓平地起',
                        #actions:點擊按鈕觸發的行為，一個按鈕一種行為，最多支援四個按鈕。
                        actions=[
                            MessageAction(
                                label='教學內容',
                                text='微積分學在科學、商學和工程學領域有廣泛的應用，並成為了現代大學教育的重要組成部分，用來解決那些僅依靠代數學和幾何學不能有效解決的問題。'
                           ),
                            URIAction(
                                label='觀看請點這',
                                uri='https://www.youtube.com/@CUSTCourses/playlists?view=50&sort=dd&shelf_id=18'
                            )
                        ]
                    ),
                   CarouselColumn(
                        thumbnail_image_url='https://is1-ssl.mzstatic.com/image/thumb/Podcasts126/v4/69/79/72/697972be-cf1b-557a-dcab-64cd665766b3/mza_14417997536117382377.jpeg/1200x600wp.png',
                        title='AmazingTalker Show',
                        text='娛樂節目',
                        actions=[
                            MessageAction(
                                label='教學內容',
                                text='學習如何與人互動、交流，還可以學到各種語言'
                            ),
                            URIAction(
                                label='觀看請點這',
                                uri='https://www.youtube.com/@amazingtalkershow/videos'
                            )
                        ]
                    ),
                    CarouselColumn(
                        thumbnail_image_url='https://is1-ssl.mzstatic.com/image/thumb/Podcasts126/v4/69/79/72/697972be-cf1b-557a-dcab-64cd665766b3/mza_14417997536117382377.jpeg/1200x600wp.png',
                        title='AmazingTalker Show',
                        text='娛樂節目',
                        actions=[
                            MessageAction(
                                label='其他選項',
                                text='其他選項'
                            ),
                            URIAction(
                                label='觀看請點這',
                                uri='https://www.youtube.com/@amazingtalkershow/videos'
                            )
                        ]
                    )

                ]
            )
        )
       line_bot_api.reply_message(event.reply_token,carousel_template_message)
    elif re.match('其他選項',message):
         #大圖片(內容包含:颱風情報、南台選課、 BMI值計算、食物熱量查詢)
            carousel_template_message2 = ImagemapSendMessage(
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
            line_bot_api.reply_message(event.reply_token, carousel_template_message2)
    else:
        #選擇按鈕
        confirm_template_message = TemplateSendMessage(
            alt_text='問問題',
            template=ConfirmTemplate(
                text='需要我幫忙嗎？',
                actions=[
                    
                    PostbackAction(
                        label='不需要謝謝!',
                        display_text='不需要謝謝!',
                        data='action=其實不需要謝謝!'
                    ),
                    MessageAction(
                        label='呼叫機器人',
                        text='呼叫機器人'
                    )
                ]
            )
        )
        line_bot_api.reply_message(event.reply_token, confirm_template_message)
        #line_bot_api.reply_message(event.reply_token,TextSendMessage(message))
       
       

import os
if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
    
    