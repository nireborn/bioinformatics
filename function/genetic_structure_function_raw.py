# This is genetic_structure_function.py
# DATE:2024-02-25
# NAME:KWD
# MAIL:nireborn@163.com
# GOOD LUCK!
"""
该py文件仅为公众号提供实例文件，未用来进行函数功能的使用，仅做理解和参考。
"""
import matplotlib.pyplot as plt

from haplot.base import Gene

# 创建5个Gene对象，每个对象至少需要提供6个参数来初始化，包括基因名、染色体、起始位置、终止位置、链方向、以及一个包含外显子坐标的列表
fig, ax = plt.subplots()
gene = Gene('gene', 'chr1', 10, 1500, '+',
            [[100, 200], [300, 400], [500, 600], [700, 800], [900, 1200]])
gene2 = Gene('gene2', 'chr1', 10, 1500, '+',
             [[100, 200], [300, 400], [500, 600], [700, 800], [900, 1200]])
gene3 = Gene('gene3', 'chr1', 10, 1500, '-',
             [[100, 200], [300, 400], [500, 600], [700, 800], [900, 1200]])
gene4 = Gene('gene4', 'chr1', 1000, 3500, '+',
             [[1100, 1200], [1300, 1400], [1500, 1600], [1700, 1800], [1900, 2200],
              [2300, 2400], [2500, 2600], [2700, 2800], [2900, 3200], [3300, 3400]])
gene5 = Gene('gene5', 'chr1', 1000, 3500, '+',
             [[1100, 1400], [1500, 1600], [1700, 2200], [2300, 2400], [2500, 2600],
              [2700, 2800], [2900, 3200], [3300, 3400]])

# 基因在y轴的位置
gene.set_center(0.2)
# 外显子颜色
gene.set_exons_color(['C1', 'C2', 'C3', 'C4', 'C5'])
# 外显子绘制高度
gene.set_exons_height(0.06)
# 从零开始绘制
gene.set_zero_start()
# 基因可视化
gene.plot(ax)

gene2.set_center(0.4)
gene2.set_exons_shape(['ellipse', 'ellipse', 'ellipse', 'ellipse', 'ellipse'])
gene2.set_exons_height(0.06)
gene2.set_zero_start()
gene2.plot(ax)

gene3.set_center(0.6)
gene3.set_exons_shape(['fancy_box', 'fancy_box', 'fancy_box', 'fancy_box', 'fancy_box'])
gene3.set_exons_height(0.06)
gene3.set_zero_start()
gene3.plot(ax)

gene4.set_center(0.8)
gene4.set_exons_height(0.06)
gene4.set_zero_start()
gene4.plot(ax)

gene5.set_center(1.0)
gene5.set_exons_height(0.06)
gene5.set_exons_color('C3')
gene5.set_zero_start()
gene5.plot(ax)

gene5.set_center(1.2)
gene5.set_exons_height(0.06)
gene5.set_exons_color('C4')
gene5.set_zero_start()
gene5.plot(ax)

plt.show()
