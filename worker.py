import boto3
import random
#launch the server and wait for requests
ec2 = boto3.client('ec2')
sqs = boto3.client('sqs')
s3 = boto3.resource('s3')
bucketname = 'photoshotdogs'
bucket = s3.Bucket(bucketname)

urls = []
for obj in bucket.objects.all():
    urls.append("https://%s.s3.amazonaws.com/%s" % (bucketname,obj.key))

clienturls = random.sample(urls,4)

print(clienturls)
#queue = sqs.create_queue(QueueName='photos', Attributes={'Url'})
response = sqs.send_message(
        QueueUrl="photosHotDogs",
        MessageBody=' '.join(clienturls)
    )  


#inQueue = sqs.get_queue_by_name(QueueName='requestQueue')

#print(inQueue.attributes.get('Message'))

