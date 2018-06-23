function [Rank,Norm]  = R2Ranking(PopObj,W,zmin,zmax)
% R2 ranking algorithm based on the metric of ASF

%--------------------------------------------------------------------------
% Copyright (c) 2016-2017 BIMK Group
% You are free to use the PlatEMO for research purposes. All publications
% which use this platform or any code in the platform should acknowledge
% the use of "PlatEMO" and reference "Ye Tian, Ran Cheng, Xingyi Zhang, and
% Yaochu Jin, PlatEMO: A MATLAB Platform for Evolutionary Multi-Objective
% Optimization, IEEE Computational Intelligence Magazine, 2017, in press".
%--------------------------------------------------------------------------

    N  = size(PopObj,1);
    NW = size(W,1);

    %% Normalize the population
    PopObj = (PopObj-repmat(zmin,N,1))./repmat(zmax-zmin,N,1);
    
    %% Calculate the L2-norm of each solution
    Norm = sqrt(sum(PopObj.^2,2));
    
    %% Rank the population
    Rank = zeros(N,NW);
    for i = 1 : NW
        ASF           = max(PopObj./repmat(W(i,:),N,1),[],2);
        [~,rank]      = sortrows([ASF,Norm]);
        [~,Rank(:,i)] = sort(rank);
    end
    Rank = min(Rank,[],2);
end