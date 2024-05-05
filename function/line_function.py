# This is line.py
# DATE:2024-01-29
# NAME:KWD
# MAIL:nireborn@163.com
# GOOD LUCK!


import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns


def line_plot(line_read, line_write):
    # 读取文本文件的第一行
    with open(line_read, 'r') as file:
        # 读取第一行，并去除换行符
        first_line = file.readline().strip()

    # 根据第一行的值创建列名
    column_names = first_line.split('\t')

    # 读取文本文件，指定制表符分隔
    data = pd.read_csv(line_read, sep='\t', names=column_names, skiprows=1)

    # 设置样式
    sns.set(style="whitegrid")

    # 设置图片大小
    plt.figure(figsize=(20, 12))

    # 创建折线图，以第一列为横轴，第二列为纵轴，按第三列进行分组
    ax = sns.lineplot(x=data.columns[0], y=data.columns[2], hue=data.columns[1], data=data, palette='Set2')

    # 标记每条线的最高点
    for group in data[data.columns[1]].unique():
        max_index = data[data[data.columns[1]] == group][data.columns[2]].idxmax()
        max_value = data.at[max_index, data.columns[2]]
        ax.annotate(f'{max_value:.2f}', (data.at[max_index, data.columns[0]], max_value),
                    ha='left', va='bottom', xytext=(10, 0), textcoords='offset points')

    # 添加标签
    plt.xlabel(data.columns[0])  # 横轴列名
    plt.ylabel(data.columns[2])  # 纵轴列名

    plt.savefig(line_write, bbox_inches='tight')


if __name__ == '__main__':
    read = ".\\line.txt"
    write = ".\\"
    line_plot(read, write)
