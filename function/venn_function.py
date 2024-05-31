# This is venn.py
# DATE:2024-01-29
# NAME:KWD
# MAIL:nireborn@163.com
# GOOD LUCK!
import time

import matplotlib
import matplotlib.pyplot as plt
import pandas as pd

from pyvenn import venn

# 设置matplotlib后端
matplotlib.use('Agg')  # 使用 Agg 后端（matplotlib默认后端）来生成静态图像文件


# Venn图函数 【利用pyvenn绘制】
def venn_plot(venn_read, venn_write):
    data = pd.read_csv(venn_read, sep='\t')

    # 将每一列的基因名字转换为集合
    sets = [set(data[col].dropna()) for col in data.columns]

    # 获取集合数量
    num_sets = len(sets)

    # 获取第一行数据
    first_row = pd.read_csv(venn_read, header=None).iloc[0].tolist()[0].split('\t')

    labels = venn.get_labels(sets, fill=['number'])

    # 设置图片大小
    plt.figure(figsize=(15, 9), dpi=300)  # 宽度15英寸，高度9英寸，每英寸像素数300

    # 根据集合数量选择绘制 Venn 图的函数
    if num_sets == 2:
        fig, ax = venn.venn2(labels, names=first_row, fontsize=20, dpi=300)
    elif num_sets == 3:
        fig, ax = venn.venn3(labels, names=first_row, fontsize=18, dpi=300)
    elif num_sets == 4:
        fig, ax = venn.venn4(labels, names=first_row, fontsize=16, dpi=300)
    elif num_sets == 5:
        fig, ax = venn.venn5(labels, names=first_row, fontsize=14, dpi=300)
    elif num_sets == 6:
        fig, ax = venn.venn6(labels, names=first_row, fontsize=12, dpi=300)
    else:
        return

    fig.savefig(venn_write, bbox_inches='tight')
    plt.clf()

if __name__ == '__main__':
    from datetime import datetime

    # read = "../data/9_venn3.txt"
    read = "../data/9_venn6.txt"

    current_time_str = datetime.now().strftime("%Y_%m_%d_%H%M%S")  # 获取当前时间的字符串表示（包含秒）（年_月_日_时分秒）

    write = "../result/" + current_time_str + ".png"

    venn_plot(read, write)

    read = "../data/9_venn3.txt"
    print("1")
    time.sleep(5)
    print("2")
    venn_plot(read, write)

