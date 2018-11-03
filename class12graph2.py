'''import matplotlib.pyplot as plt
import csv
plt=csv.reader()
target_doc = csv.reader(open('eg.csv', 'rU'), delimiter=",", quotechar='|')
plt.plot(data)
plt.xlabel('X axis')
plt.ylabel('y axis')
plt.title('my graph')
plt.show()'''
import matplotlib.pyplot as plt
import csv

x=[]
y=[]

with open('eg.csv', 'r') as csvfile:
    plots= csv.reader(csvfile, delimiter=',')

plt.plot(x,y)
plt.title('Data from the CSV File: People and Expenses')
plt.xlabel('x axis')
plt.ylabel('y axis')
plt.show()









