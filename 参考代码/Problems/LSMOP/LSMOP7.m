function varargout = LSMOP7(Operation,Global,input)
% <problem> <LSMOP>
% Test Problems for Large-Scale Multiobjective and Many-Objective
% Optimization
% nk --- 5 --- Number of subcomponents in each variable group
% operator --- EAreal

%--------------------------------------------------------------------------
% Copyright (c) 2016-2017 BIMK Group
% You are free to use the PlatEMO for research purposes. All publications
% which use this platform or any code in the platform should acknowledge
% the use of "PlatEMO" and reference "Ye Tian, Ran Cheng, Xingyi Zhang, and
% Yaochu Jin, PlatEMO: A MATLAB Platform for Evolutionary Multi-Objective
% Optimization, IEEE Computational Intelligence Magazine, 2017, in press".
%--------------------------------------------------------------------------

persistent sublen len;

    nk = Global.ParameterSet(5);
    switch Operation
        case 'init'
            if isempty(Global.lower)
                Global.M = 3;
                Global.D = 100*Global.M;
                c = 3.8*0.1*(1-0.1);
                for i = 1 : Global.M-1
                    c = [c,3.8.*c(end).*(1-c(end))];
                end
                sublen = ceil(round(c./sum(c).*Global.D)/nk);
                len    = [0,cumsum(sublen*nk)];
                Global.D        = Global.M - 1 + len(end);
                Global.lower    = zeros(1,Global.D);
                Global.upper    = [ones(1,Global.M-1),10.*ones(1,len(end))];
                Global.operator = @EAreal;
            end            

            PopDec    = rand(input,Global.D).*repmat(Global.upper-Global.lower,input,1) + repmat(Global.lower,input,1);
            varargout = {PopDec};
        case 'value'
            PopDec = input;
            [N,D]  = size(PopDec);
            M      = Global.M;
            
            PopDec(:,M:D) = (1+repmat(cos((M:D)./D*pi/2),N,1)).*PopDec(:,M:D) - repmat(PopDec(:,1)*10,1,D-M+1);
            G = zeros(N,M);
            for i = 1 : 2 : M
                for j = 1 : nk
                    G(:,i) = G(:,i) + Ackley(PopDec(:,len(i)+M-1+(j-1)*sublen(i)+1:len(i)+M-1+j*sublen(i)));
                end
            end
            for i = 2 : 2 : M
                for j = 1 : nk
                    G(:,i) = G(:,i) + Rosenbrock(PopDec(:,len(i)+M-1+(j-1)*sublen(i)+1:len(i)+M-1+j*sublen(i)));
                end
            end
            G      = G./repmat(sublen,N,1)./nk;
            PopObj = (1+G+[G(:,2:end),zeros(N,1)]).*fliplr(cumprod([ones(N,1),cos(PopDec(:,1:M-1)*pi/2)],2)).*[ones(N,1),sin(PopDec(:,M-1:-1:1)*pi/2)];
            
            PopCon = [];
            
            varargout = {input,PopObj,PopCon};
        case 'PF'
            f = UniformPoint(input,Global.M);
            f = f./repmat(sqrt(sum(f.^2,2)),1,Global.M);
            varargout = {f};
    end
end

function f = Ackley(x)
    f = 20-20.*exp(-0.2.*sqrt(sum(x.^2,2)./size(x,2)))-exp(sum(cos(2.*pi.*x),2)./size(x,2))+exp(1);
end

function f = Rosenbrock(x)
    f = sum(100.*(x(:,1:size(x,2)-1).^2-x(:,2:size(x,2))).^2+(x(:,1:size(x,2)-1)-1).^2,2);
end