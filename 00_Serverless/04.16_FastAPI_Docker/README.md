aws ecr create-repository --repository-name my-webapp

aws ecr get-login-password --region <region> | docker login --username AWS --password-stdin <aws_account_id>.dkr.ecr.<region>.amazonaws.com


docker tag test-webapp <aws_account_id>.dkr.ecr.<region>.amazonaws.com/<repository_name>:<tag>
docker push <aws_account_id>.dkr.ecr.<region>.amazonaws.com/<repository_name>:<tag>



Repository: my-webapp
Region:     eu-central-1
Account-ID: 864199764664


aws ecr create-repository --repository-name my-webapp
{
    "repository": {
        "repositoryArn": "arn:aws:ecr:eu-central-1:864199764664:repository/my-webapp",
        "registryId": "864199764664",
        "repositoryName": "my-webapp",
        "repositoryUri": "864199764664.dkr.ecr.eu-central-1.amazonaws.com/my-webapp",
        "createdAt": "2023-04-17T13:18:07+03:00",
        "imageTagMutability": "MUTABLE",
        "imageScanningConfiguration": {
            "scanOnPush": false
        },
        "encryptionConfiguration": {
            "encryptionType": "AES256"
        }
    }
}

aws ecr get-login-password --region eu-central-1 | docker login --username AWS --password-stdin 864199764664.dkr.ecr.eu-central-1.amazonaws.com


docker tag test-webapp 864199764664.dkr.ecr.eu-central-1.amazonaws.com/my-webapp:webAppTag
docker push 864199764664.dkr.ecr.eu-central-1.amazonaws.com/my-webapp:webAppTag
