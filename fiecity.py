from linebot import (LineBotApi, WebhookHandler)
from linebot.exceptions import (InvalidSignatureError)
from linebot.models import *

def fec():
    message = FlexSendMessage(
        alt_text='縣市選單',
        contents={
            "type": "bubble",
            "body": {
                "type": "box",
                "layout": "vertical",
                "contents": [
                    {
                        "type": "text",
                        "text": "哪一個縣市?",
                        "weight": "bold",
                        "size": "xl",
                        "align": "center"
                    }
                ]
            },
            "footer": {
                "type": "box",
                "layout": "vertical",
                "spacing": "sm",
                "contents": [
                    {
                        "type": "button",
                        "style": "secondary",
                        "height": "sm",
                        "action": {
                            "type": "postback",
                            "label": "花蓮縣",
                            "data": "hello",
                            "displayText": "抱歉沒有相關資訊"
                        },
                        "color": "#F0F0F0"
                    },
                    {
                        "type": "button",
                        "style": "secondary",
                        "height": "sm",
                        "action": {
                            "type": "message",
                            "label": "臺東縣",
                            "text": "臺東縣50嵐飲料店"
                        },
                        "color": "#F0F0F0"
                    },
                    {
                        "type": "button",
                        "style": "secondary",
                        "height": "sm",
                        "action": {
                            "type": "message",
                            "label": "返回選項",
                            "text": "返回選項"
                        },
                        "color": "#F0F0F0"
                    }
                ],
                "flex": 0
            }
        }
    )
    return message