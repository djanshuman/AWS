import requests
import boto3
import uuid
import time
import random
import json


client= boto3.client('kinesis',region_name='us-east-1');
partition_key=str(uuid.uuid4())

number_of_result=200
r=requests.get('https://randomuser.me/api/?exc=login&results='+str(number_of_result));
data=r.json()["results"]

while True:
	user_index=int(random.uniform(0,(number_of_result-1)))
	random_user=data[user_index]
	random_user=json.dumps(random_user)
	client.put_record(
		StreamName='DemoStream',
		Data=random_user,
		PartitionKey=partition_key)
	time.sleep(random.uniform(0,1))

