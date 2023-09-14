from linebot import (LineBotApi, WebhookHandler)
from linebot.exceptions import (InvalidSignatureError)
from linebot.models import *

def rec():
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
                        "text": "返回選項",
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
                            "label": "手搖飲料選項",
                            "text": "想喝手搖杯"
                        },
                        "color": "#F0F0F0"
                    },
                    {
                        "type": "button",
                        "style": "secondary",
                        "height": "sm",
                        "action": {
                            "type": "message",
                            "label": "CoCo菜單",
                            "text": "CoCo菜單"
                        },
                        "color": "#F0F0F0"
                    },
                    {
                        "type": "button",
                        "style": "secondary",
                        "height": "sm",
                        "action": {
                            "type": "message",
                            "label": "50嵐菜單",
                            "text": "50嵐菜單"
                        },
                        "color": "#F0F0F0"
                    },
                    {
                        "type": "button",
                        "style": "secondary",
                        "height": "sm",
                        "action": {
                            "type": "message",
                            "label": "CoCo地區",
                            "text": "CoCo飲料店"
                        },
                        "color": "#F0F0F0"
                    },
                    {
                        "type": "button",
                        "style": "secondary",
                        "height": "sm",
                        "action": {
                            "type": "message",
                            "label": "50嵐地區",
                            "text": "50嵐飲料店"
                        },
                        "color": "#F0F0F0"
                    },
                    {
                        "type": "button",
                        "style": "secondary",
                        "height": "sm",
                        "action": {
                            "type": "message",
                            "text": "北部CoCo飲料店",
                            "label": "北部CoCo縣市"
                        },
                        "color": "#F0F0F0"
                    },
                    {
                        "type": "button",
                        "style": "secondary",
                        "height": "sm",
                        "action": {
                            "type": "message",
                            "label": "西部CoCo縣市",
                            "text": "西部CoCo飲料店"
                        },
                        "color": "#F0F0F0"
                    },
                    {
                        "type": "button",
                        "style": "secondary",
                        "height": "sm",
                        "action": {
                            "type": "message",
                            "label": "南部CoCo縣市",
                            "text": "南部CoCo飲料店"
                        },
                        "color": "#F0F0F0"
                    },
                    {
                        "type": "button",
                        "style": "secondary",
                        "height": "sm",
                        "action": {
                            "type": "message",
                            "label": "東部CoCo縣市",
                            "text": "東部CoCo飲料店"
                        },
                        "color": "#F0F0F0"
                    },
                    {
                        "type": "button",
                        "style": "secondary",
                        "height": "sm",
                        "action": {
                            "type": "message",
                            "label": "北部50嵐縣市",
                            "text": "北部50嵐飲料店"
                        },
                        "color": "#F0F0F0"
                    },
                    {
                        "type": "button",
                        "style": "secondary",
                        "height": "sm",
                        "action": {
                            "type": "message",
                            "label": "西部50嵐縣市",
                            "text": "西部50嵐飲料店"
                        },
                        "color": "#F0F0F0"
                    },
                    {
                        "type": "button",
                        "style": "secondary",
                        "height": "sm",
                        "action": {
                            "type": "message",
                            "label": "南部50嵐縣市",
                            "text": "南部50嵐飲料店"
                        },
                        "color": "#F0F0F0"
                    },
                    {
                        "type": "button",
                        "style": "secondary",
                        "height": "sm",
                        "action": {
                            "type": "message",
                            "label": "東部50嵐縣市",
                            "text": "東部50嵐飲料店"
                        },
                        "color": "#F0F0F0"
                    },
                    {
                        "type": "button",
                        "style": "secondary",
                        "height": "sm",
                        "action": {
                            "type": "message",
                            "label": "主要選單",
                            "text": "呼叫機器人"
                        },
                        "color": "#F0F0F0"
                    }
                ],
                "flex": 0
            }
        }
    )
    return message