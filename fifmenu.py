from linebot import (LineBotApi, WebhookHandler)
from linebot.exceptions import (InvalidSignatureError)
from linebot.models import *

def fif():
    message = FlexSendMessage(
        alt_text='50嵐菜單',
        contents=
        {
            "type": "carousel",
            "contents": [  
                {
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
                                    "text": "50嵐飲料店"
                                }
                            }
                        ]
                    }
                },
                {
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
                                    "text": "50嵐飲料店"
                                }
                            }
                        ]
                    }
                },
                {
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
                                    "text": "50嵐飲料店"
                                }
                            }
                        ]
                    }
                },
                {
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
                                    "text": "50嵐飲料店"
                                }
                            }
                        ]
                    }
                },
                {
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
                                    "text": "50嵐飲料店"
                                }
                            }
                        ]
                    }
                }

            ]
        }    
    )
    return message