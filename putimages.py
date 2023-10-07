import boto3

s3 = boto3.resource('s3')

# Get list of objects for indexing
images=[('image1.jpg','Cristiano Ronaldo'),
      ('image2.jpg','Cristiano Ronaldo'),
      ('image3.jpg','Lionel Messi'),
      ('image4.jpg','Lionel Messi'),
      ('image5.jpg','Neymar'),
      ('image6.jpg','Neymar')
      ]

# Iterate through list to upload objects to S3   
for image in images:
    file = open(image[0],'rb')
    object = s3.Object('celebratiesfaces','index/'+ image[0])
    ret = object.put(Body=file,
                    Metadata={'FullName':image[1]})