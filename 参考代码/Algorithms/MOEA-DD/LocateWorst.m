function x = LocateWorst(PopObj,W,Region,FrontNo,Z)
% Detect the worst solution in the population

%--------------------------------------------------------------------------
% Copyright (c) 2016-2017 BIMK Group
% You are free to use the PlatEMO for research purposes. All publications
% which use this platform or any code in the platform should acknowledge
% the use of "PlatEMO" and reference "Ye Tian, Ran Cheng, Xingyi Zhang, and
% Yaochu Jin, PlatEMO: A MATLAB Platform for Evolutionary Multi-Objective
% Optimization, IEEE Computational Intelligence Magazine, 2017, in press".
%--------------------------------------------------------------------------

    Crowd  = hist(Region,1:size(W,1));
    Phi    = find(Crowd==max(Crowd));
    PBI    = CalPBI(PopObj,W,Region,Z,ismember(Region,Phi));
    PBISum = zeros(1,size(W,1));
    for j = 1 : length(PBI)
        PBISum(Region(j)) = PBISum(Region(j)) + PBI(j);
    end
    [~,Phi] = max(PBISum);
    Phih    = find(Region==Phi);
    R       = Phih(FrontNo(Phih)==max(FrontNo(Phih)));
    [~,x]   = max(PBI(R));
    x       = R(x);
end