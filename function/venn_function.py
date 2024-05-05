# This is venn.py
# DATE:2024-01-29
# NAME:KWD
# MAIL:nireborn@163.com
# GOOD LUCK!

import matplotlib.pyplot as plt
import pandas as pd
from pyvenn import venn


def venn_plot(venn_read, venn_write):
    data = pd.read_csv(venn_read, sep='\t')

    # 将每一列的基因名字转换为集合
    sets = [set(data[col].dropna()) for col in data.columns]
    # print(sets)

    # 获取集合数量
    num_sets = len(sets)

    # 获取第一行数据
    first_row = pd.read_csv(venn_read, header=None).iloc[0].tolist()[0].split('\t')
    # ['Set1', 'Set2', 'Set3']

    labels = venn.get_labels(sets, fill=['number'])

    # fig, ax = venn.venn3(labels, names=first_row, fontsize=8, dpi=72)  # 控制组名及中间数字大小
    # fig.show()

    # 根据集合数量选择绘制 Venn 图的函数
    if num_sets == 2:
        fig, ax = venn.venn2(labels, names=first_row, fontsize=24, dpi=72)
    elif num_sets == 3:
        fig, ax = venn.venn3(labels, names=first_row, fontsize=24, dpi=72)
    elif num_sets == 4:
        fig, ax = venn.venn4(labels, names=first_row, fontsize=24, dpi=72)
    elif num_sets == 5:
        fig, ax = venn.venn5(labels, names=first_row, fontsize=24, dpi=72)
    elif num_sets == 6:
        fig, ax = venn.venn6(labels, names=first_row, fontsize=24, dpi=72)
    else:
        # print(f"Sorry, the number of sets ({num_sets}) is not supported for automatic Venn diagram plotting.")
        return
    fig.show()
    # 创建 Venn 图
    # venn_function(sets, set_labels=data.columns)

    # 获取当前时间的字符串表示（包含秒）
    # current_time_str = datetime.now().strftime("%Y_%m_%d_%H%M%S")
    #
    # URL = venn_write + "\\" + current_time_str + ".png"

    fig.savefig(venn_write, bbox_inches='tight')

    # 显示图形
    # plt.show()


if __name__ == '__main__':
    # 读取数据
    read = "..\\data\\venn6.txt"
    write = ".\\venn.png"
    # 绘制 Venn 图
    venn_plot(read, write)
