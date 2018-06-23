#!/usr/local/bin/python
# -*- coding: utf-8 -*-

# 天线问题："00" 自适应阵列：“01” 单目标测试问题：“02” 多目标测试问题：“03”
# 参数 g12 # 02 # g12_conf.py

#基因范围：
upper=[10,10,10]

lower=[0,0,0]


#每个基因要达到的精度
#prec=[0.01, 0.01,0.01]
p=1e-4
prec=[]
for i in xrange(3):
    prec.append(p)

#对应的基因
keys=['x1','x2','x3']

