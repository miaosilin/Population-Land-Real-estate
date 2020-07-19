function [X,e,d,w]=entropy(x,ind)
%Use entropy method to calculate the weight of each index (column)
%X is the raw data matrix, one row represents a sample, and each column corresponds to an index
%Ind is an indication vector
[n,m]=size(x); % n cities, m indices
%%Normalization processing of data

s1 = 9 %count the number of indicators in system 1
s2 = 10 %count the number of indicators in system 2
s3 = 7  %count the number of indicators in system 3

for i=1:m
    if ind(i)==1 
        X(:,i)=normalization(x(:,i),1,0.002,0.996);    
    else 
        X(:,i)=normalization(x(:,i),2,0.002,0.996);
    end
end
%%The proportion of the ith city in this index P (I, J)
for i=1:n
    for j=1:m
        p(i,j)=X(i,j)/sum(X(:,j));
    end
end
%%Calculate the entropy of the Jth index e(j)
k=1/log(n);


for j=1:m
    e(j)=-k*sum(p(:,j).*log(p(:,j)));
end
     
d=ones(1,m)-e; %Calculate information entropy redundancy
%w=d./sum(d);
for j=1:s1
    w(j)= d(j)./sum(d(1:s1))   
end
for j=s1+1:s1+s2
    w(j)= d(j)./sum(d(s1+1:s1+s2))   
end
for j=s1+s2+1:s1+s2+s3
    w(j)= d(j)./sum(d(s1+s2+1:s1+s2+s3))   
end

end
