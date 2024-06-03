# README

> 项目所在GitHub地址：
>
> https：https://github.com/nireborn/bioinformatics.git
>
> ssh：git@github.com:nireborn/bioinformatics.git

项目名：<u>bioinformatics</u>

#### 1.如何运行：

##### 需要环境：

- python：＞＝v3.10

##### python自带库：（以下版本均为项目所使用版本）

- PyQt5（5.15.9）
- Biopython（1.83）
- pandas（1.5.3）
- matplotlib（3.6.2）
- seaborn（0.12.2）

第三方库：（均包含在项目源代码中）

- pyvenn
- haplot

##### 运行方法：

在github上克隆项目到本地，使用pycharm打开项目，运行主函数： <u>main文件夹下的GUI.py</u> 即可

#### 2.实现功能：

- 序列编辑
  - 序列剪切
  - GC含量统计
- fasta/fastq文件处理
  - 单碱基替换
  - 互补序列
  - 反向互补序列
  - 长度计算
- gff文件处理
- 可视化功能
  - 散点图
  - 折线图
  - 柱状图
  - 饼状图
  - 热力图
  - Venn图
  - 基因结构
  - 进化树

#### 3.测试数据：

测试数据均存放在`"data"`文件夹中。每一个功能对应一个数据文件，详见文件名。

> 例如：序列功能对应`01_seq.txt`文件。

数据格式需要按照测试数据格式存放，具体说明在平台对应功能的分页中。

各个功能对应的测试文件：

|     功能     |            测试文件            |
| :----------: | :----------------------------: |
|   序列剪切   |           01_seq.txt           |
|  GC含量统计  |           01_seq.txt           |
|  单碱基替换  |         02_fasta.fasta         |
|   互补序列   |         02_fasta.fasta         |
| 反向互补序列 |         02_fasta.fasta         |
|   长度计算   |         02_fasta.fasta         |
| gff文件处理  |          03_gff3.gff3          |
|    散点图    |       04_scatterplot.txt       |
|    折线图    |          05_line.txt           |
|    柱状图    |           06_bar.txt           |
|    饼状图    |           07_pie.txt           |
|    热力图    |         08_heatmap.txt         |
|    Venn图    | 09_venn3.txt<br />09_venn6.txt |
|   基因结构   |     10_gene_struction.txt      |
|    进化树    |        11_gene_tree.txt        |

