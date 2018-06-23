#!/usr/local/bin/python
# -*- coding: utf-8 -*-

# 天线问题："00" 自适应阵列：“01” 单目标测试问题：“02” 多目标测试问题：“03”
##参数 c05 # 02 # c05_conf.py
##model

import dimension

#基因数：
D = dimension.dimension

###基因
upper = [ 600.0]*D
lower = [-600.0]*D


###每个基因要达到的精度
prec = [0.01]*D


keys = ['x1','x2','x3','x4','x5','x6','x7','x8','x9','x10']

