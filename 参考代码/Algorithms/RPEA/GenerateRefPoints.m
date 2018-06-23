function R = GenerateRefPoints(Q,diff,alpha,N)
% Generate the reference points according to the combined population

%--------------------------------------------------------------------------
% Copyright (c) 2016-2017 BIMK Group
% You are free to use the PlatEMO for research purposes. All publications
% which use this platform or any code in the platform should acknowledge
% the use of "PlatEMO" and reference "Ye Tian, Ran Cheng, Xingyi Zhang, and
% Yaochu Jin, PlatEMO: A MATLAB Platform for Evolutionary Multi-Objective
% Optimization, IEEE Computational Intelligence Magazine, 2017, in press".
%--------------------------------------------------------------------------

    Q    = Q(NDSort(Q.objs,1)==1);
    R    = [];
    subN = min(length(Q),ceil(alpha*N));
    CrowdDis = CrowdingDistanceInEachObj(Q.objs);
    [~,rank] = sort(CrowdDis,'descend');
    for m = 1 : length(Q(1).obj)
        Rm      = Q(rank(1:subN,m)).objs;
        Rm(:,m) = Rm(:,m) - diff(m);
        R       = [R;Rm];
    end
    R = R(NDSort(R,1)==1,:);
    if size(R,1) > N
        CrowdDis = CrowdingDistanceInEachObj(R);
        [~,rank] = sort(sum(CrowdDis,2),'descend');
        R        = R(rank(1:N),:);
    end
end

function CrowdDis = CrowdingDistanceInEachObj(PopObj)
% Calculate the crowding distance of each solution in each objective

    [N,M]    = size(PopObj);
    
    CrowdDis = zeros(N,M);
    Fmax     = max(PopObj,[],1);
    Fmin     = min(PopObj,[],1);
    for i = 1 : M
        [~,rank] = sortrows(PopObj(:,i));
        CrowdDis(rank(1),i)   = inf;
        CrowdDis(rank(end),i) = inf;
        for j = 2 : N-1
            CrowdDis(rank(j),i) = (PopObj(rank(j+1),i)-PopObj(rank(j-1),i))/(Fmax(i)-Fmin(i));
        end
    end
end