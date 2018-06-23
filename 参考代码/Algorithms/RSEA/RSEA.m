function RSEA(Global)
% <algorithm> <O-Z>
% A radial space division based evolutionary algorithm for many-objective
% optimization

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
    Range      = inf(2,Global.M);
    
    %% Optimization
    while Global.NotTermination(Population)
        Range(1,:) = min([Range(1,:);Population.objs],[],1);
        Range(2,:) = max(Population(NDSort(Population.objs,1)==1).objs,[],1);
        MatingPool = MatingSelection(Population.objs,Range,ceil(Global.N/2)*2);
        Offspring  = Global.Variation(Population(MatingPool));
        Population = EnvironmentalSelection(Global,[Population,Offspring],Range,Global.N);
    end
end