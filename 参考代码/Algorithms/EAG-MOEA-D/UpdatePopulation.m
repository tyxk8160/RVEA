function Population = UpdatePopulation(Population,Offspring,offspringLoc,W,B)
% Update the population by MOEA/D

%--------------------------------------------------------------------------
% Copyright (c) 2016-2017 BIMK Group
% You are free to use the PlatEMO for research purposes. All publications
% which use this platform or any code in the platform should acknowledge
% the use of "PlatEMO" and reference "Ye Tian, Ran Cheng, Xingyi Zhang, and
% Yaochu Jin, PlatEMO: A MATLAB Platform for Evolutionary Multi-Objective
% Optimization, IEEE Computational Intelligence Magazine, 2017, in press".
%--------------------------------------------------------------------------

    for i = 1 : length(Offspring)
        % Update the parents by weight sum approach
        g_old = sum(Population(B(offspringLoc(i),:)).objs.*W(B(offspringLoc(i),:),:),2);
        g_new = W(B(offspringLoc(i),:),:)*Offspring(i).obj';
        Population(B(offspringLoc(i),g_old>=g_new)) = Offspring(i);
    end
end