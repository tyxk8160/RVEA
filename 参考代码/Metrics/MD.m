function Score = MD(PopObj,PF)
% <metric> <min>
% Mapped diversity

%--------------------------------------------------------------------------
% Copyright (c) 2016-2017 BIMK Group
% You are free to use the PlatEMO for research purposes. All publications
% which use this platform or any code in the platform should acknowledge
% the use of "PlatEMO" and reference "Ye Tian, Ran Cheng, Xingyi Zhang, and
% Yaochu Jin, PlatEMO: A MATLAB Platform for Evolutionary Multi-Objective
% Optimization, IEEE Computational Intelligence Magazine, 2017, in press".
%--------------------------------------------------------------------------

    [~,Close] = min(pdist2(PopObj,PF),[],2);
    Dis  = pdist2(PF,PF);
    Dis2 = Dis;
    Dis2(logical(eye(length(Dis)))) = inf;
    Score = mean(min(Dis(:,Close),[],2).*min(Dis2,[],2));
end