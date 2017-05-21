import os
from wordcloud import WordCloud
import matplotlib.pyplot as plt

d = os.path.dirname(__file__)
font=os.path.join(os.path.dirname(__file__), "DroidSansFallbackFull.ttf") #设置字体格式，否则显示不了中文
txt = open(u"E:/一带一路.txt").read()
wordcloud = WordCloud(font_path=font).generate(txt)
plt.figure()
plt.imshow(wordcloud)
plt.axis("off")
plt.show()
