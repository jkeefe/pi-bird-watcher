#!/usr/bin/env python
# coding: utf-8

# In[1]:


import boto3
import requests


# In[8]:


image_name = 'bird-article-l.png'
image_path = '../testdata/' + image_name
analyzer_url = 'https://pi-bird-watcher.onrender.com/checkurl'
bucket = 'pi-bird-images'
bucket_url = 'https://pi-bird-images.s3.amazonaws.com/'


# In[3]:


s3 = boto3.client('s3')
s3.upload_file(
    image_path, bucket, image_name,
    ExtraArgs={'ACL': 'public-read'}
)


# In[9]:


url = bucket_url + image_name
response = requests.post(analyzer_url, json={ 'url': url })

