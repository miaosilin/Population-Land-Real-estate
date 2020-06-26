% main program
% population-land-real estate
% Author? Kong Qingshan, Miao Silin, Kong Haiyang
% Date: 2020.06

function y=normalization(x,type,ymin,ymax)
%Normalization of positive or negative indicators
%X is the raw data matrix, one row represents a sample, and each column corresponds to an index
%Type set positive indicator 1 and negative indicator 2
%ymin,ymax are normalized interval endpoints
[n,m]=size(x); %N and m are the rows and columns of the matrix
y=zeros(n,m);  %Generates a zero vector matrix with n rows and m columns
xmin=min(x); %Each column takes a minimum
xmax=max(x); %Each column takes a maximum value
switch type
    case 1  %The forward indicator performs this operation
        for j=1:m
            y(:,j)=(ymax-ymin)*(x(:,j)-xmin(j))/(xmax(j)-xmin(j))+ymin;
        end
    case 2
        for j=1:m  %The negative indicator performs this operation
            y(:,j)=(ymax-ymin)*(xmax(j)-x(:,j))/(xmax(j)-xmin(j))+ymin;
        end
end
end
