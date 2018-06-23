function Weight = UpdateWeight(Weight,PopObj,K)
% Update the weight vectors in MSOPS-II

%--------------------------------------------------------------------------
% Copyright (c) 2016-2017 BIMK Group
% You are free to use the PlatEMO for research purposes. All publications
% which use this platform or any code in the platform should acknowledge
% the use of "PlatEMO" and reference "Ye Tian, Ran Cheng, Xingyi Zhang, and
% Yaochu Jin, PlatEMO: A MATLAB Platform for Evolutionary Multi-Objective
% Optimization, IEEE Computational Intelligence Magazine, 2017, in press".
%--------------------------------------------------------------------------

    %% Normalization
    W = [Weight;PopObj];
    [N,M] = size(W);
    W = W - repmat(min(W,[],1),N,1);
    W = W./repmat(sqrt(sum(W.^2,2)),1,M);
    
    %% Combine weight vectors with the population
    Weight = [Weight;PopObj];
    WIndex = 1 : N;
    % The cosine between each two vectors
    Cosine = 1 - pdist2(W,W,'cosine');
    Cosine(logical(eye(length(Cosine)))) = 0;
    % Reduce the number of vectors
    while length(WIndex) > K
        [~,rank] = sortrows(sort(-Cosine(WIndex,WIndex),2));
        WIndex(rank(1)) = [];
    end
    Weight = Weight(WIndex,:);
end