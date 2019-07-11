from wordcloud import WordCloud
import matplotlib.pyplot as plt
import binascii
def generate_worldcloud(content):
    font_path = './SimSun.ttf'
    wordcloud = WordCloud(
        font_path=font_path,
        background_color="black",  # 设置背景为白色，默认为黑色
        width = 1500,  # 设置图片的宽度
        height= 960,  # 设置图片的高度
        margin= 10  # 设置图片的边缘
    ).generate(content)
    wordcloud.to_file('./worldcloud.png')
    # filename = './worldcloud.png'
    # with open(filename, 'rb') as f:
    #     content = f.read()
    # print(binascii.hexlify(content))
    # return str(binascii.hexlify(content))
    # plt.imshow(wordcloud)  # 绘制图片
    # plt.axis("off")  # 消除坐标轴
    # plt.show()  # 展示图片
# content = '123456 7897 da s87e7 98e   79f8d 78 9 7f97 ad 7s89'
#generate_worldcloud(content)
def generate_world(members):
    world = ''
    for key, value in members.items():
        if 'cd' in value:
            goal = value['cd']
            goal = goal.replace('&nbsp','')
            goal = goal.replace('20','')
            goal = goal.replace('-','')
            goal = goal.replace(';','')
            goal = goal.replace('～','')
            goal = goal.replace('－','')
            goal = goal.replace('+','')
            goal = goal.replace(',', '')
            goal = goal.replace('，', '')
            goal = goal.replace('~', '')
            goal = goal.replace('_', '')
            goal += ' '
            world += goal
    generate_worldcloud(world)
