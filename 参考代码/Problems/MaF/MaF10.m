function varargout = MaF10(Operation,Global,input)
% <problem> <MaF>
% Benchmark Functions for CEC 2017 Competition on Many-Objective
% Optimization
% operator --- EAreal

%--------------------------------------------------------------------------
% Copyright (c) 2016-2017 BIMK Group
% You are free to use the PlatEMO for research purposes. All publications
% which use this platform or any code in the platform should acknowledge
% the use of "PlatEMO" and reference "Ye Tian, Ran Cheng, Xingyi Zhang, and
% Yaochu Jin, PlatEMO: A MATLAB Platform for Evolutionary Multi-Objective
% Optimization, IEEE Computational Intelligence Magazine, 2017, in press".
%--------------------------------------------------------------------------

    % This problem is WFG1 with K=M-1
    K = Global.M - 1;
    switch Operation
        case 'init'
            Global.M          = 3;
            Global.D          = Global.M + 9;
            Global.lower      = zeros(1,Global.D);
            Global.upper      = 2 : 2 : 2*Global.D;
            Global.operator   = @EAreal;
            Global.evaluation = max(1e5,1e4*Global.D);
            
            PopDec    = rand(input,Global.D).*repmat(2:2:2*Global.D,input,1);
            varargout = {PopDec};
        case 'value'
            PopDec = input;
            [N,D]  = size(PopDec);
            M      = Global.M;
            
            L = D - K;
            D = 1;
            S = 2 : 2 : 2*M;
            A = ones(1,M-1);

            z01 = PopDec./repmat(2:2:size(PopDec,2)*2,N,1);

            t1 = zeros(N,K+L);
            t1(:,1:K)     = z01(:,1:K);
            t1(:,K+1:end) = s_linear(z01(:,K+1:end),0.35);

            t2 = zeros(N,K+L);
            t2(:,1:K)     = t1(:,1:K);
            t2(:,K+1:end) = b_flat(t1(:,K+1:end),0.8,0.75,0.85);

            t3 = zeros(N,K+L);
            t3 = b_poly(t2,0.02);

            t4 = zeros(N,M);
            for i = 1 : M-1
                t4(:,i) = r_sum(t3(:,(i-1)*K/(M-1)+1:i*K/(M-1)),2*((i-1)*K/(M-1)+1):2:2*i*K/(M-1));
            end
            t4(:,M) = r_sum(t3(:,K+1:K+L),2*(K+1):2:2*(K+L));

            x = zeros(N,M);
            for i = 1 : M-1
                x(:,i) = max(t4(:,M),A(i)).*(t4(:,i)-0.5)+0.5;
            end
            x(:,M) = t4(:,M);

            h      = convex(x);
            h(:,M) = mixed(x);
            PopObj = repmat(D*x(:,M),1,M) + repmat(S,N,1).*h;
            
            PopCon = [];
            
            varargout = {input,PopObj,PopCon};
        case 'PF'
            M = Global.M;
            h = UniformPoint(input,M);
            for i = 1 : size(h,1)
                c = ones(1,M);
                k = find(h(i,:)~=0,1);
                for j = k+1 : M
                    temp     = h(i,j)/h(i,k)*prod(1-c(M-j+2:M-k));
                    c(M-j+1) = (temp^2-temp+sqrt(2*temp))/(temp^2+1);
                end
                for j = 1 : M
                    h(i,j) = prod(1-c(1:M-j)).*(1-sqrt(1-c(M-j+1)^2));
                end
                temp   = acos(c(1))*2/pi;                   
                h(i,M) = 1 - temp - cos(10*pi*temp+pi/2)/10/pi;
            end
            h = repmat(2:2:2*M,size(h,1),1).*h;
            varargout = {h};
    end
end

function Output = s_linear(y,A)
    Output = abs(y-A)./abs(floor(A-y)+A);
end

function Output = b_flat(y,A,B,C)
    Output = A+min(0,floor(y-B))*A.*(B-y)/B-min(0,floor(C-y))*(1-A).*(y-C)/(1-C);
    Output = roundn(Output,-6);
end

function Output = b_poly(y,a)
    Output = y.^a;
end

function Output = r_sum(y,w)
    Output = sum(y.*repmat(w,size(y,1),1),2)./sum(w);
end

function Output = convex(x)
    Output = fliplr(cumprod([ones(size(x,1),1),1-cos(x(:,1:end-1)*pi/2)],2)).*[ones(size(x,1),1),1-sin(x(:,end-1:-1:1)*pi/2)];
end

function Output = mixed(x)
    Output = 1-x(:,1)-cos(10*pi*x(:,1)+pi/2)/10/pi;
end