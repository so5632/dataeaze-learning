import boto3
import argparse
import json


parser = argparse.ArgumentParser()
parser.add_argument("input_file",help="Input file to read from S3 Bucket")
parser.add_argument("output_file",help="Output file to dump on S3 Bucket")
args = parser.parse_args()

with open('S3_Connection.json','r') as f:
    data = json.load(f)

s3_client = boto3.client('s3',aws_access_key_id=data['aws_access_key_id'],aws_secret_access_key=data['aws_secret_access_key'])

s3 = boto3.resource('s3',aws_access_key_id=data['aws_access_key_id'],aws_secret_access_key=data['aws_secret_access_key'])

s3_client.download_file('rohansawant1','count.txt','count.txt')

file_reader = open(args.input_file,"r")
data = file_reader.read()
file_reader.close()
cnt=0

for i in data:
    cnt=cnt+1

f2 = open(args.output_file,'w')
f2.write(str(cnt))
f2.close()

file_writer = open('output.txt','rb')
s3.Bucket('rohansawant1').put_object(Key='output.txt',Body=file_writer)

print("Done!!!!")
 
