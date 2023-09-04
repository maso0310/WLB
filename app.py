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
                                QuickReplyButton(action=MessageAction(label="查看影片", text="查看影片")),
                                QuickReplyButton(action=MessageAction(label="其他選項", text="其他選項")),
                                QuickReplyButton(action=MessageAction(label="想喝手搖杯", text="想喝手搖杯"))
                            ]))
        line_bot_api.reply_message(event.reply_token, flex_message)
        #line_bot_api.reply_message(event.reply_token,TextSendMessage('error'))   
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
                        text='有關微積分教學影片',
                        #actions:點擊按鈕觸發的行為，一個按鈕一種行為，最多支援四個按鈕。
                        actions=[
                            PostbackAction(
                                label='詳細內容',
                                display_text='微積分學在科學、商學和工程學領域有廣泛的應用，並成為了現代大學教育的重要組成部分，用來解決那些僅依靠代數學和幾何學不能有效解決的問題。',
                                data='action=其實不需要謝謝!'
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
                            PostbackAction(
                                label='詳細內容',
                                display_text='學習如何與人互動、交流，還可以學到各種語言',
                                data='action=其實不需要謝謝!'
                            ),
                            URIAction(
                                label='觀看請點這',
                                uri='https://www.youtube.com/@amazingtalkershow/videos'
                            )
                        ]
                    ),
                    CarouselColumn(
                        thumbnail_image_url='https://upload.wikimedia.org/wikipedia/zh/thumb/4/48/ETTV_Crucial_Moment.jpg/250px-ETTV_Crucial_Moment.jpg',
                        title='關鍵時刻',
                        text='新聞節目',
                        actions=[
                            PostbackAction(
                                label='詳細內容',
                                display_text='探討國際社會相關問題',
                                data='action=其實不需要謝謝!'
                            ),
                            URIAction(
                                label='觀看請點這',
                                uri='https://www.youtube.com/@ebcCTime/videos'
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
                base_url ="https://i.imgur.com/eOpIya3.jpg",
                alt_text='需要什麼服務嗎?',
                base_size=BaseSize(height=1330, width=2000),
                actions=[
                    URIImagemapAction(
                        #bmi
                        link_uri="https://depart.femh.org.tw/dietary/3OPD/BMI.htm",
                        area=ImagemapArea(
                            x=0, y=0, width=667, height=665
                        )
                    ),
                    URIImagemapAction(
                        #天氣預報
                        link_uri="https://www.cwb.gov.tw/V8/C/W/week.html",
                        area=ImagemapArea(
                            x=667, y=0, width=666, height=665
                        )
                    ),
                    URIImagemapAction(
                        #飲食熱量
                        link_uri="http://211.21.168.52/FOOD/%A5D%AD%B9%C3%FE.htm",
                        area=ImagemapArea(
                            x=1333, y=0, width=667, height=665
                        )
                    ),
                    URIImagemapAction(
                        #南台選課
                        link_uri="https://course.stust.edu.tw/CourSel/Pages/QueryAndSelect.aspx",
                        area=ImagemapArea(
                            x=0, y=665, width=667, height=665
                        )
                    ),
                    URIImagemapAction(
                        #杜芳子菜單
                        link_uri="https://www.popdaily.com.tw/forum/food/1190866",
                        area=ImagemapArea(
                            x=667, y=665, width=666, height=665
                        )
                    ),
                    MessageImagemapAction(
                        #youtube影片
                        text='查看影片',
                        area=ImagemapArea(
                            x=1333, y=665, width=667, height=665
                        )
                    )
                ]
            )
            line_bot_api.reply_message(event.reply_token, carousel_template_message2)
    #大圖按鈕
    elif re.match('想喝手搖杯',message):
        image_carousel_template_message = TemplateSendMessage(
            alt_text='免費教學影片',
            template=ImageCarouselTemplate(
                columns=[
                    ImageCarouselColumn(
                        image_url='https://images.deliveryhero.io/image/fd-tw/LH/q716-hero.jpg',
                        action=MessageAction(
                            label='CoCo飲料店',
                            text='CoCo菜單'
                        )
                    ),
                    ImageCarouselColumn(
                        image_url='https://i.imgur.com/W7nI6fg.jpg',
                        action=PostbackAction(
                            label='LineBot聊天機器人',
                            display_text='台灣最廣泛使用的通訊軟體',
                            data='action=興趣不能當飯吃，但總比吃飯當興趣好'
                        )
                   )
                ]
            )
        )
        line_bot_api.reply_message(event.reply_token, image_carousel_template_message)
     #選擇按鈕
    elif re.match('CoCo菜單',message):
        flex_message = TextSendMessage(text='想要系列???',
                            quick_reply=QuickReply(items=[
                                QuickReplyButton(action=MessageAction(label="經典好茶道", text="經典好茶道")),
                                QuickReplyButton(action=MessageAction(label="繽紛水果茶", text="繽紛水果茶")),
                                QuickReplyButton(action=MessageAction(label="簡單喝奶茶", text="簡單喝奶茶")),
                                QuickReplyButton(action=MessageAction(label="新品專區", text="新品專區")),
                                QuickReplyButton(action=MessageAction(label="濃濃醇鮮奶", text="濃濃醇鮮奶")),
                                QuickReplyButton(action=MessageAction(label="季節限定", text="季節限定")),
                                QuickReplyButton(action=MessageAction(label="醇品咖啡香", text="醇品咖啡香"))
                            ]))
        line_bot_api.reply_message(event.reply_token, flex_message)
   
   
    elif re.match('經典好茶道',message):
        flex_message = FlexSendMessage(
            alt_text='行銷',
            contents={
                "type": "bubble",
                "hero": {
                    "type": "image",
                    "url": "https://images.deliveryhero.io/image/fd-tw/LH/q716-hero.jpg",
                    "size": "full",
                    "aspectRatio": "20:13",
                    "aspectMode": "cover",
                    "action": {
                        "type": "postback",
                        "label": "action",
                        "data": "hello"
                    }
                },
                "body": {
                    "type": "box",
                    "layout": "vertical",
                    "spacing": "md",
                    "action": {
                    "type": "postback",
                    "label": "action",
                    "data": "hello"
                    },
                    "contents": [
                        {
                            "type": "text",
                            "size": "xl",
                            "weight": "bold",
                            "text": "CoCo都可 2023年9月菜單"
                        },
                        {
                            "type": "box",
                            "layout": "vertical",
                            "spacing": "sm",
                            "contents": [
                                {
                                    "type": "box",
                                    "layout": "baseline",
                                    "contents": [
                                        {
                                            "type": "text",
                                            "text": "中 / 大",
                                            "size": "sm",
                                            "align": "end",
                                            "color": "#aaaaaa"
                                        }
                                    ]
                                },
                                {
                                    "type": "box",
                                    "layout": "baseline",
                                    "contents": [
                                        {
                                            "type": "text",
                                            "weight": "bold",
                                            "margin": "sm",
                                            "flex": 0,
                                            "text": "☆茉莉綠茶"
                                        },
                                        {
                                            "type": "text",
                                            "text": "$30/$35",
                                            "size": "sm",
                                            "align": "end",
                                            "color": "#aaaaaa"
                                        }
                                    ]
                                },
                                {
                                    "type": "box",
                                    "layout": "baseline",
                                    "contents": [
                                        {
                                            "type": "text",
                                            "text": "★四季春青茶",
                                            "weight": "bold",
                                            "margin": "sm",
                                            "flex": 0
                                        },
                                        {
                                            "type": "text",
                                            "text": "$30/$35",
                                            "size": "sm",
                                            "align": "end",
                                            "color": "#aaaaaa"
                                        }
                                    ]
                                },
                                {
                                    "type": "box",
                                    "layout": "baseline",
                                    "contents": [
                                        {
                                            "type": "text",
                                            "weight": "bold",
                                            "margin": "sm",
                                            "flex": 0,
                                            "text": "☆手採紅茶"
                                        },
                                        {
                                            "type": "text",
                                            "text": "$30/$35",
                                            "size": "sm",
                                            "align": "end",
                                            "color": "#aaaaaa"
                                        }
                                    ]
                                },
                                {
                                    "type": "box",
                                    "layout": "baseline",
                                    "contents": [
                                        {
                                            "type": "text",
                                            "weight": "bold",
                                            "margin": "sm",
                                            "flex": 0,
                                            "text": "★焙韻鐵觀音"
                                        },
                                        {
                                            "type": "text",
                                            "text": "$35/$40",
                                            "size": "sm",
                                            "align": "end",
                                            "color": "#aaaaaa"
                                        }
                                    ]
                                },
                                {
                                    "type": "box",
                                    "layout": "baseline",
                                    "contents": [
                                        {
                                            "type": "text",
                                            "weight": "bold",
                                            "margin": "sm",
                                            "flex": 0,
                                            "text": "★伯爵果茶"
                                        },
                                        {
                                            "type": "text",
                                            "text": "$35/$40",
                                            "size": "sm",
                                            "align": "end",
                                            "color": "#aaaaaa"
                                        }
                                    ]
                                },
                                {
                                    "type": "box",
                                    "layout": "baseline",
                                    "contents": [
                                        {
                                            "type": "text",
                                            "weight": "bold",
                                            "margin": "sm",
                                            "flex": 0,
                                            "text": "☆伯爵蜜香凍果茶"
                                        },
                                        {
                                            "type": "text",
                                            "text": "$45/$50",
                                            "size": "sm",
                                            "align": "end",
                                            "color": "#aaaaaa"
                                        }
                                    ]
                                },
                                {
                                    "type": "box",
                                    "layout": "baseline",
                                    "contents": [
                                        {
                                            "type": "text",
                                            "weight": "bold",
                                            "margin": "sm",
                                            "flex": 0,
                                            "text": "☆四季珍椰青"
                                        },
                                        {
                                            "type": "text",
                                            "text": "$40/$45",
                                            "size": "sm",
                                            "align": "end",
                                            "color": "#aaaaaa"
                                        }
                                    ]
                                },
                                {
                                    "type": "box",
                                    "layout": "baseline",
                                    "contents": [
                                        {
                                            "type": "text",
                                            "weight": "bold",
                                            "margin": "sm",
                                            "flex": 0,
                                            "text": "☆蜜香凍(紅/綠/清茶)"
                                        },
                                        {
                                            "type": "text",
                                            "text": "$40/$45",
                                            "size": "sm",
                                            "align": "end",
                                            "color": "#aaaaaa"
                                        }
                                    ]
                                },
                                {
                                    "type": "box",
                                    "layout": "baseline",
                                    "contents": [
                                        {
                                            "type": "text",
                                            "weight": "bold",
                                            "margin": "sm",
                                            "flex": 0,
                                            "text": "☆仙草蜜"
                                        },
                                        {
                                            "type": "text",
                                            "text": "$35/$40",
                                            "size": "sm",
                                            "align": "end",
                                            "color": "#aaaaaa"
                                        }
                                    ]
                                }
                            ]
                        }
                    ]
                }
            }
        )
        line_bot_api.reply_message(event.reply_token, flex_message)
    elif re.match('繽紛水果茶',message):
        flex_message = FlexSendMessage(
            alt_text='行銷',
            contents={
                "type": "bubble",
                "hero": {
                    "type": "image",
                    "url": "https://images.deliveryhero.io/image/fd-tw/LH/q716-hero.jpg",
                    "size": "full",
                    "aspectRatio": "20:13",
                    "aspectMode": "cover",
                    "action": {
                        "type": "postback",
                        "label": "action",
                        "data": "hello"
                    }
                },
                "body": {
                    "type": "box",
                    "layout": "vertical",
                    "spacing": "md",
                    "action": {
                        "type": "postback",
                        "label": "action",
                        "data": "hello"
                    },
                    "contents": [
                        {
                            "type": "text",
                            "text": "繽紛水果茶",
                            "size": "xl",
                            "weight": "bold"
                        },
                        {
                            "type": "box",
                            "layout": "vertical",
                            "spacing": "sm",
                            "contents": [
                                {
                                    "type": "box",
                                    "layout": "baseline",
                                    "contents": [
                                        {
                                            "type": "text",
                                            "text": "中 / 大",
                                            "size": "sm",
                                            "align": "end",
                                            "color": "#aaaaaa"
                                        }
                                    ]
                                },
                                {
                                    "type": "box",
                                    "layout": "baseline",
                                    "contents": [
                                        {
                                            "type": "text",
                                            "text": "☆百香綠茶",
                                            "weight": "bold",
                                            "margin": "sm",
                                            "flex": 0
                                        },
                                        {
                                            "type": "text",
                                            "text": "$35/$40",
                                            "size": "sm",
                                            "align": "end",
                                            "color": "#aaaaaa"
                                        }
                                    ]
                                },
                                {
                                    "type": "box",
                                    "layout": "baseline",
                                    "contents": [
                                        {
                                            "type": "text",
                                            "text": "☆鮮檸檬(紅/綠/青茶)",
                                            "weight": "bold",
                                            "margin": "sm",
                                            "flex": 0
                                        },
                                        {
                                            "type": "text",
                                            "text": "$35/$40",
                                            "size": "sm",
                                            "align": "end",
                                            "color": "#aaaaaa"
                                        }
                                    ]
                                },
                                {
                                    "type": "box",
                                    "layout": "baseline",
                                    "contents": [
                                        {
                                            "type": "text",
                                            "text": "☆芒果綠茶",
                                            "weight": "bold",
                                            "margin": "sm",
                                            "flex": 0
                                        },
                                        {
                                            "type": "text",
                                            "text": "$35/$40",
                                            "size": "sm",
                                            "align": "end",
                                            "color": "#aaaaaa"
                                        }
                                    ]
                                },
                                {
                                    "type": "box",
                                    "layout": "baseline",
                                    "contents": [
                                        {
                                            "type": "text",
                                            "text": "☆檸檬冬瓜露",
                                            "weight": "bold",
                                            "margin": "sm",
                                            "flex": 0
                                        },
                                        {
                                            "type": "text",
                                            "text": "$35/$40",
                                            "size": "sm",
                                            "align": "end",
                                            "color": "#aaaaaa"
                                        }
                                    ]
                                },
                                {
                                    "type": "box",
                                    "layout": "baseline",
                                    "contents": [
                                        {
                                            "type": "text",
                                            "text": "☆冬瓜西谷米",
                                            "weight": "bold",
                                            "margin": "sm",
                                            "flex": 0
                                        },
                                        {
                                            "type": "text",
                                            "text": "$40/$45",
                                            "size": "sm",
                                            "align": "end",
                                            "color": "#aaaaaa"
                                        }
                                    ]
                                },
                                {
                                    "type": "box",
                                    "layout": "baseline",
                                    "contents": [
                                        {
                                            "type": "text",
                                            "text": "☆蕎麥冬瓜露",
                                            "weight": "bold",
                                            "margin": "sm",
                                            "flex": 0
                                        },
                                        {
                                            "type": "text",
                                            "text": "$40/$45",
                                            "size": "sm",
                                            "align": "end",
                                            "color": "#aaaaaa"
                                        }
                                    ]
                                },
                                {
                                    "type": "box",
                                    "layout": "baseline",
                                    "contents": [
                                        {
                                            "type": "text",
                                            "text": "★蜜香檸凍(紅/綠/青/冬)",
                                            "weight": "bold",
                                            "margin": "sm",
                                            "flex": 0
                                        },
                                        {
                                            "type": "text",
                                            "text": "$45/$50",
                                            "size": "sm",
                                            "align": "end",
                                            "color": "#aaaaaa"
                                        }
                                    ]
                                },
                                {
                                    "type": "box",
                                    "layout": "baseline",
                                    "contents": [
                                        {
                                            "type": "text",
                                            "text": "☆金桔檸檬",
                                            "weight": "bold",
                                            "margin": "sm",
                                            "flex": 0
                                        },
                                        {
                                            "type": "text",
                                            "text": "$50/$55",
                                            "size": "sm",
                                            "align": "end",
                                            "color": "#aaaaaa"
                                        }
                                    ]
                                },
                                {
                                    "type": "box",
                                    "layout": "baseline",
                                    "contents": [
                                        {
                                            "type": "text",
                                            "text": "☆鲜榨蘋果百香",
                                            "weight": "bold",
                                            "margin": "sm",
                                            "flex": 0
                                        },
                                        {
                                            "type": "text",
                                            "size": "sm",
                                            "align": "end",
                                            "color": "#aaaaaa",
                                            "text": "$55/$60"
                                        }
                                    ]
                                },
                                {
                                    "type": "box",
                                    "layout": "baseline",
                                    "contents": [
                                        {
                                            "type": "text",
                                            "text": "☆鮮香橙冰茶",
                                            "weight": "bold",
                                            "margin": "sm",
                                            "flex": 0
                                        },
                                        {
                                            "type": "text",
                                            "text": "$60/$65",
                                            "size": "sm",
                                            "align": "end",
                                            "color": "#aaaaaa"
                                        }
                                    ]
                                },
                                {
                                    "type": "box",
                                    "layout": "baseline",
                                    "contents": [
                                        {
                                            "type": "text",
                                            "text": "☆綠茶養樂多",
                                            "weight": "bold",
                                            "margin": "sm",
                                            "flex": 0
                                        },
                                        {
                                            "type": "text",
                                            "text": "$55",
                                            "size": "sm",
                                            "align": "end",
                                            "color": "#aaaaaa"
                                        }
                                    ]
                                },
                                {
                                    "type": "box",
                                    "layout": "baseline",
                                    "contents": [
                                        {
                                            "type": "text",
                                            "text": "★百香雙響炮",
                                            "weight": "bold",
                                            "margin": "sm",
                                            "flex": 0
                                        },
                                        {
                                            "type": "text",
                                            "text": "$60",
                                            "size": "sm",
                                            "align": "end",
                                            "color": "#aaaaaa"
                                        }
                                    ]
                                },
                                {
                                    "type": "box",
                                    "layout": "baseline",
                                    "contents": [
                                        {
                                            "type": "text",
                                            "text": "☆檸檬霸",
                                            "weight": "bold",
                                            "margin": "sm",
                                            "flex": 0
                                        },
                                        {
                                            "type": "text",
                                            "text": "$55",
                                            "size": "sm",
                                            "align": "end",
                                            "color": "#aaaaaa"
                                        }
                                    ]
                                },
                                {
                                    "type": "box",
                                    "layout": "baseline",
                                    "contents": [
                                        {
                                            "type": "text",
                                            "text": "★星空葡萄",
                                            "weight": "bold",
                                            "margin": "sm",
                                            "flex": 0
                                        },
                                        {
                                            "type": "text",
                                            "text": "$80",
                                            "size": "sm",
                                            "align": "end",
                                            "color": "#aaaaaa"
                                        }
                                    ]
                                }
                            ]
                        }
                    ]
                }
            }
        )
        line_bot_api.reply_message(event.reply_token, flex_message)
    elif re.match('簡單喝奶茶',message):
        flex_message = FlexSendMessage(
            alt_text='行銷',
            contents={
                "type": "bubble",
                "hero": {
                    "type": "image",
                    "url": "https://images.deliveryhero.io/image/fd-tw/LH/q716-hero.jpg",
                    "size": "full",
                    "aspectRatio": "20:13",
                    "aspectMode": "cover",
                    "action": {
                        "type": "postback",
                        "label": "action",
                        "data": "hello"
                    }
                },
                "body": {
                    "type": "box",
                    "layout": "vertical",
                    "spacing": "md",
                    "action": {
                        "type": "postback",
                        "label": "action",
                        "data": "hello"
                    },
                    "contents": [
                        {
                            "type": "text",
                            "text": "簡單喝奶茶",
                            "size": "xl",
                            "weight": "bold"
                        },
                        {
                            "type": "box",
                            "layout": "vertical",
                            "spacing": "sm",
                            "contents": [
                                {
                                    "type": "box",
                                    "layout": "baseline",
                                    "contents": [
                                        {
                                            "type": "text",
                                            "text": "中 / 大",
                                            "size": "sm",
                                            "align": "end",
                                            "color": "#aaaaaa"
                                        }
                                    ]
                                },
                                {
                                    "type": "box",
                                    "layout": "baseline",
                                    "contents": [
                                        {
                                            "type": "text",
                                            "text": "☆阿薩姆奶茶",
                                            "weight": "bold",
                                            "margin": "sm",
                                            "flex": 0
                                        },
                                        {
                                            "type": "text",
                                            "text": "$35/$40",
                                            "size": "sm",
                                            "align": "end",
                                            "color": "#aaaaaa"
                                        }
                                    ]
                                },
                                {
                                    "type": "box",
                                    "layout": "baseline",
                                    "contents": [
                                        {
                                            "type": "text",
                                            "text": "★珍珠奶茶",
                                            "weight": "bold",
                                            "margin": "sm",
                                            "flex": 0
                                        },
                                        {
                                            "type": "text",
                                            "text": "$45/$50",
                                            "size": "sm",
                                            "align": "end",
                                            "color": "#aaaaaa"
                                        }
                                    ]
                                },
                                {
                                    "type": "box",
                                    "layout": "baseline",
                                    "contents": [
                                        {
                                            "type": "text",
                                            "text": "☆西谷米奶茶",
                                            "weight": "bold",
                                            "margin": "sm",
                                            "flex": 0
                                        },
                                        {
                                            "type": "text",
                                            "text": "$45/$50",
                                            "size": "sm",
                                            "align": "end",
                                            "color": "#aaaaaa"
                                        }
                                    ]
                                },
                                {
                                    "type": "box",
                                    "layout": "baseline",
                                    "contents": [
                                        {
                                            "type": "text",
                                            "text": "☆鐵觀音奶茶",
                                            "weight": "bold",
                                            "margin": "sm",
                                            "flex": 0
                                        },
                                        {
                                            "type": "text",
                                            "text": "$45/$50",
                                            "size": "sm",
                                            "align": "end",
                                            "color": "#aaaaaa"
                                        }
                                    ]
                                },
                                {
                                    "type": "box",
                                    "layout": "baseline",
                                    "contents": [
                                        {
                                            "type": "text",
                                            "text": "☆布丁奶茶",
                                            "weight": "bold",
                                            "margin": "sm",
                                            "flex": 0
                                        },
                                        {
                                            "type": "text",
                                            "text": "$45/$50",
                                            "size": "sm",
                                            "align": "end",
                                            "color": "#aaaaaa"
                                        }
                                    ]
                                },
                                {
                                    "type": "box",
                                    "layout": "baseline",
                                    "contents": [
                                        {
                                            "type": "text",
                                            "text": "★奶茶三兄弟",
                                            "weight": "bold",
                                            "margin": "sm",
                                            "flex": 0
                                        },
                                        {
                                            "type": "text",
                                            "text": "$55",
                                            "size": "sm",
                                            "align": "end",
                                            "color": "#aaaaaa"
                                        }
                                    ]
                                },
                                {
                                    "type": "box",
                                    "layout": "baseline",
                                    "contents": [
                                        {
                                            "type": "text",
                                            "text": "★雲朵奶蓋(紅/綠茶)",
                                            "weight": "bold",
                                            "margin": "sm",
                                            "flex": 0
                                        },
                                        {
                                            "type": "text",
                                            "text": "$45/$50",
                                            "size": "sm",
                                            "align": "end",
                                            "color": "#aaaaaa"
                                        }
                                    ]
                                },
                                {
                                    "type": "box",
                                    "layout": "baseline",
                                    "contents": [
                                        {
                                            "type": "text",
                                            "text": "☆伯爵奶蓋紅茶",
                                            "weight": "bold",
                                            "margin": "sm",
                                            "flex": 0
                                        },
                                        {
                                            "type": "text",
                                            "text": "$45/$50",
                                            "size": "sm",
                                            "align": "end",
                                            "color": "#aaaaaa"
                                        }
                                    ]
                                }
                            ]
                        }
                    ]
                }
            }
        )
        line_bot_api.reply_message(event.reply_token, flex_message) 
    elif re.match('新品專區',message):
        flex_message = FlexSendMessage(
            alt_text='行銷',
            contents={
                "type": "bubble",
                "hero": {
                    "type": "image",
                    "url": "https://images.deliveryhero.io/image/fd-tw/LH/q716-hero.jpg",
                    "size": "full",
                    "aspectRatio": "20:13",
                    "aspectMode": "cover",
                    "action": {
                        "type": "postback",
                        "label": "action",
                        "data": "hello"
                    }
                },
                "body": {
                    "type": "box",
                    "layout": "vertical",
                    "spacing": "md",
                    "action": {
                        "type": "postback",
                        "label": "action",
                        "data": "hello"
                    },
                    "contents": [
                        {
                            "type": "text",
                            "text": "新品專區",
                            "size": "xl",
                            "weight": "bold"
                        },
                        {
                            "type": "box",
                            "layout": "vertical",
                            "spacing": "sm",
                            "contents": [
                                {
                                    "type": "box",
                                    "layout": "baseline",
                                    "contents": [
                                        {
                                            "type": "text",
                                            "text": "中 / 大",
                                            "size": "sm",
                                            "align": "end",
                                            "color": "#aaaaaa"
                                        }
                                    ]
                                },
                                {
                                    "type": "box",
                                    "layout": "baseline",
                                    "contents": [
                                        {
                                            "type": "text",
                                            "text": "☆纖細楊枝甘露",
                                            "weight": "bold",
                                            "margin": "sm",
                                            "flex": 0
                                        },
                                        {
                                            "type": "text",
                                            "text": "$70/$90",
                                            "size": "sm",
                                            "align": "end",
                                            "color": "#aaaaaa"
                                        }
                                    ]
                                },
                                {
                                    "type": "box",
                                    "layout": "baseline",
                                    "contents": [
                                        {
                                            "type": "text",
                                            "text": "☆胖胖楊枝甘露",
                                            "weight": "bold",
                                            "margin": "sm",
                                            "flex": 0
                                        },
                                        {
                                            "type": "text",
                                            "text": "$70/$90",
                                            "size": "sm",
                                            "align": "end",
                                            "color": "#aaaaaa"
                                        }
                                    ]
                                },
                                {
                                    "type": "box",
                                    "layout": "baseline",
                                    "contents": [
                                        {
                                            "type": "text",
                                            "text": "☆輕盈楊枝甘露",
                                            "weight": "bold",
                                            "margin": "sm",
                                            "flex": 0
                                        },
                                        {
                                            "type": "text",
                                            "text": "$60/$80",
                                            "size": "sm",
                                            "align": "end",
                                            "color": "#aaaaaa"
                                        }
                                    ]
                                },
                                {
                                    "type": "box",
                                    "layout": "baseline",
                                    "contents": [
                                        {
                                            "type": "text",
                                            "text": "☆蜜橘果茶",
                                            "weight": "bold",
                                            "margin": "sm",
                                            "flex": 0
                                        },
                                        {
                                            "type": "text",
                                            "text": "$60/-無-",
                                            "size": "sm",
                                            "align": "end",
                                            "color": "#aaaaaa",
                                            "position": "relative"
                                        }
                                    ]
                                },
                                {
                                    "type": "box",
                                    "layout": "baseline",
                                    "contents": [
                                        {
                                            "type": "text",
                                            "text": "☆蜜橘優酪",
                                            "weight": "bold",
                                            "margin": "sm",
                                            "flex": 0
                                        },
                                        {
                                            "type": "text",
                                            "text": "$70/-無-",
                                            "size": "sm",
                                            "align": "end",
                                            "color": "#aaaaaa"
                                        }
                                    ]
                                },
                                {
                                    "type": "box",
                                    "layout": "baseline",
                                    "contents": [
                                        {
                                            "type": "text",
                                            "weight": "bold",
                                            "margin": "sm",
                                            "flex": 0,
                                            "text": "☆椰奶啵啵恰恰"
                                        },
                                        {
                                            "type": "text",
                                            "text": "$65/-無-",
                                            "size": "sm",
                                            "align": "end",
                                            "color": "#aaaaaa"
                                        }
                                    ]
                                }
                            ]
                        }
                    ]
                }
            }
        )
        line_bot_api.reply_message(event.reply_token, flex_message) 
    elif re.match('濃濃醇鮮奶',message):
        flex_message = FlexSendMessage(
            alt_text='行銷',
            contents={
                "type": "bubble",
                "hero": {
                    "type": "image",
                    "url": "https://images.deliveryhero.io/image/fd-tw/LH/q716-hero.jpg",
                    "size": "full",
                    "aspectRatio": "20:13",
                    "aspectMode": "cover",
                    "action": {
                        "type": "postback",
                        "label": "action",
                        "data": "hello"
                    }
                },
                "body": {
                    "type": "box",
                    "layout": "vertical",
                    "spacing": "md",
                    "action": {
                        "type": "postback",
                        "label": "action",
                        "data": "hello"
                    },
                    "contents": [
                        {
                            "type": "text",
                            "text": "濃濃醇鮮奶",
                            "size": "xl",
                            "weight": "bold"
                        },
                        {
                            "type": "box",
                            "layout": "vertical",
                            "spacing": "sm",
                            "contents": [
                                {
                                    "type": "box",
                                    "layout": "baseline",
                                    "contents": [
                                        {
                                            "type": "text",
                                            "text": "中 / 大",
                                            "size": "sm",
                                            "align": "end",
                                            "color": "#aaaaaa"
                                        }
                                    ]
                                },
                                {
                                    "type": "box",
                                    "layout": "baseline",
                                    "contents": [
                                        {
                                            "type": "text",
                                            "text": "☆英式鮮奶茶",
                                            "weight": "bold",
                                            "margin": "sm",
                                            "flex": 0
                                        },
                                        {
                                            "type": "text",
                                            "text": "$55/$70",
                                            "size": "sm",
                                            "align": "end",
                                            "color": "#aaaaaa"
                                        }
                                    ]
                                },
                                {
                                    "type": "box",
                                    "layout": "baseline",
                                    "contents": [
                                        {
                                            "type": "text",
                                            "text": "★珍珠鮮奶茶",
                                            "weight": "bold",
                                            "margin": "sm",
                                            "flex": 0
                                        },
                                        {
                                            "type": "text",
                                            "text": "$60/$70",
                                            "size": "sm",
                                            "align": "end",
                                            "color": "#aaaaaa"
                                        }
                                    ]
                                },
                                {
                                    "type": "box",
                                    "layout": "baseline",
                                    "contents": [
                                        {
                                            "type": "text",
                                            "text": "☆鐵觀音鮮奶茶",
                                            "weight": "bold",
                                            "margin": "sm",
                                            "flex": 0
                                        },
                                        {
                                            "type": "text",
                                            "text": "$60/$70",
                                            "size": "sm",
                                            "align": "end",
                                            "color": "#aaaaaa"
                                        }
                                    ]
                                },
                                {
                                    "type": "box",
                                    "layout": "baseline",
                                    "contents": [
                                        {
                                            "type": "text",
                                            "text": "☆伯爵厚鮮奶茶",
                                            "weight": "bold",
                                            "margin": "sm",
                                            "flex": 0
                                        },
                                        {
                                            "type": "text",
                                            "text": "$65/$75",
                                            "size": "sm",
                                            "align": "end",
                                            "color": "#aaaaaa",
                                            "position": "relative"
                                        }
                                    ]
                                },
                                {
                                    "type": "box",
                                    "layout": "baseline",
                                    "contents": [
                                        {
                                            "type": "text",
                                            "text": "★芋頭牛奶",
                                            "weight": "bold",
                                            "margin": "sm",
                                            "flex": 0
                                        },
                                        {
                                            "type": "text",
                                            "text": "$65/-無-",
                                            "size": "sm",
                                            "align": "end",
                                            "color": "#aaaaaa"
                                        }
                                    ]
                                },
                                {
                                    "type": "box",
                                    "layout": "baseline",
                                    "contents": [
                                        {
                                            "type": "text",
                                            "weight": "bold",
                                            "margin": "sm",
                                            "flex": 0,
                                            "text": "☆芋頭西谷米牛奶"
                                        },
                                        {
                                            "type": "text",
                                            "text": "$70/-無-",
                                            "size": "sm",
                                            "align": "end",
                                            "color": "#aaaaaa"
                                        }
                                    ]
                                }
                            ]
                        }
                    ]
                }
            }
        )
        line_bot_api.reply_message(event.reply_token, flex_message) 
    elif re.match('季節限定',message):
        flex_message = FlexSendMessage(
            alt_text='行銷',
            contents={
                "type": "bubble",
                "hero": {
                    "type": "image",
                    "url": "https://images.deliveryhero.io/image/fd-tw/LH/q716-hero.jpg",
                    "size": "full",
                    "aspectRatio": "20:13",
                    "aspectMode": "cover",
                    "action": {
                        "type": "postback",
                        "label": "action",
                        "data": "hello"
                    }
                },
                "body": {
                    "type": "box",
                    "layout": "vertical",
                    "spacing": "md",
                    "action": {
                        "type": "postback",
                        "label": "action",
                        "data": "hello"
                    },
                    "contents": [
                        {
                            "type": "text",
                            "text": "季節限定",
                            "size": "xl",
                            "weight": "bold"
                        },
                        {
                            "type": "box",
                            "layout": "vertical",
                            "spacing": "sm",
                            "contents": [
                                {
                                    "type": "box",
                                    "layout": "baseline",
                                    "contents": [
                                        {
                                            "type": "text",
                                            "text": "中 / 大",
                                            "size": "sm",
                                            "align": "end",
                                            "color": "#aaaaaa"
                                        }
                                    ]
                                },
                                {
                                    "type": "box",
                                    "layout": "baseline",
                                    "contents": [
                                        {
                                            "type": "text",
                                            "text": "☆芒果冰沙",
                                            "weight": "bold",
                                            "margin": "sm",
                                            "flex": 0
                                        },
                                        {
                                            "type": "text",
                                            "text": "$50/$60",
                                            "size": "sm",
                                            "align": "end",
                                            "color": "#aaaaaa"
                                        }
                                    ]
                                },
                                {
                                    "type": "box",
                                    "layout": "baseline",
                                    "contents": [
                                        {
                                            "type": "text",
                                            "text": "☆芒果歐蕾",
                                            "weight": "bold",
                                            "margin": "sm",
                                            "flex": 0
                                        },
                                        {
                                            "type": "text",
                                            "text": "$60/$75",
                                            "size": "sm",
                                            "align": "end",
                                            "color": "#aaaaaa"
                                        }
                                    ]
                                },
                                {
                                    "type": "box",
                                    "layout": "baseline",
                                    "contents": [
                                        {
                                            "type": "text",
                                            "text": "☆綠豆沙",
                                            "weight": "bold",
                                            "margin": "sm",
                                            "flex": 0
                                        },
                                        {
                                            "type": "text",
                                            "text": "$50/$60",
                                            "size": "sm",
                                            "align": "end",
                                            "color": "#aaaaaa"
                                        }
                                    ]
                                },
                                {
                                    "type": "box",
                                    "layout": "baseline",
                                    "contents": [
                                        {
                                            "type": "text",
                                            "text": "★綠豆沙牛奶",
                                            "weight": "bold",
                                            "margin": "sm",
                                            "flex": 0
                                        },
                                        {
                                            "type": "text",
                                            "text": "$60/$75",
                                            "size": "sm",
                                            "align": "end",
                                            "color": "#aaaaaa",
                                            "position": "relative"
                                        }
                                    ]
                                }
                            ]
                        }
                    ]
                }
            }
        )
        line_bot_api.reply_message(event.reply_token, flex_message) 
    elif re.match('醇品咖啡香',message):
        flex_message = FlexSendMessage(
            alt_text='行銷',
            contents={
                "type": "bubble",
                "hero": {
                    "type": "image",
                    "url": "https://images.deliveryhero.io/image/fd-tw/LH/q716-hero.jpg",
                    "size": "full",
                    "aspectRatio": "20:13",
                    "aspectMode": "cover",
                    "action": {
                        "type": "postback",
                        "label": "action",
                        "data": "hello"
                    }
                },
                "body": {
                    "type": "box",
                    "layout": "vertical",
                    "spacing": "md",
                    "action": {
                        "type": "postback",
                        "label": "action",
                        "data": "hello"
                    },
                    "contents": [
                        {
                            "type": "text",
                            "text": "醇品咖啡香",
                            "size": "xl",
                            "weight": "bold"
                        },
                        {
                            "type": "box",
                            "layout": "vertical",
                            "spacing": "sm",
                            "contents": [
                                {
                                    "type": "box",
                                    "layout": "baseline",
                                    "contents": [
                                        {
                                            "type": "text",
                                            "text": "16oz",
                                            "size": "sm",
                                            "align": "end",
                                            "color": "#aaaaaa"
                                        }
                                    ]
                                },
                                {
                                    "type": "box",
                                    "layout": "baseline",
                                    "contents": [
                                        {
                                            "type": "text",
                                            "text": "☆美式咖啡",
                                            "weight": "bold",
                                            "margin": "sm",
                                            "flex": 0
                                        },
                                        {
                                            "type": "text",
                                            "text": "$45",
                                            "size": "sm",
                                            "align": "end",
                                            "color": "#aaaaaa"
                                        }
                                    ]
                                },
                                {
                                    "type": "box",
                                    "layout": "baseline",
                                    "contents": [
                                        {
                                            "type": "text",
                                            "text": "☆拿鐵咖啡",
                                            "weight": "bold",
                                            "margin": "sm",
                                            "flex": 0
                                        },
                                        {
                                            "type": "text",
                                            "text": "$60",
                                            "size": "sm",
                                            "align": "end",
                                            "color": "#aaaaaa"
                                        }
                                    ]
                                },
                                {
                                    "type": "box",
                                    "layout": "baseline",
                                    "contents": [
                                        {
                                            "type": "text",
                                            "text": "★珍珠拿鐵咖啡",
                                            "weight": "bold",
                                            "margin": "sm",
                                            "flex": 0
                                        },
                                        {
                                            "type": "text",
                                            "text": "$65",
                                            "size": "sm",
                                            "align": "end",
                                            "color": "#aaaaaa"
                                        }
                                    ]
                                }
                            ]
                        }
                    ]
                }
            }
        )
        line_bot_api.reply_message(event.reply_token, flex_message) 
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
    
    