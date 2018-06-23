function Population = Truncation(Population,N)
% Limit the size of final popualtion in RVEA*

%--------------------------------------------------------------------------
% Copyright (c) 2016-2017 BIMK Group
% You are free to use the PlatEMO for research purposes. All publications
% which use this platform or any code in the platform should acknowledge
% the use of "PlatEMO" and reference "Ye Tian, Ran Cheng, Xingyi Zhang, and
% Yaochu Jin, PlatEMO: A MATLAB Platform for Evolutionary Multi-Objective
% Optimization, IEEE Computational Intelligence Magazine, 2017, in press".
%--------------------------------------------------------------------------

    Choose = true(1,length(Population));
    Cosine = 1 - pdist2(Population.objs,Population.objs,'cosine');
    Cosine(logical(eye(length(Cosine)))) = 0;
    while sum(Choose) > N
        Remain   = find(Choose);
        Temp     = sort(-Cosine(Remain,Remain),2);
        [~,Rank] = sortrows(Temp);
        Choose(Remain(Rank(1))) = false;
    end
    Population = Population(Choose);
end