#导入词云库
from wordcloud import WordCloud,STOPWORDS,ImageColorGenerator
import matplotlib.pyplot as plt
from scipy.misc import imread
#打开文件，需要字符串文件
data = open(r"C:\Users\LENOVO\Desktop\Sublime\lianYuTianShi.txt",)
df = data.read()
data.close()
#字体库
font = r'C:\Windows\Fonts\simfang.ttf'
#生成词云
wordcloud = WordCloud(collocations=True,font_path=font,background_color='white',width=500,height=300).generate(df)
#显示，建议用cmd更快速
plt.imshow(wordcloud)
plt.axis('off')
plt.show()