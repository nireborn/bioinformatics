# This is f2.py
# DATE:2024-01-24
# NAME:KWD
# MAIL:nireborn@163.com
# GOOD LUCK!
"""
对gff3文件进行操作：
①筛选出文件中1号染色体100000-500000之间的基因；
②输出基因的名字，染色体，起始位置，终止位置信息用tab分隔各列
"""
from datetime import datetime


def filter_gff3(input_file, output_file, start_range, end_range):
    """
    :param input_file: 输入的gff3文件路径。
    :param output_file: 输出文件路径。
    :param start_range: 起始位置
    :param end_range: 结束位置
    :return:
    """

    fr = open(input_file, "r")
    fw = open(output_file, "w")

    found_data = False  # 标记是否找到符合条件的数据

    for line in fr:
        line = line.strip()
        if not line.startswith("#"):
            tmp = line.split("\t")
            if tmp[0] == "1" and tmp[2] == "gene" and start_range < int(tmp[3]) < end_range:
                gene_id = tmp[8].split(";")[0].split("=")[1]
                mystr = "\t".join([tmp[0], tmp[3], tmp[4], gene_id]) + "\n"
                fw.write(mystr)
                found_data = True

    if not found_data:
        fw.write("None\n")

    fr.close()
    fw.close()


if __name__ == '__main__':
    # 从文本框读取需要读取的txt文件路径
    read_url = "../data/Arabidopsis_thaliana.TAIR10.44.chromosome.1.gff3"  # 在GUI中获取的是绝对路径

    # 获取当前时间的字符串表示（包含秒）
    current_time_str = datetime.now().strftime("%Y_%m_%d_%H%M%S")

    # 选择输出文件夹
    write = "..\\result"

    gff3_url = write + "\\" + "gff3_" + current_time_str + ".txt"

    start = 100000

    end = 500000

    filter_gff3(read_url, gff3_url, start, end)
