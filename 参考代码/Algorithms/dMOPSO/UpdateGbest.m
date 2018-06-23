function Gbest = UpdateGbest(W,Population,Z)
% Update the global best set

%--------------------------------------------------------------------------
% Copyright (c) 2016-2017 BIMK Group
% You are free to use the PlatEMO for research purposes. All publications
% which use this platform or any code in the platform should acknowledge
% the use of "PlatEMO" and reference "Ye Tian, Ran Cheng, Xingyi Zhang, and
% Yaochu Jin, PlatEMO: A MATLAB Platform for Evolutionary Multi-Objective
% Optimization, IEEE Computational Intelligence Magazine, 2017, in press".
%--------------------------------------------------------------------------

    %% PBI value of each solution on each weight vector
    PopObj = Population.objs - repmat(Z,length(Population),1);
    Cosine = 1 - pdist2(PopObj,W,'cosine');
    NormP  = sqrt(sum(PopObj.^2,2));
    PBI    = repmat(NormP,1,size(W,1)).*(Cosine+5*sqrt(1-Cosine.^2));

    %% Find the global best particle of each weight vector
    Associate = zeros(1,size(W,1));
    Remain    = 1 : length(Population);
    for i = 1 : size(W,1)
        [~,best]     = min(PBI(Remain,i));
        Associate(i) = Remain(best);
        Remain(best) = [];
    end
    Gbest = Population(Associate);
end