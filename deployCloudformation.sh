aws cloudformation deploy \
  --template-file serverless-webapp.yaml \
  --stack-name myServerlessWebAppStack \
  --parameter-overrides \
    BucketName=myserverlesswebapp-202411161622 \
    DynamoDBTableName=Contacts \
    GitHubRepo=MubasharSadiq/myServerlessWebApp \
    GitHubBranch=main \
    CodeStarConnectionArn=arn:aws:codeconnections:eu-west-1:509399609846:connection/1cf7a19f-2722-4cd8-abe4-1ec525701fe6 \
    SESFromEmail=imubashar.sadiq@gmail.com \
    LambdaRoleToAccessDynamoDBArn=arn:aws:iam::509399609846:role/LambdaRoleToAccessDynamoDB \
    LambdaRoleToAccessSESArn=arn:aws:iam::509399609846:role/LambdaRoleToAccessSES \
  --capabilities CAPABILITY_NAMED_IAM
  