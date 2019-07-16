# -*- encoding: utf-8 -*-
from wordcloud import WordCloud
import os
import jieba


cur_path = os.path.dirname(__file__)
txt = '胸大了 体重高了'

# content = " ".join(jieba.cut(txt))
# print(content)

wordcloud = WordCloud(background_color = 'white',
font_path='/home/dragon/Downloads/stxingka.ttf',
width=600,height=600,
max_font_size=200,min_font_size=20).generate(txt)
image = wordcloud.to_image(
                           )
image.show()