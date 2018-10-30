import csv
from math import *
import random
import  pylab as plt
import  numpy as np
path=[] #tsp问题的路径
path_temp=[] #tsp问题的

list_path=[]
for i in range(1,31):
    list_path.append(i)
print(list_path)
#读取文件，获取数据
path_dir="G:/untitled/data"
f=open(path_dir+"/tsp.csv",mode="r")
data=[]
for line in f.readlines():
    line=line.strip( )
    line=line.split(",")
    data.append(line)
f.close()
#print(data)

#函数：计算两城市之间的距离
dis=[]  #距离矩阵
diseum=[]
def distance(x1,y1,x2,y2):
    d=sqrt((x1-x2)**2+(y1-y2)**2)
    return  d
for i in range(len(data)):
    diseum = []
    for j in range(len(data)):
        diseum.append(distance(float(data[i][0]),float(data[i][1]),float(data[j][0]),float(data[j][1])))
    dis.append(diseum)
#for i in range(len(dis)):
 #   print(dis[i])

#计算路径长度
def path_distance(path):
    path_sum=0
    for i in range(0,len(path)-1):
        path_sum+=dis[path[i]-1][path[i+1]-1]
    path_sum+=dis[path[29]-1][path[0]-1]
    return path_sum

#状态产生
def change_list(list):
    index1=random.randint(0,29)
    index2=random.randint(0,29)
    if(index1==index2):
        index2=random.randint(0,29)
    i1=min(index2,index1)
    i2=max(index1,index2)
    list_part1=list[:i1]
    list_part2=list[i1:i2+1]
    list_part3=list[i2+1:]
    list_part2.reverse()
    list=list_part1+list_part2+list_part3
    return list



K=1
count=0
distance_coll=[]
count_list=[]
#path=change_list(list_path) #初始解
path=list_path
print(path_distance(path))
path_min=path
distance_min=path_distance(path)
for i in range(10):
    path_curr=path
    distance_coll.append(path_distance(path))
    count_list.append(i)
    distance_min=inf
    for j in range(500):
        path_temp=change_list(path_curr)
        if(path_distance(path_temp)<distance_min):
            path=path_temp
            distance_min=path_distance(path_temp)
    if path_distance(path)>path_distance(path_curr):
        break;
T=0.5/(0.8**10)
path=path_curr
print(path_distance(path),"vneknbvkvnkjev",path,i+1)
while T>0.5:
    for i in range(500):
        path_temp=change_list(path)
        #print(path_temp)
        if(path_distance(path_temp)<path_distance(path)):
            path = path_temp
        else:
            index=e**(-(path_distance(path_temp)-path_distance(path))/(K*T))
            if(index>random.random()):
                path = path_temp

    print(path_distance(path))
    if(path_distance(path)<distance_min):
        path_min=path
        distance_min=path_distance(path)
    T=0.8*T
    distance_coll.append(path_distance(path))
    count_list.append(count+10)

    count +=1
print (path_distance(path_min))
print(path_min)
#plt.plot(count_list, distance_coll)
plt.plot(count_list, distance_coll,"bo-")
plt.show()


