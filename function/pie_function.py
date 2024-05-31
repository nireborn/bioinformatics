# This is pie.py
# DATE:2024-01-30
# NAME:KWD
# MAIL:nireborn@163.com
# GOOD LUCK!
import matplotlib
import matplotlib.pyplot as plt
import pandas as pd

# 设置matplotlib后端
matplotlib.use('Agg')  # 使用 Agg 后端（matplotlib默认后端）来生成静态图像文件


# 绘制饼状图函数 【第一列为值，第二列为组】
def pie_plot(pie_read, pie_write):
    # 读取txt文件，以第一行为参数说明，第一列为数据，第二列为分组
    data = pd.read_csv(pie_read, sep='\t')

    # 设置图片大小
    plt.figure(figsize=(15, 9), dpi=300)  # 宽度15英寸，高度9英寸，每英寸像素数300

    # 绘制饼图，显示百分比，并返回每个扇形的相关信息
    wedges, texts, autotexts = plt.pie(data.iloc[:, 0],  # 提取第一列数据，作为饼图中每个扇形的数值
                                       labels=data.iloc[:, 1],  # 提取第二列数据，作为饼图中每个扇形的标签
                                       autopct='%1.1f%%',  # 自动显示每个扇形所占的百分比，格式为小数点后一位的百分数
                                       startangle=90,  # 从90度开始绘制饼图，使第一个扇形从上方开始。
                                       wedgeprops=dict(edgecolor='white', linewidth=1)  # 每个分片边框为白色，线粗为1
                                       )
    '''
    wedges：饼图的分片
    texts：与 labels 相对应的标签文本
    autotexts：相应的百分比文本
    '''

    # 添加组名和百分比标签
    for text, autotext, label in zip(texts, autotexts, data.iloc[:, 1]):
        # 文本设置
        text.set(size=12,  # 字体12
                 weight='bold'  # 加粗
                 )
        # 百分比设置
        autotext.set(size=12,  # 字体12
                     color='white',  # 白色
                     weight='bold')  # 加粗
        # 百分比文本设置
        autotext.set_text(f"{autotext.get_text()}")  # 仅保留百分比
    '''
    zip：将多个可迭代对象（如列表、元组等）打包成一个元组的迭代器
    e.g.：
        list1 = [1, 2, 3]
        list2 = ['a', 'b', 'c']
        → [(1, 'a'), (2, 'b'), (3, 'c')]
    '''

    # 添加图例
    plt.legend(wedges,
               data.iloc[:, 1],  # 提取第二列数据，作为图例中的标签
               title='Groups',  # 标题为“Groups”
               loc='center left',  # 将图例放置在图的左侧中心位置
               bbox_to_anchor=(1, 0, 0.5, 1)  # 图例坐标，使其在图的外部左侧
               )

    plt.savefig(pie_write, bbox_inches='tight')


if __name__ == '__main__':
    from datetime import datetime

    read = "../data/7_pie.txt"

    current_time_str = datetime.now().strftime("%Y_%m_%d_%H%M%S")  # 获取当前时间的字符串表示（包含秒）（年_月_日_时分秒）

    write = "../result/" + current_time_str + ".png"

    pie_plot(read, write)
