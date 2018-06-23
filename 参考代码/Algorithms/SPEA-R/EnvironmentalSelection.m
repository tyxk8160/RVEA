function Population = EnvironmentalSelection(Population,Ei,FV,N)
% The environmental selection of SPEA/R

%--------------------------------------------------------------------------
% Copyright (c) 2016-2017 BIMK Group
% You are free to use the PlatEMO for research purposes. All publications
% which use this platform or any code in the platform should acknowledge
% the use of "PlatEMO" and reference "Ye Tian, Ran Cheng, Xingyi Zhang, and
% Yaochu Jin, PlatEMO: A MATLAB Platform for Evolutionary Multi-Objective
% Optimization, IEEE Computational Intelligence Magazine, 2017, in press".
%--------------------------------------------------------------------------

    Choose = [];
    while length(Choose) < N
        H = [];
        for i = unique(Ei)
            if i > 0
                Local = find(Ei==i);
                [~,q] = min(FV(Local));
                H     = [H,Local(q)];
                Ei(Local(q)) = -1;
            end
        end
        if length(Choose) + length(H) < N
            Choose = [Choose,H];
        else
            [~,rank] = sort(FV(H));
            Choose   = [Choose,H(rank(1:N-length(Choose)))];
        end
    end
    Population = Population(Choose);
end