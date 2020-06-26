% main program
% population-land-real estate
% Author? Kong Qingshan, Miao Silin, Kong Haiyang
% Date: 2020.06

clear all; clc

    [data,txt]=xlsread('data_2017.xlsx') %input data
    [num_of_cities,num_of_indicators]=size(data)%set the number of cities and indicators
    ind= ones(1,num_of_indicators)%generate an array to determine the symbol of indicators
    ind(2)= 1 %set the symbol of each indicators: positive or negative
    
    %num_of_cities = 14

     [normalization,entropy,d,W]=entropy(data,ind)%Entropy weight method is used to calculate the weight

     s1 = 9 %count the number of indicators in system 1
     s2 = 10 %count the number of indicators in system 2
     s3 = 7  %count the number of indicators in system 3

     %weight
     pj=1./abs(W)%intermediate variable
     for j=1:s1
        lambda(:,j)=[1./abs(W(j))]/sum(pj(1:s1))   %weight in population system
     end
     for j=s1+1:s1+s2
        lambda(:,j)=[1./abs(W(j))]/sum(pj(s1+1:s1+s2))   %weight in land system
     end
     for j=s1+s2+1:s1+s2+s3
        lambda(:,j)=[1./abs(W(j))]/sum(pj(s1+s2+1:s1+s2+s3))   %weight in real estate system
     end

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


