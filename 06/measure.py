from datetime import datetime, timedelta
import boto3

def upload_latency(s3, bucket_name, file_name):
    with open(file_name, "rb") as f:
        timer1 = datetime.now()
        s3.upload_fileobj(f, bucket_name,file_name)
        # 다운로드 = s3.download_fileobj('euidong-seoul-bucket','1kb.txt',f)
        # 삭제 = s3.delete_object('1kb.txt')
        timer2 = datetime.now()
    return (timer2 - timer1).total_seconds()

s32 = boto3.resource('s3')
s3 = boto3.client('s3')
file_name = "1kb.txt"

# initializing
avg_latency = {}
for bucket in s32.buckets.all():
    avg_latency[bucket.name] = 0

ITER_CNT = 10
for i in range(ITER_CNT):
    print('#' + str(i + 1))
    for bucket in s32.buckets.all():
        bucket_name = bucket.name
        latency = upload_latency(s3, bucket.name, file_name)
        avg_latency[bucket_name] += latency
        print (bucket_name + ": " + str(latency))
    print("\n")

for bucket in avg_latency:
    print(bucket + "'s avg: " + str(avg_latency[bucket] / ITER_CNT))
