function NewParticles = NMPSO_operator(Global,Particles)
% <operator> <real>
% Particle swarm optimization in NMPSO

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
    r3 = repmat(rand(N/3,1),1,D);
    C1 = repmat(rand(N/3,1)+1.5,1,D);
    C2 = repmat(rand(N/3,1)+1.5,1,D);
    C3 = repmat(rand(N/3,1)+1.5,1,D);
    NewSpeed = W.*ParticleSpeed + C1.*r1.*(PBestDec-ParticleDec) + C2.*r2.*(GBestDec-ParticleDec) + C3.*r3.*(GBestDec-PBestDec);
    NewDec   = ParticleDec + NewSpeed;

    NewParticles = INDIVIDUAL(NewDec,NewSpeed);
end