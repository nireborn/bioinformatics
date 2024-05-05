# This is pie.py
# DATE:2024-01-30
# NAME:KWD
# MAIL:nireborn@163.com
# GOOD LUCK!

import matplotlib.pyplot as plt
import pandas as pd


def pie_plot(pie_read, pie_write):
    # 读取txt文件，以第一行为参数说明，第一列为数据，第二列为分组
    data = pd.read_csv(pie_read, sep='\t')

    # 绘制饼状图
    plt.figure(figsize=(8, 8))

    # 绘制饼图，显示百分比，并返回每个扇形的相关信息
    wedges, texts, autotexts = plt.pie(data.iloc[:, 0], labels=data.iloc[:, 1], autopct='%1.1f%%', startangle=90)

    # 添加组名和百分比标签
    for text, autotext, label in zip(texts, autotexts, data.iloc[:, 1]):
        text.set(size=10, weight='bold')
        autotext.set(size=8, color='white', weight='bold')
        # autotext.set_text(f"{label}\n{autotext.get_text()}")
        autotext.set_text(f"{autotext.get_text()}")

    # 添加图例
    plt.legend(wedges, data.iloc[:, 1], title='Groups', loc='center left', bbox_to_anchor=(1, 0, 0.5, 1))

    # plt.title('Pie Chart for Value Distribution by Group')
    # plt.show()

    plt.savefig(pie_write, bbox_inches='tight')
