function varargout = CF5(Operation,Global,input)
% <problem> <CF>
% Multiobjective optimization Test Instances for the CEC 2009 Special
% Session and Competition
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
            Global.lower    = [0,zeros(1,Global.D-1)-2];
            Global.upper    = [1,zeros(1,Global.D-1)+2];
            Global.operator = @EAreal;
            
            PopDec    = rand(input,Global.D).*repmat(Global.upper-Global.lower,input,1) + repmat(Global.lower,input,1);
            varargout = {PopDec};
        case 'value'
            X = input;
            D = size(X,2);
            
            J1 = 3:2:D;
            J2 = 2:2:D;
            Y       = zeros(size(X));
            Y(:,J1) = X(:,J1)-0.8*repmat(X(:,1),1,length(J1)).*cos(6*pi*repmat(X(:,1),1,length(J1))+repmat(J1,size(X,1),1)*pi/D);
            Y(:,J2) = X(:,J2)-0.8*repmat(X(:,1),1,length(J2)).*sin(6*pi*repmat(X(:,1),1,length(J2))+repmat(J2,size(X,1),1)*pi/D);
            h          = 2*Y.^2-cos(4*pi*Y)+1;
            temp       = Y(:,2)<3/2*(1-sqrt(1/2));
            h(temp,2)  = abs(Y(temp,2));
            h(~temp,2) = 0.125+(Y(~temp,2)-1).^2;
            PopObj(:,1) = X(:,1)   + sum(h(:,J1),2);
            PopObj(:,2) = 1-X(:,1) + sum(h(:,J2),2);
            
            PopCon = -X(:,2)+0.8*X(:,1).*sin(6*pi*X(:,1)+2*pi/D)+0.5*X(:,1)-0.25;
            
            varargout = {input,PopObj,PopCon};
        case 'PF'
            f(:,1) = (0:1/(input-1):1)';
            f(:,2) = 1-f(:,1);
            temp1  = 0.5<f(:,1) & f(:,1)<=0.75;
            temp2  = 0.75<f(:,1);
            f(temp1,2) = -0.5*f(temp1,1)+3/4;
            f(temp2,2) = 1-f(temp2,1)+0.125;
            varargout  = {f};
    end
end