function varargout = C2_DTLZ2(Operation,Global,input)
% <problem> <DTLZ special>
% An Evolutionary Many-Objective Optimization Algorithm Using
% Reference-Point Based Nondominated Sorting Approach, Part II: Handling
% Constraints and Extending to an Adaptive Approach
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
            
            if M == 3; r = 0.4; else r = 0.5; end
            PopCon = min(min((PopObj-1).^2+repmat(sum(PopObj.^2,2),1,M)-PopObj.^2-r^2,[],2),sum((PopObj-1/sqrt(M)).^2,2)-r^2);
            
            varargout = {input,PopObj,PopCon};
        case 'PF'
            M = Global.M;
            f = UniformPoint(input,M);
            f = f./repmat(sqrt(sum(f.^2,2)),1,M);
            if M == 3; r = 0.4; else r = 0.5; end
            f(min(min((f-1).^2+repmat(sum(f.^2,2),1,M)-f.^2-r^2,[],2),sum((f-1/sqrt(M)).^2,2)-r^2)>0,:) = [];
            varargout = {f};
    end
end