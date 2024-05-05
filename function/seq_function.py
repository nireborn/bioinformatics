# This is seq操作.py
# DATE:2024-01-26
# NAME:KWD
# MAIL:nireborn@163.com
# GOOD LUCK!
"""
文件处理：
    输入txt文件
    输出txt文件
实现功能：
    对序列的切片操作
    计算GC%
"""

from datetime import datetime

from Bio.Seq import Seq
from Bio.SeqUtils import gc_fraction
from PyQt5.QtCore import pyqtSlot


@pyqtSlot()
# 基因序列存储在txt文本中，是按照特定的长度进行换行。
# 获取完整序列
def joint_seq(seq_read):
    """
    :param seq_read: 存储序列文件
    :return: 拼接完成后的序列（字符串类型）
    """
    # 读取文件
    with open(seq_read, "r") as fr:
        # 使用列表推导式将行的首尾空白去掉，然后使用 join 拼接字符串
        tmp = ''.join(line.strip() for line in fr)
    return tmp  # 字符串类型的序列


# 对序列的切片操作
def slicing(seq_read, seq_write, first, last):
    """
    :param seq_read: 序列存储文件URL
    :param seq_write: 写入切片后的文件URL
    :param first: 切片开始位置
    :param last: 切片结束位置
    :return: None
    """
    # 获取序列
    seq = joint_seq(seq_read)
    # 切片
    seq_slice = seq[int(first) - 1:int(last)]
    # 打开文件操作
    fw = open(seq_write, "w")
    fw.write(seq_slice)
    fw.close()


# 计算GC%
# txt文件第一行为序列，第二行为GC含量
def gc_calculation(seq_read, seq_write):
    """
    :param seq_read: 序列存储文件
    :param seq_write: 输出文件路径
    :return: GC含量百分比
    """
    # 获取序列
    seq = joint_seq(seq_read)

    # 转换为Seq对象
    my_seq_gc = Seq(seq)

    # 进行计算，转化为百分比，四舍五入保留两位
    gc_per = round(gc_fraction(my_seq_gc) * 100, 2)

    # 转化为字符串格式，末尾加百分号
    result = str(gc_per) + "%"

    # 将结果写入指定路径的文本文件
    with open(seq_write, "w") as fw:
        fw.write("seq:" + seq + "\n")  # 写入完整序列
        fw.write("GC(%):" + result + "\n")  # 写入GC含量的结果


if __name__ == '__main__':
    # 从文本框读取需要读取的txt文件路径
    read_url = "..\\data\\01_seq.txt"  # 在GUI中获取的是绝对路径

    # 获取当前时间的字符串表示（包含秒）
    current_time_str = datetime.now().strftime("%Y_%m_%d_%H%M%S")

    # 选择输出文件夹
    write = "..\\result"

    gc_url = write + "\\" + "gc_" + current_time_str + ".txt"
    seq_url = write + "\\" + "seq_" + current_time_str + ".txt"

    gc_calculation(read_url, gc_url)

    first, last = 4, 57
    # 计算长度，超出则弹出提示框。
    slicing(read_url, seq_url, first, last)
