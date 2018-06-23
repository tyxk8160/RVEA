function SMSEGO(Global)
% <algorithm> <O-Z>
% Multiobjective Optimization on a Limited Budget of Evaluations Using
% Model-Assisted S-Metric Selection
% wmax --- 10000 --- The maximum number of internal evluation

%--------------------------------------------------------------------------
% Copyright (c) 2016-2017 BIMK Group
% You are free to use the PlatEMO for research purposes. All publications
% which use this platform or any code in the platform should acknowledge
% the use of "PlatEMO" and reference "Ye Tian, Ran Cheng, Xingyi Zhang, and
% Yaochu Jin, PlatEMO: A MATLAB Platform for Evolutionary Multi-Objective
% Optimization, IEEE Computational Intelligence Magazine, 2017, in press".
%--------------------------------------------------------------------------

% This function is written by Cheng He

    %% Parameter setting
    wmax = Global.ParameterSet(10000);

    %% Generate initial population based on Latin hypercube sampling
    N          = 11*Global.D-1;
    P          = lhsamp(N,Global.D);
    Population = INDIVIDUAL(repmat(Global.upper-Global.lower,N,1).*P+repmat(Global.lower,N,1));
    THETA      = 5.*ones(Global.M,Global.D);
    Model      = cell(1,Global.M);
    % Lower confident bound parameter
    alpha = 1/normcdf(0.5+1/2^Global.M);
    
    %% Optimization
    while Global.NotTermination(Population)
        % Delete duplicated solutions
        [~,index]  = unique(Population.decs,'rows');
        Population = Population(index);
        PopDec     = Population.decs;
        PopObj     = Population.objs;
        
        % Optimization
        for i = 1 : Global.M
            [dmodel,~] = dacefit(PopDec,PopObj(1:end,i),'regpoly1','corrgauss',THETA(i,:),1e-5.*ones(1,Global.D),20.*ones(1,Global.D));
            Model{i}   = dmodel;
            THETA(i,:) = dmodel.theta;
        end
        w = 0;
        while w < wmax
            drawnow();
            OffDec = Global.VariationDec(PopDec);
            PopDec = [PopDec;OffDec]; 
            [N,~]  = size(PopDec);
            OffObj = zeros(N,Global.M);
            sigma2 = zeros(N,Global.M);
            for i = 1 : size(PopDec,1)
                for j = 1 : Global.M
                    [OffObj(i,j),~,sigma2(i,j)] = predictor(PopDec(i,:),Model{j});
                end
            end
            ypot      = OffObj-alpha.*sqrt(sigma2);                           %Lower confidence bound
            fit       = Contribution(Global.evaluation-Global.evaluated,Population(NDSort(Population.objs,1)==1).objs,ypot);
            [~,index] = sort(fit);
            PopDec 	  = PopDec(index(1:floor(N/2)),:);
            fit       = fit(index(1:floor(N/2)),:);
            w = w + floor(N/2);
        end
        [~,INDEX]  = min(fit);
        PopNew     = INDIVIDUAL(PopDec(INDEX,:));
        Population = [Population,PopNew];
    end
end