"""

"""
import matplotlib
import matplotlib.pyplot as plt

from haplot.base import Gene

# 设置matplotlib后端
matplotlib.use('Agg')  # 使用 Agg 后端（matplotlib默认后端）来生成静态图像文件


def genetic_structure(structure_read, structure_write):
    """
    :param structure_read:
    :param structure_write:
    :return:
    """
    # 设置图片大小，创建图形和轴对象
    fig, ax = plt.figure(figsize=(15, 9), dpi=300), plt.gca()# 宽度15英寸，高度9英寸，每英寸像素数300
    """
    fig：表示图形对象，是整个绘图的容器。可以包含多个子图，标题，图例等。
    ax：表示子图对象，它是实际绘图的区域。
    plt.figure(dpi=xxx)：创建一个具有指定DPI的Figure对象。
    plt.gca()：获取当前的Axes对象。
    """

    # 添加文件读取和数据处理部分
    with open(structure_read, 'r') as fr:
        num = 0.2
        y = 0
        for line in fr:
            # 去除换行符并按“ ”分割每行数据
            gene_data = line.strip().split(' ')

            # 提取基因信息
            gene_name = gene_data[0]  # 基因名
            chromosome = gene_data[1]  # 染色体
            start = int(gene_data[2])  # 外显子起始位置
            end = int(gene_data[3])  # 外显子终止位置
            strand = gene_data[4]  # 延伸方向
            exons = eval(gene_data[5])  # 使用eval函数将字符串转换为列表

            # 创建Gene对象并设置属性
            gene = Gene(gene_name, chromosome, start, end, strand, exons)

            # 基因在y轴的位置
            y += num
            gene.set_center(y)

            # 外显子颜色
            color_list = [f'C{i % 10}' for i in range(len(exons))]  # 使用取余运算实现循环使用预定义的颜色
            gene.set_exons_color(color_list)

            # 外显子绘制高度
            gene.set_exons_height(0.06)

            # 从零开始绘制
            gene.set_zero_start()

            # 基因可视化
            gene.plot(ax)

    plt.savefig(structure_write, bbox_inches='tight')


if __name__ == '__main__':
    from datetime import datetime

    read = "../data/10_gene_struction.txt"

    current_time_str = datetime.now().strftime("%Y_%m_%d_%H%M%S")  # 获取当前时间的字符串表示（包含秒）（年_月_日_时分秒）

    write = "../result/" + current_time_str + ".png"

    genetic_structure(read, write)
