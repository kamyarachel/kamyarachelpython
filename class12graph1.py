import matplotlib.pyplot as plt 
left=[1,2,3,4,5]
height=[10,20,30,35,40]
tick_label=['one','two','three','four','five']
plt.bar(left,height,tick_label=tick_label,width=0.5,color=['blue','yellow'])
plt.xlabel('x axis')
plt.ylabel('y axis')
plt.title('my bar graph')
plt.show()