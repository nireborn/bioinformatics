# This is scatterplot.py
# DATE:2024-01-29
# NAME:KWD
# MAIL:nireborn@163.com
# GOOD LUCK!
"""
【多组相关性散点图：】
对数据进行按组分类，输入格式为txt文件，第一行为说明，第一、二列为数据，第三列为分组数据
"""

import matplotlib
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

# 设置matplotlib后端
matplotlib.use('Agg')  # 使用 Agg 后端（matplotlib默认后端）来生成静态图像文件


# 绘制散点图函数 【多组散点图】
def scatter_plot(scatter_read, scatter_write):
    """
    :param scatter_read: 读取存储数据txt文件所在URL
    :param scatter_write: 存放结果txt文件所在URL
    :return: None
    """
    # 读取文本文件的第一行
    with open(scatter_read, 'r') as fr:
        first_line = fr.readline().strip()  # 读取第一行，并去除换行符
    # 创建列名
    column_names = first_line.split('\t')  # 根据第一行的值创建列名

    # 读取文本文件，指定制表符分隔
    data = pd.read_csv(scatter_read,
                       sep='\t',
                       names=column_names,  # 每一列赋予列名
                       skiprows=1  # 跳过第一行
                       )

    # 设置图片大小
    plt.figure(figsize=(12, 10), dpi=300)  # 宽度48英寸，高度40英寸，每英寸像素数300

    # 设置背景样式，白色网格
    sns.set(style="whitegrid")

    # 创建散点图，以第三列 'Species' 为分组标准
    sns.scatterplot(x=data.columns[0],  # x轴是第一列
                    y=data.columns[1],  # y轴是第二列
                    hue=data.columns[2],  # 按照第三列分组着色，hue参数会根据数据自动识别并处理唯一值，为每个唯一值分配颜色
                    data=data,
                    palette='Set2',  # 调色板是Set2调色板
                    s=100,  # 散点大小为100个单位
                    )

    # 移动图例到右上角
    plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')

    # 添加x，y轴标签
    plt.xlabel(data.columns[0])
    plt.ylabel(data.columns[1])

    # 保存图片
    plt.savefig(scatter_write, bbox_inches='tight')


if __name__ == '__main__':
    from datetime import datetime

    read = "../data/04_scatterplot.txt"

    current_time_str = datetime.now().strftime("%Y_%m_%d_%H%M%S")  # 获取当前时间的字符串表示（包含秒）（年_月_日_时分秒）
    write = "../result/" + current_time_str + ".png"

    scatter_plot(read, write)
