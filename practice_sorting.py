#!/usr/bin/env python
# coding: utf-8

# In[ ]:





# In[51]:


# Insertion Sort

A = [4,7,9,1,5,2,8,3,6]

print(A)

for j in range(1, len(A)):
    key = A[j]    
    i = j - 1
    while i >= 0 and A[i] > key:
        A[i + 1] = A[i]
        i = i - 1
    A[i + 1] = key
    
print(A)


# In[ ]:





# In[50]:


arr = [4,7,9,1,5,2,8,3,6]

print(arr)

for i in range(1, len(arr)):  
        key = arr[i]  
        # Move elements of arr[0..i-1], that are
        # greater than key, to one position ahead
        # of their current position
        j = i-1
        while j >=0 and key < arr[j] :
                arr[j+1] = arr[j]
                j -= 1
        arr[j+1] = key
        
print(arr)


# In[ ]:




