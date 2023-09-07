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
                        image_url='https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcS_nsx7pU2Q8uTh5Q5xof3z1G0lCR4758BLzLSg-EiRbngZ9YRHVQyJo68fZZwnifEGpLU&usqp=CAU',
                        action=MessageAction(
                            label='50嵐飲料店',
                            text='50嵐菜單'                          
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
    elif re.match('50嵐菜單',message):
        flex_message = TextSendMessage(text='想要系列???',
                            quick_reply=QuickReply(items=[
                                QuickReplyButton(action=MessageAction(label="找好茶", text="找好茶")),
                                QuickReplyButton(action=MessageAction(label="找奶茶", text="找奶茶")),
                                QuickReplyButton(action=MessageAction(label="找拿鐵", text="找拿鐵")),
                                QuickReplyButton(action=MessageAction(label="找新鮮", text="找新鮮")),
                                QuickReplyButton(action=MessageAction(label="季節限定", text="季節限定"))                     
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
                },
                "footer": {
                    "type": "box",
                    "layout": "vertical",
                    "contents": [
                        {
                            "type": "button",
                            "style": "primary",
                            "color": "#905c44",
                            "margin": "xxl",
                            "action": {
                                "type": "message",
                                "label": "地址前往",
                                "text": "CoCo飲料店"
                            }
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
                },
                "footer": {
                    "type": "box",
                    "layout": "vertical",
                    "contents": [
                        {
                            "type": "button",
                            "style": "primary",
                            "color": "#905c44",
                            "margin": "xxl",
                            "action": {
                                "type": "message",
                                "label": "地址前往",
                                "text": "CoCo飲料店"
                            }
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
                },
                "footer": {
                    "type": "box",
                    "layout": "vertical",
                    "contents": [
                        {
                            "type": "button",
                            "style": "primary",
                            "color": "#905c44",
                            "margin": "xxl",
                            "action": {
                                "type": "message",
                                "label": "地址前往",
                                "text": "CoCo飲料店"
                            }
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
                },
                "footer": {
                    "type": "box",
                    "layout": "vertical",
                    "contents": [
                        {
                            "type": "button",
                            "style": "primary",
                            "color": "#905c44",
                            "margin": "xxl",
                            "action": {
                                "type": "message",
                                "label": "地址前往",
                                "text": "CoCo飲料店"
                            }
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
                },
                "footer": {
                    "type": "box",
                    "layout": "vertical",
                    "contents": [
                        {
                            "type": "button",
                            "style": "primary",
                            "color": "#905c44",
                            "margin": "xxl",
                            "action": {
                                "type": "message",
                                "label": "地址前往",
                                "text": "CoCo飲料店"
                            }
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
                },
                "footer": {
                    "type": "box",
                    "layout": "vertical",
                    "contents": [
                        {
                            "type": "button",
                            "style": "primary",
                            "color": "#905c44",
                            "margin": "xxl",
                            "action": {
                                "type": "message",
                                "label": "地址前往",
                                "text": "CoCo飲料店"
                            }
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
                },
                "footer": {
                    "type": "box",
                    "layout": "vertical",
                    "contents": [
                        {
                            "type": "button",
                            "style": "primary",
                            "color": "#905c44",
                            "margin": "xxl",
                            "action": {
                                "type": "message",
                                "label": "地址前往",
                                "text": "CoCo飲料店"
                            }
                        }
                    ]
                }
            }
        )
        line_bot_api.reply_message(event.reply_token, flex_message) 
    elif re.match('找好茶',message):
        flex_message = FlexSendMessage(
            alt_text='行銷',
            contents={
                "type": "bubble",
                "hero": {
                    "type": "image",
                    "url": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcS_nsx7pU2Q8uTh5Q5xof3z1G0lCR4758BLzLSg-EiRbngZ9YRHVQyJo68fZZwnifEGpLU&usqp=CAU",
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
                            "text": "找好茶 FLAVORED TEA",
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
                                            "text": "☆茉莉綠茶/阿薩姆紅茶",
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
                                            "text": "★黃金烏龍",
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
                                            "text": "☆椰果紅/綠",
                                            "weight": "bold",
                                            "margin": "sm",
                                            "flex": 0
                                        },
                                        {
                                            "type": "text",
                                            "text": "$35/$45",
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
                                            "text": "☆波霸紅/綠",
                                            "weight": "bold",
                                            "margin": "sm",
                                            "flex": 0
                                        },
                                        {
                                            "type": "text",
                                            "text": "$35/$45",
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
                                            "text": "★燕麥紅/綠/青",
                                            "weight": "bold",
                                            "margin": "sm",
                                            "flex": 0
                                        },
                                        {
                                            "type": "text",
                                            "text": "$35/$45",
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
                                            "text": "☆微檸檬紅/青",
                                            "weight": "bold",
                                            "margin": "sm",
                                            "flex": 0
                                        },
                                        {
                                            "type": "text",
                                            "text": "$35/$45",
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
                                            "text": "☆檸檬綠/青",
                                            "weight": "bold",
                                            "margin": "sm",
                                            "flex": 0
                                        },
                                        {
                                            "type": "text",
                                            "text": "$40/$55",
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
                                            "text": "★梅の綠",
                                            "weight": "bold",
                                            "margin": "sm",
                                            "flex": 0
                                        },
                                        {
                                            "type": "text",
                                            "text": "$40/$55",
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
                                            "text": "☆8冰綠/情人茶",
                                            "weight": "bold",
                                            "margin": "sm",
                                            "flex": 0
                                        },
                                        {
                                            "type": "text",
                                            "text": "$40/$55",
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
                                            "text": "☆柚子紅/綠",
                                            "weight": "bold",
                                            "margin": "sm",
                                            "flex": 0
                                        },
                                        {
                                            "type": "text",
                                            "text": "$40/$55",
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
                                            "text": "☆柚子青/烏",
                                            "weight": "bold",
                                            "margin": "sm",
                                            "flex": 0
                                        },
                                        {
                                            "type": "text",
                                            "text": "$40/$55",
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
                                            "text": "★冰淇淋紅茶",
                                            "weight": "bold",
                                            "margin": "sm",
                                            "flex": 0
                                        },
                                        {
                                            "type": "text",
                                            "text": "$40/$55",
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
                                            "text": "☆多多綠/紅",
                                            "weight": "bold",
                                            "margin": "sm",
                                            "flex": 0
                                        },
                                        {
                                            "type": "text",
                                            "text": "$40/$55",
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
                                            "text": "☆多多檸檬綠",
                                            "weight": "bold",
                                            "margin": "sm",
                                            "flex": 0
                                        },
                                        {
                                            "type": "text",
                                            "text": "$50/$65",
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
    elif re.match('找奶茶',message):
        flex_message = FlexSendMessage(
            alt_text='行銷',
            contents={
                "type": "bubble",
                "hero": {
                    "type": "image",
                    "url": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcS_nsx7pU2Q8uTh5Q5xof3z1G0lCR4758BLzLSg-EiRbngZ9YRHVQyJo68fZZwnifEGpLU&usqp=CAU",
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
                            "text": "找奶茶 MILK TEA",
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
                                            "text": "☆奶茶",
                                            "weight": "bold",
                                            "margin": "sm",
                                            "flex": 0
                                        },
                                        {
                                            "type": "text",
                                            "text": "$40/$55",
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
                                            "text": "☆奶綠",
                                            "weight": "bold",
                                            "margin": "sm",
                                            "flex": 0
                                        },
                                        {
                                            "type": "text",
                                            "text": "$40/$55",
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
                                            "text": "★烏龍奶",
                                            "weight": "bold",
                                            "margin": "sm",
                                            "flex": 0
                                        },
                                        {
                                            "type": "text",
                                            "text": "$40/$55",
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
                                            "text": "☆椰果奶茶",
                                            "weight": "bold",
                                            "margin": "sm",
                                            "flex": 0
                                        },
                                        {
                                            "type": "text",
                                            "text": "$40/$55",
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
                                            "text": "$40/$55",
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
                                            "text": "★波霸奶茶",
                                            "weight": "bold",
                                            "margin": "sm",
                                            "flex": 0
                                        },
                                        {
                                            "type": "text",
                                            "text": "$40/$55",
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
                                            "text": "☆燕麥奶茶/奶青",
                                            "weight": "bold",
                                            "margin": "sm",
                                            "flex": 0
                                        },
                                        {
                                            "type": "text",
                                            "text": "$40/$55",
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
                                            "text": "☆燕麥烏龍奶",
                                            "weight": "bold",
                                            "margin": "sm",
                                            "flex": 0
                                        },
                                        {
                                            "type": "text",
                                            "text": "$40/$55",
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
                                            "text": "$50/$65",
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
                                            "text": "☆冰淇淋奶茶",
                                            "weight": "bold",
                                            "margin": "sm",
                                            "flex": 0
                                        },
                                        {
                                            "type": "text",
                                            "text": "$50/$65",
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
                                            "text": "☆紅茶瑪奇朵",
                                            "weight": "bold",
                                            "margin": "sm",
                                            "flex": 0
                                        },
                                        {
                                            "type": "text",
                                            "text": "$40/$55",
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
                                            "text": "☆青茶瑪奇朵",
                                            "weight": "bold",
                                            "margin": "sm",
                                            "flex": 0
                                        },
                                        {
                                            "type": "text",
                                            "text": "$40/$55",
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
                                            "text": "☆阿華田",
                                            "weight": "bold",
                                            "margin": "sm",
                                            "flex": 0
                                        },
                                        {
                                            "type": "text",
                                            "text": "$45/$60",
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
                                            "text": "☆燕麥阿華田",
                                            "weight": "bold",
                                            "margin": "sm",
                                            "flex": 0
                                        },
                                        {
                                            "type": "text",
                                            "text": "$45/$60",
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
                                            "text": "☆可可芭蕾",
                                            "weight": "bold",
                                            "margin": "sm",
                                            "flex": 0
                                        },
                                        {
                                            "type": "text",
                                            "text": "$50/$65",
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
    elif re.match('找拿鐵',message):
        flex_message = FlexSendMessage(
            alt_text='行銷',
            contents={
                "type": "bubble",
                "hero": {
                    "type": "image",
                    "url": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcS_nsx7pU2Q8uTh5Q5xof3z1G0lCR4758BLzLSg-EiRbngZ9YRHVQyJo68fZZwnifEGpLU&usqp=CAU",
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
                            "text": "找拿鐵 TEA LATTE",
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
                                            "text": "★紅茶拿鐵",
                                            "weight": "bold",
                                            "margin": "sm",
                                            "flex": 0
                                        },
                                        {
                                            "type": "text",
                                            "text": "$50/$65",
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
                                            "text": "☆綠茶拿鐵",
                                            "weight": "bold",
                                            "margin": "sm",
                                            "flex": 0
                                        },
                                        {
                                            "type": "text",
                                            "text": "$50/$65",
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
                                            "text": "☆烏龍拿鐵",
                                            "weight": "bold",
                                            "margin": "sm",
                                            "flex": 0
                                        },
                                        {
                                            "type": "text",
                                            "text": "$50/$65",
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
                                            "text": "☆珍珠紅茶拿鐵",
                                            "weight": "bold",
                                            "margin": "sm",
                                            "flex": 0
                                        },
                                        {
                                            "type": "text",
                                            "text": "$50/$65",
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
                                            "text": "☆波霸紅茶拿鐵",
                                            "weight": "bold",
                                            "margin": "sm",
                                            "flex": 0
                                        },
                                        {
                                            "type": "text",
                                            "text": "$50/$65",
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
                                            "text": "★燕麥紅茶拿鐵",
                                            "weight": "bold",
                                            "margin": "sm",
                                            "flex": 0
                                        },
                                        {
                                            "type": "text",
                                            "text": "$50/$65",
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
                                            "text": "☆布丁紅茶拿鐵",
                                            "weight": "bold",
                                            "margin": "sm",
                                            "flex": 0
                                        },
                                        {
                                            "type": "text",
                                            "text": "$55/$75",
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
                                            "text": "☆冰淇淋紅茶拿鐵",
                                            "weight": "bold",
                                            "margin": "sm",
                                            "flex": 0
                                        },
                                        {
                                            "type": "text",
                                            "text": "$55/$75",
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
                                            "text": "☆阿華田拿鐵",
                                            "weight": "bold",
                                            "margin": "sm",
                                            "flex": 0
                                        },
                                        {
                                            "type": "text",
                                            "text": "$55/$75",
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
                                            "text": "☆燕麥阿華田拿鐵",
                                            "weight": "bold",
                                            "margin": "sm",
                                            "flex": 0
                                        },
                                        {
                                            "type": "text",
                                            "text": "$55/$75",
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
                                            "text": "☆可可芭蕾拿鐵",
                                            "weight": "bold",
                                            "margin": "sm",
                                            "flex": 0
                                        },
                                        {
                                            "type": "text",
                                            "text": "$55/$75",
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
    elif re.match('找新鮮',message):
        flex_message = FlexSendMessage(
            alt_text='行銷',
            contents={
                "type": "bubble",
                "hero": {
                    "type": "image",
                    "url": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcS_nsx7pU2Q8uTh5Q5xof3z1G0lCR4758BLzLSg-EiRbngZ9YRHVQyJo68fZZwnifEGpLU&usqp=CAU",
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
                            "text": "找新鮮 FRESH JUICE",
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
                                            "text": "★柚子茶",
                                            "weight": "bold",
                                            "margin": "sm",
                                            "flex": 0
                                        },
                                        {
                                            "type": "text",
                                            "text": "$40/$55",
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
                                            "text": "★8冰茶",
                                            "weight": "bold",
                                            "margin": "sm",
                                            "flex": 0
                                        },
                                        {
                                            "type": "text",
                                            "text": "$40/$55",
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
                                            "text": "☆檸檬汁",
                                            "weight": "bold",
                                            "margin": "sm",
                                            "flex": 0
                                        },
                                        {
                                            "type": "text",
                                            "text": "$50/$65",
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
                                            "text": "$50/$65",
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
                                            "text": "☆檸檬梅汁",
                                            "weight": "bold",
                                            "margin": "sm",
                                            "flex": 0
                                        },
                                        {
                                            "type": "text",
                                            "text": "$50/$65",
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
                                            "text": "☆檸檬多多",
                                            "weight": "bold",
                                            "margin": "sm",
                                            "flex": 0
                                        },
                                        {
                                            "type": "text",
                                            "text": "$55/$75",
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
                    "url": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcS_nsx7pU2Q8uTh5Q5xof3z1G0lCR4758BLzLSg-EiRbngZ9YRHVQyJo68fZZwnifEGpLU&usqp=CAU",
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
                            "text": "找新鮮 FRESH JUICE",
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
                                            "text": "☆蜂蜜紅/綠",
                                            "weight": "bold",
                                            "margin": "sm",
                                            "flex": 0
                                        },
                                        {
                                            "type": "text",
                                            "text": "$40/$55",
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
                                            "text": "☆蜂蜜奶茶",
                                            "weight": "bold",
                                            "margin": "sm",
                                            "flex": 0
                                        },
                                        {
                                            "type": "text",
                                            "text": "$50/$65",
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
                                            "text": "☆鮮柚綠/葡萄柚汁",
                                            "weight": "bold",
                                            "margin": "sm",
                                            "flex": 0
                                        },
                                        {
                                            "type": "text",
                                            "text": "$50/$65",
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
                                            "text": "☆葡萄柚蜜",
                                            "weight": "bold",
                                            "margin": "sm",
                                            "flex": 0
                                        },
                                        {
                                            "type": "text",
                                            "text": "$55/$75",
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
                                            "text": "☆葡萄柚多多",
                                            "weight": "bold",
                                            "margin": "sm",
                                            "flex": 0
                                        },
                                        {
                                            "type": "text",
                                            "text": "$55/$75",
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
                                            "text": "☆檸檬蜜",
                                            "weight": "bold",
                                            "margin": "sm",
                                            "flex": 0
                                        },
                                        {
                                            "type": "text",
                                            "text": "$55/$75",
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
                                            "text": "☆金桔檸檬蜜",
                                            "weight": "bold",
                                            "margin": "sm",
                                            "flex": 0
                                        },
                                        {
                                            "type": "text",
                                            "text": "$55/$75",
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
    elif re.match('CoCo飲料店',message):
        flex_message = TextSendMessage(text='東北西南部哪一區???',
                            quick_reply=QuickReply(items=[
                                QuickReplyButton(action=MessageAction(label="北部", text="北部CoCo飲料店")),
                                QuickReplyButton(action=MessageAction(label="西部", text="西部CoCo飲料店")),
                                QuickReplyButton(action=MessageAction(label="東部", text="東部CoCo飲料店")),
                                QuickReplyButton(action=MessageAction(label="南部", text="南部CoCo飲料店"))                     
                            ]))
        line_bot_api.reply_message(event.reply_token, flex_message)
#北部CoCo飲料店------------------------------------------------------------
    elif re.match('北部CoCo飲料店',message):
        flex_message = TextSendMessage(text='哪一縣市???',
                            quick_reply=QuickReply(items=[
                                QuickReplyButton(action=MessageAction(label="臺北市", text="臺北市CoCo飲料店")),
                                QuickReplyButton(action=MessageAction(label="新北市", text="新北市CoCo飲料店")),
                                QuickReplyButton(action=MessageAction(label="基隆市", text="基隆市CoCo飲料店")),
                                QuickReplyButton(action=MessageAction(label="新竹市", text="新竹市CoCo飲料店")),   
                                QuickReplyButton(action=MessageAction(label="桃園市", text="桃園市CoCo飲料店")),
                                QuickReplyButton(action=MessageAction(label="新竹縣", text="新竹縣CoCo飲料店")),
                                QuickReplyButton(action=MessageAction(label="宜蘭縣", text="宜蘭縣CoCo飲料店"))                  
                            ]))
        line_bot_api.reply_message(event.reply_token, flex_message)
#西部CoCo飲料店------------------------------------------------------------
    elif re.match('西部CoCo飲料店',message):
        flex_message = TextSendMessage(text='哪一縣市???',
                            quick_reply=QuickReply(items=[
                                QuickReplyButton(action=MessageAction(label="臺中市", text="臺中市CoCo飲料店")),
                                QuickReplyButton(action=MessageAction(label="苗栗縣", text="苗栗縣CoCo飲料店")),
                                QuickReplyButton(action=MessageAction(label="彰化縣", text="彰化縣CoCo飲料店")),
                                QuickReplyButton(action=PostbackAction(label="南投縣", display_text="抱歉沒有相關資訊",data='action=其實不需要謝謝!')),   
                                QuickReplyButton(action=MessageAction(label="雲林縣", text="雲林縣CoCo飲料店"))               
                            ]))
        line_bot_api.reply_message(event.reply_token, flex_message)
#南部CoCo飲料店------------------------------------------------------------
    elif re.match('南部CoCo飲料店',message):
        flex_message = TextSendMessage(text='哪一縣市???',
                            quick_reply=QuickReply(items=[
                                QuickReplyButton(action=MessageAction(label="高雄市", text="高雄市CoCo飲料店")),
                                QuickReplyButton(action=MessageAction(label="臺南市", text="臺南市CoCo飲料店")),
                                QuickReplyButton(action=PostbackAction(label="嘉義縣", display_text="抱歉沒有相關資訊",data='action=其實不需要謝謝!')),
                                QuickReplyButton(action=PostbackAction(label="嘉義市", display_text="抱歉沒有相關資訊",data='action=其實不需要謝謝!')),   
                                QuickReplyButton(action=PostbackAction(label="屏東縣", display_text="抱歉沒有相關資訊",data='action=其實不需要謝謝!')),
                                QuickReplyButton(action=MessageAction(label="澎湖縣", text="澎湖縣CoCo飲料店"))                     
                            ]))
        line_bot_api.reply_message(event.reply_token, flex_message)
#東部CoCo飲料店------------------------------------------------------------
    elif re.match('東部CoCo飲料店',message):
        flex_message = TextSendMessage(text='哪一縣市???',
                            quick_reply=QuickReply(items=[
                                QuickReplyButton(action=MessageAction(label="花蓮縣", text="抱歉沒有相關資訊")),
                                QuickReplyButton(action=MessageAction(label="臺東縣", text="抱歉沒有相關資訊"))                     
                            ]))
        line_bot_api.reply_message(event.reply_token, flex_message)
#台灣北部----------------------------------------------------
    #臺北市CoCo飲料店
    elif re.match('臺北市CoCo飲料店',message):
        flex_message = TextSendMessage(text='選擇店家???',
                            quick_reply=QuickReply(items=[
                                QuickReplyButton(action=MessageAction(label="台北建國店", text="台北建國店")),
                                QuickReplyButton(action=MessageAction(label="金山店", text="金山店")),
                                QuickReplyButton(action=MessageAction(label="台北民生店", text="台北民生店")),
                                QuickReplyButton(action=MessageAction(label="安居店", text="安居店")),
                                QuickReplyButton(action=MessageAction(label="延平店", text="延平店"))                     
                            ]))
        line_bot_api.reply_message(event.reply_token, flex_message)
    #新北市CoCo飲料店
    elif re.match('新北市CoCo飲料店',message):
        flex_message = TextSendMessage(text='選擇店家???',
                            quick_reply=QuickReply(items=[
                                QuickReplyButton(action=MessageAction(label="新店北新店", text="新店北新店")),
                                QuickReplyButton(action=MessageAction(label="新莊中和店", text="新莊中和店")),
                                QuickReplyButton(action=MessageAction(label="合宜店", text="合宜店")),
                                QuickReplyButton(action=MessageAction(label="新店民族店", text="新店民族店")),
                                QuickReplyButton(action=MessageAction(label="板橋民治店", text="板橋民治店"))                     
                            ]))
        line_bot_api.reply_message(event.reply_token, flex_message)
    #基隆市CoCo飲料店
    elif re.match('基隆市CoCo飲料店',message):
        flex_message = TextSendMessage(text='選擇店家???',
                            quick_reply=QuickReply(items=[
                                QuickReplyButton(action=MessageAction(label="基隆廟口店", text="基隆廟口店")),
                                QuickReplyButton(action=MessageAction(label="百福門市", text="百福門市")),
                                QuickReplyButton(action=MessageAction(label="基隆武崙店", text="基隆武崙店")),
                                QuickReplyButton(action=MessageAction(label="基隆復興店", text="基隆復興店")),
                                QuickReplyButton(action=MessageAction(label="基隆成功店", text="基隆成功店"))                     
                            ]))
        line_bot_api.reply_message(event.reply_token, flex_message)
    #新竹市CoCo飲料店
    elif re.match('新竹市CoCo飲料店',message):
        flex_message = TextSendMessage(text='選擇店家???',
                            quick_reply=QuickReply(items=[
                                QuickReplyButton(action=MessageAction(label="新竹中正店", text="新竹中正店")),
                                QuickReplyButton(action=MessageAction(label="新竹光華店", text="新竹光華店")),
                                QuickReplyButton(action=MessageAction(label="新竹食品店", text="新竹食品店")),
                                QuickReplyButton(action=MessageAction(label="新竹城隍廟店", text="新竹城隍廟店")),
                                QuickReplyButton(action=MessageAction(label="新竹巨城店", text="新竹巨城店"))                     
                            ]))
        line_bot_api.reply_message(event.reply_token, flex_message)
    #桃園市CoCo飲料店
    elif re.match('桃園市CoCo飲料店',message):
        flex_message = TextSendMessage(text='選擇店家???',
                            quick_reply=QuickReply(items=[
                                QuickReplyButton(action=MessageAction(label="桃園中華店", text="桃園中華店")),
                                QuickReplyButton(action=MessageAction(label="桃園寶山店", text="桃園寶山店")),
                                QuickReplyButton(action=MessageAction(label="桃園大同店", text="桃園大同店")),
                                QuickReplyButton(action=MessageAction(label="桃園縣府店", text="桃園縣府店")),
                                QuickReplyButton(action=MessageAction(label="桃園莊敬店", text="桃園莊敬店"))                     
                            ]))
        line_bot_api.reply_message(event.reply_token, flex_message)
    #新竹縣CoCo飲料店
    elif re.match('新竹縣CoCo飲料店',message):
        flex_message = TextSendMessage(text='選擇店家???',
                            quick_reply=QuickReply(items=[
                                QuickReplyButton(action=MessageAction(label="新竹新埔店", text="新竹新埔店")),
                                QuickReplyButton(action=MessageAction(label="新竹芎林店", text="新竹芎林店")),
                                QuickReplyButton(action=MessageAction(label="竹北文興店", text="竹北文興店")),
                                QuickReplyButton(action=MessageAction(label="竹北中正店", text="竹北中正店")),
                                QuickReplyButton(action=MessageAction(label="新竹北埔店", text="新竹北埔店"))                     
                            ]))
        line_bot_api.reply_message(event.reply_token, flex_message)
    #宜蘭縣CoCo飲料店
    elif re.match('宜蘭縣CoCo飲料店',message):
        flex_message = TextSendMessage(text='選擇店家???',
                            quick_reply=QuickReply(items=[
                                QuickReplyButton(action=MessageAction(label="宜蘭店", text="宜蘭店")),
                                QuickReplyButton(action=MessageAction(label="礁溪門市", text="礁溪門市")),
                                QuickReplyButton(action=MessageAction(label="宜蘭五結門市", text="宜蘭五結門市")),
                                QuickReplyButton(action=MessageAction(label="頭城店", text="頭城店")),
                                QuickReplyButton(action=MessageAction(label="羅東門市", text="羅東門市"))                     
                            ]))
        line_bot_api.reply_message(event.reply_token, flex_message)
#台灣西部----------------------------------------------------    
    elif re.match('臺中市CoCo飲料店',message):
        flex_message = TextSendMessage(text='選擇店家??????',
                            quick_reply=QuickReply(items=[
                                QuickReplyButton(action=MessageAction(label="台中靜宜店", text="台中靜宜店")),
                                QuickReplyButton(action=MessageAction(label="台中新時代店", text="台中新時代店")),
                                QuickReplyButton(action=MessageAction(label="文心秀泰店", text="文心秀泰店")),
                                QuickReplyButton(action=MessageAction(label="台中后里店", text="台中后里店")),   
                                QuickReplyButton(action=MessageAction(label="清水服務區店", text="清水服務區店"))               
                            ]))
        line_bot_api.reply_message(event.reply_token, flex_message)
    elif re.match('苗栗縣CoCo飲料店',message):
        flex_message = TextSendMessage(text='選擇店家??????',
                            quick_reply=QuickReply(items=[
                                QuickReplyButton(action=MessageAction(label="苗栗至公店", text="苗栗至公店")),
                                QuickReplyButton(action=MessageAction(label="南苗中正店", text="南苗中正店")),
                                QuickReplyButton(action=MessageAction(label="苗栗正發店", text="苗栗正發店")),
                                QuickReplyButton(action=MessageAction(label="苗栗通霄店", text="苗栗通霄店")),   
                                QuickReplyButton(action=MessageAction(label="苗栗公館店", text="苗栗公館店"))               
                            ]))
        line_bot_api.reply_message(event.reply_token, flex_message)
    elif re.match('彰化縣CoCo飲料店',message):
        flex_message = TextSendMessage(text='選擇店家??????',
                            quick_reply=QuickReply(items=[
                                QuickReplyButton(action=MessageAction(label="員林中山店", text="員林中山店")),
                                QuickReplyButton(action=MessageAction(label="大溪崎頂店", text="大溪崎頂店"))             
                            ]))
        line_bot_api.reply_message(event.reply_token, flex_message)
    elif re.match('雲林縣CoCo飲料店',message):
        flex_message = TextSendMessage(text='選擇店家??????',
                            quick_reply=QuickReply(items=[
                                QuickReplyButton(action=MessageAction(label="雲林西螺店", text="雲林西螺店"))             
                            ]))
        line_bot_api.reply_message(event.reply_token, flex_message)
#台灣南部----------------------------------------------------
    elif re.match('高雄市CoCo飲料店',message):
        flex_message = TextSendMessage(text='選擇店家??????',
                            quick_reply=QuickReply(items=[
                                QuickReplyButton(action=MessageAction(label="夢時代店", text="夢時代店")),   
                                QuickReplyButton(action=MessageAction(label="左營新光店", text="左營新光店")),
                                QuickReplyButton(action=MessageAction(label="高雄SKM Park店", text="高雄SKM Park店")),
                                QuickReplyButton(action=MessageAction(label="成功家樂福店", text="成功家樂福店")),
                                QuickReplyButton(action=MessageAction(label="TEA", text="TEA"))          
                            ]))
        line_bot_api.reply_message(event.reply_token, flex_message)
    elif re.match('臺南市CoCo飲料店',message):
        flex_message = TextSendMessage(text='選擇店家??????',
                            quick_reply=QuickReply(items=[
                                QuickReplyButton(action=MessageAction(label="南紡購物中心店", text="南紡購物中心店")),   
                                QuickReplyButton(action=MessageAction(label="永康自強店", text="永康自強店")),
                                QuickReplyButton(action=MessageAction(label="台南新市店", text="台南新市店"))      
                            ]))
        line_bot_api.reply_message(event.reply_token, flex_message)
    elif re.match('澎湖縣CoCo飲料店',message):
        flex_message = TextSendMessage(text='選擇店家??????',
                            quick_reply=QuickReply(items=[
                                QuickReplyButton(action=MessageAction(label="敲敲Knock knock", text="敲敲Knock knock"))          
                            ]))
        line_bot_api.reply_message(event.reply_token, flex_message)
#台灣東部---------------------------------------------------------  


    #地圖座標位址---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    #北部---------------------------------
    elif re.match('台北建國店',message):
        location_message = LocationSendMessage(
            title = '台北建國店',
            address = '106台北市大安區建國南路二段17號',
            latitude =25.039071997150213,
            longitude=121.53669930442271
        )
        line_bot_api.reply_message(event.reply_token, location_message) 
    elif re.match('延平店',message):
        location_message = LocationSendMessage(
            title = '延平店',
            address = 'CoCo都可',
            latitude =25.071417664066562,
            longitude=121.51129342170938
        )
        line_bot_api.reply_message(event.reply_token, location_message)  
    elif re.match('金山店',message):
        location_message = LocationSendMessage(
            title = '金山店',
            address = '100台北市中正區信義路二段91-4號',
            latitude =25.040938325322085,
            longitude=121.52571297676292
        )
        line_bot_api.reply_message(event.reply_token, location_message)
    elif re.match('台北民生店',message):
        location_message = LocationSendMessage(
            title = '台北民生店',
            address = '103台北市大同區民生西路159號',
            latitude =25.06364304280146,
            longitude=121.51644326279994
        )
        line_bot_api.reply_message(event.reply_token, location_message)   
    elif re.match('安居店',message):
        location_message = LocationSendMessage(
            title = '安居店',
            address = '106台北市大安區安居街18號',
            latitude =25.06364304280146,
            longitude=121.51644326279994
        )
        line_bot_api.reply_message(event.reply_token, location_message)               
    elif re.match('新店北新店',message):
        location_message = LocationSendMessage(
            title = '新店北新店',
            address = '231新北市新店區北新路一段209號',
            latitude =24.970195704972266,
            longitude=121.53957934893903
        )
        line_bot_api.reply_message(event.reply_token, location_message)   
    elif re.match('新莊中和店',message):
        location_message = LocationSendMessage(
            title = '新莊中和店',
            address = '242新北市新莊區中和街178號',
            latitude =25.056862513585973,
            longitude=121.44822363989651
        )
        line_bot_api.reply_message(event.reply_token, location_message)   
    elif re.match('合宜店',message):
        location_message = LocationSendMessage(
            title = '合宜店',
            address = '220新北市板橋區合宜路81號1樓',
            latitude =25.00584594835963,
            longitude=121.44547705798156
        )
        line_bot_api.reply_message(event.reply_token, location_message)   
    elif re.match('新店民族店',message):
        location_message = LocationSendMessage(
            title = '新店民族店',
            address = '231新北市新店區民族路243號',
            latitude =24.982819336788477,
            longitude=121.53611426117504
        )
        line_bot_api.reply_message(event.reply_token, location_message) 
    elif re.match('板橋民治店',message):
        location_message = LocationSendMessage(
            title = '板橋民治店',
            address = '220新北市板橋區民治街115號',
            latitude =25.0369561340203,
            longitude=121.47774939548226
        )
        line_bot_api.reply_message(event.reply_token, location_message) 
    elif re.match('基隆廟口店',message):
        location_message = LocationSendMessage( 
            title = '基隆廟口店',
            address = '200基隆市仁愛區愛三路28號',
            latitude =25.132272739901207,
            longitude=121.74206591881864
        )
        line_bot_api.reply_message(event.reply_token, location_message) 
    elif re.match('百福門市',message):
        location_message = LocationSendMessage(
            title = '百福門市',
            address = '206基隆市七堵區百三街60號',
            latitude =25.083775154203707,
            longitude=121.69606067163414
        )
        line_bot_api.reply_message(event.reply_token, location_message) 
    elif re.match('基隆武崙店',message):
        location_message = LocationSendMessage( 
            title = '基隆武崙店',
            address = '20445基隆市安樂區基金一路135巷21弄1號底一層之6',
            latitude =25.144083339007157,
            longitude=121.70945025846953
        )
        line_bot_api.reply_message(event.reply_token, location_message) 
    elif re.match('基隆復興店',message):
        location_message = LocationSendMessage(
            title = '基隆復興店',
            address = '203基隆市中山區復興路156號',
            latitude =25.148745103323357,
            longitude=121.72695971817735
        )
        line_bot_api.reply_message(event.reply_token, location_message) 
    elif re.match('基隆成功店',message):
        location_message = LocationSendMessage(
            title = '基隆成功店',
            address = '200基隆市仁愛區成功一路130號',
            latitude =25.131495686122204,
            longitude=121.73725940035844
        )
        line_bot_api.reply_message(event.reply_token, location_message) 
    elif re.match('新竹中正店',message):
        location_message = LocationSendMessage(
            title = '新竹中正店',
            address = '300新竹市北區中正路276號',
            latitude =24.81496463315398,
            longitude=120.96404475956182
        )
        line_bot_api.reply_message(event.reply_token, location_message) 
    elif re.match('新竹光華店',message):
        location_message = LocationSendMessage(
            title = '新竹光華店',
            address = '300新竹市北區光華東街38號',
            latitude =24.81839243912497,
            longitude=120.97434444174289
        )
        line_bot_api.reply_message(event.reply_token, location_message) 
    elif re.match('新竹食品店',message):
        location_message = LocationSendMessage(
            title = '新竹食品店',
            address = '300新竹市東區食品路198號',
            latitude =24.801252461116995,
            longitude=120.9764043781791
        )
        line_bot_api.reply_message(event.reply_token, location_message) 
    elif re.match('新竹城隍廟店',message):
        location_message = LocationSendMessage(
            title = '新竹城隍廟店',
            address = '300新竹市北區中山路98號',
            latitude =24.807641275454124,
            longitude=120.96576137325866
        )
        line_bot_api.reply_message(event.reply_token, location_message) 
    elif re.match('新竹巨城店',message):
        location_message = LocationSendMessage(
            title = '新竹巨城店',
            address = '300新竹市東區中央路227號',
            latitude =24.81231580904683,
            longitude=120.97400111900353
        )
        line_bot_api.reply_message(event.reply_token, location_message) 
    elif re.match('桃園中華店',message):
        location_message = LocationSendMessage(
            title = '桃園中華店',
            address = '33065桃園市桃園區中華路61號',
            latitude =24.997262659363674,
            longitude=121.3113991675563
        )
        line_bot_api.reply_message(event.reply_token, location_message) 
    elif re.match('桃園寶山店',message):
        location_message = LocationSendMessage(
            title = '桃園寶山店',
            address = '33074桃園市桃園區寶山街182號',
            latitude =25.01997545933184,
            longitude=121.31551904042874
        )
        line_bot_api.reply_message(event.reply_token, location_message) 
    elif re.match('桃園大同店',message):
        location_message = LocationSendMessage(
            title = '桃園大同店',
            address = '33065桃園市桃園區大同路41號',
            latitude =24.995395667116288,
            longitude=121.3113991675563
        )
        line_bot_api.reply_message(event.reply_token, location_message) 
    elif re.match('桃園縣府店',message):
        location_message = LocationSendMessage(
            title = '桃園縣府店',
            address = '330026桃園市桃園區縣府路296號',
            latitude =25.00068540481401,
            longitude=121.30041283989648
        )
        line_bot_api.reply_message(event.reply_token, location_message) 
    elif re.match('桃園莊敬店',message):
        location_message = LocationSendMessage(
            title = '桃園莊敬店',
            address = '330桃園市桃園區莊敬路一段315號',
            latitude =25.030863667995153,
            longitude=121.29629296702407
        )
        line_bot_api.reply_message(event.reply_token, location_message)  
    elif re.match('新竹新埔店',message):
        location_message = LocationSendMessage( 
            title = '新竹新埔店',
            address = '305新竹縣新埔鎮中正路302號',
            latitude =24.83454674328046,
            longitude=121.08128343245075
        )
        line_bot_api.reply_message(event.reply_token, location_message)     
    elif re.match('新竹芎林店',message):
        location_message = LocationSendMessage(
            title = '新竹芎林店',
            address = '307新竹縣芎林鄉文山路511號',
            latitude =24.781879583965804,
            longitude=121.07785020505705
        )
        line_bot_api.reply_message(event.reply_token, location_message) 
    elif re.match('竹北文興店',message):
        location_message = LocationSendMessage(
            title = '竹北文興店',
            address = '302新竹縣竹北市文興路二段48號',
            latitude =24.813981166885334,
            longitude=121.0315016352422
        )
        line_bot_api.reply_message(event.reply_token, location_message) 
    elif re.match('竹北中正店',message):
        location_message = LocationSendMessage(
            title = '竹北中正店',
            address = '302新竹縣竹北市中正西路123號',
            latitude =24.847009066746622,
            longitude=120.99922929774151
        )
        line_bot_api.reply_message(event.reply_token, location_message) 
    elif re.match('新竹北埔店',message):
        location_message = LocationSendMessage(
            title = '新竹北埔店',
            address = '314新竹縣北埔鄉南興街152號',
            latitude =24.70954269429988,
            longitude=121.05519090425868
        )
        line_bot_api.reply_message(event.reply_token, location_message) 
    elif re.match('宜蘭店',message):
        location_message = LocationSendMessage(
            title = '宜蘭店',
            address = '260宜蘭縣宜蘭市中山路三段201號1樓',
            latitude =24.777215555855662,
            longitude=121.75078983867235
        )
        line_bot_api.reply_message(event.reply_token, location_message) 
    elif re.match('礁溪門市',message):
        location_message = LocationSendMessage(
            title = '礁溪門市',
            address = '262宜蘭縣礁溪鄉礁溪路五段70號',
            latitude =24.838297219089956,
            longitude=121.77207584851323
        )
        line_bot_api.reply_message(event.reply_token, location_message) 
    elif re.match('宜蘭五結門市',message):
        location_message = LocationSendMessage(
            title = '宜蘭五結門市',
            address = '268宜蘭縣五結鄉五結路二段440號',
            latitude =24.70238073207602,
            longitude=121.7981683767053
        )
        line_bot_api.reply_message(event.reply_token, location_message) 
    elif re.match('頭城店',message):
        location_message = LocationSendMessage(
            title = '頭城店',
            address = '26143宜蘭縣頭城鎮青雲路三段169號',
            latitude =24.871941591836926,
            longitude=121.82563419585485
        )
        line_bot_api.reply_message(event.reply_token, location_message) 
    elif re.match('羅東門市',message):
        location_message = LocationSendMessage(
            title = '羅東門市',
            address = '265宜蘭縣羅東鎮民生路120號',
            latitude =24.689903884831775,
            longitude=121.7638361027684
        )
        line_bot_api.reply_message(event.reply_token, location_message) 
    #西部---------------------------------
    elif re.match('台中靜宜店',message):
        location_message = LocationSendMessage(
            title = '台中靜宜店',
            address = '433台中市沙鹿區北勢東路609號',
            latitude =24.234743990233493,
            longitude=120.57307760705014
        )
        line_bot_api.reply_message(event.reply_token, location_message)
    elif re.match('台中新時代店',message):
        location_message = LocationSendMessage(
            title = '台中新時代店',
            address = '401台中市東區復興路四段186號B1',
            latitude =24.142887103536093,
            longitude=120.6852595352422
        )
        line_bot_api.reply_message(event.reply_token, location_message)
    elif re.match('文心秀泰店',message):
        location_message = LocationSendMessage(
            title = '文心秀泰店',
            address = '408台中市南屯區文心南路289號B1',
            latitude =24.136621115676036,
            longitude=120.64406080651794
        )
        line_bot_api.reply_message(event.reply_token, location_message)
    elif re.match('台中后里店',message):
        location_message = LocationSendMessage(
            title = '台中后里店',
            address = '421台中市后里區甲后路一段337號',
            latitude =24.314845047678688,
            longitude=120.72462457167843
        )
        line_bot_api.reply_message(event.reply_token, location_message)
    elif re.match('清水服務區店',message):
        location_message = LocationSendMessage(
            title = '清水服務區店',
            address = '436台中市清水區吳厝二街89號',
            latitude =24.288579977496404,
            longitude=120.60191671715714
        )
        line_bot_api.reply_message(event.reply_token, location_message)
    elif re.match('苗栗公館店',message):
        location_message = LocationSendMessage(
            title = '苗栗公館店',
            address = '360苗栗縣苗栗市至公路140號',
            latitude =24.56865452749032,
            longitude=120.81477833910452
        )
        line_bot_api.reply_message(event.reply_token, location_message)
    elif re.match('南苗中正店',message):
        location_message = LocationSendMessage(
            title = '南苗中正店',
            address = '360苗栗縣苗栗市中正路886號',
            latitude =24.5642830971332,
            longitude=120.81477833910452
        )
        line_bot_api.reply_message(event.reply_token, location_message)
    elif re.match('苗栗正發店',message):
        location_message = LocationSendMessage(
            title = '苗栗正發店',
            address = '360苗栗縣苗栗市正發路35號',
            latitude =24.58301672502616,
            longitude=120.82095814841314
        )
        line_bot_api.reply_message(event.reply_token, location_message)
    elif re.match('苗栗通霄店',message):
        location_message = LocationSendMessage( 
            title = '苗栗通霄店',
            address = '357苗栗縣通霄鎮中山路145號',
            latitude =24.50181745648209,
            longitude=120.67744924335682
        )
        line_bot_api.reply_message(event.reply_token, location_message)
    elif re.match('苗栗公館店',message):
        location_message = LocationSendMessage(
            title = '苗栗公館店',
            address = '363苗栗縣公館鄉大同路225號',
            latitude =24.517436780246936,
            longitude=120.83331776703045
        )
        line_bot_api.reply_message(event.reply_token, location_message)
    elif re.match('員林中山店',message):
        location_message = LocationSendMessage(
            title = '員林中山店',
            address = '510彰化縣員林市中山路二段12號',
            latitude =23.97039148529133,
            longitude=120.57216197979301
        )
        line_bot_api.reply_message(event.reply_token, location_message)
    elif re.match('大溪崎頂店',message):
        location_message = LocationSendMessage(
            title = '大溪崎頂店',
            address = '335桃園市大溪區介壽路844-5號',
            latitude =24.911660854403653,
            longitude=121.27883187048437
        )
        line_bot_api.reply_message(event.reply_token, location_message)
    elif re.match('雲林西螺店',message):
        location_message = LocationSendMessage( 
            title = '雲林西螺店',
            address = '648雲林縣西螺鎮1',
            latitude =23.800155139136976,
            longitude=120.47211353598186
        )
        line_bot_api.reply_message(event.reply_token, location_message)
    #南部---------------------------------
    elif re.match('夢時代店',message):
        location_message = LocationSendMessage(
            title = '夢時代店',
            address = '806高雄市前鎮區中華五路789號B1',
            latitude =22.59819913951536,
            longitude=120.30661889720888
        )
        line_bot_api.reply_message(event.reply_token, location_message)
    elif re.match('左營新光店',message):
        location_message = LocationSendMessage( 
            title = '左營新光店',
            address = '813高雄市左營區高鐵路123號B2地下2樓',
            latitude =22.690041077285354,
            longitude=120.30974318131796
        )
        line_bot_api.reply_message(event.reply_token, location_message)
    elif re.match('高雄SKM Park店',message):
        location_message = LocationSendMessage( 
            title = '高雄SKM Park店',
            address = '806高雄市前鎮區中安路1-1號',
            latitude =22.586620235170443,
            longitude=120.32866040625143
        )
        line_bot_api.reply_message(event.reply_token, location_message)
    elif re.match('成功家樂福店',message):
        location_message = LocationSendMessage( 
            title = '成功家樂福店',
            address = '806高雄市前鎮區中華五路1111號1樓',
            latitude =22.608490799066303,
            longitude=120.30462781449555
        )
        line_bot_api.reply_message(event.reply_token, location_message)
    elif re.match('TEA',message):
        location_message = LocationSendMessage( 
            title = 'TEA',
            address = '840高雄市大樹區',
            latitude =22.660046956841143,
            longitude=120.42123318131796
        )
        line_bot_api.reply_message(event.reply_token, location_message)
    elif re.match('南紡購物中心店',message):
        location_message = LocationSendMessage( 
            title = '南紡購物中心店',
            address = '701台南市東區中華路一段366號B1',
            latitude =22.992656502947344,
            longitude=120.23350936622536
        )
        line_bot_api.reply_message(event.reply_token, location_message)
    elif re.match('永康自強店',message):
        location_message = LocationSendMessage( 
            title = '永康自強店',
            address = '710036台南市永康區自強路662號',
            latitude =23.03875522668223,
            longitude=120.25978682899078
        )
        line_bot_api.reply_message(event.reply_token, location_message)
    elif re.match('台南新市店',message):
        location_message = LocationSendMessage( 
            title = '台南新市店',
            address = '744007台南市新市區復興路187號',
            latitude =23.0861378040116,
            longitude=120.29377578018834
        )
        line_bot_api.reply_message(event.reply_token, location_message)
    elif re.match('敲敲Knock knock',message):
        location_message = LocationSendMessage( 
            title = '敲敲Knock knock',
            address = '880澎湖縣馬公市光復路181之1號',
            latitude =23.57411348393427,
            longitude=119.57225065423698
        )
        line_bot_api.reply_message(event.reply_token, location_message)
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
    
    