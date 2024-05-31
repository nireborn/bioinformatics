# This is genetic_tree_function.py
# DATE:2024-02-25
# NAME:KWD
# MAIL:nireborn@163.com
# GOOD LUCK!

from io import StringIO

import matplotlib
import matplotlib.pyplot as plt
import pandas as pd
from Bio import Phylo

from haplot.chart import TreeWithGenePlot

# 设置matplotlib后端
matplotlib.use('Agg')  # 使用 Agg 后端（matplotlib默认后端）来生成静态图像文件


def genetic_tree(tree_read, tree_write):
    # 读取基因信息
    genes_data = []
    with open(tree_read, 'r') as fr:
        for line in fr:
            # 从头开始读取文件，读到“#”行就退出读取
            if not line.startswith("#"):
                gene_data = line.strip().split(' ')  # 空格分隔
                gene_info = {
                    "id": gene_data[0],
                    "chrom": gene_data[1],
                    "start": int(gene_data[2]),
                    "end": int(gene_data[3]),
                    "strand": gene_data[4],
                    "exons": gene_data[5].strip('"')
                }
                genes_data.append(gene_info)
            else:
                break
    # 将基因信息存储为DataFrame
    genes_df = pd.DataFrame(genes_data)

    # 读取基因树信息
    tree_data = ""
    start_reading = False
    with open(tree_read, "r") as fr:
        for line in fr:
            if start_reading:
                tree_data = line.strip()  # 读取注释行下一行的内容
                break
            elif line.startswith("#GENE TREE"):
                start_reading = True

    # 动态确定颜色分组：
    # 初始化两个列表，用于存储不同分组的基因
    upper_genes = []
    lower_genes = []
    # 遍历所有基因信息
    for gene_info in genes_data:
        # 获取当前基因的外显子信息，“，”分割
        exons = gene_info["exons"].split(",")
        middle_exon = exons[len(exons) // 2]
        if "-" in middle_exon:
            middle_position = middle_exon.split("-")[0]
        else:
            middle_position = middle_exon
        if int(middle_position) < 50:
            upper_genes.append(gene_info["id"])
        else:
            lower_genes.append(gene_info["id"])

    # 树信息：
    """
    存储的基因树数据示例如下：
    (((gene1,gene2),(gene3,gene4)),(gene5,gene6,gene7));
    """
    handel = StringIO(tree_data)  # 导入并读取数据
    tree = Phylo.read(handel, "newick")  # 树数据的格式为“Newick”
    tree = tree.as_phyloxml()  # 将树的格式转换为PhyloXML格式
    tree.root.color = "gray"  # 根节点的颜色为灰色

    # 遍历树的所有分支
    for clade in tree.find_clades():
        # 树分支上半，颜色为红色
        if clade.name in upper_genes:
            clade.color = "red"
        # 树分支下半，颜色为蓝色
        elif clade.name in lower_genes:
            clade.color = "blue"

    plt.figure(figsize=(15, 9), dpi=300)

    TreeWithGenePlot(tree, genes_df)

    plt.savefig(tree_write, bbox_inches='tight')


if __name__ == '__main__':
    from datetime import datetime

    read = "../data/11_gene_tree.txt"

    current_time_str = datetime.now().strftime("%Y_%m_%d_%H%M%S")  # 获取当前时间的字符串表示（包含秒）（年_月_日_时分秒）

    write = "../result/" + current_time_str + ".png"

    genetic_tree(read, write)
