import boto3
#connect to server and send request
sqs = boto3.resource('sqs')
queue = sqs.create_queue(QueueName='requestQueue',Attributes={'DelaySeconds' : '5'})


print("Enter values (space separated):")
input = input()
queueOut = sqs.get_queue_by_name(QueueName='requestQueue')
queueOut.send_message(MessageBody=input)

