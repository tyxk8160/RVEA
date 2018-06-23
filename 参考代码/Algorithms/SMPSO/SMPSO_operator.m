function NewParticles = SMPSO_operator(Global,Particles)
% <operator> <real>
% Particle swarm optimization in SMPSO

%--------------------------------------------------------------------------
% Copyright (c) 2016-2017 BIMK Group
% You are free to use the PlatEMO for research purposes. All publications
% which use this platform or any code in the platform should acknowledge
% the use of "PlatEMO" and reference "Ye Tian, Ran Cheng, Xingyi Zhang, and
% Yaochu Jin, PlatEMO: A MATLAB Platform for Evolutionary Multi-Objective
% Optimization, IEEE Computational Intelligence Magazine, 2017, in press".
%--------------------------------------------------------------------------

    Particles      = Particles([1:end,1:ceil(end/3)*3-end]);
    ParticlesDec   = Particles.decs;
    [N,D]          = size(ParticlesDec);
    ParticlesSpeed = Particles.adds(zeros(N,D));

    %% PSO
    ParticleDec   = ParticlesDec(1:N/3,:);
    ParticleSpeed = ParticlesSpeed(1:N/3,:);
    PBestDec      = ParticlesDec(N/3+1:N/3*2,:);
    GBestDec      = ParticlesDec(N/3*2+1:end,:);
    W  = repmat(rand(N/3,1)*0.4+0.1,1,D);
    r1 = repmat(rand(N/3,1),1,D);
    r2 = repmat(rand(N/3,1),1,D);
    C1 = repmat(rand(N/3,1)+1.5,1,D);
    C2 = repmat(rand(N/3,1)+1.5,1,D);
    NewSpeed = W.*ParticleSpeed + C1.*r1.*(PBestDec-ParticleDec) + C2.*r2.*(GBestDec-ParticleDec);
    phi      = max(4,C1+C2);
    NewSpeed = NewSpeed.*2./abs(2-phi-sqrt(phi.^2-4*phi));
    delta    = repmat((Global.upper-Global.lower)/2,N/3,1);
    NewSpeed = max(min(NewSpeed,delta),-delta);
    NewDec   = ParticleDec + NewSpeed;
    
    %% Deterministic back
    Lower  = repmat(Global.lower,N/3,1);
    Upper  = repmat(Global.upper,N/3,1);
    repair = NewDec < Lower | NewDec > Upper;
    NewSpeed(repair) = 0.001*NewSpeed(repair);
    
    %% Polynomial mutation
    disM  = 20;
    Site1 = repmat(rand(N/3,1)<0.15,1,D);
    Site2 = rand(N/3,D) < 1/D;
    mu    = rand(N/3,D);
    temp  = Site1 & Site2 & mu<=0.5;
    NewDec(temp) = NewDec(temp)+(Upper(temp)-Lower(temp)).*((2.*mu(temp)+(1-2.*mu(temp)).*...
                   (1-(NewDec(temp)-Lower(temp))./(Upper(temp)-Lower(temp))).^(disM+1)).^(1/(disM+1))-1);
    temp  = Site1 & Site2 & mu>0.5; 
    NewDec(temp) = NewDec(temp)+(Upper(temp)-Lower(temp)).*(1-(2.*(1-mu(temp))+2.*(mu(temp)-0.5).*...
                   (1-(Upper(temp)-NewDec(temp))./(Upper(temp)-Lower(temp))).^(disM+1)).^(1/(disM+1)));

    NewParticles = INDIVIDUAL(NewDec,NewSpeed);
end