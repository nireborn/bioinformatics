# This is test2.py
# DATE:2024-02-25
# NAME:KWD
# MAIL:nireborn@163.com
# GOOD LUCK!
"""
该py文件仅为公众号提供实例文件，未用来进行函数功能的使用，仅做理解和参考。
"""

from io import StringIO

import matplotlib.pyplot as plt
import pandas as pd
from Bio import Phylo

from haplot.chart import TreeWithGenePlot

# 创建模拟数据用于绘制基因结构
# gene format: [id, chrom, start, end, strand, exons]
# exons format: "start1-end1,start2-end2,..."
genes = pd.DataFrame({
    "id": ["A", "B", "C", "D", "E", "F", "G"],
    "chrom": ["chr1"] * 7,
    "start": [0, 0, 0, 0, 0, 0, 0],
    "end": [80, 80, 80, 80, 100, 100, 100],
    "strand": ["+"] * 7,
    "exons": ["0-20,40-60", "0-20,40-60", "0-20,40-60", "0-20,40-60",
              "20-40,60-80", "20-40,60-80", "20-40,60-80"]
})
print(genes)
# 使用biopython读取进化树文件
# 1. load tree with newick format
handel = StringIO("(((A,B),(C,D)),(E,F,G));")  # 实际上可以修改为自己的树文件名，此处写法是为了便于演示
tree = Phylo.read(handel, "newick")
# print(tree)

# 2. convert tree to phyloxml format
tree = tree.as_phyloxml()

# 3. color tree
tree.root.color = "gray"

for clade in tree.find_clades():
    if clade.name in ["gene1", "gene2", "gene3", "gene4"]:
        clade.color = "write"
    elif clade.name in ["gene5", "gene6", "gene7"]:
        clade.color = "blue"

# plot tree and genes
fig = plt.figure(figsize=(8, 5))
TreeWithGenePlot(tree, genes)
plt.show()
