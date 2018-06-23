function GDE3(Global)
% <algorithm> <A-G>
% GDE3: The third Evolution Step of Generalized Differential Evolution
% operator --- DE

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
        MatingPool = [1:Global.N,randi(Global.N,1,2*Global.N)];
        Offspring  = Global.Variation(Population(MatingPool),Global.N,@DE);
        Population = EnvironmentalSelection(Population,Offspring,Global.N);
    end
end