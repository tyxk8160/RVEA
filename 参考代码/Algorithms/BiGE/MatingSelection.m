function MatingPool = MatingSelection(BiObj)
% The mating selection of BiGE

%--------------------------------------------------------------------------
% Copyright (c) 2016-2017 BIMK Group
% You are free to use the PlatEMO for research purposes. All publications
% which use this platform or any code in the platform should acknowledge
% the use of "PlatEMO" and reference "Ye Tian, Ran Cheng, Xingyi Zhang, and
% Yaochu Jin, PlatEMO: A MATLAB Platform for Evolutionary Multi-Objective
% Optimization, IEEE Computational Intelligence Magazine, 2017, in press".
%--------------------------------------------------------------------------

    N = size(BiObj,1);
    
    %% Binary tournament selection
    Parents1   = randi(N,1,N);
    Parents2   = randi(N,1,N);
    Dominate   = any(BiObj(Parents1,:)<BiObj(Parents2,:),2) - any(BiObj(Parents1,:)>BiObj(Parents2,:),2);
    MatingPool = [Parents1(Dominate>=0),...
                  Parents2(Dominate<0)];
end