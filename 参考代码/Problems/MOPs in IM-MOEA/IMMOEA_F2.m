function varargout = IMMOEA_F2(Operation,Global,input)
% <problem> <IMMOEA>
% A Multiobjective Evolutionary Algorithm using Gaussian Process based
% Inverse Modeling
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
            
            t = (1+5*repmat(2:D,size(X,1),1)/D).*X(:,2:D) - repmat(X(:,1),1,D-1);
            g = 1 + 9*mean(t.^2,2);
            PopObj(:,1) = X(:,1);
            PopObj(:,2) = g.*(1-(PopObj(:,1)./g).^2);
            
            PopCon = [];
            
            varargout = {input,PopObj,PopCon};
        case 'PF'
            f(:,1)    = (0:1/(input-1):1)';
            f(:,2)    = 1 - f(:,1).^2;
            varargout = {f};
    end
end