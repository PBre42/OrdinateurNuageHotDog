import boto3
import os
import random
import json
from flask import Flask, render_template, request, redirect
from werkzeug.utils import secure_filename


ACCESS_KEY_ID = ''
ACCESS_SECRET_KEY = ''
bucketname2 = 'hotdogsdata'
bucketname = 'photoshotdogs'

#launch the server and wait for
sqs = boto3.client('sqs')
s3 = boto3.resource('s3')

UPLOAD_FOLDER = "uploads"
app=Flask(__name__)

@app.route("/")
def home():
    urls = []
     #List pictures and parse their urls
    for obj in s3.Bucket(bucketname).objects.all():
        #Get random pictures
        urls.append("https://%s.s3.amazonaws.com/%s" % (bucketname,obj.key))
    return render_template("index.html",list_to_send=random.sample(urls,4))


@app.route("/upload")
def upload():
    if request.method == "POST":
        img = request.files['file']
        if img:
            img.save(os.path.join(UPLOAD_FOLDER, secure_filename(img.filename)))
            s3.upload_file(Bucket =bucketname, Filename = img.filename)
            return redirect("/")




if __name__ == "__main__":
    app.run(debug=True)


def sendImages():
     urls = []
     #List pictures and parse their urls
     for obj in s3.Bucket(bucketname).objects.all():
         urls.append("https://%s.s3.amazonaws.com/%s" % (bucketname,obj.key))
     #Get random pictures
     return random.sample(urls,4)


# def storeDataInJson(data):
#     #data parse ou a parser
#     s3.Object(bucketname2,'votes.json').put(Body=bytes(json.dumps(data).encode('UTF-8')))
#
# def uploadImages(picture):
#     #Create a key for new picture
#     imgCount = 0
#     for obj in s3.Bucket(bucketname).objects.all():
#         imgCount += 1
#     #Create key
#     extension = picture.split('.',2)
#     key = "%s." + extension % (imgCount+1)
#
#     #Upload to S3
#     s3.upload_file(picture,bucketname,key)
#
# #print(inQueue.attributes.get('Message'))

