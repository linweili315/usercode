%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% Program to read and interpolate 2D efficiency functions %
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
clear;


%%%%%%%%%%%%%%%%%%%%
% Global constants %
%%%%%%%%%%%%%%%%%%%%
fileName    = '../../efficiency/H2Deff_MisTag_q2Bin';
NbinsX      = 5;
NbinsY      = 5;
NstepsX     = 120;  % [120]
NstepsY     = 120;  % [120]
effMinValue = 2e-5; % [2e-5]
effAtBound  = 1e-5; % [1e-5]


%%%%%%%%%%%%%%%%%%%%
% Global variables %
%%%%%%%%%%%%%%%%%%%%
q2Indx = 0; % q^2 bin index
% - q^2 bin 0-2: spline + linear + contraints
% - q^2 bin 3-8: linear + linear + no contraints
interpMethod  = 'spline';
extrapMethod  = 'linear'; % [linear]
addContraints = true;
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% ==> Interpolation/Extrapolation methods <== %
% linear, nearest, cubic, spline              %
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%


%%%%%%%%%%%%%%%%%%%%%
% Prepare variables %
%%%%%%%%%%%%%%%%%%%%%
if addContraints == true
    deltaBins = 2;
else
    deltaBins = 0;
end

Xvec    = zeros(1,NbinsX);
Yvec    = zeros(1,NbinsY);
origEff = zeros(NbinsY,NbinsX);
Eff     = zeros(NbinsY+deltaBins,NbinsX+deltaBins);


%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% Read efficiency from file %
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
fileIDin = fopen(strcat(fileName,sprintf('_%d.txt',q2Indx)),'r');
formatData = '%f   %f   %f   %f   %f   %f';
i = 1;
j = 1;
fprintf('@@@ Reading 2D binned efficiency from txt file %s @@@\n',fileName);
while i <= NbinsX
    row = textscan(fileIDin,formatData,1);

    Xvec(i) = row{1,1} + row{1,2}/2;
    Yvec(j) = row{1,3} + row{1,4}/2;

    origEff(j,i)                     = row{1,5};
    Eff(j+deltaBins/2,i+deltaBins/2) = row{1,5};

    fprintf('Val=%e at X=%.3f; Y=%.3f\n',origEff(j,i),Xvec(i),Yvec(j));

    j = j + 1;    
    if (j > NbinsY)
        j = 1;
        i = i + 1;
    end
end


%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% Plot original efficiency %
%%%%%%%%%%%%%%%%%%%%%%%%%%%%
figure;
surf(Xvec, Yvec, origEff);
colorbar;
title('Original Efficiency');
xlabel('cos(\theta_K)');
ylabel('cos(\theta_l)');


%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% Check if original efficiency goes negative %
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
isPOS = true;
for i = 1:NbinsX
    for j = 1:NbinsY
        if Eff(j+deltaBins/2,i+deltaBins/2) < 0
            isPOS = false;
            Eff(j+deltaBins/2,i+deltaBins/2) = effMinValue;
        end
    end
end
if isPOS == false
   fprintf('@@@ The efficiency before interpolation is negative --> corrected to %e @@@\n',effMinValue);
else
    fprintf('@@@ The efficiency before interpolation is OK @@@\n');
end


%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% Apply constraints at boundaries %
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
if addContraints == true
    for i = 1:NbinsX+2
        Eff(1,i)        = effAtBound;
        Eff(NbinsY+2,i) = effAtBound;
    end
    
    for j = 1:NbinsY+2
        Eff(j,1)        = effAtBound;
        Eff(j,NbinsX+2) = effAtBound;
    end
    
    actualX = [-1 Xvec 1];
    actualY = [-1 Yvec 1];

    
    %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
    % Compute efficiency at boundaries %
    %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
    EffAtBound = zeros(NbinsY+deltaBins,NbinsX+deltaBins);
    
    XvecAtBound = actualX;
    YvecAtBound = actualY;

    XvecAtBound(2)        = 2*XvecAtBound(2) - XvecAtBound(1);
    XvecAtBound(NbinsX+1) = 2*XvecAtBound(NbinsX+1) - XvecAtBound(NbinsX+2);

    YvecAtBound(2)        = 2*YvecAtBound(2) - YvecAtBound(1);
    YvecAtBound(NbinsX+1) = 2*YvecAtBound(NbinsY+1) - YvecAtBound(NbinsY+2);

    [XvecAtBound_,YvecAtBound_] = meshgrid(XvecAtBound, YvecAtBound);
    XvecAtBound_ = XvecAtBound_';
    YvecAtBound_ = YvecAtBound_';

    %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
    % Set low X bound to nearest values %
    %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
    for i = 1:NbinsX
        EffAtBound(1,i+1) = Eff(1+deltaBins/2,i+deltaBins/2);
    end
    
    %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
    % Set high X bound to nearest values %
    %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
    for i = 1:NbinsX
        EffAtBound(NbinsY+2,i+1) = Eff(NbinsY+deltaBins/2,i+deltaBins/2);
    end
    
    %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
    % Set low Y bound to nearest values %
    %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
    for j = 1:NbinsY
        EffAtBound(j+1,1) = Eff(j+deltaBins/2,1+deltaBins/2);
    end
    
    %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
    % Set high Y bound to nearest values %
    %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
    for j = 1:NbinsY
        EffAtBound(j+1,NbinsX+2) = Eff(j+deltaBins/2,NbinsX+deltaBins/2);
    end
    
    %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
    % Set corners to nearest values %
    %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
    EffAtBound(1,1)               = Eff(1+deltaBins/2,1+deltaBins/2);
    EffAtBound(1,NbinsX+2)        = Eff(1+deltaBins/2,NbinsX+deltaBins/2);
    EffAtBound(NbinsY+2,1)        = Eff(NbinsY+deltaBins/2,1+deltaBins/2);
    EffAtBound(NbinsY+2,NbinsX+2) = Eff(NbinsY+deltaBins/2,NbinsX+deltaBins/2);
    
    EB = griddedInterpolant(XvecAtBound_, YvecAtBound_, EffAtBound', 'nearest', 'nearest');

    %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
    % Plot efficiency at boundaries %
    %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
    figure;
    surf(XvecAtBound_', YvecAtBound_', EB(XvecAtBound_, YvecAtBound_)');
    colorbar;
    title('Efficiency at Boundaries');
    xlabel('cos(\theta_K)');
    ylabel('cos(\theta_l)');

else
    actualX = Xvec;
    actualY = Yvec;
end


%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% Plot efficiency after negative values correction %
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
figure;
surf(actualX, actualY, Eff);
colorbar;
title('Efficiency');
xlabel('cos(\theta_K)');
ylabel('cos(\theta_l)');


%%%%%%%%%%%%%%%%%%%%%%%
% Create interpolants %
%%%%%%%%%%%%%%%%%%%%%%%
[actualX_,actualY_] = meshgrid(actualX, actualY);
actualX_ = actualX_';
actualY_ = actualY_';

E = griddedInterpolant(actualX_, actualY_, Eff', interpMethod, extrapMethod);

[newXvec,newYvec] = meshgrid(linspace(-1,1,NstepsX),linspace(-1,1,NstepsY));
newXvec = newXvec';
newYvec = newYvec';

newEff  = E(newXvec, newYvec);

newXvec = newXvec';
newYvec = newYvec';
newEff  = newEff';


%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% Plot original new efficiency %
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
figure;
surf(newXvec, newYvec, newEff);
colorbar;
title('Original Interpolated Efficiency');
xlabel('cos(\theta_K)');
ylabel('cos(\theta_l)');


if addContraints == true
    %%%%%%%%%%%%%%%%%%%%%%%%%%%
    % Cast boundaries to zero %
    %%%%%%%%%%%%%%%%%%%%%%%%%%%
    for i = 1:length(newXvec)
        for j = 1:length(newYvec)
            if newXvec(j,i) < actualX(1+deltaBins/2) ||...
                    newXvec(j,i) > actualX(NbinsX+deltaBins/2) ||...
                    newYvec(j,i) < actualY(1+deltaBins/2) ||...
                    newYvec(j,i) > actualY(NbinsY+deltaBins/2)
                newEff(j,i) = 0.0;
            end
        end
    end
    
    
    %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
    % Plot original new efficiency with casted bondaries %
    %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
    figure;
    surf(newXvec, newYvec, newEff);
    colorbar;
    title('Original Interpolated Efficiency (casted boundaries)');
    xlabel('cos(\theta_K)');
    ylabel('cos(\theta_l)');
    
    
    %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
    % Combine boundaries and new efficiency %
    %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
    newXvec = newXvec';
    newYvec = newYvec';
    
    newEffAtBound = EB(newXvec, newYvec);
    
    newXvec = newXvec';
    newYvec = newYvec';
    newEffAtBound = newEffAtBound';
    
    
    %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
    % Plot efficiency at boundaries after interpolation %
    %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
    figure;
    surf(newXvec, newYvec, newEffAtBound);
    colorbar;
    title('Efficiency at Boundaries after Interpolation');
    xlabel('cos(\theta_K)');
    ylabel('cos(\theta_l)');

    
    newEff = newEff + newEffAtBound;
end


%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% Check if new efficiency goes negative %
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
isPOS = true;
for i = 1:NstepsX
    for j = 1:NstepsY
        if newEff(j,i) < 0
            isPOS = false;
            newEff(j,i) = effMinValue;
        end
    end
end
if isPOS == false
   fprintf('@@@ The efficiency after interpolation is negative --> corrected to %e @@@\n',effMinValue);
else
    fprintf('@@@ The efficiency after interpolation is OK @@@\n');
end


%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% Plot new efficiency after negative values correction %
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
figure;
surf(newXvec, newYvec, newEff);
colorbar;
title('Final Interpolated Efficiency');
xlabel('cos(\theta_K)');
ylabel('cos(\theta_l)');


%%%%%%%%%%%%%%%%%%%%%%%%%%%
% Save efficiency to file %
%%%%%%%%%%%%%%%%%%%%%%%%%%%
fileIDout = fopen(strcat(fileName,sprintf('_interp_%d.txt',q2Indx)),'w');
i = 1;
j = 1;
fprintf('@@@ Saving 2D binned efficiency to txt file @@@\n');
while i <= NstepsX-1
    formatData = sprintf(' ');
    formatData = strcat(formatData,sprintf('%f   %f',newXvec(j,i),newXvec(j,i+1) - newXvec(j,i)));
    formatData = strcat(formatData,sprintf('   %f   %f',newYvec(j,i),newYvec(j+1,i) - newYvec(j,i)));
    formatData = strcat(formatData,sprintf('   %f   %f',newEff(j,i),0));

    fprintf(fileIDout,'%s\n',formatData);
    
    j = j + 1;    
    if (j > NstepsY-1)
        j = 1;
        i = i + 1;
    end
    
    clear newRow;
end


fprintf('@@@ I''ve generated interpolated efficiency @@@\n');
fclose(fileIDout);
fclose(fileIDin);