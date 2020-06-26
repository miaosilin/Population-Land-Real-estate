% main program
% population-land-real estate
% Author? Kong Qingshan, Miao Silin, Kong Haiyang
% Date: 2020.06

% Initialize the result (using the cell structure, the same size as the output, each element corresponds to a grid in Excel)
output = cell(num_of_cities+1,7);
% Establish a header·
title = {'city','Coupling Degree','Coordination Degree','Coupling Coordination Degree','Population Evaluation Index','Land Evaluation Index','Real estate Evaluation Index'};
% set up a data
name(:,1) = txt(2:num_of_cities+1,1); %Get city name 
name(:,1) = strtrim(name(:,1))

C=roundn(Ci',-3)  
T=roundn(Ti',-3) 
D=roundn(Di',-3) %Transpose the result and retain three decimal places
POP=roundn(pop',-3)
LAND=roundn(land',-3)
ESTATE=roundn(estate',-3)

% formatting: Ordinary arrays are converted to the cell format of the same size using the following function
C = num2cell(C);
T = num2cell(T);
D = num2cell(D);
POP = num2cell(POP);
LAND = num2cell(LAND);
ESTATE = num2cell(ESTATE);
% integration
output(1,:)=title;
output(2:end,1)=name;
output(2:end,2)=C;
output(2:end,3)=T;
output(2:end,4)=D;
output(2:end,5)=POP;
output(2:end,6)=LAND;
output(2:end,7)=ESTATE;%output

xlswrite('output2017.xlsx',output);

