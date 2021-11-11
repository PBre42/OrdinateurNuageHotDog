import boto3
import random
import json

#launch the server and wait for requests
ec2 = boto3.client('ec2')
sqs = boto3.client('sqs')
s3 = boto3.resource('s3')
bucketname = 'photoshotdogs'
bucketname2 = 'hotdogsdata'

def sendImages():
    urls = []
    #List pictures and parse their urls
    for obj in s3.Bucket(bucketname).objects.all():
        urls.append("https://%s.s3.amazonaws.com/%s" % (bucketname,obj.key))
    #Get random pictures        
    clienturls = random.sample(urls,4)
    #Send 4 urls
    response = sqs.send_message(
            QueueUrl="photosHotDogs",
            MessageBody=' '.join(clienturls)
        )  

def storeDataInJson(data):
    #data parse ou a parser
    s3.Object(bucketname2,'votes.json').put(Body=bytes(json.dumps(data).encode('UTF-8')))

def uploadImages(picture):
    #Create a key for new picture
    imgCount = 0
    for obj in s3.Bucket(bucketname).objects.all():
        imgCount += 1
    #Create key
    extension = picture.split('.',2)
    key = "%s." + extension % (imgCount+1) 
    
    #Upload to S3
    s3.upload_file(picture,bucketname,key)


