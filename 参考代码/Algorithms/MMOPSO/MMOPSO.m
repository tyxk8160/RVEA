function MMOPSO(Global)
% <algorithm> <H-N>
% A novel multi-objective particle swarm optimization with multiple search 
% strategies
% operator --- MMOPSO_operator

%--------------------------------------------------------------------------
% Copyright (c) 2016-2017 BIMK Group
% You are free to use the PlatEMO for research purposes. All publications
% which use this platform or any code in the platform should acknowledge
% the use of "PlatEMO" and reference "Ye Tian, Ran Cheng, Xingyi Zhang, and
% Yaochu Jin, PlatEMO: A MATLAB Platform for Evolutionary Multi-Objective
% Optimization, IEEE Computational Intelligence Magazine, 2017, in press".
%--------------------------------------------------------------------------

    %% Generate the weight vectors
    [W,Global.N] = UniformPoint(Global.N,Global.M);
    W = W./repmat(sqrt(sum(W.^2,2)),1,size(W,2));
   
    %% Generate random population
    Population    = Global.Initialization();
    Z             = min(Population.objs,[],1);
    Population    = Classification(Global,Population,W,Z);
    Archive       = UpdateArchive(Population,Global.N); 
    
    %% Optimization
    while Global.NotTermination(Archive)
        [Pbest,Gbest] = GetBest(Archive,W,Z);
        Population    = Global.Variation([Population,Pbest,Gbest],inf,@MMOPSO_operator);
        Z             = min([Z;Population.objs],[],1);
        Archive       = UpdateArchive([Archive,Population],Global.N); 
        S             = Global.Variation(Archive([1:length(Archive),randi(ceil(length(Archive)/2),1,length(Archive))]),length(Archive),@EAreal);
        Z             = min([Z;S.objs],[],1);
        Archive       = UpdateArchive([Archive,S],Global.N);
    end
end