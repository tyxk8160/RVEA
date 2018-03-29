#/usr/bin/env python
import numpy as np
from queue import Queue

'''
'''
def HV(popobj,PF):
    '''
    descripe:
      计算HV得分
    args:
        popobj:numpy.array类型 优化选择的种群，维度为 种群数量x目标数量
        PF:numpy.array类型    PF数组
    return:
        score:float 计算得分矩阵
    example:
        score = HV(popobj,PF)
    '''
    (N,d) = popobj.shape
    #
    #RefPoint = max(PF,[],1)*1.1;
    #
    RefPoint =  np.max(PF,axis =0)*1.1
    

    # np.delete(np.any(popobj>RefPoint))
    popobj = np.delete(popobj,
                    np.nonzero(np.any(popobj>RefPoint),
                                axis=1),
                    axis =0) #删除行
    if popobj.shape[0] is 0：
        score = 0
    elif d < 5:
        # 按照矩阵的第一列进行排序
        #
        pl = popobj[popobj[:,0].argssort()]
        S = [(1,pl)]

        ### @todo: 计算最终的S矩阵
        for k in range(d-1):
            S_ =[]
            for i in range(S):
                pass

        ### @end
        score = 0
        for item in S:
            tmp_score = item[0]
            p = item[1]
            score += tmp_score*np.abs(p[d-1] - RefPoint[d-1]
    else:
        SampleNum = 1000000
        MaxValue = RefPoint
        MinValue = np.min(popobj,axis = 0)
        Samples = np.random.rand(SampleNum,d)*(MaxValue-MinValue) + MinValue

        Domi = np.zeros((1,SampleNum))
        for i in range(popobj.shape[0]):
            index =  np.nonzeros(np.all(popobj[i]<=Samples,
                    axis = 1))
            Domi(0，index) = 1
        score np.prod(MaxValue - MinValue)*np.sum(Domi)/SampleNum
    
    return score



def Slice(pl,k,RefPoint):
    '''
    descripe:
        计算slice
    args:
        pl:vector or matrix?
        k:第 k 个维度 
        RefPoint:参考点
    '''
    pass




