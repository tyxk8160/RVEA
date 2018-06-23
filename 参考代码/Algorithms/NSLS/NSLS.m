function NSLS(Global)
% <algorithm> <H-N>
% A New Local Search-based Multiobjective Optimization Algorithm
% operator --- NSLS_operator

%--------------------------------------------------------------------------
% Copyright (c) 2016-2017 BIMK Group
% You are free to use the PlatEMO for research purposes. All publications
% which use this platform or any code in the platform should acknowledge
% the use of "PlatEMO" and reference "Ye Tian, Ran Cheng, Xingyi Zhang, and
% Yaochu Jin, PlatEMO: A MATLAB Platform for Evolutionary Multi-Objective
% Optimization, IEEE Computational Intelligence Magazine, 2017, in press".
%--------------------------------------------------------------------------

    %% Generate random population
    Population = Global.Initialization();

    %% Optimization
    while Global.NotTermination(Population)
        Offspring  = Global.Variation(Population,inf,@NSLS_operator);
        Population = EnvironmentalSelection([Population,Offspring],Global.N);
    end
end