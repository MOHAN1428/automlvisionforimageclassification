import os
import numpy as np
import pandas as pd
from google.cloud import storage
# Instantiates a client
storage_client = storage.Client()
# Define bucket name: change this to your own
bucket_name = 'ekabasandbox-vcm'
# Get GCS bucket
bucket = storage_client.get_bucket(bucket_name)
# Retrieve blobs in the train dataset
blobs = bucket.list_blobs(prefix='chest_xray/chest_xray/train/')
# Retrieve list of blobs
blob_list = []
for blob in blobs:
    blob_list.append(blob.name)
  len(blob_list)
print(blob_list[0])
print(blob_list[1])
# Remove .DS_Store from list created by the datasource system
# We don't mind doing this O(n) operation because the list size is manageable.
# For larger datasets, it may be better to simply delete this file from Google Cloud Storage.

# Append the bucket_prefix to the object file path

i, length = 0, len(blob_list)
bucket_prefix = 'gs://ekabasandbox-vcm/'
data = []
for blob in blob_list:
    if '.DS_Store' not in blob:
        entry = [''.join([bucket_prefix, blob]), blob.split('/')[3]]
        data.append(entry)
print(data[0])
print(data[1])
# convert to Pandas DataFrame
data_pd = pd.DataFrame(np.array(data))
data_pd.to_csv("data.csv", header=None, index=None)
# Upload data.csv to Google Cloud Storage
output_blob = bucket.blob('data.csv')
output_blob.upload_from_filename('data.csv')
