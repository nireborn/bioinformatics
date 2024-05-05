# This is fasta处理.py
# DATE:2024-01-26
# NAME:KWD
# MAIL:nireborn@163.com
# GOOD LUCK!
"""
fasta文件处理：
    输入fasta文件
    输出fasta文件
实现功能：
    单碱基替换
    获取互补序列
    获取反向互补序列
    输出格式为id + 序列 + 长度
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
    # r权限读文件，如果没有文件则报错 -- 后续加一个报错提示
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


# 获取互补序列
def complement_seq(fasta_read, fasta_write):
    """
    :param fasta_read: 读取fasta文件URL
    :param fasta_write: 输出fasta文件URL
    :return: None
    """
    fr = open(fasta_read, "r")
    fw = open(fasta_write, "w")

    for line in fr:
        line = line.strip()
        # 序列行进行操作
        # >开头的文件不进行操作，直接写入
        if line and line[0] == ">":
            fw.write(line + '\n')
        else:
            # 转换为Seq对象
            tmp = Seq(line)
            # 对Seq进行互补操作
            tmp = tmp.complement()
            # 写入文件
            fw.write(str(tmp) + '\n')

    fr.close()
    fw.close()


# 获取反向互补序列
def reverse_complement_seq(fasta_read, fasta_write):
    """
    :param fasta_read: 读取fasta文件URL
    :param fasta_write: 输出fasta文件URL
    :return: None
    """
    fr = open(fasta_read, "r")
    fw = open(fasta_write, "w")

    for line in fr:
        line = line.strip()
        # 序列行进行操作
        # ">"开头的文件不进行操作，直接写入
        if line and line[0] == ">":
            fw.write(line + '\n')
        else:
            # 转换为Seq对象
            tmp = Seq(line)
            # 对Seq进行反向互补操作
            tmp = tmp.reverse_complement()
            # 写入文件
            fw.write(str(tmp) + '\n')

    fr.close()
    fw.close()


# 获取长度
# 输出格式为id + 序列 + 长度
def get_length(fasta_read, fasta_write):
    """
    :param fasta_read: 读取fasta文件URL
    :param fasta_write: 输出fasta文件URL
    :return: None
    """
    for seq_record in SeqIO.parse(fasta_read, "fasta"):
        with open(fasta_write, "w") as f:
            # 输出id
            f.write(seq_record.id)
            # 输出序列
            f.write(repr(seq_record.seq) + '\n')
            # 输出序列长度
            f.write("输出序列长度为：" + str(len(seq_record)))


if __name__ == '__main__':
    read = "../data/02_fasta.fasta"
    write1 = "../result/1.fasta"
    write2 = "../result/2.fasta"
    write3 = "../result/3.fasta"
    write4 = "../result/4.fasta"

    raw = "A"
    process = "T"
    single_base_substitution(read, write1, raw, process)
    complement_seq(read, write2)
    reverse_complement_seq(read, write3)
    get_length(read, write4)
