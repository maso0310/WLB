from linebot import (LineBotApi, WebhookHandler)
from linebot.exceptions import (InvalidSignatureError)
from linebot.models import *
def sts():
    message = TemplateSendMessage(
        alt_text='免費教學影片',
        template=CarouselTemplate(
            columns=[
                CarouselColumn(
                    thumbnail_image_url='https://www.stust.edu.tw/tc/images/about/trans-img.jpg',
                    title='南台最新消息',
                    text=' ',
                    actions=[
                        URIAction(
                            label='馬上查看',
                            uri='https://news.stust.edu.tw/User/RwdNewsList.aspx'
                        )
                    ]
                ),
                CarouselColumn(
                        thumbnail_image_url='https://www.stust.edu.tw/tc/images/about/trans-img.jpg',
                        title='學生輔導問卷',
                        text=' ',
                        actions=[
                            URIAction(
                                label='馬上查看',
                                uri='https://portal.stust.edu.tw/osa/login.aspx'
                            )
                        ]
                    ),
                CarouselColumn(
                    thumbnail_image_url='https://www.stust.edu.tw/tc/images/about/trans-img.jpg',
                    title='學雜費減免',
                    text=' ',
                    actions=[
                        URIAction(
                            label='馬上查看',
                            uri='https://aura.stust.edu.tw/activity/reg_reduce.aspx'
                        )
                    ]
                ),
                CarouselColumn(
                    thumbnail_image_url='https://www.stust.edu.tw/tc/images/about/trans-img.jpg',
                    title='FlipClass數位學習',
                    text=' ',
                    actions=[
                        URIAction(
                            label='馬上查看',
                            uri='https://flipclass.stust.edu.tw/'
                        )
                    ]
                ),
                CarouselColumn(
                    thumbnail_image_url='https://www.stust.edu.tw/tc/images/about/trans-img.jpg',
                    title='課程時序',
                    text=' ',
                    actions=[
                        URIAction(
                            label='馬上查看',
                            uri='https://academic.stust.edu.tw/tc/node/course1'
                        )
                    ]
                ),
                CarouselColumn(
                    thumbnail_image_url='https://www.stust.edu.tw/tc/images/about/trans-img.jpg',
                    title='行事曆',
                    text=' ',
                    actions=[
                        URIAction(
                            label='馬上查看',
                            uri='https://academic.stust.edu.tw/tc/node/calendar'
                        )
                    ]
                ),
                CarouselColumn(
                    thumbnail_image_url='https://www.stust.edu.tw/tc/images/about/trans-img.jpg',
                    title='學費入口網',
                    text=' ',
                    actions=[
                        URIAction(
                            label='馬上查看',
                            uri='https://ebill.chb.com.tw/eBill/cs/student_login'
                        )
                    ]
                ),
                CarouselColumn(
                    thumbnail_image_url='https://www.stust.edu.tw/tc/images/about/trans-img.jpg',
                    title='選課系統',
                    text=' ',
                    actions=[
                        URIAction(
                            label='馬上查看',
                            uri='https://course.stust.edu.tw/CourSel/board.aspx'
                        )
                    ]
                ),
                CarouselColumn(
                    thumbnail_image_url='https://www.stust.edu.tw/tc/images/about/trans-img.jpg',
                    title='社團活動列表',
                    text=' ',
                    actions=[
                        URIAction(
                            label='馬上查看',
                            uri='https://portal.stust.edu.tw/studclub/Pages/stud/acti_studactilist.aspx'
                        )
                    ]
                )
            ]
        )
    )
    return message