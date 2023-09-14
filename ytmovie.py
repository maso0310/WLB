from linebot import (LineBotApi, WebhookHandler)
from linebot.exceptions import (InvalidSignatureError)
from linebot.models import *
def ytm():
    #多樣版組合按鈕
    message = TemplateSendMessage(
        alt_text='影片瀏覽',
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
                ),
                CarouselColumn(
                    thumbnail_image_url='https://yt3.googleusercontent.com/ytc/AOPolaTri_-obIKaqk2CJapBWOrvUYaFr-VY1NTQR7dPJQ=s900-c-k-c0x00ffffff-no-rj',
                    title='Eko Languages',
                    text='學習各國語言',
                    actions=[
                        PostbackAction(
                            label='詳細內容',
                            display_text='如果您想要學習更多的語言，非常推薦你來觀看',
                            data='action=其實不需要謝謝!'
                        ),
                        URIAction(
                            label='觀看請點這',
                            uri='https://www.youtube.com/@EkoLanguages/videos'
                        )
                    ]
                ),
                CarouselColumn(
                    thumbnail_image_url='https://yt3.googleusercontent.com/VnKzy6UKvr4EJppQhjxfAtUWD4vibPBYZEU2jziPFrG_0V8XqZTO9TT6b32Fp0GzOoJYucD4OtA=s900-c-k-c0x00ffffff-no-rj',
                    title='英语兔',
                    text='學習英語',
                    actions=[
                        PostbackAction(
                            label='詳細內容',
                            display_text='想增進自己的英文能力也許這部視頻會對您有所幫助',
                            data='action=其實不需要謝謝!'
                        ),
                        URIAction(
                            label='觀看請點這',
                            uri='https://www.youtube.com/@yingyutu/videos'
                        )
                    ]
                ),
                CarouselColumn(
                    thumbnail_image_url='https://yt3.googleusercontent.com/VnKzy6UKvr4EJppQhjxfAtUWD4vibPBYZEU2jziPFrG_0V8XqZTO9TT6b32Fp0GzOoJYucD4OtA=s900-c-k-c0x00ffffff-no-rj',
                    title=' ',
                    text=' ',
                    actions=[
                        MessageAction(
                            label='返回選項',
                            text='返回選項'
                        )
                    ]
                )
            ]
        )
    )
    return message