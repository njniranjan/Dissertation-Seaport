#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import seaborn as sns
import numpy as np
import numpy_financial as npf
import matplotlib.pyplot as plt


# In[2]:


data=pd.read_excel("D:/Dissertation/Dataset-filtered/30-1 normal.xlsx")
data


# In[3]:


total_ed=data['QC+YC/MWh'].sum()
total_ed


# In[4]:


data.describe()
g=sns.pairplot(data)


# In[5]:


total_ed=(data['QC+YC/MWh'].sum())*148.9
total_ed


# In[6]:


edm=total_ed*30
edm


# In[7]:


l1=[]
for i in range(1,61):               #Increase of 3% half yearly
    Ed= edm + (i*(3/100)*edm)
    l1.append(Ed)
print(l1) 


# In[8]:


l2=[]
for i in range(1,61,2):   #yearly demand
    ee=l1[i]
    l2.append(ee)
print(l2)


# In[9]:


#Revenue: Since the mean is 6, values <=6  is considered small and the rest as big.
#Smaller ships:SD $20K ; Bigger ships: SD $25K
#There are 10 big ships and 20 small ships
R= 20*20000+10*25000
Rpy=R*30*12
Rpy


# In[10]:


#Profit 2percent
profit_y = 0.02*Rpy
#profit_yy= np.full((10,0),2)
profit_yy=[profit_y]*30
profit_yy


# In[11]:


costd=[]
inc=[5,5,6,6,7,7,8,8,9,9,10,10,11,11,12,12,13,13,14,14,15,15,16,16,17,17,18,18,19,19]          #cost of depreciation
for i in inc:  
    costdd= ((i)/100)*profit_y
    costd.append(costdd)
costd


# In[12]:


#Case 1.1: 27270 panels, 500W per panel-->660 SGD, per MWh cost=148.9  
cost= (27270*660)+(500*27270*0.000001*148.9 )
cost


# In[13]:


costr=[]
inc=[5,5,6,6,7,7,8,8,9,9,10,10,11,11,12,12,13,13,14,14,15,15,16,16,17,17,18,18,19,19]
for i in inc:  ##alter range
    costrr= ((i)/100)*cost         #cost of replacement
    costr.append(costrr)
costr


# In[14]:


tcost = [costr[i]+costd[i] for i in range(len(costr))]
tcost


# In[15]:


#Yearly Profit accounting yearly demand
Net_p= (np.array(profit_yy)-np.array(l2))
Net_p


# In[16]:


Net_pd= Net_p-tcost #dynamic profit
Net_pd


# In[17]:


cost1 = np.array(-18000230.2515)
cost1
CashF= np.append(cost1,Net_p)
print(CashF)

CashFd= np.append(cost1,Net_pd) #dynamic cashflow
CashFd


# In[18]:


lst=[]
for i in range(1,31):
    NPV=npf.npv(0.1,CashFd[0:i])
    lst.append(NPV)
print(lst)


# In[19]:


lst2=[]
for i in range(lst.index(lst[-1])+1):
    lst2.insert(i,(lst[i]-lst[i-1]))
mx=0
for i in range(2,30):
    if(lst[i]>mx):
         mx=lst[i]
   
print(mx)    
print(lst2)
max_slope = max([x - z for x, z in zip(lst[:-1], lst[1:])])
print(abs(max_slope))


# In[20]:


x= np.arange(-1,31,1)
NPV=[]
print(x)
for i in range(32):
    NPV1=npf.npv(0.1,CashFd[0:i])
    NPV.append(NPV1)
print(NPV)


plt.plot(x,NPV)
plt.show()


# In[21]:


#MAX CASE: #Case 1.2:  panels, 400W per panel-->SD $525, per MWh cost=148.9SGD  
cost= (42000*525)+(400*42000*0.000001*148.9 )
cost


# In[22]:


costr=[]
inc=[5,5,6,6,7,7,8,8,9,9,10,10,11,11,12,12,13,13,14,14,15,15,16,16,17,17,18,18,19,19]
for i in inc:  ##alter range
    costrr= ((i)/100)*cost         #cost of replacement
    costr.append(costrr)
costr


# In[23]:


tcost = [costr[i]+costd[i] for i in range(len(costr))]
tcost


# In[24]:


#Yearly Profit accounting yearly demand
Net_p= (np.array(profit_yy)-np.array(l2))
Net_p


# In[25]:


Net_pd= Net_p-tcost #dynamic profit
Net_pd


# In[26]:


cost1 = np.array(-22052501.52)
cost1
CashF= np.append(cost1,Net_p)
print(CashF)

CashFd= np.append(cost1,Net_pd) ################dynamic cashflow
CashFd


# In[27]:


lst=[]
for i in range(1,31):
    NPV=npf.npv(0.1,CashFd[0:i])
    lst.append(NPV)
print(lst)   

lst2=[]
for i in range(lst.index(lst[-1])+1):
    lst2.insert(i,(lst[i]-lst[i-1]))
mx=0
for i in range(2,30):
    if(lst[i]>mx):
         mx=lst[i]
   
print("max=",mx)    
print(lst2)
max_slope = max([x - z for x, z in zip(lst[:-1], lst[1:])])
print(abs(max_slope))


# In[28]:


x= np.arange(-1,31,1)
NPV=[]
print(x)
for i in range(32):
    NPV1=npf.npv(0.1,CashFd[0:i])
    NPV.append(NPV1)
print(NPV)


plt.plot(x,NPV)
plt.show() 


# In[29]:


#MAX CASE: #Case 1.3:  panels, 300W per panel-->SD $395, per MWh cost=148.9  
cost= (52360*395)+(300*52360*0.000001*148.9 )
cost


# In[30]:


costr=[]
inc=[5,5,6,6,7,7,8,8,9,9,10,10,11,11,12,12,13,13,14,14,15,15,16,16,17,17,18,18,19,19]
for i in inc:  ##alter range
    costrr= ((i)/100)*cost         #cost of replacement
    costr.append(costrr)
costr


# In[31]:


tcost = [costr[i]+costd[i] for i in range(len(costr))]
tcost


# In[32]:


#Yearly Profit accounting yearly demand
Net_p= (np.array(profit_yy)-np.array(l2))
Net_p


# In[33]:


Net_pd= Net_p-tcost #dynamic profit
Net_pd


# In[37]:


x= np.arange(0,30,1)
plt.plot(x,Net_pd)
plt.show() 


# In[34]:


cost1 = np.array(-20684538.9212)
cost1
CashF= np.append(cost1,Net_p)
print(CashF)

CashFd= np.append(cost1,Net_pd) ################dynamic cashflow
CashFd


# In[35]:


lst=[]
for i in range(1,31):
    NPV=npf.npv(0.1,CashFd[0:i])
    lst.append(NPV)
print(lst)    

lst2=[]
for i in range(lst.index(lst[-1])+1):
    lst2.insert(i,(lst[i]-lst[i-1]))
mx=0
for i in range(2,30):
    if(lst[i]>mx):
         mx=lst[i]
   
print(mx)    
print(lst2)
max_slope = max([x - z for x, z in zip(lst[:-1], lst[1:])])
print(abs(max_slope))


# In[36]:


x= np.arange(-1,31,1)
NPV=[]
print(x)
for i in range(32):
    NPV1=npf.npv(0.1,CashFd[0:i])
    NPV.append(NPV1)
print(NPV)


plt.plot(x,NPV)
plt.show() 


# In[ ]:




