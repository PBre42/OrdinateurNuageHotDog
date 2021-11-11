import boto3
import random
#launch the server and wait for requests
ec2 = boto3.client('ec2')
sqs = boto3.resource('sqs')
s3 = boto3.resource('s3')
bucketname = 'photoshotdogs'
bucket = s3.Bucket(bucketname)

urls = []
for obj in bucket.objects.all():
    urls.append("https://%s.s3.amazonaws.com/%s" % (bucketname,obj.key))

clienturls = random.sample(urls,4)

#queue = sqs.create_queue(QueueName='responseQueue', Attributes={'Min','Max','Mean','Median'})
#inQueue = sqs.get_queue_by_name(QueueName='requestQueue')

#print(inQueue.attributes.get('Message'))

