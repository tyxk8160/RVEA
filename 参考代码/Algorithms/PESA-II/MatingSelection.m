function MatingPool = MatingSelection(PopObj,N,div)
% The mating selection of PESA-II

%--------------------------------------------------------------------------
% Copyright (c) 2016-2017 BIMK Group
% You are free to use the PlatEMO for research purposes. All publications
% which use this platform or any code in the platform should acknowledge
% the use of "PlatEMO" and reference "Ye Tian, Ran Cheng, Xingyi Zhang, and
% Yaochu Jin, PlatEMO: A MATLAB Platform for Evolutionary Multi-Objective
% Optimization, IEEE Computational Intelligence Magazine, 2017, in press".
%--------------------------------------------------------------------------
    
    %% Calculte the grid location of each solution
    fmax = max(PopObj,[],1);
    fmin = min(PopObj,[],1);
    d    = (fmax-fmin)/div;
    GLoc = floor((PopObj-repmat(fmin,size(PopObj,1),1))./repmat(d,size(PopObj,1),1));
    GLoc(GLoc>=div)   = div - 1;
    GLoc(isnan(GLoc)) = 0;
    
    %% Calculate the crowding degree of each grid
    [UniqueGLoc,~,Site] = unique(GLoc,'rows');
    CrowdG              = hist(Site,1:max(Site));
    
    %% Binary tournament selection
    MatingPool = zeros(1,N);
    for i = 1 : length(MatingPool)
        grid          = randi(size(UniqueGLoc,1),1,2);
        [~,best]      = min(CrowdG(grid));
        current       = find(Site==grid(best));
        MatingPool(i) = current(randi(length(current)));
    end
end