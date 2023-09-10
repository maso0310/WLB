from linebot import (LineBotApi, WebhookHandler)
from linebot.exceptions import (InvalidSignatureError)
from linebot.models import *

def oth():
    message = ImagemapSendMessage(
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
    return message