# This is genetic_tree_function.py
# DATE:2024-02-25
# NAME:KWD
# MAIL:nireborn@163.com
# GOOD LUCK!

from io import StringIO

import matplotlib.pyplot as plt
import pandas as pd
from Bio import Phylo

from haplot.chart import TreeWithGenePlot


def genetic_tree(tree_read, tree_write):
    # 读取基因信息
    genes_data = []
    with open(tree_read, 'r') as file:
        for line in file:
            if not line.startswith("#"):
                gene_data = line.strip().split(' ')
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
    with open(tree_read, "r") as file:
        for line in file:
            if start_reading:
                tree_data = line.strip()  # 读取注释行下一行的内容
                break
            elif line.startswith("#GENE TREE"):
                start_reading = True

    # 基因树信息
    handel = StringIO(tree_data)
    tree = Phylo.read(handel, "newick")
    tree = tree.as_phyloxml()
    tree.root.color = "gray"

    # 动态确定颜色分组
    upper_genes = []
    lower_genes = []
    for gene_info in genes_data:
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

    for clade in tree.find_clades():
        if clade.name in upper_genes:
            clade.color = "salmon"
        elif clade.name in lower_genes:
            clade.color = "green"

    fig = plt.figure(figsize=(8, 5))
    TreeWithGenePlot(tree, genes_df)

    plt.savefig(tree_write, bbox_inches='tight')


if __name__ == '__main__':
    write = "C:\\Users\\10484\\Desktop\\python_graduate\\data\\11_gene_tree.txt"
    save = "C:\\Users\\10484\\Desktop\\python_graduate\\result\\11.png"
    genetic_tree(write, save)
