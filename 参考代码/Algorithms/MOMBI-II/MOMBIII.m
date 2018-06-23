function MOMBIII(Global)
% <algorithm> <H-N>
% Improved Metaheuristic Based on the R2 Indicator for Many-Objective
% Optimization
% alpha   ---   0.5 --- Threshold of variances
% epsilon --- 0.001 --- Tolerance threshold
% record  ---     5 --- The record size of nadir vectors

%--------------------------------------------------------------------------
% Copyright (c) 2016-2017 BIMK Group
% You are free to use the PlatEMO for research purposes. All publications
% which use this platform or any code in the platform should acknowledge
% the use of "PlatEMO" and reference "Ye Tian, Ran Cheng, Xingyi Zhang, and
% Yaochu Jin, PlatEMO: A MATLAB Platform for Evolutionary Multi-Objective
% Optimization, IEEE Computational Intelligence Magazine, 2017, in press".
%--------------------------------------------------------------------------

    %% Parameter setting
    [alpha,epsilon,recordSize] = Global.ParameterSet(0.5,0.001,5);
    
    %% Generate random population
    [W,Global.N] = UniformPoint(Global.N,Global.M);
    Population   = Global.Initialization();
    % Ideal and nadir points
    zmin = min(Population.objs,[],1);
    zmax = max(Population.objs,[],1);
    % For storing the nadir vectors of a few generations
    Record = repmat(zmax,recordSize,1);
    % For storing whether each objective has been marked for a few
    % generations
    Mark = false(recordSize,Global.M);
    % R2 ranking procedure
    [Rank,Norm] = R2Ranking(Population.objs,W,zmin,zmax);

    %% Optimization
    while Global.NotTermination(Population)
        MatingPool  = TournamentSelection(2,Global.N,Rank,Norm);
        Offspring   = Global.Variation(Population(MatingPool));
        Population  = [Population,Offspring];
        [Rank,Norm] = R2Ranking(Population.objs,W,zmin,zmax);
        [~,rank]    = sortrows([Rank,Norm]);
        Population  = Population(rank(1:Global.N));
        Rank        = Rank(rank(1:Global.N));
        Norm        = Norm(rank(1:Global.N));
        [zmin,zmax,Record,Mark] = UpdateReferencePoints(Population.objs,zmin,zmax,Record,Mark,alpha,epsilon);
    end
end