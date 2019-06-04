import plotly.plotly as py
import plotly.graph_objs as go

inc_school=[]
inc_imr=[]

def column(matrix,i):
     dummy2=[]
     #print(matrix)
     for row in matrix:
            if len(row)!=0:
                #print(row,"*****")
                dummy2.append(row[i])
            #print(row[i])
     return dummy2
    
a=[]
f=open("plot.txt","r")
for line in f:
    a.append(line)
myList=[i.split('\n')[0] for i in a]
temp=[i.split(',')for i in myList]

x1=column(temp,1)
x2=column(temp,2)
diff=[]

for i in range(len(x1)):
     diff=x1[i+1:]
     #print(diff)
     for j in range(len(diff)):
          inc_school.append(float(x1[i])-float(diff[j]))
     
diff=[]
for i in range(len(x1)):
     diff=x1[i+1:]
     #print(diff)
     for j in range(len(diff)):
          inc_imr.append(float(x2[i])-float(diff[j]))
     


trace1 = go.Bar(
    x=column(temp,0),
    y=column(temp,1),
    name='SCHOOLING STATUS'
)
trace2 = go.Bar(
    x=column(temp,0),
    y=column(temp,2),
    name='IMR'
)
data = [trace1, trace2]
layout = go.Layout(
    barmode='group'
)
fig = go.Figure(data=data, layout=layout)
plot_url = py.plot(fig, filename='grouped-bar')
 

# Create traces
trace0 = go.Scatter(
    x = column(temp,0),
    y = inc_school,
    mode = 'lines',
    name = 'lines'
)
trace1 = go.Scatter(
    x = column(temp,0),
    y = inc_imr,
    mode = 'lines+markers',
    name = 'lines+markers'
)
data = [trace0, trace1]
plot_url=py.plot(data, filename='line-mode')
