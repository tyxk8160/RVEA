#!/usr/local/bin/python
# -*- coding: utf-8 -*-

# 天线问题："00" 自适应阵列：“01” 单目标测试问题：“02” 多目标测试问题：“03”
# 参数 g11 # 02 # g11_conf.py

#基因范围：
upper=[1,1]

lower=[-1,-1]


#每个基因要达到的精度
#prec=[0.01, 0.01]
p=1e-4
prec=[]
for i in xrange(2):
    prec.append(p)

#对应的基因
keys=['x1','x2']

