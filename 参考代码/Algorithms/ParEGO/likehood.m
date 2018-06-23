function phi = likehood(PDec,PCheby,theta,F) 
% The likehood calculation according to given theta values.

%--------------------------------------------------------------------------
% Copyright (c) 2016-2017 BIMK Group
% You are free to use the PlatEMO for research purposes. All publications
% which use this platform or any code in the platform should acknowledge
% the use of "PlatEMO" and reference "Ye Tian, Ran Cheng, Xingyi Zhang, and
% Yaochu Jin, PlatEMO: A MATLAB Platform for Evolutionary Multi-Objective
% Optimization, IEEE Computational Intelligence Magazine, 2017, in press".
%--------------------------------------------------------------------------

% This function is written by Cheng He

    N = size(PDec,1);
    R = zeros(N);
    for i = 1 : N
        for j = 1 : N
            R(i,j) = exp(-sum(theta.*(PDec(i,:)-PDec(j,:)).^2));
        end
    end
    bt     = (F'/R*F)\F'/R*PCheby;
    sigma2 = 1/N.*(PCheby-F*bt)'/R*(PCheby-F*bt);
    phi    = N.*log(sigma2)+log(det(R));
end