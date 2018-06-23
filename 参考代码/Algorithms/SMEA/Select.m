function [Population,FrontNo] = Select(Population,FrontNo,y)
% And one offspring to the population and delete the worst one

%--------------------------------------------------------------------------
% Copyright (c) 2016-2017 BIMK Group
% You are free to use the PlatEMO for research purposes. All publications
% which use this platform or any code in the platform should acknowledge
% the use of "PlatEMO" and reference "Ye Tian, Ran Cheng, Xingyi Zhang, and
% Yaochu Jin, PlatEMO: A MATLAB Platform for Evolutionary Multi-Objective
% Optimization, IEEE Computational Intelligence Magazine, 2017, in press".
%--------------------------------------------------------------------------

    %% Identify the solutions in the last front
    Population = [Population,y];
    PopObj     = Population.objs;
    [N,M]      = size(PopObj);
    FrontNo    = UpdateFront(PopObj,FrontNo);
    
    %% Delete the worst solution
    if max(FrontNo) > 1
        Distance  = pdist2(PopObj,PopObj);
        Distance(logical(eye(N))) = inf;
        LastFront = find(FrontNo==max(FrontNo));
        [~,worst] = min(min(Distance(LastFront,:),[],2));
        worst     = LastFront(worst);
    else
        deltaS = inf(1,N);
        if M == 2
            [~,rank] = sortrows(PopObj);
            for i = 2 : N-1
                deltaS(rank(i)) = (PopObj(rank(i+1),1)-PopObj(rank(i),1)).*(PopObj(rank(i-1),2)-PopObj(rank(i),2));
            end
        elseif N > 1
            deltaS = CalHV(PopObj,max(PopObj,[],1)*1.1,1,10000);
        end
        [~,worst] = min(deltaS);
    end
    FrontNo = UpdateFront(PopObj,FrontNo,worst);
    Population(worst) = [];
end