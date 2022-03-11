# HGG.SNV_Reptile
一个HGG.SNV数据库爬虫
HGG.SNV: 了解不同人群中人类单核苷酸变异的进化和医学意义的数据库
# 使用
首先使用`pip`安装依赖库
```
pip install pandas == 1.3.1
```
输入文档必须为`csv`格式, 表格结构如下(可不按顺序):
|SNP|CHR|BP|A1|A2|
|:---:|:---:|:---:|:---:|:---:|
|rs7849487|9|1757274|T|G|

说明: SNP: RSID, CHR: 染色体编号, BP: 碱基对位置, A1: 参考等位基因, A2: 祖先等位基因
# 参考链接：
网站主页: https://www.pggsnv.org/
[1] Chao Zhang#, Yang Gao#, Zhilin Ning#, Yan Lu#, Xiaoxi Zhang, Jiaojiao Liu, Bo Xie, Zhe Xue, Xiaoji Wang, Kai Yuan, Xueling Ge, Yuwen Pan, Chang Liu, Lei Tian, Yuchen Wang, Dongsheng Lu, Boon-Peng Hoh, Shuhua Xu*. PGG.SNV: understanding the evolutionary and medical implications of human single nucleotide variations in diverse populations. Genome Biology (2019), 20:215. https://doi.org/10.1186/s13059-019-1838-5
