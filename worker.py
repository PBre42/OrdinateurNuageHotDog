import boto3
import os
import random
from flask import Flask, render_template, request, redirect
from werkzeug.utils import secure_filename

#Bucket for photos
bucketname = 'photoshotdogs'
#Bucket for data
bucketname2 = 'hotdogsdata'

s3 = boto3.resource('s3')
app=Flask(__name__)

#Initialization of the home page (index.html)
@app.route("/")
def home():
    urls = []
    #List pictures and parse their urls
    for obj in s3.Bucket(bucketname).objects.all():
        #Get random pictures
        urls.append("https://%s.s3.amazonaws.com/%s" % (bucketname,obj.key))
    #Giving 4 random urls for the html
    return render_template("index.html",list_to_send=random.sample(urls,4))

#Upload photos from FileSystem to S3 
@app.route("/upload", methods=['GET', 'POST'])
def upload():
    if request.method == "POST":
        img = request.files['file']
        if img:
            #Save image and upload it to S3
            filename = secure_filename(img.filename)
            img.save(filename)
            #Give it public access
            s3.meta.client.upload_file(Bucket = bucketname,Filename=filename,Key = filename,ExtraArgs={'ACL':'public-read'})
            return redirect("/")

#Submit votes from HTML to S3
@app.route("/submit", methods=['GET', 'POST'])
def submit():
    #Données pour le bucket
    dataToS3 = "\n" + request.form.get("l1") + ";" + request.form.get("p1") + "\n" + request.form.get("l2") + ";" + request.form.get("p2") + "\n" + request.form.get("l3") + ";" + request.form.get("p3") + "\n" + request.form.get("l4") + ";" + request.form.get("p4")
    #Write in data.txt file and upload it in S3
    file_object = open('data.txt', 'a')
    file_object.write(dataToS3)  
    file_object.close()
    #Give public credentials
    s3.meta.client.upload_file(Bucket = bucketname2,Filename="data.txt",Key = "data.txt",ExtraArgs={'ACL':'public-read'})
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)