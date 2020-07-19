% main program
% population-land-real estate
% Author? Kong Qingshan, Miao Silin, Kong Haiyang
% Date: 2020.06

clear all; clc

    [data,txt]=xlsread('data_2017.xlsx') %input data
    [num_of_cities,num_of_indicators]=size(data)%set the number of cities and indicators
    ind= ones(1,num_of_indicators)%generate an array to determine the symbol of indicators
    ind(2)= 1 %set the symbol of each indicators: positive or negative
    

    [normalization,entropy,d,lambda]=entropy(data,ind)%Entropy weight method is used to calculate the weight

     s1 = 9 %count the number of indicators in system 1
     s2 = 10 %count the number of indicators in system 2
     s3 = 7  %count the number of indicators in system 3
     A  = [14 29 11 26 18 25 9 8 9 15 10]
     A1= [1 12 40 51 76 91 116 125 133 142 157]


     %calculation
    for i=1:num_of_cities
        pop(i)=[sum(normalization(i,1:s1).* lambda(1,1:s1))]%population evaluation index
        land(i)=[sum(normalization(i,s1+1:s1+s2).* lambda(1,s1+1:s1+s2))]%land evaluation index
        estate(i)=[sum(normalization(i,s1+s2+1:s1+s2+s3).* lambda(1,s1+s2+1:s1+s2+s3))]%real estate evaluation index
        Ci(i)=(pop(i)*land(i)*estate(i)/((pop(i)+land(i)+estate(i))/3)^3)^(1/3)%coupling degree
        Ti(i)=sqrt((pop(i)^2+land(i)^2+ estate(i)^2))/sqrt(3) %coordination degree
        %Ti(i)=(pop(i)^2+land(i)^2+ estate(i)^2)/(pop(i)+land(i)+ estate(i)) %coordination degree
        Di(i)=(Ci(i)*Ti(i))^(1/2)%coupling and coordination degree
    end

    %output as excel
    outputexcel

    % generate figure1
    figure1

    %Relative entropy 
   % for i = 1:11       
   %     Sum(i)= sum(Di(A1(i):A(i)+A1(i)-1))
    %end

   % mid=zeros(1,11)
    %for i = 1:11
   %     for j = A1(i):A(i)+A1(i)-1
    %        mid(i)= mid(i) +(Di(j)/Sum(i))*log((Di(j)/Sum(i)))
    %    end
    %     Dr(i)=-(1/log(A(i)))*mid(i)
   % end

   % CityAgglomeration(:,1)={'Beijing-Tianjin-Hebei Urban Agglomeration','Central Plains Urban Agglomeration' ...
   %     ,'Guanzhong plain city group','Yangtze River Delta Urban Agglomerations',' Urban Agglomeration on the West Side of the Straits'...
   %     ,'Triangle of Central China','the Pearl River Delta urban agglomerations','Shandong Peninsula urban agglomerations','mid-southern Liaoning urban agglomerations' ...
   %     ,'Chengdu-Chongqing urban agglomerations','Beibu Gulf Urban Agglomeration'}
    % Dr2=roundn(Dr',-3)  
   %  Dr2 = num2cell(Dr2);
    %    outputDr(:,1)=CityAgglomeration
    %    outputDr(:,2)=Dr2
   % xlswrite('PLR_2relative entropy2017.xlsx',outputDr)
    
    
    
    
