function NewGoal = GeneGoal(PopObj,NGoal)
% Generate new goals

%--------------------------------------------------------------------------
% Copyright (c) 2016-2017 BIMK Group
% You are free to use the PlatEMO for research purposes. All publications
% which use this platform or any code in the platform should acknowledge
% the use of "PlatEMO" and reference "Ye Tian, Ran Cheng, Xingyi Zhang, and
% Yaochu Jin, PlatEMO: A MATLAB Platform for Evolutionary Multi-Objective
% Optimization, IEEE Computational Intelligence Magazine, 2017, in press".
%--------------------------------------------------------------------------

    Gmax    = max(PopObj,[],1)*1.2;
    Gmin    = min(PopObj,[],1);
    NewGoal = rand(NGoal,size(PopObj,2)).*(repmat(Gmax-Gmin,NGoal,1))+repmat(Gmin,NGoal,1);
end