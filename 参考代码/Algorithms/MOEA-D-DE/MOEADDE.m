function MOEADDE(Global)
% <algorithm> <H-N>
% Multiobjective Optimization Problems With Complicated Pareto Sets, MOEA/D
% and NSGA-II
% delta --- 0.9 --- The probability of choosing parents locally
% nr    ---   2 --- Maximum number of solutions replaced by each offspring
% operator      --- DE

%--------------------------------------------------------------------------
% Copyright (c) 2016-2017 BIMK Group
% You are free to use the PlatEMO for research purposes. All publications
% which use this platform or any code in the platform should acknowledge
% the use of "PlatEMO" and reference "Ye Tian, Ran Cheng, Xingyi Zhang, and
% Yaochu Jin, PlatEMO: A MATLAB Platform for Evolutionary Multi-Objective
% Optimization, IEEE Computational Intelligence Magazine, 2017, in press".
%--------------------------------------------------------------------------

    %% Parameter setting
    [delta,nr] = Global.ParameterSet(0.9,2);

    %% Generate the weight vectors
    [W,Global.N] = UniformPoint(Global.N,Global.M);
    T = ceil(Global.N/10);

    %% Detect the neighbours of each solution
    B = pdist2(W,W);
    [~,B] = sort(B,2);
    B = B(:,1:T);

    %% Generate random population
    Population = Global.Initialization();
    Z = min(Population.objs,[],1);

    %% Optimization
    while Global.NotTermination(Population)
        % For each solution
        for i = 1 : Global.N
            % Choose the parents
            if rand < delta
                P = B(i,randperm(size(B,2)));
            else
                P = randperm(Global.N);
            end

            % Generate an offspring
            Offspring = Global.Variation(Population([i,P(1:2)]),1,@DE);

            % Update the ideal point
            Z = min(Z,Offspring.obj);

            % Update the solutions in P by Tchebycheff approach
            g_old = max(abs(Population(P).objs-repmat(Z,length(P),1)).*W(P,:),[],2);
            g_new = max(repmat(abs(Offspring.obj-Z),length(P),1).*W(P,:),[],2);
            Population(P(find(g_old>=g_new,nr))) = Offspring;
        end
    end
end