% main program
% population-land-real estate
% Author? Kong Qingshan, Miao Silin, Kong Haiyang
% Date: 2020.06


%figure 1
c=estate;%C is for coloring the z axis
scatter3(pop,land,estate,50,c)
cityname=name'

for i=1:num_of_cities
    text(pop(i),land(i),estate(i),cityname(i))
end
       %%Set the X-axis, Y-axis, z-axis, content corresponding to the title and value range of the three coordinate axes of the 3d surface%%
       xlabel('Population');
       ylabel('Land');
       zlabel('Real Estate');
       
figure_FontSize=12;
set(get(gca,'XLabel'),'FontSize',figure_FontSize,'Vertical','top');
set(get(gca,'YLabel'),'FontSize',figure_FontSize,'Vertical','middle');
set(findobj('FontSize',10),'FontSize',figure_FontSize);
