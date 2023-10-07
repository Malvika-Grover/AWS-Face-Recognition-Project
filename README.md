# AWS-Face-Recognition-Project
<img width="1013" alt="Screenshot 2023-10-07 at 9 51 43 PM" src="https://github.com/Malvika-Grover/AWS-Face-Recognition-Project/assets/43317657/ec2964a7-17d7-46c6-acf7-4b3e02ea7ad9">



**Command used in the project**

**Install aws-shell** -> 
pip install aws-shell

**Configure** -> 
aws configure

**Create a collection on aws rekognition** -> 
aws rekognition create-collection --collection-id facerecognition_collection --region us-east-1

**Create a table on DynamoDB** ->
aws dynamodb create-table --table-name facerecognition \
--attribute-definitions AttributeName=RekognitionId,AttributeType=S \
--key-schema AttributeName=RekognitionId,KeyType=HASH \
--provisioned-throughput ReadCapacityUnits=1,WriteCapacityUnits=1 \
--region us-east-1

**Create S3 bucket** -> 
aws s3 mb s3://bucket-name --region us-east-1


**Note:**
1. If you do not have AWS CLI, download it using  -> sudo installer -pkg ./AWSCLIV2.pkg -target and then use -> aws --version 

2. While using code for lambda function, you might face an issue in the boto3 library, to resolve that follow the the below steps -
  
3. To install pip into your system use - curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py python3 get-pip.py pip3 --version
  
4. Now you can install boto3 library using -> pip3 install boto3 

5. While testing you might face an issue in line - from PIL import Image, to resolve this use -> pip3 install pillow
