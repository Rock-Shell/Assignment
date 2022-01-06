import time
from scipy.stats import uniform
import pandas as pd

data = pd.DataFrame(columns=["x1","x2","y"])
# data.loc[0] = [0,0,1]
# print(data)

# '''
count = 0
t1 = time.time()
x1= uniform.rvs(0,1,size=10,random_state=1)

x2 = []
y = []
for i in x1:
        rand = uniform.rvs(0,1,size=10,random_state=1)
        for j in rand:
                x2.append(0.5*i + j)
                rand = uniform.rvs(0,1,size=10,random_state=1)
                for k in rand:
                        temp = 2 + 2*i + 0.3*x2[-1] + k
                        y.append(temp)
                        data.loc[count] = [i,x2[-1],temp]
                        count += 1

t2 = time.time()
l = len(y)
s = sum(y)

print(t2-t1,"s")
print("length: ",l," mean",s/l)
print(data.head())
# '''