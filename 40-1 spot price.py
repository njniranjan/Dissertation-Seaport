#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import seaborn as sns
import numpy as np
import numpy_financial as npf
import matplotlib.pyplot as plt


# In[2]:


data=pd.read_excel("D:/Dissertation/Dataset-filtered/40 SHIP-1_spotprice.xlsx")
data


# In[43]:


x= np.arange(0,40,1)
plt.plot(x,data['ED'])
plt.xlabel("Number of vessels")
plt.ylabel("Energy demand in MWh")
plt.show() 


# In[3]:


total_ed=data['ED'].sum()
total_ed


# In[4]:


edm=total_ed*30
edm


# In[5]:


l1=[]
for i in range(1,61):               #Increase of 3% half yearly
    Ed= edm + (i*(3/100)*edm)
    l1.append(Ed)
print(l1) 


# In[6]:


l2=[]
for i in range(1,61,2):   #yearly demand
    ee=l1[i]
    l2.append(ee)
print(l2)


# In[7]:


#Revenue: Since the mean is 6, values <=6  is considered small and the rest as big.
#Smaller ships:SD $20K ; Bigger ships: SD $25K
#There are 11 big ships and 29 small ships
R= 29*20000+11*25000
Rpy=R*30*12
Rpy


# In[8]:


#Profit 2percent
profit_y = 0.02*Rpy
#profit_yy= np.full((10,0),2)
profit_yy=[profit_y]*30
profit_yy


# In[9]:


costd=[]
inc=[5,5,6,6,7,7,8,8,9,9,10,10,11,11,12,12,13,13,14,14,15,15,16,16,17,17,18,18,19,19]          #cost of depreciation
for i in inc:  
    costdd= ((i)/100)*profit_y
    costd.append(costdd)
costd


# In[10]:


#Case 1.1: 27270 panels, 500W per panel-->660 SGD, per MWh cost=155.59  
cost= (27270*660)+(500*27270*0.000001*155.59 )
cost


# In[11]:


costr=[]
inc=[5,5,6,6,7,7,8,8,9,9,10,10,11,11,12,12,13,13,14,14,15,15,16,16,17,17,18,18,19,19]
for i in inc:  ##alter range
    costrr= ((i)/100)*cost         #cost of replacement
    costr.append(costrr)
costr


# In[12]:


tcost = [costr[i]+costd[i] for i in range(len(costr))]
tcost


# In[13]:


#Yearly Profit accounting yearly demand
Net_p= (np.array(profit_yy)-np.array(l2))
Net_p


# In[14]:


Net_pd= Net_p-tcost #dynamic profit
Net_pd


# In[ ]:





# In[15]:


cost1 = np.array(-18000321.46965)
cost1
CashF= np.append(cost1,Net_p)
print(CashF)
CashFd= np.append(cost1,Net_pd) #dynamic cashflow
CashFd


# In[16]:


lst=[]
for i in range(1,31):
    NPV=npf.npv(0.1,CashFd[0:i])
    lst.append(NPV)
print(lst) 


# In[17]:



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


# In[18]:



x= np.arange(-1,31,1)
NPV=[]
print(x)
for i in range(32):
    NPV1=npf.npv(0.1,CashFd[0:i])
    NPV.append(NPV1)
print(NPV)


plt.plot(x,NPV)
plt.show() 


# In[19]:


#MAX CASE: #Case 1.2:  panels, 400W per panel-->SD $525, per MWh cost=155.59  
cost= (42000*525)+(400*42000*0.000001*155.59 )
cost


# In[20]:


costr=[]
inc=[5,5,6,6,7,7,8,8,9,9,10,10,11,11,12,12,13,13,14,14,15,15,16,16,17,17,18,18,19,19]
for i in inc:  ##alter range
    costrr= ((i)/100)*cost         #cost of replacement
    costr.append(costrr)
costr


# In[21]:


tcost = [costr[i]+costd[i] for i in range(len(costr))]
tcost


# In[22]:


#Yearly Profit accounting yearly demand
Net_p= (np.array(profit_yy)-np.array(l2))
Net_p


# In[23]:


Net_pd= Net_p-tcost #dynamic profit
Net_pd


# In[24]:


cost1 = np.array(-22052613.912)
cost1
CashF= np.append(cost1,Net_p)
print(CashF)
CashFd= np.append(cost1,Net_pd) ################dynamic cashflow
CashFd


# In[25]:


lst=[]
for i in range(1,31):
    NPV=npf.npv(0.1,CashFd[0:i])
    lst.append(NPV)
print(lst) 


# In[26]:


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


# In[27]:


x= np.arange(-1,31,1)
NPV=[]
print(x)
for i in range(32):
    NPV1=npf.npv(0.1,CashFd[0:i])
    NPV.append(NPV1)
print(NPV)


plt.plot(x,NPV)
plt.show() 


# In[28]:


#MAX CASE: #Case 1.3:  panels, 300W per panel-->SD $395, per MWh cost=155.59  
cost= (52360*395)+(300*52360*0.000001*155.59 )
cost


# In[29]:


costr=[]
inc=[5,5,6,6,7,7,8,8,9,9,10,10,11,11,12,12,13,13,14,14,15,15,16,16,17,17,18,18,19,19]
for i in inc:  ##alter range
    costrr= ((i)/100)*cost         #cost of replacement
    costr.append(costrr)
costr


# In[30]:


tcost = [costr[i]+costd[i] for i in range(len(costr))]
tcost


# In[31]:


#Yearly Profit accounting yearly demand
Net_p= (np.array(profit_yy)-np.array(l2))
Net_p


# In[32]:


Net_pd= Net_p-tcost #dynamic profit
Net_pd


# In[38]:


x= np.arange(0,30,1)
plt.plot(x,Net_pd)
plt.xlabel("Number of years")
plt.ylabel("Profit")
plt.show() 


# In[34]:


cost1 = np.array(-20684644.00772)
cost1
CashF= np.append(cost1,Net_p)
print(CashF)
CashFd= np.append(cost1,Net_pd) #dynamic cashflow
CashFd


# In[35]:


lst=[]
for i in range(1,31):
    NPV=npf.npv(0.1,CashFd[0:i])
    lst.append(NPV)
print(lst) 


# In[36]:


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


# In[39]:


x= np.arange(-1,31,1)
NPV=[]
print(x)
for i in range(32):
    NPV1=npf.npv(0.1,CashFd[0:i])
    NPV.append(NPV1)
print(NPV)


plt.plot(x,NPV)
plt.xlabel("Number of years")
plt.ylabel("NPV")
plt.show() 


# In[ ]:





# In[ ]:




