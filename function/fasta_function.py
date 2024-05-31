"""
fasta文件处理：
    输入fasta文件
    输出fasta文件
实现功能：
    单碱基替换
    获取互补序列
    获取反向互补序列
    获取长度（输出格式为id + 序列 + 长度）
"""

from Bio import SeqIO
from Bio.Seq import Seq


# 单碱基替换：
def single_base_substitution(fasta_read, fasta_write, raw, process):
    """
    :param fasta_read: 读取fasta文件URL
    :param fasta_write: 输出fasta文件URL
    :param raw:需要替换的碱基
    :param process:替换后的碱基
    :return:None
    """
    fr = open(fasta_read, "r")
    fw = open(fasta_write, "w")

    for line in fr:
        line = line.strip()
        if line and line[0] == ">":  # '>'开头和空行直接写入
            fw.write(line + '\n')
        else:
            tmp = line.replace(raw, process)
            fw.write(tmp + '\n')

    fr.close()
    fw.close()


# 获取互补序列函数
def complement_seq(fasta_read, fasta_write):
    """
    :param fasta_read: 读取fasta文件URL
    :param fasta_write: 输出fasta文件URL
    :return: None
    """

    with open(fasta_read, "r") as fr, open(fasta_write, "w") as fw:
        current_header = ""
        current_genes = []
        current_genes_per_line = None

        for line in fr:
            line = line.strip()
            if line.startswith(">"):
                # 如果当前正在处理的基因序列不为空
                if current_genes:
                    # 合并基因序列并进行互补操作
                    combined_seq = "".join(current_genes)
                    complemented_seq = str(Seq(combined_seq).complement())

                    # 按照第一个基因行的基因数进行分割，并写入文件
                    for i in range(0, len(complemented_seq), current_genes_per_line):
                        fw.write(complemented_seq[i:i + current_genes_per_line] + "\n")
                    fw.write("\n")
                    # 清空当前基因序列
                    current_genes = []

                # 更新当前标题行
                current_header = line
                fw.write(line + "\n")
            else:
                # 如果当前正在处理的基因序列为空，则获取第一个基因行的基因数
                if current_genes_per_line is None:
                    current_genes_per_line = len(line)
                # 将基因加入当前基因序列
                current_genes.append(line)

        # 处理最后一个 ">" 符号下的基因序列
        if current_genes:
            combined_seq = "".join(current_genes)
            complemented_seq = str(Seq(combined_seq).reverse_complement())
            for i in range(0, len(complemented_seq), current_genes_per_line):
                fw.write(complemented_seq[i:i + current_genes_per_line] + "\n")


# 获取反向互补序列
def reverse_complement_seq(fasta_read, fasta_write):
    """
    :param fasta_read: 读取fasta文件URL
    :param fasta_write: 输出fasta文件URL
    :return: None
    """
    with open(fasta_read, "r") as fr, open(fasta_write, "w") as fw:
        current_header = ""
        current_genes = []
        current_genes_per_line = None

        for line in fr:
            line = line.strip()
            if line.startswith(">"):
                # 如果当前正在处理的基因序列不为空
                if current_genes:
                    # 合并基因序列并进行互补操作
                    combined_seq = "".join(current_genes)
                    complemented_seq = str(Seq(combined_seq).reverse_complement())

                    # 按照第一个基因行的基因数进行分割，并写入文件
                    for i in range(0, len(complemented_seq), current_genes_per_line):
                        fw.write(complemented_seq[i:i + current_genes_per_line] + "\n")
                    fw.write("\n")
                    # 清空当前基因序列
                    current_genes = []

                # 更新当前标题行
                current_header = line
                fw.write(line + "\n")
            else:
                # 如果当前正在处理的基因序列为空，则获取第一个基因行的基因数
                if current_genes_per_line is None:
                    current_genes_per_line = len(line)
                # 将基因加入当前基因序列
                current_genes.append(line)

        # 处理最后一个 ">" 符号下的基因序列
        if current_genes:
            combined_seq = "".join(current_genes)
            complemented_seq = str(Seq(combined_seq).reverse_complement())
            for i in range(0, len(complemented_seq), current_genes_per_line):
                fw.write(complemented_seq[i:i + current_genes_per_line] + "\n")


# 获取长度  【输出格式为id + 基因序列长度 + 基因序列】
def get_length(fasta_read, fasta_write):
    """
    :param fasta_read: 输入的fasta文件路径
    :param fasta_write: 输出的fasta文件路径
    :return: None
    """
    with open(fasta_write, "w") as fw:
        for seq_record in SeqIO.parse(fasta_read, "fasta"):
            # 输出fasta记录的标识符
            fw.write(f">{seq_record.id}\n")

            # 统计并输出每个序列的长度
            sequence_length = len(seq_record.seq)
            fw.write(f"Sequence length: {sequence_length}\n")

            # 输出序列本身
            fw.write(f"{seq_record.seq}\n\n")


if __name__ == '__main__':
    read = "../data/02_fasta.fasta"
    write1 = "../result/1.fasta"
    write2 = "../result/2.fasta"
    write3 = "../result/3.fasta"
    write4 = "../result/4.fasta"

    raw = "A"
    process = "T"
    # single_base_substitution(read, write1, raw, process)
    # complement_seq(read, write2)
    # reverse_complement_seq(read, write3)
    get_length(read, write4)
