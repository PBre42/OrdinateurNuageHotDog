import boto3
#connect to server and send request
sqs = boto3.client('sqs')

queueOut = sqs.create_queue(
    QueueName='requestQueue',
    Attributes={
        "DelaySeconds" : "0",
        "VisibilityTimeout" : "60"}
    )

qURL = sqs.get_queue_url(
    QueueName='requestQueue',
)

#queueIn = sqs.get_queue_by_name(QueueName='response')

#condition pour attendre un message (boucle)
while 1:
    print("Enter values (space separated):")
    inputs = input().split(' ')
    #vérifier inputs
    

    #remplir la queue
    sqs.send_message(
        QueueUrl=qURL["QueueUrl"],
        MessageBody=str(inputs)
    )  
    
    #attendre la réponse
    reponse = sqs.receive_message(
        QueueUrl=qURL["QueueUrl"]
    )
    print(reponse['Body'])

    #parser la queue 
    
    #afficher valeurs
