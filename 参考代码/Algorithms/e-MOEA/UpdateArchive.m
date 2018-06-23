function Archive = UpdateArchive(Archive,Offspring,epsilon)
% Update the archive

%--------------------------------------------------------------------------
% Copyright (c) 2016-2017 BIMK Group
% You are free to use the PlatEMO for research purposes. All publications
% which use this platform or any code in the platform should acknowledge
% the use of "PlatEMO" and reference "Ye Tian, Ran Cheng, Xingyi Zhang, and
% Yaochu Jin, PlatEMO: A MATLAB Platform for Evolutionary Multi-Objective
% Optimization, IEEE Computational Intelligence Magazine, 2017, in press".
%--------------------------------------------------------------------------

    N = length(Archive);

    %% Calculate the grid location of each solution
    ArchiveObj  = Archive.objs;
    ChildGrid   = floor((Offspring.obj-min(ArchiveObj,[],1))/epsilon);
    ArchiveGrid = floor((ArchiveObj-repmat(min(ArchiveObj,[],1),N,1))/epsilon);
    
    %% Insert the offspring into the archive by epsilon-dominance and grid locations
    if ~any(all(ArchiveGrid<=repmat(ChildGrid,N,1),2))
        Dominate = find(all(repmat(ChildGrid,N,1)<=ArchiveGrid,2));
        if ~isempty(Dominate)
            Archive(Dominate) = [];
            Archive = [Archive,Offspring];
        else
            SameGrid = find(ismember(ArchiveGrid,ChildGrid,'rows'),1);
            if isempty(SameGrid)
                Archive = [Archive,Offspring];
            else
                B = ChildGrid*epsilon+min(ArchiveObj,[],1);
                if norm(Offspring.obj-B) < norm(ArchiveObj(SameGrid,:)-B)
                    Archive(SameGrid) = Offspring;
                end
            end
        end
    end
end