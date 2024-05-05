import matplotlib.pyplot as plt

from haplot.base import Gene


def genetic_structure(structure_read, structure_write):
    # 创建图形和轴对象
    fig, ax = plt.subplots()

    # 添加文件读取和数据处理部分
    with open(structure_read, 'r') as file:
        num = 0.2
        y = 0
        for line in file:
            # 去除换行符并按逗号分割每行数据
            gene_data = line.strip().split(' ')
            # 提取基因信息
            gene_name = gene_data[0]
            chromosome = gene_data[1]
            start = int(gene_data[2])
            end = int(gene_data[3])
            strand = gene_data[4]
            exons = eval(gene_data[5])  # 使用eval函数将字符串转换为列表

            # 创建Gene对象并设置属性
            gene = Gene(gene_name, chromosome, start, end, strand, exons)

            # 设置其他属性和绘制基因
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
    write = "C:\\Users\\10484\\Desktop\\python_graduate\\data\\10_gene_struction.txt"
    save = "C:\\Users\\10484\\Desktop\\python_graduate\\result\\1.png"
    genetic_structure(write, save)
