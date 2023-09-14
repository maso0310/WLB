from linebot import (LineBotApi, WebhookHandler)
from linebot.exceptions import (InvalidSignatureError)
from linebot.models import *

def fsc():
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
                            "label": "高雄市",
                            "text": "高雄市50嵐飲料店"
                        },
                        "color": "#F0F0F0"
                    },
                    {
                        "type": "button",
                        "style": "secondary",
                        "height": "sm",
                        "action": {
                            "type": "message",
                            "label": "臺南市",
                            "text": "臺南市50嵐飲料店"
                        },
                        "color": "#F0F0F0"
                    },
                    {
                        "type": "button",
                        "style": "secondary",
                        "height": "sm",
                        "action": {
                            "type": "message",
                            "label": "嘉義縣",
                            "text": "嘉義縣50嵐飲料店"
                        },
                        "color": "#F0F0F0"
                    },
                    {
                        "type": "button",
                        "style": "secondary",
                        "height": "sm",
                        "action": {
                            "type": "message",
                            "label": "嘉義市",
                            "text": "嘉義市50嵐飲料店"
                        },
                        "color": "#F0F0F0"
                    },
                    {
                        "type": "button",
                        "style": "secondary",
                        "height": "sm",
                        "action": {
                            "type": "message",
                            "label": "屏東縣",
                            "text": "屏東縣50嵐飲料店"
                        },
                        "color": "#F0F0F0"
                    },
                    {
                        "type": "button",
                        "style": "secondary",
                        "height": "sm",
                        "action": {
                            "type": "message",
                            "label": "澎湖縣",
                            "text": "澎湖縣50嵐飲料店"
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