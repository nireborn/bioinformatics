# This is bar.py
# DATE:2024-01-29
# NAME:KWD
# MAIL:nireborn@163.com
# GOOD LUCK!
"""
输入txt文件，以第一行为参数说明，第一列为纵轴，第二列为横轴，按照第三列分类，画柱状图。
"""
import matplotlib
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

# 设置matplotlib后端
matplotlib.use('Agg')  # 使用 Agg 后端（matplotlib默认后端）来生成静态图像文件


# 绘制柱状图函数 【第一列为数据，第二列为x轴分组，第三列为同一x轴刻度对比组】
def bar_plot(bar_read, bar_write):
    # 读取文本文件
    data = pd.read_csv(bar_read, sep='\t')

    # 设置图片大小
    plt.figure(figsize=(15, 9), dpi=300)  # 宽度15英寸，高度9英寸，每英寸像素数300

    # 设置柱状图样式
    sns.set(style="whitegrid")

    # 创建柱状图
    barplot = sns.barplot(x=data.columns[1],
                          y=data.columns[0],
                          hue=data.columns[2],
                          data=data,
                          palette='Set2'
                          )

    # 在每个柱形上方显示具体数值
    for p in barplot.patches:
        barplot.annotate(f'{p.get_height():.2f}', (p.get_x() + p.get_width() / 2., p.get_height()),
                         ha='center',
                         va='center',
                         xytext=(0, 10),
                         textcoords='offset points'
                         )

    # 移动图例到右上角
    plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')

    # 添加标签
    plt.xlabel(data.columns[1])  # 横轴列名
    plt.ylabel(data.columns[0])  # 纵轴列名

    plt.savefig(bar_write, bbox_inches='tight')


if __name__ == '__main__':
    from datetime import datetime

    read = "../data/6_bar.txt"

    current_time_str = datetime.now().strftime("%Y_%m_%d_%H%M%S")  # 获取当前时间的字符串表示（包含秒）（年_月_日_时分秒）

    write = "../result/" + current_time_str + ".png"

    bar_plot(read, write)
