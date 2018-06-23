function PopObj = ObjectiveNormalization(Population)
% Objective normalization in SPEA/R

%--------------------------------------------------------------------------
% Copyright (c) 2016-2017 BIMK Group
% You are free to use the PlatEMO for research purposes. All publications
% which use this platform or any code in the platform should acknowledge
% the use of "PlatEMO" and reference "Ye Tian, Ran Cheng, Xingyi Zhang, and
% Yaochu Jin, PlatEMO: A MATLAB Platform for Evolutionary Multi-Objective
% Optimization, IEEE Computational Intelligence Magazine, 2017, in press".
%--------------------------------------------------------------------------

    PopObj = Population.objs;
    ND     = NDSort(PopObj,1) == 1;
    zmin   = min(PopObj(ND,:),[],1);
    zmax   = max(PopObj(ND,:),[],1);
    PopObj = (PopObj-repmat(zmin,size(PopObj,1),1))./repmat(zmax-zmin,size(PopObj,1),1);
end