#!/usr/bin/env python
# coding: utf-8

# In[36]:


from rembg import remove 
import base64


# In[4]:


from PIL import Image 


# //input the image address in the image var 
# 
# 

# In[39]:


image1=open(r"C:\Users\Harshit Bansal\Pictures\Screenshots\Screenshot_20230224_194120.png","rb")
input = Image.open(image1) 


# In[40]:


outputimage =(r"C:\Users\Harshit Bansal\Pictures\Screenshots\Screenshot_20230224_194120removedbg.png")


# In[41]:


output=remove(input)


# In[43]:


output.save(outputimage)


# In[ ]:




