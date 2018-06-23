function varargout = ZDT6(Operation,Global,input)
% <problem> <ZDT>
% Comparison of Multiobjective Evolutionary Algorithms: Empirical Results
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
            Global.D        = 10;
            Global.lower    = zeros(1,Global.D);
            Global.upper    = ones(1,Global.D);
            Global.operator = @EAreal;
            
            PopDec    = rand(input,Global.D);
            varargout = {PopDec};
        case 'value'
            PopDec = input;
            
            PopObj(:,1) = 1-exp(-4*PopDec(:,1)).*sin(6*pi*PopDec(:,1)).^6;
            g = 1+9*sum(PopDec(:,2:end),2).^0.25;
            h = 1-(PopObj(:,1)./g).^2;
            PopObj(:,2) = g.*h;
            
            PopCon = [];
            
            varargout = {input,PopObj,PopCon};
        case 'PF'
            minf1     = 0.280775;
            f(:,1)    = (minf1:(1-minf1)/(input-1):1)';
            f(:,2)    = 1-f(:,1).^2;
            varargout = {f};
    end
end