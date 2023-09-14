from linebot import (LineBotApi, WebhookHandler)
from linebot.exceptions import (InvalidSignatureError)
from linebot.models import *

def fwc():
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
                            "type": "message",
                            "label": "臺中市",
                            "text": "臺中市50嵐飲料店"
                        },
                        "color": "#F0F0F0"
                    },
                    {
                        "type": "button",
                        "style": "secondary",
                        "height": "sm",
                        "action": {
                            "type": "message",
                            "label": "苗栗縣",
                            "text": "苗栗縣50嵐飲料店"
                        },
                        "color": "#F0F0F0"
                    },
                    {
                        "type": "button",
                        "style": "secondary",
                        "height": "sm",
                        "action": {
                            "type": "message",
                            "label": "彰化縣",
                            "text": "彰化縣50嵐飲料店"
                        },
                        "color": "#F0F0F0"
                    },
                    {
                        "type": "button",
                        "style": "secondary",
                        "height": "sm",
                        "action": {
                            "type": "message",
                            "label": "南投縣",
                            "text": "南投縣50嵐飲料店"
                        },
                        "color": "#F0F0F0"
                    },
                    {
                        "type": "button",
                        "style": "secondary",
                        "height": "sm",
                        "action": {
                            "type": "message",
                            "label": "雲林縣",
                            "text": "雲林縣50嵐飲料店"
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