function SMEA(Global)
% <algorithm> <O-Z>
% A Self-Organizing Multiobjective Evolutionary Algorithm
% D    ---     --- Number of neurons in each dimension of the latent space
% tau0 --- 0.7 --- Initial learning rate
% H    ---   5 --- Size of neighborhood mating pools
% operator     --- DE

%--------------------------------------------------------------------------
% Copyright (c) 2016-2017 BIMK Group
% You are free to use the PlatEMO for research purposes. All publications
% which use this platform or any code in the platform should acknowledge
% the use of "PlatEMO" and reference "Ye Tian, Ran Cheng, Xingyi Zhang, and
% Yaochu Jin, PlatEMO: A MATLAB Platform for Evolutionary Multi-Objective
% Optimization, IEEE Computational Intelligence Magazine, 2017, in press".
%--------------------------------------------------------------------------

    %% Parameter setting
    [D,tau0,H] = Global.ParameterSet(repmat(ceil(Global.N.^(1/(Global.M-1))),1,Global.M-1),0.7,5);
    Global.N   = prod(D);
    sigma0     = sqrt(sum(D.^2)/(Global.M-1))/2;

    %% Generate random population
    Population = Global.Initialization();
    FrontNo    = NDSort(Population.objs,inf);
    
    %% Initialize the SOM
    % Training set
    S = Population.decs;
    % Weight vector of each neuron
    W = S;
    % Position of each neuron
    D = arrayfun(@(S)1:S,D,'UniformOutput',false);
    eval(sprintf('[%s]=ndgrid(D{:});',sprintf('c%d,',1:length(D))))
    eval(sprintf('Z=[%s];',sprintf('c%d(:),',1:length(D))))
    % Distance between each two neurons in latent space
    LDis = pdist2(Z,Z);
    % H nearest neurons of each neuron in latent space
    [~,B] = sort(LDis,2);
    B     = B(:,2:min(H+1,end));

    %% Optimization
    while Global.NotTermination(Population)
        % Update SOM
        for s = 1 : size(S,1)
            sigma  = sigma0*(1-(Global.evaluated+s)/Global.evaluation);
            tau    = tau0*(1-(Global.evaluated+s)/Global.evaluation);
            [~,u1] = min(pdist2(S(s,:),W));
            U      = LDis(u1,:) < sigma;
            W(U,:) = W(U,:) + tau.*repmat(exp(-LDis(u1,U))',1,size(W,2)).*(repmat(S(s,:),sum(U),1)-W(U,:));
        end
        
        % Associate each solution with a neuron
        A  = 1 : Global.N;
        U  = 1 : Global.N;
        XU = zeros(1,Global.N);
        for i = 1 : Global.N
            x        = randi(length(A));
            [~,u]    = min(pdist2(Population(A(x)).dec,W(U,:)));
            XU(U(u)) = A(x);
            A(x)     = [];
            U(u)     = [];
        end
        
        % Evolution
        A = Population.decs;
        for u = 1 : Global.N
            drawnow();
            if rand < 0.9
                Q = XU(B(u,:));
            else
                Q = 1 : Global.N;
            end
            y = Global.Variation(Population([u,Q(randperm(length(Q),2))]),1,@DE);
            [Population,FrontNo] = Select(Population,FrontNo,y);
        end
        
        % Update the training set
        S = setdiff(Population.decs,A,'rows');
    end
end