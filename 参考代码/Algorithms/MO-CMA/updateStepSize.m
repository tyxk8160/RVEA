function a = updateStepSize(a,psucc,ptarget)
% Update the step size of CMA model based on the success rate

%--------------------------------------------------------------------------
% Copyright (c) 2016-2017 BIMK Group
% You are free to use the PlatEMO for research purposes. All publications
% which use this platform or any code in the platform should acknowledge
% the use of "PlatEMO" and reference "Ye Tian, Ran Cheng, Xingyi Zhang, and
% Yaochu Jin, PlatEMO: A MATLAB Platform for Evolutionary Multi-Objective
% Optimization, IEEE Computational Intelligence Magazine, 2017, in press".
%--------------------------------------------------------------------------

    % Success rate averaging parameter
    cp = ptarget/(2+ptarget);
    % Step size damping
    d = 1 + length(a.x)/2;
    % Update the averaged success rate
    a.psucc = (1-cp)*a.psucc + cp*psucc;
    % Update the global step size
    a.sigma = a.sigma*exp((a.psucc-ptarget)/d/(1-ptarget));
end