function DMOEAeC(Global)
% <algorithm> <A-G>
% DMOEA-��C: Decomposition-Based Multi-objective Evolutionary Algorithm with the ��-Constraint Framework
% INm --- 0.2 --- Iteration interval of alternating the main objective function

%--------------------------------------------------------------------------
% Copyright (c) 2016-2017 BIMK Group
% You are free to use the PlatEMO for research purposes. All publications
% which use this platform or any code in the platform should acknowledge
% the use of "PlatEMO" and reference "Ye Tian, Ran Cheng, Xingyi Zhang, and
% Yaochu Jin, PlatEMO: A MATLAB Platform for Evolutionary Multi-Objective
% Optimization, IEEE Computational Intelligence Magazine, 2017, in press".
%--------------------------------------------------------------------------

    %% Parameter setting
    INm = Global.ParameterSet(0.2);

    %% Generate the weight vectors
    [W,N] = ReplicatePoint(Global.N,Global.M-1);
    % Size of neighborhood
    T = ceil(N/10);
    % Maximum number of solutions replaced by each offspring
    nr = ceil(N/100);

    %% Detect the neighbours of each solution
    B = pdist2(W,W);
    [~,B] = sort(B,2);
    B = B(:,1:T);

    %% Generate random population
    Population     = Global.Initialization(N);
    [Archive,znad] = UpdateArchive(Population,Global.N);
    z  = min(Population.objs,[],1);
    Pi = ones(N,1);

    %% Optimization
    gen = 0;
    while Global.NotTermination(Archive)
        if ~mod(gen,ceil(INm*Global.evaluation/N))
           % Solution-to-subproblem matching
           s = randi(Global.M);
           S = 1 : N;
           while ~isempty(S)
               PopObj = (Population(S).objs-repmat(z,length(S),1))./repmat(znad-z,length(S),1);
               l      = randi(length(S));
               [~,k]  = min(sum(abs(PopObj(:,[1:s-1,s+1:end])-repmat(W(S(l),:),length(S),1)),2));
               temp             = Population(S(l));
               Population(S(l)) = Population(S(k));
               Population(S(k)) = temp;
               S(l) = [];
           end
           PopObj = Population.objs;
           oldObj = PopObj(:,s) + 1e-6*sum(PopObj(:,[1:s-1,s+1:end]),2);
        end
        if ~mod(gen,10)
            % Allocation of computing resources
            PopObj    = Population.objs;
            newObj    = PopObj(:,s) + 1e-6*sum(PopObj(:,[1:s-1,s+1:end]),2);
            DELTA     = (oldObj-newObj)./oldObj;
            Temp      = DELTA <= 0.001;
            Pi(~Temp) = 1;
            Pi(Temp)  = (0.95+0.05*DELTA(Temp)/0.001).*Pi(Temp);
            oldObj    = newObj;
        end
        for subgeneration = 1 : 5
            % Choose I
            Bounday = find(sum(W==1,2)==1&sum(W<1e-3,2)==size(W,2)-1)';
            I = [Bounday,TournamentSelection(10,floor(N/5)-length(Bounday),-Pi)];

            % Evolve each solution in I
            Offsprings(1:length(I)) = INDIVIDUAL();
            for i = 1 : length(I)
                % Choose the parents
                if rand < 0.9
                    P = B(I(i),randperm(size(B,2)));
                else
                    P = randperm(N);
                end

                % Generate an offspring
                Offsprings(i) = Global.Variation(Population(P(1:2)),1);

                % Update the ideal point
                z = min(z,Offsprings(i).obj);
                
                % Subproblem-to-solution matching
                OObj      = (Offsprings(i).obj-z)./(znad-z);
                CV        = sum(max(0,repmat(OObj([1:s-1,s+1:end]),N,1)-W),2);
                CV(CV==0) = 1./sum(repmat(OObj([1:s-1,s+1:end]),sum(CV==0),1)-W(CV==0,:),2);
                [~,k]     = min(CV);
                P         = B(k,randperm(size(B,2)));
                
                % Update the solutions
                PObj   = Population(P).objs;
                OObj   = repmat(Offsprings(i).obj,length(P),1);
                FmainP = PObj(:,s) + 1e-6*sum(PObj(:,[1:s-1,s+1:end]),2);
                FmainO = OObj(:,s) + 1e-6*sum(OObj(:,[1:s-1,s+1:end]),2);
                PObj   = (PObj-repmat(z,length(P),1))./repmat(znad-z,length(P),1);
                OObj   = (OObj-repmat(z,length(P),1))./repmat(znad-z,length(P),1);
                CVP    = sum(max(0,PObj(:,[1:s-1,s+1:end])-W(P,:)),2);
                CVO    = sum(max(0,OObj(:,[1:s-1,s+1:end])-W(P,:)),2);
                Population(P(find(CVO==0&CVP==0&FmainO<FmainP|CVO<CVP,nr))) = Offsprings(i);
            end
            
            % Update the archive
            [Archive,znad] = UpdateArchive([Archive,Offsprings],Global.N);
        end
        gen = gen + 1;
    end
end

function [W,N] = ReplicatePoint(SampleNum,M)
    if M > 1
        SampleNum = (ceil(SampleNum^(1/M)))^M;
        Gap       = 0:1/(SampleNum^(1/M)-1):1;
        eval(sprintf('[%s]=ndgrid(Gap);',sprintf('c%d,',1:M)))
        eval(sprintf('W=[%s];',sprintf('c%d(:),',1:M)))
    else
        W = (0:1/(SampleNum-1):1)';
    end
    N = size(W,1);
end