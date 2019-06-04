import math
import numpy as np
import statistics
from sklearn import preprocessing
from sklearn import svm

a=[]
points=[]
category=[]
category_output=[]
def main():
    f=open("train_data.txt","r")
    for line in f:
        a.append(line)
    myList=[i.split('\n')[0] for i in a]
    temp=[i.split(',')for i in myList]
    n_data=len(temp)
    n_attrib=len(temp[0])
    print(temp)
    print(n_attrib)
    points=transform(temp,n_attrib,n_data)
    print(points)
    for i in temp:
        cat=i[n_attrib-1]
        if cat in "yes":
            category.append(1)
        else:
            category.append(0)
    print(category) 
    clf=apply_svm()
    predict_svm(clf)

def output(label):
    b=[]
    f1=open("test_data.txt","r")
    for line1 in f1:
        b.append(line1)
    myList=[i.split('\n')[0] for i in b]
    temp=[i.split(',')for i in myList]
    #print(temp)
    n_attrib2=len(temp[0])
    k=0
    for i in temp:
        i[n_attrib2-1]=label[k]
        k+=1
    f2=open('output.txt','w')
    for i in temp:
        for j in range(n_attrib2):
            f2.write(i[j]+',')
        f2.write('\n')    
        
def column(matrix, i):
    return [row[i] for row in matrix]

def apply_svm():
    clf=svm.SVC()
    #print(clf)
    k=clf.fit(points,category)
    return clf

def predict_svm(clf):
    a1=[]
    f=open("test_data.txt","r")
    for line in f:
        a1.append(line)
    myList1=[i.split('\n')[0] for i in a1]
    temp1=[i.split(',')for i in myList1]
    n_data1=len(temp1)
    n_attrib1=len(temp1[0])
    points=transform(temp1,n_attrib1,n_data1)
    for i in points:
        l=[]
        l.append(i)
        arr=clf.predict(l)
        category_output.append(arr.tolist())
    #print(category_output)
    label=[]             
    for j in range(n_data1):
        for i in range(0,1):
            if category_output[j][i] == 1:
                 label.append("yes")
            else:
                 label.append("no")
    output(label)              
      
def transform(temp,n_attrib,n_data):
    for i in temp:
        a=float(i[0])
        b=float(i[1])
        c=float(i[2])
        d=float(i[3])
        e=float(i[4])
        f=float(i[5])
        l=[]
        l.append(a)
        l.append(b)
        l.append(c)
        l.append(d)
        l.append(e)
        l.append(f)
        points.append(l)
    #print(points)
    #print("MEAN")    
    a=np.array(points)
    arr1=[[]]
    arr1=a.mean(axis=0)
    #print(arr1)

    
    #variance=[]
    dummy=[]
    v=[]
    #print("VARIANCE")
    for i in range(0,n_attrib-2):
        dummy=column(points,i)
        variance=np.var(dummy)
        v.append(variance)
    print(v)

    
    for j in range(0,n_attrib-2):
        for i in range(0,n_data):
            if(points[i][j]==0):
                points[i][j]=(points[i][j]-arr1[j])/(v[j])
            else:
               points[i][j]=(points[i][j]-arr1[j])/(v[j]/points[i][j])
            
    return points                    
    
main()
