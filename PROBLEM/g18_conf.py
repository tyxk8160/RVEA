#!/usr/local/bin/python
# -*- coding: utf-8 -*-

# 天线问题："00" 自适应阵列：“01” 单目标测试问题：“02” 多目标测试问题：“03”
# 参数 g18 # 02 # g18_conf.py

#基因范围：
upper=[10,10,10,10,10,10,10,10,20]

lower=[-10,-10,-10,-10,-10,-10,-10,-10,0]


#每个基因要达到的精度
#prec=[0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01]
p=1e-4
prec=[]
for i in xrange(9):
    prec.append(p)

#对应的基因
keys=['x1','x2','x3','x4','x5','x6','x7','x8','x9']

