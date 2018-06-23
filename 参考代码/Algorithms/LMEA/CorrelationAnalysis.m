function DVSet = CorrelationAnalysis(Global,Population,DV,nCor)
% Detect the group of each distance variable

%--------------------------------------------------------------------------
% Copyright (c) 2016-2017 BIMK Group
% You are free to use the PlatEMO for research purposes. All publications
% which use this platform or any code in the platform should acknowledge
% the use of "PlatEMO" and reference "Ye Tian, Ran Cheng, Xingyi Zhang, and
% Yaochu Jin, PlatEMO: A MATLAB Platform for Evolutionary Multi-Objective
% Optimization, IEEE Computational Intelligence Magazine, 2017, in press".
%--------------------------------------------------------------------------
    
    DVSet = {};
    for v = DV
        RelatedSet = [];
        for d = 1 : length(DVSet)
            for u = DVSet{d}
                drawnow();
                sign = false;
                for i = 1 : nCor
                    p    = Population(randi(length(Population)));
                    a2   = rand*(Global.upper(v)-Global.lower(v)) + Global.lower(v);
                    b2   = rand*(Global.upper(u)-Global.lower(u)) + Global.lower(u);
                    decs = repmat(p.dec,3,1);
                    decs(1,v)     = a2;
                    decs(2,u)     = b2;
                    decs(3,[v,u]) = [a2,b2];
                    F = INDIVIDUAL(decs);
                    delta1 = F(1).obj - p.obj;
                    delta2 = F(3).obj - F(2).obj;
                    if any(delta1.*delta2<0)
                        sign = true;
                        RelatedSet = [RelatedSet,d];
                        break;
                    end
                end
                if sign
                    break;
                end
            end
        end
        if isempty(RelatedSet)
            DVSet = [DVSet,v];
        else
            DVSet = [DVSet,[cell2mat(DVSet(RelatedSet)),v]];
            DVSet(RelatedSet) = [];
        end
    end
end