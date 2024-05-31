# This is Heatmap.py
# DATE:2024-01-29
# NAME:KWD
# MAIL:nireborn@163.com
# GOOD LUCK!
"""
转录组经RPKM/FPKM标准化的基因表达数据，对样本相关性进行Pearson算法分析，最终以Heatmap热图可视化。
数据示例：
Gene	TCGA-OR-A5LC-01	TCGA-OR-A5JJ-01	TCGA-OR-A5K3-01	TCGA-OR-A5KT-01	TCGA-OR-A5LN-01	TCGA-OR-A5JA-01	TCGA-P6-A5OF-01	TCGA-OR-A5KW-01	TCGA-OR-A5JI-01	TCGA-OR-A5L3-01
GeneA	3.629	2.765	1.947	3.69	1.801	3.113	3.281	2.288	1.629	1.773
GeneB	0.8954	0.2751	0.389	0.4785	3.546	0.4082	0.1542	0.2301	0.5855	0.085
GeneC	0	0	0.1497	0	2.42	0	0.0876	0	0	0
GeneD	0.2366	0	0.2373	0	2.011	0.1696	0.3864	0	0.3052	0.0811
GeneE	0.5069	0	0	0.187	2.067	0	0.0847	0	0.097	0
GeneF	0.3222	0	0.2024	0.1783	1.492	0	0	0	0.2208	0
GeneG	0.1042	0	0.1045	0.1355	1.382	0.1438	0	0.0697	0.0697	0
GeneH	0.1958	0.1253	0.1015	0.1316	1.324	0	0	0.0676	0	0
GeneI	0.1094	0.1353	0	0	1.261	0	0.0638	0	0.2094	0
GeneJ	0	0.0586	0.093	0	1.056	0	0.054	0	0	0
{说明：}
原数据需要进行RPKM/FPKM标准化。
第一行为标题
第二行【GeneA】表示基因A，【3.629】表示基因A经RPKM/FPKM标准化后，在样本TCGA-OR-A5LC-01中的数据
数据之间需要使用Tab分隔
【TCGA-OR-A5LC-01】：TCGA数据库样本（simple）
"""
import matplotlib
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

# 设置matplotlib后端
matplotlib.use('Agg')  # 使用 Agg 后端（matplotlib默认后端）来生成静态图像文件


# 热力图函数  【绘制热力图】
def heatmap_plot(map_read, map_write):
    """
    :param map_read:输入txt文件，txt文件要求：第一行分组，第一列Gene。
    :param map_write:文件夹路径，在传参时需要加上PNG图片的名字。
    :return:None
    """
    # 获取数据
    data = pd.read_csv(map_read, sep='\t', index_col=0)  # 读取数据，Tab分隔，第一列用作[行索引]
    # 进行Pearson计算
    correlation_matrix = data.T.corr(method='pearson')  # 计算Pearson相关系数

    # 生成热图：
    # 【1】设置图片大小
    plt.figure(figsize=(48, 40), dpi=300)  # 宽度48英寸，高度40英寸，每英寸像素数300
    # 【2】设置热力图背景样式
    sns.set(style="whitegrid")  # 背景设置为“白色”样式
    # 【3】绘制热力图
    heatmap = sns.heatmap(
        correlation_matrix,  # 相关系数矩阵z
        cmap="bwr",  # 颜色映射，蓝(-1)→白(0)→红(1)
        annot=True,  # 在每个热图方块上显示数值
        fmt=".2f",  # 设置显示数值的格式，保留两位小数
        annot_kws={"size": 40, "color": 'white'},  # 设置数值字体大小40，颜色白色
        linewidths=.5,  # 设置方块之间的边框宽度为 0.5
        cbar_kws={"shrink": 0.5},  # 设置颜色条（color bar）的大小缩小为原来的一半
        vmin="-1",  # 设置颜色条的最小值
        vmax="1",  # 设置颜色条的最大值
        xticklabels=data.index,  # 设置x轴刻度标签为Gene名（行索引）
        yticklabels=data.index  # 设置y轴刻度标签
    )
    # 【4】设置颜色条刻度字体的大小，并在颜色条上添加文字
    cbar = heatmap.collections[0].colorbar  # 获取颜色条对象
    cbar.ax.tick_params(labelsize=45)  # 设置字体大小30
    cbar.ax.text(0.5,  # 在 x 方向上居中
                 1.02,  # 在 y 方向上略高于颜色条的顶部位置
                 'Corr',  # 文本
                 ha='center',  # 文本水平居中对齐
                 va='bottom',  # 文本垂直底部对齐，使其位于颜色条的正上方
                 fontsize=45,  # 字体大小
                 transform=cbar.ax.transAxes  # 使用颜色条对象的坐标变换，确保文本的位置正确相对于颜色条的位置。
                 )
    # 【5】设置每一列正方形的标签的字体大小,即x轴刻度标签“xticklabels”值
    plt.xticks(fontsize=50, rotation=45, ha='right')  # 字体大小50，将标签旋转45度，并水平对齐到右侧
    plt.yticks(fontsize=50, rotation=0)  # 将纵轴标签设置为横向显示
    plt.tick_params(axis='both', pad=90)  # 距离x,y轴线90点

    # 【6】删除轴标题
    plt.xlabel('')
    plt.ylabel('')

    # 保存图片到本地，侧边不留白
    plt.savefig(map_write, bbox_inches='tight')


if __name__ == '__main__':
    from datetime import datetime

    read = "../data/8_heatmap.txt"

    current_time_str = datetime.now().strftime("%Y_%m_%d_%H%M%S")  # 获取当前时间的字符串表示（包含秒）（年_月_日_时分秒）

    write = "../result/" + current_time_str + ".png"

    heatmap_plot(read, write)
