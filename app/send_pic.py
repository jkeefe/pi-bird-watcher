#!/usr/bin/env python
# coding: utf-8

# In[1]:


import boto3
import requests
import sys


# In[ ]:


image_path = sys.argv[1]
if not image_path:
    print("Need a file name to check!")
    sys.exit(1)


# In[10]:


analyzer_url = 'https://pi-bird-watcher.onrender.com/checkurl'
bucket = 'pi-bird-images'
bucket_url = 'https://pi-bird-images.s3.amazonaws.com/'


# In[3]:


s3 = boto3.client('s3')
s3.upload_file(
    image_path, bucket, image_path,
    ExtraArgs={'ACL': 'public-read'}
)


# In[9]:


url = bucket_url + image_path
response = requests.post(analyzer_url, json={ 'url': url })

