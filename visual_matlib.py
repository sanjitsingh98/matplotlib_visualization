#MATPLOTLIB
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

#use of pandas to read database
df=pd.read_csv('Salaries.csv')
df.info()

#histogram
plt.hist(df['TotalPay'])
plt.xlabel("Total Pay")#label the x axis
plt.ylabel("Value")#label the y axis
plt.title("Sample Histogram")#title of the plot
plt.show()#to display the graph

#bar plot
plt.bar(['A','B','C','D','E'],[40,30,65,55,90])
plt.xlabel("Type")
plt.ylabel("Frequency")
plt.title("Sample Bar plot")
plt.show()

#scatter plot
plt.scatter(['A','B','C','D','E'],[40,30,65,55,90])
plt.xlabel("Type")
plt.ylabel("Frequency")
plt.title("Sample Scatter plot")
plt.show()

#pie chart
plt.pie([20,30,40],labels=['A','B','C'])
plt.title("Sample Pie Chart")
plt.show()

x=np.linspace(0,10,10)
y=x**3

#line plot
plt.plot(x,y)
plt.xlabel("x values")
plt.ylabel("cube values")
plt.title("X vs Cube function method")
plt.show()

#subplots
plt.subplot(1,2,1)# 1,2 means 1 row 2 columns and the third parameter is the index
plt.plot(x,y,"r--")#r-- means color is red and the design is '--', you can change to color of your choice and the design to ':','-','-.'
plt.subplot(1,2,2)
plt.plot(x,y,"g")
plt.show()

#object oriented method
fig = plt.figure()
a=fig.add_axes([0.12,0.1,0.8,0.8]) #left bottom width height
a.plot(x,y)
a.set_xlabel("x values")
a.set_ylabel("cube values")
a.set_title("X vs Cube OO method")
plt.show()

#figure inside a figure
fig = plt.figure()
a=fig.add_axes([0.12,0.1,0.8,0.8])#define axes for main figure
b=fig.add_axes([0.2,0.4,0.4,0.4])#define axes for small figure
a.plot(x,y,"r")#color=red
b.plot(y,x,"y")#color=yellow
a.set_title("big one")
b.set_title("small one")
a.set_xlabel("big X")
a.set_ylabel("big Y")
b.set_xlabel("small X")
b.set_ylabel("small y")
plt.show()

#subplots using for loop object oriented method
q,p=plt.subplots(2,1)#rows,column & q is the figure object and p is the axes object
for p1 in p:
    p1.plot(x,y)
plt.tight_layout()#removes any kind of overlapping
plt.show()

#subplots
q,p=plt.subplots(1,3)
p1=p[0].plot(x,y)
p2=p[1].plot(y,x)
p[0].set_title("ONE")
#p2.set_title("TWO")#ERROR
p[1].set_title("TWO")
plt.tight_layout()
p[2].set_title("blank")
plt.show()

#specify custom figure size
a,b=plt.subplots(1,2,figsize=(6,4),dpi=150)#figsize in width and height
plt.show()

#2 plot in same figure
abc=plt.figure()
a1=abc.add_axes([0.1,0.1,0.8,0.8])
a1.plot(x,x**3,label="x**3")
a1.plot(x,x**2,label="x**2")
a1.legend()#leave it blank to define the best position for legend,otherwise specify a number,check google for the same
#a1.legend(loc=(0.1,0.1))#user defined position
plt.show()

#custom customization of the plot design
abc=plt.figure()
a1=abc.add_axes([0.1,0.1,0.8,0.8])
a1.plot(x,x**3,label="x**3",color="pink",lw="3",ls="--",marker="o",markersize="10",markerfacecolor="green",markeredgewidth="1",markeredgecolor="black")
plt.show()
# possible marker symbols: marker = '+', 'o', '*', 's', ',', '.', '1', '2', '3', '4', ...
# possible linestype options ‘-‘, ‘–’, ‘-.’, ‘:’, ‘steps’
#lw=linewidth
#alpha value decides the transparency of the graph
#ls=linestyle

#line plot
abc=plt.figure()
a1=abc.add_axes([0.1,0.1,0.8,0.8])
a1.plot(x,y,"g--")
plt.show()

#default,tight,custom axes
fig, axes = plt.subplots(1, 3, figsize=(12, 4))
axes[0].plot(x, x**2, x, x**3)
axes[0].set_title("default axes ranges")
axes[1].plot(x, x**2, x, x**3)
axes[1].axis('tight')
axes[1].set_title("tight axes")
axes[2].plot(x, x**2, x, x**3)
axes[2].set_ylim([0, 60])
axes[2].set_xlim([2, 5])
axes[2].set_title("custom axes range")
plt.show()
