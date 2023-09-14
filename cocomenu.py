from linebot import (LineBotApi, WebhookHandler)
from linebot.exceptions import (InvalidSignatureError)
from linebot.models import *

def Co():
    message = FlexSendMessage(
        alt_text='Coco菜單',
        contents={
            "type": "carousel",
            "contents": [
                {
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
                                "text": "經典好茶道"
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
                },
                {
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
                },
                {
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
                },
                {
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
                },
                {
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
                },
                {
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
                },
                {
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
            ]
        }
    )
    return message