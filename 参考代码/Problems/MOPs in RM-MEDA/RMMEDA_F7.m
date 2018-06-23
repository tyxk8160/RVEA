function varargout = RMMEDA_F7(Operation,Global,input)
% <problem> <RMMEDA>
% RM-MEDA: A Regularity Model-Based Multiobjective Estimation of
% Distribution Algorithm
% operator --- EAreal

%--------------------------------------------------------------------------
% Copyright (c) 2016-2017 BIMK Group
% You are free to use the PlatEMO for research purposes. All publications
% which use this platform or any code in the platform should acknowledge
% the use of "PlatEMO" and reference "Ye Tian, Ran Cheng, Xingyi Zhang, and
% Yaochu Jin, PlatEMO: A MATLAB Platform for Evolutionary Multi-Objective
% Optimization, IEEE Computational Intelligence Magazine, 2017, in press".
%--------------------------------------------------------------------------

    switch Operation
        case 'init'
            Global.M        = 2;
            Global.M        = 2;
            Global.D        = 30;
            Global.lower    = zeros(1,Global.D);
            Global.upper    = ones(1,Global.D);
            Global.operator = @EAreal;
            
            PopDec    = rand(input,Global.D);
            varargout = {PopDec};
        case 'value'
            X = input;
            D = size(X,2);
            
            g = 1 + 9*(sum((X(:,2:end).^2-repmat(X(:,1),1,D-1)).^2,2)/9).^0.25;
            PopObj(:,1) = 1 - exp(-4*X(:,1)).*sin(6*pi*X(:,1)).^6;
            PopObj(:,2) = g.*(1-(PopObj(:,1)./g).^2);
            
            PopCon = [];
            
            varargout = {input,PopObj,PopCon};
        case 'PF'
            minf1     = min(1-exp(-4*(0:1e-6:1)).*(sin(6*pi*(0:1e-6:1))).^6);
            f(:,1)    = (minf1:(1-minf1)/(input-1):1)';
            f(:,2)    = 1-f(:,1).^2;
            varargout = {f};
    end
end