# This is bar.py
# DATE:2024-01-29
# NAME:KWD
# MAIL:nireborn@163.com
# GOOD LUCK!
"""
输入txt文件，以第一行为参数说明，第一列为纵轴，第二列为横轴，按照第三列分类，画柱状图。
"""
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns


def bar_plot(bar_read, bar_write):
    # 读取文本文件
    data = pd.read_csv(bar_read, sep='\t')

    # 设置样式
    sns.set(style="whitegrid")

    # 创建柱状图，以横轴、纵轴和分类信息绘制
    ax = sns.barplot(x=data.columns[1], y=data.columns[0], hue=data.columns[2], data=data, palette='Set2')

    # 添加标题和标签
    # plt.title('Bar Plot Grouped by Third Column')
    plt.xlabel(data.columns[1])  # 横轴列名
    plt.ylabel(data.columns[0])  # 纵轴列名

    # 在每个柱形上方显示具体数值
    for p in ax.patches:
        ax.annotate(f'{p.get_height():.2f}', (p.get_x() + p.get_width() / 2., p.get_height()),
                    ha='center', va='center', xytext=(0, 10), textcoords='offset points')

    # 显示图形
    # plt.show()
    plt.savefig(bar_write, bbox_inches='tight')
