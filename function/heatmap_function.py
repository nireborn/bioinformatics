# This is Heatmap.py
# DATE:2024-01-29
# NAME:KWD
# MAIL:nireborn@163.com
# GOOD LUCK!
"""
转录组经RPKM/FPKM标准化的基因表达数据，对样本相关性进行Pearson算法分析，最终以Heatmap热图可视化。
"""

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns


def heatmap_plot(map_read, map_write):
    """
    :param map_read:输入txt文件，txt文件要求：第一行分组，第一列Gene。
    :param map_write: 文件夹路径
    :return:
    """
    # 1. 读取数据
    data = pd.read_csv(map_read, sep='\t', index_col=0)

    # 2. 去除第一行和第一列的标签
    data_no_labels = data.iloc[1:, :]

    # 3. 计算Pearson相关系数
    correlation_matrix = data_no_labels.T.corr(method='pearson')

    # 4. 生成热图
    sns.set(style="whitegrid")  # 背景设置为白色网格（white grid）样式
    plt.figure(figsize=(10, 8))  # 宽度 10 英寸、高度 8 英寸

    sns.heatmap(
        correlation_matrix,  # 相关系数矩阵
        cmap="coolwarm",  # 颜色映射
        annot=True,  # 在每个热图方块上显示数值
        fmt=".2f",  # 设置显示数值的格式，保留两位小数
        linewidths=.5,  # 设置方块之间的边框宽度为 0.5
        cbar_kws={"shrink": .5},  # 设置颜色条（color bar）的大小缩小为原来的一半
        xticklabels=data_no_labels.columns,  # 设置横纵坐标轴标签
        yticklabels=data_no_labels.columns  # 设置横纵坐标轴标签
    )

    plt.savefig(map_write, bbox_inches='tight')


if __name__ == '__main__':
    read = ".\\RNAseq.txt"
    write = ".\\"
    heatmap_plot(read, write)
