from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import *

#======這裡是呼叫的檔案內容=====
from ytmovie import *
from stust import *
from other import *
from cocomenu import *
from fifmenu import *
from concity import *
from cowcity import *
from coscity import *
from coecity import *
from fincity import * 
from fiwcity import *
from fiscity import *
from fiecity import *
from rech import *
#載入Selenium相關模組
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
#======python的函數庫==========
import re
import tempfile, os
import datetime
import time
from bs4 import BeautifulSoup

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
    message = event.message.text
    stw = event.message.text
    #文字表達
    if re.match('呼叫機器人',message):
        flex_message = TextSendMessage(text='需要什麼幫忙嗎???',
                            quick_reply=QuickReply(items=[
                                QuickReplyButton(action=MessageAction(label="查看影片", text="查看影片")),
                                QuickReplyButton(action=MessageAction(label="南台科技大學", text="南台科技大學")),
                                QuickReplyButton(action=MessageAction(label="其他選項", text="其他選項")),
                                QuickReplyButton(action=MessageAction(label="館長最近影片", text="館長最近影片")),
                                QuickReplyButton(action=MessageAction(label="想喝手搖杯", text="想喝手搖杯"))

                            ]))
        line_bot_api.reply_message(event.reply_token, flex_message)
        #line_bot_api.reply_message(event.reply_token,TextSendMessage('error'))  
    elif re.match('館長最近影片',stw):
        def body():
            driver=webdriver.Chrome()
            driver.maximize_window()#視窗最大化
            driver.get("https://www.youtube.com/@Notorious_3cm/videos")
            n=0
            while n<3:
                driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
                time.sleep(5)
                n+=1

            titleTags=driver.find_elements(By.CLASS_NAME,"style-scope ytd-rich-grid-media")
            links = driver.find_elements(By.CSS_SELECTOR,".yt-simple-endpoint.inline-block.style-scope.ytd-thumbnail")
            video_data = []
            i = 1
            for titleTag, link in zip(titleTags, links):
                titel_menu="標題",i,":",titleTag.text
                link.get_attribute("href")
                if video_url and "/watch?" in video_url:
                    video_url = "標題",i,"影片連結:"
                    video_data.append((titel_menu,video_url))
            driver.close()        
            message = []
            message.append(video_data)
            return message
        message=body()
        line_bot_api.reply_message(event.reply_token,message)


    

    elif re.match('查看影片',stw):
        message = ytm()
        line_bot_api.reply_message(event.reply_token,message)
    #
    elif re.match('南台科技大學',stw):
        message = sts()
        line_bot_api.reply_message(event.reply_token,message)
    #大圖片(內容包含:颱風情報、南台選課、 BMI值計算、食物熱量查詢)    
    elif re.match('其他選項',stw):
        message = oth()    
        line_bot_api.reply_message(event.reply_token,message)
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
    #coco菜單系列
    elif re.match('CoCo菜單',stw):
        message = Co()
        line_bot_api.reply_message(event.reply_token,message)
    #50嵐菜單系列
    elif re.match('50嵐菜單',stw):
        message = fif()
        line_bot_api.reply_message(event.reply_token,message) 
    #返回選項
    elif re.match('返回選項',stw):
        message = rec()
        line_bot_api.reply_message(event.reply_token,message) 
   
     
  
    
    elif re.match('CoCo飲料店',message):
        flex_message = FlexSendMessage(
            alt_text='訊息',
            contents={
                "type": "bubble",
                "hero": {
                    "type": "image",
                    "url": "https://i0.wp.com/whityeat.com/wp-content/uploads/20200804043847_39.png?fit=1161%2C1161&quality=100&ssl=1",
                    "size": "full",
                    "aspectRatio": "20:13"
                },
                "body": {
                    "type": "box",
                    "layout": "vertical",
                    "contents": [
                        {
                            "type": "text",
                            "text": "選擇台灣地區?",
                            "align": "center",
                            "margin": "none",
                            "size": "xl",
                            "color": "#FFFFFF"
                        }
                    ],
                    "backgroundColor": "#000000"
                },
                "footer": {
                    "type": "box",
                    "layout": "vertical",
                    "spacing": "sm",
                    "contents": [
                        {
                            "type": "button",
                            "style": "primary",
                            "height": "sm",
                            "action": {
                                "type": "message",
                                "label": "北",
                                "text": "北部CoCo飲料店"
                            },
                            "color": "#FF5151"
                        },
                        {
                            "type": "button",
                            "style": "primary",
                            "height": "sm",
                            "action": {
                                "type": "message",
                                "label": "西",
                                "text": "西部CoCo飲料店"
                            },
                            "color": "#FF8040"
                        },
                        {
                            "type": "button",
                            "style": "primary",
                            "height": "sm",
                            "action": {
                                "type": "message",
                                "label": "南",
                                "text": "南部CoCo飲料店"
                            },
                            "color": "#2894FF"
                        },
                        {
                            "type": "button",
                            "style": "primary",
                            "height": "sm",
                            "action": {
                                "type": "message",
                                "label": "東",
                                "text": "東部CoCo飲料店"
                            },
                            "color": "#00EC00"
                        }
                    ],
                    "flex": 0,
                    "backgroundColor": "#000000"
                }
            }
        )
        line_bot_api.reply_message(event.reply_token, flex_message)

    elif re.match('50嵐飲料店',message):
        flex_message = FlexSendMessage(
            alt_text='訊息',
            contents={
                "type": "bubble",
                "hero": {
                    "type": "image",
                    "url": "https://lh3.googleusercontent.com/p/AF1QipNxx0ndc2NblqMOhxXUGH93fesb9f-C8e-NeDA5=w1080-h608-p-no-v0",
                    "size": "full",
                    "aspectRatio": "20:13"
                },
                "body": {
                    "type": "box",
                    "layout": "vertical",
                    "contents": [
                        {
                            "type": "text",
                            "text": "選擇台灣地區?",
                            "align": "center",
                            "margin": "none",
                            "size": "xl",
                            "color": "#FFFFFF"
                        }
                    ],
                    "backgroundColor": "#642100"
                },
                "footer": {
                    "type": "box",
                    "layout": "vertical",
                    "spacing": "sm",
                    "contents": [
                        {
                            "type": "button",
                            "style": "primary",
                            "height": "sm",
                            "action": {
                                "type": "message",
                                "label": "北",
                                "text": "北部50嵐飲料店"
                            },
                            "color": "#FF5151"
                        },
                        {
                            "type": "button",
                            "style": "primary",
                            "height": "sm",
                            "action": {
                                "type": "message",
                                "label": "西",
                                "text": "西部50嵐飲料店"
                            },
                            "color": "#FF8040"
                        },
                        {
                            "type": "button",
                            "style": "primary",
                            "height": "sm",
                            "action": {
                                "type": "message",
                                "label": "南",
                                "text": "南部50嵐飲料店"
                            },
                            "color": "#2894FF"
                        },
                        {
                            "type": "button",
                            "style": "primary",
                            "height": "sm",
                            "action": {
                                "type": "message",
                                "label": "東",
                                "text": "東部50嵐飲料店"
                            },
                            "color": "#00EC00"
                        }
                    ],
                    "flex": 0,
                    "backgroundColor": "#642100"
                }
            }
        )
        line_bot_api.reply_message(event.reply_token, flex_message)


#北部CoCo飲料店------------------------------------------------------------
    elif re.match('北部CoCo飲料店',stw):
        message = cnc()
        line_bot_api.reply_message(event.reply_token,message)        
#西部CoCo飲料店------------------------------------------------------------
    elif re.match('西部CoCo飲料店',stw):
        message = cwc()
        line_bot_api.reply_message(event.reply_token,message)
#南部CoCo飲料店------------------------------------------------------------
    elif re.match('南部CoCo飲料店',stw):
        message = csc()
        line_bot_api.reply_message(event.reply_token,message)
#東部CoCo飲料店------------------------------------------------------------
    elif re.match('東部CoCo飲料店',stw):
        message = cec()
        line_bot_api.reply_message(event.reply_token,message)


#北部50嵐飲料店------------------------------------------------------------
    elif re.match('北部50嵐飲料店',stw):
        message = fnc()
        line_bot_api.reply_message(event.reply_token,message)
#西部50嵐飲料店------------------------------------------------------------
    elif re.match('西部50嵐飲料店',stw):
        message = fwc()
        line_bot_api.reply_message(event.reply_token,message)
#南部50嵐飲料店------------------------------------------------------------
    elif re.match('南部50嵐飲料店',stw):
        message = fsc()
        line_bot_api.reply_message(event.reply_token,message)
#東部50嵐飲料店------------------------------------------------------------
    elif re.match('東部50嵐飲料店',stw):
        message = fec()
        line_bot_api.reply_message(event.reply_token,message)


#臺北市CoCo飲料店




#台灣北部----------------------------------------------------
#cooc   
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
#50嵐
    elif re.match('臺北市50嵐飲料店',message):
        flex_message = TextSendMessage(text='選擇店家???',
                            quick_reply=QuickReply(items=[
                                QuickReplyButton(action=MessageAction(label="開封店", text="開封店")),
                                QuickReplyButton(action=MessageAction(label="重慶店", text="重慶店")),
                                QuickReplyButton(action=MessageAction(label="信陽店", text="信陽店")),
                                QuickReplyButton(action=MessageAction(label="北車店", text="北車店")),
                                QuickReplyButton(action=MessageAction(label="伊通店", text="伊通店"))                     
                            ]))
        line_bot_api.reply_message(event.reply_token, flex_message)  
    elif re.match('新北市50嵐飲料店',message):
        flex_message = TextSendMessage(text='選擇店家???',
                            quick_reply=QuickReply(items=[
                                QuickReplyButton(action=MessageAction(label="重新店", text="重新店")),
                                QuickReplyButton(action=MessageAction(label="新泰店", text="新泰店")),
                                QuickReplyButton(action=MessageAction(label="樂華店", text="樂華店")),
                                QuickReplyButton(action=MessageAction(label="新莊中和店", text="新莊中和店")),
                                QuickReplyButton(action=MessageAction(label="南勢角店", text="南勢角店"))                     
                            ]))
        line_bot_api.reply_message(event.reply_token, flex_message) 
    elif re.match('基隆市50嵐飲料店',message):
        flex_message = TextSendMessage(text='選擇店家???',
                            quick_reply=QuickReply(items=[
                                QuickReplyButton(action=MessageAction(label="基隆廟口店", text="基隆廟口店"))                     
                            ]))
        line_bot_api.reply_message(event.reply_token, flex_message)
    elif re.match('新竹市50嵐飲料店',message):
        flex_message = TextSendMessage(text='選擇店家???',
                            quick_reply=QuickReply(items=[
                                QuickReplyButton(action=MessageAction(label="新竹東門店", text="新竹東門店")),
                                QuickReplyButton(action=MessageAction(label="新竹民生店", text="新竹民生店")),
                                QuickReplyButton(action=MessageAction(label="新竹光復店", text="新竹光復店")),
                                QuickReplyButton(action=MessageAction(label="新竹中山店", text="新竹中山店")),
                                QuickReplyButton(action=MessageAction(label="新竹林森店", text="新竹林森店"))                     
                            ]))
        line_bot_api.reply_message(event.reply_token, flex_message) 
    elif re.match('桃園市50嵐飲料店',message):
        flex_message = TextSendMessage(text='選擇店家???',
                            quick_reply=QuickReply(items=[
                                QuickReplyButton(action=MessageAction(label="中正店", text="中正店")),
                                QuickReplyButton(action=MessageAction(label="中山東店", text="中山東店")),
                                QuickReplyButton(action=MessageAction(label="大興店", text="大興店")),
                                QuickReplyButton(action=MessageAction(label="桃鶯店", text="桃鶯店")),
                                QuickReplyButton(action=MessageAction(label="長庚店", text="長庚店"))                     
                            ]))
        line_bot_api.reply_message(event.reply_token, flex_message) 
    elif re.match('新竹縣50嵐飲料店',message):
        flex_message = TextSendMessage(text='選擇店家???',
                            quick_reply=QuickReply(items=[
                                QuickReplyButton(action=MessageAction(label="竹北正東店", text="竹北正東店")),
                                QuickReplyButton(action=MessageAction(label="湖口新工店", text="湖口新工店")),
                                QuickReplyButton(action=MessageAction(label="竹北正西", text="竹北正西")),
                                QuickReplyButton(action=MessageAction(label="竹北博愛店", text="竹北博愛店")),
                                QuickReplyButton(action=MessageAction(label="嘉豐南店", text="嘉豐南店"))                     
                            ]))
        line_bot_api.reply_message(event.reply_token, flex_message) 
#台灣西部----------------------------------------------------    
#coco
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
#50嵐
    elif re.match('臺中市50嵐飲料店',message):
        flex_message = TextSendMessage(text='選擇店家???',
                            quick_reply=QuickReply(items=[
                                QuickReplyButton(action=MessageAction(label="英才店", text="英才店")),
                                QuickReplyButton(action=MessageAction(label="公園店", text="公園店")),
                                QuickReplyButton(action=MessageAction(label="繼光店", text="繼光店")),
                                QuickReplyButton(action=MessageAction(label="美村一店", text="美村一店")),
                                QuickReplyButton(action=MessageAction(label="學士店", text="學士店"))                     
                            ]))
        line_bot_api.reply_message(event.reply_token, flex_message) 
    elif re.match('苗栗縣50嵐飲料店',message):
        flex_message = TextSendMessage(text='選擇店家???',
                            quick_reply=QuickReply(items=[
                                QuickReplyButton(action=MessageAction(label="苗栗中正店", text="苗栗中正店")),
                                QuickReplyButton(action=MessageAction(label="苗栗府前店", text="苗栗府前店")),
                                QuickReplyButton(action=MessageAction(label="苗栗為公店", text="苗栗為公店")),
                                QuickReplyButton(action=MessageAction(label="苗栗公館店", text="苗栗公館店")),
                                QuickReplyButton(action=MessageAction(label="苑裡店", text="苑裡店"))                     
                            ]))
        line_bot_api.reply_message(event.reply_token, flex_message)
    elif re.match('彰化縣50嵐飲料店',message):
        flex_message = TextSendMessage(text='選擇店家???',
                            quick_reply=QuickReply(items=[
                                QuickReplyButton(action=MessageAction(label="彰化彰美店", text="彰化彰美店")),
                                QuickReplyButton(action=MessageAction(label="秀水店", text="秀水店")),
                                QuickReplyButton(action=MessageAction(label="彰化白沙店", text="彰化白沙店")),
                                QuickReplyButton(action=MessageAction(label="彰化大竹店", text="彰化大竹店")),
                                QuickReplyButton(action=MessageAction(label="彰化大村店", text="彰化大村店"))                     
                            ]))
        line_bot_api.reply_message(event.reply_token, flex_message)
    elif re.match('南投縣50嵐飲料店',message):
        flex_message = TextSendMessage(text='選擇店家???',
                            quick_reply=QuickReply(items=[
                                QuickReplyButton(action=MessageAction(label="草屯中正店", text="草屯中正店")),
                                QuickReplyButton(action=MessageAction(label="南投民族店", text="南投民族店")),
                                QuickReplyButton(action=MessageAction(label="南投民族二店", text="南投民族二店")),
                                QuickReplyButton(action=MessageAction(label="南投名間店", text="南投名間店")),
                                QuickReplyButton(action=MessageAction(label="南投集集店", text="南投集集店"))                     
                            ]))
        line_bot_api.reply_message(event.reply_token, flex_message)
    elif re.match('雲林縣50嵐飲料店',message):
        flex_message = TextSendMessage(text='選擇店家???',
                            quick_reply=QuickReply(items=[
                                QuickReplyButton(action=MessageAction(label="麥寮店", text="麥寮店")),
                                QuickReplyButton(action=MessageAction(label="虎尾林森店", text="虎尾林森店")),
                                QuickReplyButton(action=MessageAction(label="北港中山店", text="北港中山店")),
                                QuickReplyButton(action=MessageAction(label="雲林土庫店", text="雲林土庫店")),
                                QuickReplyButton(action=MessageAction(label="斗南中山店", text="斗南中山店"))                     
                            ]))
        line_bot_api.reply_message(event.reply_token, flex_message)
#台灣南部----------------------------------------------------
#coco
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
#50嵐
    elif re.match('高雄市50嵐飲料店',message):
        flex_message = TextSendMessage(text='選擇店家???',
                            quick_reply=QuickReply(items=[
                                QuickReplyButton(action=MessageAction(label="自立七賢店", text="自立七賢店")),
                                QuickReplyButton(action=MessageAction(label="重愛店", text="重愛店")),
                                QuickReplyButton(action=MessageAction(label="河堤裕誠店", text="河堤裕誠店")),
                                QuickReplyButton(action=MessageAction(label="大社二店", text="大社二店")),
                                QuickReplyButton(action=MessageAction(label="大順店", text="大順店"))                     
                            ]))
        line_bot_api.reply_message(event.reply_token, flex_message)
    elif re.match('臺南市50嵐飲料店',message):
        flex_message = TextSendMessage(text='選擇店家???',
                            quick_reply=QuickReply(items=[
                                QuickReplyButton(action=MessageAction(label="赤崁店", text="赤崁店")),
                                QuickReplyButton(action=MessageAction(label="青年店", text="青年店")),
                                QuickReplyButton(action=MessageAction(label="公園店", text="公園店")),
                                QuickReplyButton(action=MessageAction(label="民族店", text="民族店")),
                                QuickReplyButton(action=MessageAction(label="南園店", text="南園店"))                     
                            ]))
        line_bot_api.reply_message(event.reply_token, flex_message)
    elif re.match('嘉義縣50嵐飲料店',message):
        flex_message = TextSendMessage(text='選擇店家???',
                            quick_reply=QuickReply(items=[
                                QuickReplyButton(action=MessageAction(label="嘉義太保店", text="嘉義太保店")),
                                QuickReplyButton(action=MessageAction(label="太保中山店", text="太保中山店")),
                                QuickReplyButton(action=MessageAction(label="嘉義水上店", text="嘉義水上店")),
                                QuickReplyButton(action=MessageAction(label="嘉義頭橋店", text="嘉義頭橋店")),
                                QuickReplyButton(action=MessageAction(label="嘉義民雄店", text="嘉義民雄店"))                     
                            ]))
        line_bot_api.reply_message(event.reply_token, flex_message)
    elif re.match('嘉義市50嵐飲料店',message):
        flex_message = TextSendMessage(text='選擇店家???',
                            quick_reply=QuickReply(items=[
                                QuickReplyButton(action=MessageAction(label="嘉義中山店", text="嘉義中山店")),
                                QuickReplyButton(action=MessageAction(label="嘉義民族店", text="嘉義民族店")),
                                QuickReplyButton(action=MessageAction(label="嘉義文化店", text="嘉義文化店")),
                                QuickReplyButton(action=MessageAction(label="嘉義友愛店", text="嘉義友愛店")),
                                QuickReplyButton(action=MessageAction(label="嘉義新生店", text="嘉義新生店"))                     
                            ]))
        line_bot_api.reply_message(event.reply_token, flex_message)
    elif re.match('屏東縣50嵐飲料店',message):
        flex_message = TextSendMessage(text='選擇店家???',
                            quick_reply=QuickReply(items=[
                                QuickReplyButton(action=MessageAction(label="屏東勝利店", text="屏東勝利店")),
                                QuickReplyButton(action=MessageAction(label="屏東中正自由店", text="屏東中正自由店")),
                                QuickReplyButton(action=MessageAction(label="屏東棒球路店", text="屏東棒球路店")),
                                QuickReplyButton(action=MessageAction(label="屏大民生店", text="屏大民生店")),
                                QuickReplyButton(action=MessageAction(label="屏東林森店", text="屏東林森店"))                     
                            ]))
        line_bot_api.reply_message(event.reply_token, flex_message)
    elif re.match('澎湖縣50嵐飲料店',message):
        flex_message = TextSendMessage(text='選擇店家???',
                            quick_reply=QuickReply(items=[
                                QuickReplyButton(action=MessageAction(label="澎湖馬公店", text="澎湖馬公店")),
                                QuickReplyButton(action=MessageAction(label="澎湖中正店", text="澎湖中正店")),
                                QuickReplyButton(action=MessageAction(label="澎湖光復店", text="澎湖光復店"))                     
                            ]))
        line_bot_api.reply_message(event.reply_token, flex_message)
#台灣東部---------------------------------------------------------  
#50
    elif re.match('臺東縣50嵐飲料店',message):
        flex_message = TextSendMessage(text='選擇店家???',
                            quick_reply=QuickReply(items=[
                                QuickReplyButton(action=MessageAction(label="台東中華店", text="台東中華店")),
                                QuickReplyButton(action=MessageAction(label="台東東商店", text="台東東商店"))                     
                            ]))
        line_bot_api.reply_message(event.reply_token, flex_message)

#地圖座標位址---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#北部---------------------------------
#coco
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
#50嵐
    elif re.match('開封店',message):
        location_message = LocationSendMessage(
            title = '開封店',
            address = '100台北市中正區開封街一段9號',
            latitude =25.049850913457274,
            longitude=121.5138821972089
        )
        line_bot_api.reply_message(event.reply_token, location_message)    
    elif re.match('重慶店',message):
        location_message = LocationSendMessage(
            title = '重慶店',
            address = '103台北市大同區重慶北路一段84號',
            latitude =25.0560713500303,
            longitude=121.5138821972089
        )
        line_bot_api.reply_message(event.reply_token, location_message) 
    elif re.match('信陽店',message):
        location_message = LocationSendMessage(
            title = '信陽店',
            address = '100台北市中正區信陽街13號',
            latitude =25.048295754992203,
            longitude=121.51594213364511
        )
        line_bot_api.reply_message(event.reply_token, location_message) 
    elif re.match('北車店',message):
        location_message = LocationSendMessage(
            title = '北車店',
            address = 'B1, No. 49號 號忠孝西路一段中正區台北市100',
            latitude =25.049850913457274,
            longitude=121.51731542460259
        )
        line_bot_api.reply_message(event.reply_token, location_message) 
    elif re.match('伊通店',message):
        location_message = LocationSendMessage(
            title = '伊通店',
            address = '10485台北市中山區伊通街66-2號',
            latitude =25.05560482823755,
            longitude=121.53413823883167
        )
        line_bot_api.reply_message(event.reply_token, location_message) 
    elif re.match('重新店',message):
        location_message = LocationSendMessage(
            title = '重新店',
            address ='241新北市三重區重新路三段5號',
            latitude =25.064643261335295,
            longitude=121.49571371994826
        )
        line_bot_api.reply_message(event.reply_token, location_message) 
    elif re.match('新泰店',message):
        location_message = LocationSendMessage(
            title = '新泰店',
            address ='242新北市新莊區新泰路311號',
            latitude =25.043215019268168,
            longitude=121.44453345173015
        )
        line_bot_api.reply_message(event.reply_token, location_message) 
    elif re.match('樂華店',message):
        location_message = LocationSendMessage(
            title = '樂華店',
            address ='234新北市永和區永和路一段144號',
            latitude =25.012288990977442,
            longitude=121.51369581309984
        )
        line_bot_api.reply_message(event.reply_token, location_message) 
    elif re.match('新莊中和店',message):
        location_message = LocationSendMessage(
            title = '新莊中和店',
            address ='242新北市新莊區中和街196號',
            latitude =25.053360847604765,
            longitude=121.44699865173013
        )
        line_bot_api.reply_message(event.reply_token, location_message) 
    elif re.match('南勢角店',message):
        location_message = LocationSendMessage(
            title = '南勢角店',
            address ='235新北市中和區景新街396號',
            latitude =24.99204213503707,
            longitude=121.51233253583919
        )
        line_bot_api.reply_message(event.reply_token, location_message) 
    elif re.match('基隆廟口店',message):
        location_message = LocationSendMessage(
            title = '基隆廟口店',
            address ='20048基隆市仁愛區愛四路1號',
            latitude =25.12796578625099,
            longitude=121.74316374108386
        )
        line_bot_api.reply_message(event.reply_token, location_message) 
    elif re.match('新竹東門店',message):
        location_message = LocationSendMessage(
            title = '新竹東門店',
            address ='300新竹市東區東門街113號',
            latitude =24.807312816093425,
            longitude=120.96876953054579
        )
        line_bot_api.reply_message(event.reply_token, location_message) 
    elif re.match('新竹民生店',message):
        location_message = LocationSendMessage(
            title = '新竹民生店',
            address ='300新竹市東區民生路105號',
            latitude =24.811831546714853,
            longitude=120.9776959215945
        )
        line_bot_api.reply_message(event.reply_token, location_message)
    elif re.match('新竹光復店',message):
        location_message = LocationSendMessage(
            title = '新竹光復店',
            address ='300新竹市東區光復路一段183號',
            latitude =24.785807634381218,
            longitude=121.0218128927391
        )
        line_bot_api.reply_message(event.reply_token, location_message)
    elif re.match('新竹中山店',message):
        location_message = LocationSendMessage(
            title = '新竹中山店',
            address ='300新竹市北區中山路364號',
            latitude =24.804040529014767,
            longitude=120.95932815539811
        )
        line_bot_api.reply_message(event.reply_token, location_message)
    elif re.match('新竹林森店',message):
        location_message = LocationSendMessage(
            title = '新竹林森店',
            address ='300新竹市東區林森路140號',
            latitude =24.80248226671437,
            longitude=120.96430633502142
        )
        line_bot_api.reply_message(event.reply_token, location_message)
    elif re.match('中正店',message):
        location_message = LocationSendMessage(
            title = '中正店',
            address ='330桃園市桃園區中正路542號',
            latitude =25.01615383321403,
            longitude=121.30035299928778
        )
        line_bot_api.reply_message(event.reply_token, location_message)
    elif re.match('中山東店',message):
        location_message = LocationSendMessage(
            title = '中山東店',
            address ='330桃園市桃園區中山東路40號',
            latitude =25.00930910894386,
            longitude=121.32026571778106
        )
        line_bot_api.reply_message(event.reply_token, location_message)
    elif re.match('大興店',message):
        location_message = LocationSendMessage(
            title = '大興店',
            address ='330桃園市桃園區大興路146號',
            latitude =25.029219974504407,
            longitude=121.30927939033648
        )
        line_bot_api.reply_message(event.reply_token, location_message)
    elif re.match('桃鶯店',message):
        location_message = LocationSendMessage(
            title = '桃鶯店',
            address ='330桃園市桃園區桃鶯路97號',
            latitude =24.997485504905832,
            longitude=121.31957907231578
        )
        line_bot_api.reply_message(event.reply_token, location_message)
    elif re.match('長庚店',message):
        location_message = LocationSendMessage(
            title = '長庚店',
            address ='333桃園市龜山區復興一路282號',
            latitude =25.067166112518443,
            longitude=121.36352438209406
        )
        line_bot_api.reply_message(event.reply_token, location_message)
    elif re.match('竹北正東店',message):
        location_message = LocationSendMessage(
            title = '竹北正東店',
            address ='302新竹縣竹北市中正東路262號',
            latitude =24.848396325898307,
            longitude=121.013561629135
        )
        line_bot_api.reply_message(event.reply_token, location_message)
    elif re.match('湖口新工店',message):
        location_message = LocationSendMessage(
            title = '湖口新工店',
            address ='303新竹縣湖口鄉仁和路129號',
            latitude =24.88702111719869,
            longitude=121.01424827460029
        )
        line_bot_api.reply_message(event.reply_token, location_message)
    elif re.match('竹北正西',message):
        location_message = LocationSendMessage(
            title = '竹北正西',
            address ='302新竹縣竹北市中正西路124號',
            latitude =24.852757793718148,
            longitude=121.00463523808628
        )
        line_bot_api.reply_message(event.reply_token, location_message)
    elif re.match('竹北博愛店',message):
        location_message = LocationSendMessage(
            title = '竹北博愛店',
            address ='302新竹縣竹北市博愛街224號',
            latitude =24.84777324651518,
            longitude=121.008755110878
        )
        line_bot_api.reply_message(event.reply_token, location_message)
    elif re.match('嘉豐南店',message):
        location_message = LocationSendMessage(
            title = '嘉豐南店',
            address ='302新竹縣竹北市嘉豐南路二段30號',
            latitude =24.82097786548697,
            longitude=121.02798118390601
        )
        line_bot_api.reply_message(event.reply_token, location_message)
#西部---------------------------------
#coco
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
#50
    elif re.match('英才店',message):
        location_message = LocationSendMessage(
            title = '英才店',
            address ='404台中市北區英才路304號',
            latitude =24.158541767880966,
            longitude=120.67128405531601
        )
        line_bot_api.reply_message(event.reply_token, location_message)
    elif re.match('公園店',message):
        location_message = LocationSendMessage(
            title = '公園店',
            address ='400台中市中區公園路28號',
            latitude =24.148987183851357,
            longitude=120.68072543046372
        )
        line_bot_api.reply_message(event.reply_token, location_message)
    elif re.match('繼光店',message):
        location_message = LocationSendMessage(
            title = '繼光店',
            address ='403台中市西區民權路59號',
            latitude =24.140685079999077,
            longitude=120.68124041456268
        )
        line_bot_api.reply_message(event.reply_token, location_message)
    elif re.match('美村一店',message):
        location_message = LocationSendMessage(
            title = '美村一店',
            address ='403台中市西區美村路一段141號',
            latitude =24.153059716873216,
            longitude=120.66201434153469
        )
        line_bot_api.reply_message(event.reply_token, location_message)
    elif re.match('學士店',message):
        location_message = LocationSendMessage(
            title = '學士店',
            address ='404台中市北區學士路45號',
            latitude =24.15807188701251,
            longitude=120.68192706002797
        )
        line_bot_api.reply_message(event.reply_token, location_message)
    elif re.match('苗栗中正店',message):
        location_message = LocationSendMessage(
            title = '苗栗中正店',
            address ='360苗栗縣苗栗市中正路1077號',
            latitude =24.555201778048716,
            longitude=120.81603326910223
        )
        line_bot_api.reply_message(event.reply_token, location_message)
    elif re.match('苗栗府前店',message):
        location_message = LocationSendMessage(
            title = '苗栗府前店',
            address ='360苗栗縣苗栗市府前路86-2號',
            latitude =24.56862880184728,
            longitude=120.81912317369604
        )
        line_bot_api.reply_message(event.reply_token, location_message)
    elif re.match('苗栗為公店',message):
        location_message = LocationSendMessage(
            title = '苗栗為公店',
            address ='360苗栗縣苗栗市為公路156號',
            latitude =24.57862007213335,
            longitude=120.82907953294269
        )
        line_bot_api.reply_message(event.reply_token, location_message)
    elif re.match('苗栗公館店',message):
        location_message = LocationSendMessage(
            title = '苗栗公館店',
            address ='363苗栗縣公館鄉大同路231-5號',
            latitude =24.511163546278222,
            longitude=120.82942285567533
        )
        line_bot_api.reply_message(event.reply_token, location_message)
    elif re.match('苑裡店',message):
        location_message = LocationSendMessage(
            title = '苑裡店',
            address ='358苗栗縣苑裡鎮為公路85號',
            latitude =24.449046540874303,
            longitude=120.65302416003281
        )
        line_bot_api.reply_message(event.reply_token, location_message)
    elif re.match('彰化彰美店',message):
        location_message = LocationSendMessage(
            title = '彰化彰美店',
            address ='500彰化縣彰化市彰美路一段199號',
            latitude =24.095384191847323,
            longitude=120.5366382785069
        )
        line_bot_api.reply_message(event.reply_token, location_message)
    elif re.match('秀水店',message):
        location_message = LocationSendMessage(
            title = '秀水店',
            address ='504彰化縣秀水鄉彰水路二段549號',
            latitude =24.036136388987593,
            longitude=120.49612619605503
        )
        line_bot_api.reply_message(event.reply_token, location_message)
    elif re.match('彰化白沙店',message):
        location_message = LocationSendMessage(
            title = '彰化白沙店',
            address ='503彰化縣花壇鄉彰員路三段178號',
            latitude =24.05494817932854,
            longitude=120.54659463775356
        )
        line_bot_api.reply_message(event.reply_token, location_message)
    elif re.match('彰化大竹店',message):
        location_message = LocationSendMessage(
            title = '彰化大竹店',
            address ='500彰化縣彰化市彰南路二段89號',
            latitude =24.09256348852466,
            longitude=120.57921029735462
        )
        line_bot_api.reply_message(event.reply_token, location_message)
    elif re.match('彰化大村店',message):
        location_message = LocationSendMessage(
            title = '彰化大村店',
            address ='515彰化縣大村鄉中山路二段298號',
            latitude =23.996936312481946,
            longitude=120.56273080618774
        )
        line_bot_api.reply_message(event.reply_token, location_message)
    elif re.match('草屯中正店',message):
        location_message = LocationSendMessage(
            title = '草屯中正店',
            address ='542南投縣草屯鎮中正路769號',
            latitude =23.988521300838148,
            longitude=120.6848686145675
        )
        line_bot_api.reply_message(event.reply_token, location_message)
    elif re.match('南投民族店',message):
        location_message = LocationSendMessage(
            title = '南投民族店',
            address ='540南投縣南投市民族路307號',
            latitude =23.91384647638434,
            longitude=120.68383864636957
        )
        line_bot_api.reply_message(event.reply_token, location_message)
    elif re.match('南投民族二店',message):
        location_message = LocationSendMessage(
            title = '南投民族二店',
            address ='540南投縣南投市民族路41號',
            latitude =23.919181825671913,
            longitude=120.69242171468565
        )
        line_bot_api.reply_message(event.reply_token, location_message)
    elif re.match('南投名間店',message):
        location_message = LocationSendMessage(
            title = '南投名間店',
            address ='551南投縣名間鄉南雅街145號',
            latitude =23.846071078134823,
            longitude=120.70155966910222
        )
        line_bot_api.reply_message(event.reply_token, location_message)
    elif re.match('南投集集店',message):
        location_message = LocationSendMessage(
            title = '南投集集店',
            address ='552南投縣集集鎮民生路111號',
            latitude =23.832813831541426,
            longitude=120.78534038276547
        )
        line_bot_api.reply_message(event.reply_token, location_message)
    elif re.match('麥寮店',message):
        location_message = LocationSendMessage(
            title = '麥寮店',
            address ='638雲林縣麥寮鄉光復路57號',
            latitude =23.776093251838287,
            longitude=120.25903094920065
        )
        line_bot_api.reply_message(event.reply_token, location_message)
    elif re.match('虎尾林森店',message):
        location_message = LocationSendMessage(
            title = '虎尾林森店',
            address ='632雲林縣虎尾鎮林森路一段398號',
            latitude =23.738385679416616,
            longitude=120.4293190245915
        )
        line_bot_api.reply_message(event.reply_token, location_message)
    elif re.match('北港中山店',message):
        location_message = LocationSendMessage(
            title = '北港中山店',
            address ='651雲林縣北港鎮中山路86號',
            latitude =23.58241204749373,
            longitude=120.30022967711778
        )
        line_bot_api.reply_message(event.reply_token, location_message)
    elif re.match('雲林土庫店',message):
        location_message = LocationSendMessage(
            title = '雲林土庫店',
            address ='633雲林縣土庫鎮建國路121號',
            latitude =23.710726520837618,
            longitude=120.39086687853553
        )
        line_bot_api.reply_message(event.reply_token, location_message)
    elif re.match('斗南中山店',message):
        location_message = LocationSendMessage(
            title = '斗南中山店',
            address ='630雲林縣斗南鎮中山路71號',
            latitude =23.703182095760308,
            longitude=120.48287737088381
        )
        line_bot_api.reply_message(event.reply_token, location_message)
#南部---------------------------------
#coco
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
#50
    elif re.match('自立七賢店',message):
        location_message = LocationSendMessage( 
            title = '自立七賢店',
            address = '801高雄市前金區自立一路43號',
            latitude =22.64156596078769,
            longitude=120.29585876040518
        )
        line_bot_api.reply_message(event.reply_token, location_message)
    elif re.match('重愛店',message):
        location_message = LocationSendMessage( 
            title = '重愛店',
            address = '813高雄市左營區重愛路59號',
            latitude =22.690987731785974,
            longitude=120.31989135169019
        )
        line_bot_api.reply_message(event.reply_token, location_message)
    elif re.match('河堤裕誠店',message):
        location_message = LocationSendMessage( 
            title = '河堤裕誠店',
            address = '813高雄市左營區裕誠路175號',
            latitude =22.670714287219063,
            longitude=120.31233825157206
        )
        line_bot_api.reply_message(event.reply_token, location_message)
    elif re.match('大社二店',message):
        location_message = LocationSendMessage( 
            title = '大社二店',
            address = '815高雄市大社區中山路240號',
            latitude =22.740391684630353,
            longitude=120.34735717030163
        )
        line_bot_api.reply_message(event.reply_token, location_message)
    elif re.match('大順店',message):
        location_message = LocationSendMessage( 
            title = '大順店',
            address = '802高雄市苓雅區大順三路199號',
            latitude =22.641249097153246,
            longitude=120.32847442000624
        )
        line_bot_api.reply_message(event.reply_token, location_message)
    elif re.match('赤崁店',message):
        location_message = LocationSendMessage( 
            title = '赤崁店',
            address = '700台南市中西區民族路二段260號',
            latitude =23.005264140228945,
            longitude=120.20000751037608
        )
        line_bot_api.reply_message(event.reply_token, location_message)
    elif re.match('青年店',message):
        location_message = LocationSendMessage( 
            title = '青年店',
            address = '700台南市中西區青年路136號',
            latitude =22.999891728507304,
            longitude=120.21065051508805
        )
        line_bot_api.reply_message(event.reply_token, location_message)
    elif re.match('公園店',message):
        location_message = LocationSendMessage( 
            title = '公園店',
            address = '704台南市北區公園路790號',
            latitude =23.017904265254828,
            longitude=120.21305377421653
        )
        line_bot_api.reply_message(event.reply_token, location_message)
    elif re.match('民族店',message):
        location_message = LocationSendMessage( 
            title = '民族店',
            address = '700台南市中西區民族路二段139號',
            latitude =23.003368019335234,
            longitude=120.20687396502895
        )
        line_bot_api.reply_message(event.reply_token, location_message)
    elif re.match('南園店',message):
        location_message = LocationSendMessage( 
            title = '南園店',
            address = '704台南市北區南園街118號',
            latitude =23.01537633500083,
            longitude=120.22575671532432
        )
        line_bot_api.reply_message(event.reply_token, location_message)
    elif re.match('嘉義太保店',message):
        location_message = LocationSendMessage( 
            title = '嘉義太保店',
            address = '612嘉義縣太保市祥和三路東段19號',
            latitude =23.460840116071612,
            longitude=120.29197260090432
        )
        line_bot_api.reply_message(event.reply_token, location_message)
    elif re.match('太保中山店',message):
        location_message = LocationSendMessage( 
            title = '太保中山店',
            address = '612嘉義縣太保市中山路二段5-1號',
            latitude =23.50744316285785,
            longitude=120.37608667040183
        )
        line_bot_api.reply_message(event.reply_token, location_message)
    elif re.match('嘉義水上店',message):
        location_message = LocationSendMessage( 
            title = '嘉義水上店',
            address = '608嘉義縣水上鄉中興路300號',
            latitude =23.43670162281299,
            longitude=120.40191976910224
        )
        line_bot_api.reply_message(event.reply_token, location_message)
    elif re.match('嘉義頭橋店',message):
        location_message = LocationSendMessage( 
            title = '嘉義頭橋店',
            address = '621嘉義縣民雄鄉建國路三段144號',
            latitude =23.53053784777387,
            longitude=120.43693868783183
        )
        line_bot_api.reply_message(event.reply_token, location_message)
    elif re.match('嘉義民雄店',message):
        location_message = LocationSendMessage( 
            title = '嘉義民雄店',
            address = '621嘉義縣民雄鄉東榮路15號',
            latitude =23.563619658366584,
            longitude=120.43440530549807
        )
        line_bot_api.reply_message(event.reply_token, location_message)
    elif re.match('嘉義中山店',message):
        location_message = LocationSendMessage( 
            title = '嘉義中山店',
            address = '600嘉義市東區中山路57號',
            latitude =23.48404575537445,
            longitude=120.4586958791027
        )
        line_bot_api.reply_message(event.reply_token, location_message)
    elif re.match('嘉義民族店',message):
        location_message = LocationSendMessage( 
            title = '嘉義民族店',
            address = '600嘉義市西區民族路716號',
            latitude =23.476960636993113,
            longitude=120.44307469476747
        )
        line_bot_api.reply_message(event.reply_token, location_message)
    elif re.match('嘉義文化店',message):
        location_message = LocationSendMessage( 
            title = '嘉義文化店',
            address = '600嘉義市東區文化路190號',
            latitude =23.482786206590745,
            longitude=120.44951199600453
        )
        line_bot_api.reply_message(event.reply_token, location_message)
    elif re.match('嘉義友愛店',message):
        location_message = LocationSendMessage( 
            title = '嘉義友愛店',
            address = '600嘉義市西區友愛路202號',
            latitude =23.48317981687793,
            longitude=120.43431996508505
        )
        line_bot_api.reply_message(event.reply_token, location_message)
    elif re.match('嘉義新生店',message):
        location_message = LocationSendMessage( 
            title = '嘉義新生店',
            address = '600嘉義市東區新生路752號',
            latitude =23.496719295346033,
            longitude=120.45603512792475
        )
        line_bot_api.reply_message(event.reply_token, location_message)
    elif re.match('屏東勝利店',message):
        location_message = LocationSendMessage( 
            title = '屏東勝利店',
            address = '900屏東縣屏東市勝利路205號',
            latitude =22.68241273511173,
            longitude=120.47928179568784
        )
        line_bot_api.reply_message(event.reply_token, location_message)
    elif re.match('屏東中正自由店',message):
        location_message = LocationSendMessage( 
            title = '屏東中正自由店',
            address = '900屏東縣屏東市中正路348號',
            latitude =22.686530669803894,
            longitude=120.49095476859766
        )
        line_bot_api.reply_message(event.reply_token, location_message)
    elif re.match('屏東棒球路店',message):
        location_message = LocationSendMessage( 
            title = '屏東棒球路店',
            address = '900屏東縣屏東市棒球路228號',
            latitude =22.66023711472268,
            longitude=120.48031176388574
        )
        line_bot_api.reply_message(event.reply_token, location_message)
    elif re.match('屏大民生店',message):
        location_message = LocationSendMessage( 
            title = '屏大民生店',
            address = '900屏東縣屏東市民生路39號',
            latitude =22.666256566162176,
            longitude=120.50726259839823
        )
        line_bot_api.reply_message(event.reply_token, location_message)
    elif re.match('屏東林森店',message):
        location_message = LocationSendMessage( 
            title = '屏東林森店',
            address = '900屏東縣屏東市林森路109號',
            latitude =22.676552384010964,
            longitude=120.4918130754293
        )
        line_bot_api.reply_message(event.reply_token, location_message)
    elif re.match('澎湖馬公店',message):
        location_message = LocationSendMessage( 
            title = '澎湖馬公店',
            address = '880澎湖縣馬公市海埔路30號',
            latitude =23.57032943932773,
            longitude=119.5694561186501
        )
        line_bot_api.reply_message(event.reply_token, location_message)
    elif re.match('澎湖中正店',message):
        location_message = LocationSendMessage( 
            title = '澎湖中正店',
            address = '880澎湖縣馬公市中正路28號',
            latitude =23.56844134992375,
            longitude=119.56550790722468
        )
        line_bot_api.reply_message(event.reply_token, location_message)
    elif re.match('澎湖光復店',message):
        location_message = LocationSendMessage( 
            title = '澎湖光復店',
            address = '880澎湖縣馬公市光復路125-2號',
            latitude =23.57536421169638,
            longitude=119.57117273231329
        )
        line_bot_api.reply_message(event.reply_token, location_message)
#東部---------------------------------
#50
    elif re.match('台東中華店',message):
        location_message = LocationSendMessage( 
            title = '台東中華店',
            address = '950台東縣台東市中華路一段625號',
            latitude =22.75000435736271,
            longitude=121.14858745834839
        )
        line_bot_api.reply_message(event.reply_token, location_message)
    elif re.match('台東東商店',message):
        location_message = LocationSendMessage( 
            title = '台東東商店',
            address = '950台東縣台東市正氣路467號',
            latitude =22.75766220905468,
            longitude=121.14470361993536
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
    
    