#!/usr/bin/env python
# coding: utf-8

# In[3]:


import numpy as np
arr1 = np.array([1,2,3])
print (arr1)


# In[4]:


print (arr1.shape)


# In[5]:


print (type(arr1))


# In[8]:


print(arr1[2])


# In[9]:


arr1[2]=6
print(arr1)


# In[12]:


arr2 = np.array([[1,2,3,4],[5,6,7,8]])
arr2


# In[13]:


print (arr2.shape)


# In[17]:


arr2[1,2]


# In[18]:


arr2[0]


# In[19]:


arr3 = np.array(['Narok','Nakuru'])
arr3


# In[21]:


arr4 = np.arange(0,20,5)
arr4


# In[22]:


arr5 = np.linspace(0,10,20)
arr5


# In[23]:


print(np.tile(arr5,3))


# In[27]:


np.diag([5,6,7,8,9])


# In[28]:


arr5.size


# In[29]:


arr5.shape


# In[30]:


arr1=10


# In[31]:


print(arr1)


# In[32]:


arr1/2


# In[34]:


np.log2(arr1)


# In[36]:


np.log10(arr1)


# In[37]:


np.cos(arr1)


# In[38]:


np.tan(arr1)


# In[39]:


np.sin(arr1)


# In[40]:


np.sum(arr5)


# In[42]:


np.min(arr5)


# In[43]:


np.max(arr5)


# In[44]:


np.mean(arr5)


# In[45]:


np.median(arr5)


# In[46]:


np.std(arr5)


# In[47]:


np.var(arr5)


# In[48]:


arr5[1:2]


# In[49]:


arr5.T


# In[50]:


arr7 = np.array([11,12,13,14,15,16])
arr7


# In[51]:


arr8 = np.append(arr7,17)
arr8


# In[53]:


arr9 = np.insert(arr7,0,[1,2,3])
arr9


# In[54]:


arr10 = np.delete(arr9, [1,3])
arr10


# In[ ]:




