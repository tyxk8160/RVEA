function varargout = CDTLZ2(Operation,Global,input)
% <problem> <DTLZ special>
% An Evolutionary Many-Objective Optimization Algorithm Using
% Reference-point Based Non-dominated Sorting Approach, Part I: Solving
% Problems with Box Constraints
% operator --- EAreal

%--------------------------------------------------------------------------
% Copyright (c) 2016-2017 BIMK Group
% You are free to use the PlatEMO for research purposes. All publications
% which use this platform or any code in the platform should acknowledge
% the use of "PlatEMO" and reference "Ye Tian, Ran Cheng, Xingyi Zhang, and
% Yaochu Jin, PlatEMO: A MATLAB Platform for Evolutionary Multi-Objective
% Optimization, IEEE Computational Intelligence Magazine, 2017, in press".
%--------------------------------------------------------------------------

    % This problem is convex DTLZ2
    switch Operation
        case 'init'
            Global.M        = 3;
            Global.D        = Global.M + 9;
            Global.lower    = zeros(1,Global.D);
            Global.upper    = ones(1,Global.D);
            Global.operator = @EAreal;
            
            PopDec    = rand(input,Global.D);
            varargout = {PopDec};
        case 'value'
            PopDec = input;
            M      = Global.M;

            g      = sum((PopDec(:,M:end)-0.5).^2,2);
            PopObj = repmat(1+g,1,M).*fliplr(cumprod([ones(size(g,1),1),cos(PopDec(:,1:M-1)*pi/2)],2)).*[ones(size(g,1),1),sin(PopDec(:,M-1:-1:1)*pi/2)];
            PopObj = [PopObj(:,1:M-1).^4,PopObj(:,M).^2];
            
            PopCon = [];
            
            varargout = {input,PopObj,PopCon};
        case 'PF'
            f    = UniformPoint(input,Global.M).^2;
            temp = sum(sqrt(f(:,1:end-1)),2) + f(:,end);
            f    = f./[repmat(temp.^2,1,size(f,2)-1),temp];
            varargout = {f};
    end
end