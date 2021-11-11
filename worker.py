import boto3

#launch the server and wait for requests
ec2 = boto3.client('ec2')
sqs = boto3.resource('sqs')
s3 = boto3.client('s3')
bucketImages = s3.Bucket('imageshotdogs')
bucketJson = s3.Bucket('jsonhotdogs')


#queue = sqs.create_queue(QueueName='responseQueue', Attributes={'Min','Max','Mean','Median'})
inQueue = sqs.get_queue_by_name(QueueName='requestQueue')


print(inQueue.attributes.get('Message'))

