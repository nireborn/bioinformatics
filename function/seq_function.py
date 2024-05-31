# This is seq操作.py
# DATE:2024-01-26
# NAME:KWD
# MAIL:nireborn@163.com
# GOOD LUCK!
"""
文件处理：
    输入文件为：.txt文件
    输出文件为：.txt文件
数据格式：
    文件中只包含基因序列，以下是数据格式：
    CGTAACAAGGTTTCCGTAGGTGAACCTGCGGAAGGATCATTGATGAGACCGTGGAATAAACGATCGAGTG
    AATCCGGAGGACCGGTGTACTCAGCTCACCGGGGGCATTGCTCCCGTGGTGACCCTGATTTGTTGTTGGG
    CCGCCTCGGGAGCGTCCATGGCGGGTTTGAACCTCTAGCCCGGCGCAGTTTGGGCGCCAAGCCATATGAA
    AGCATCACCGGCGAATGGCATTGTCTTCCCCAAAACCCGGAGCGGCGGCGTGCTGTCGCGTGCCCAATGA
    ATTTTGATGACTCTCGCAAACGGGAATCTTGGCTCTTTGCATCGGATGGAAGGACGCAGCGAAATGCGAT
    AAGTGGTGTGAATTGCAAGATCCCGTGAACCATCGAGTCTTTTGAACGCAAGTTGCGCCCGAGGCCATCA
    GGCTAAGGGCACGCCTGCTTGGGCGTCGCGCTTCGTCTCTCTCCTGCCAATGCTTGCCCGGCATACAGCC
    AGGCCGGCGTGGTGCGGATGTGAAAGATTGGCCCCTTGTGCCTAGGTGCGGCGGGTCCAAGAGCTGGTGT
    TTTGATGGCCCGGAACCCGGCAAGAGGTGGACGGATGCTGGCAGCAGCTGCCGTGCGAATCCCCCATGTT
    GTCGTGCTTGTCGGACAGGCAGGAGAACCCTTCCGAACCCCAATGGAGGGCGGTTGACCGCCATTCGGAT
    GTGACCCCAGGTCAGGCGGGGGCACCCGCTGAGTTTACGC
    说明：可以是70个基因为一行，也可以任意长度。
实现功能：
    ①对序列的切片操作
    ②计算GC%
"""

from datetime import datetime

from Bio.Seq import Seq
from Bio.SeqUtils import gc_fraction


# 拼接序列函数  【获取完整序列】
def joint_seq(seq_read):
    """
    :param seq_read: 存储序列文件
    :return: 拼接完成后的序列（字符串类型）
    """
    with open(seq_read, "r") as fr:  # 只读取文件，没有文件会报错
        seq = ''.join(line.strip() for line in fr)  # 使用列表推导式将行的首尾空白去掉，然后使用join拼接字符串
    return seq  # 字符串类型的序列


# 切片函数  【对完整序列进行剪切，获取连续序列】
def slicing(seq_read, seq_write, first, last):
    """
    :param seq_read: 序列存储文件URL
    :param seq_write: 写入切片后的文件URL
    :param first: 切片开始位置
    :param last: 切片结束位置
    :return: None
    """
    seq = joint_seq(seq_read)  # 调用joint_seq函数，获取拼接后的完整序列
    seq_slice = seq[int(first) - 1:int(last)]  # 切片，获取连续基因序列

    with open(seq_write, "w") as fw:  # 打开文件，如果没有文件，会自动创建这个文件，如果有文件，会覆盖之前的内容
        fw.write(seq_slice)  # 写入序列


# gc计算函数  【计算GC%】
# 处理完成后获得的txt文件，第一行为序列，第二行为GC含量
def gc_calculation(seq_read, seq_write):
    """
    :param seq_read: 序列存储文件
    :param seq_write: 输出文件路径
    :return: GC含量百分比
    """
    seq = joint_seq(seq_read)  # 调用joint_seq函数，获取拼接后的完整序列

    my_seq_gc = Seq(seq)  # 转换为Seq对象，为调用gc_fraction函数做准备
    gc_per = round(gc_fraction(my_seq_gc) * 100, 2)  # 进行计算，转化为百分比，四舍五入保留两位

    result = str(gc_per) + "%"  # 转化为字符串格式，末尾加百分号

    with open(seq_write, "w") as fw:  # 将结果写入指定路径的文本文件
        fw.write("seq:" + seq + "\n")  # 写入完整序列
        fw.write("GC(%):" + result + "\n")  # 写入GC含量的结果


if __name__ == '__main__':
    # 读取文件所在位置
    read_url = "..\\data\\01_seq.txt"

    # 获取当前时间的字符串表示（包含秒）（年_月_日_时分秒）
    current_time_str = datetime.now().strftime("%Y_%m_%d_%H%M%S")

    # 选择输出文件夹
    write = "..\\result"

    gc_url = write + "\\" + "gc_" + current_time_str + ".txt"
    seq_url = write + "\\" + "seq_" + current_time_str + ".txt"

    gc_calculation(read_url, gc_url)

    first, last = 4, 57
    # 计算长度，超出则弹出提示框。
    slicing(read_url, seq_url, first, last)
