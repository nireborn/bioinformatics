# This is scatterplot.py
# DATE:2024-01-29
# NAME:KWD
# MAIL:nireborn@163.com
# GOOD LUCK!
"""
对数据进行按组分类，输入格式为txt文件，第一行为说明，第一、二列为数据，第三列为分组数据
"""

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns


def scatter_plot(scatter_read, scatter_write):
    # 读取文本文件的第一行
    with open(scatter_read, 'r') as file:
        # 读取第一行，并去除换行符
        first_line = file.readline().strip()

    # 根据第一行的值创建列名
    column_names = first_line.split('\t')

    # 读取文本文件，指定制表符分隔
    data = pd.read_csv(scatter_read, sep='\t', names=column_names, skiprows=1)

    # 设置样式
    sns.set(style="whitegrid")

    # 创建散点图，以第三列 'Species' 为分组标准
    sns.scatterplot(x=data.columns[0], y=data.columns[1], hue=data.columns[2], data=data, palette='Set2', s=100)

    # 添加标题和标签
    # plt.title('Scatter Plot Grouped by Species')
    plt.xlabel(data.columns[0])
    plt.ylabel(data.columns[1])

    # # 获取当前时间的字符串表示（包含秒）
    # current_time_str = datetime.now().strftime("%Y%m%d%H%M%S")
    #
    # URL = scatter_write + "/" + current_time_str + ".png"

    plt.savefig(scatter_write, bbox_inches='tight')

    # 显示图形
    # plt.show()


if __name__ == '__main__':
    read = ".\\scatterplot.txt"
    write = ".\\"
    scatter_plot(read, write)
