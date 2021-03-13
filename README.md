# Static Website backed by HTTPS CloudFront S3 bucket

CloudFormation template that sets up the DNS, CDN, S3 hosted website, git repository and pipleine to allow serving a static website for the specified domain. 
Updating the HTML code is done thruugh a build pipeline that, when commits are pushed,  copies repository content code over to S3 and invalidates the CDN.

## Requirements

* A Route53 Hosted Zone for your domain
Retrieve the HostedZoneID for invoking the Cloudformation template

* AWS Access Key & Secret Key, ideally saved a a profile in your environment
Use `aws configure` to configure your AK & SK or use a profile

## Commands

### Create stack

*Parameters* for Cloudformation execution

* `STACK_NAME` of your choice
* `PROFILE` configured with your credentials

Region must be us-east-1 due to CloudFront requirement for ACM Certificate to be hosted in us-east-1.

* `DOMAIN_NAME` that you own
* `HOSTED_ZONE_ID` for the hosted zone corresponding to the registered domain

```
aws cloudformation create-stack --stack-name STACK_NAME --profile PROFILE --template-body file://template.cfn.json --parameters ParameterKey=DomainName,ParameterValue=DOMAIN_NAME ParameterKey=Route53HostedZoneID,ParameterValue=HOSTED_ZONE_ID --region us-east-1 --capabilities CAPABILITY_IAM
```

### Update stack

If you make CloudFormation stack modifications, update the stack.

*Validate* syntax
```
aws cloudformation validate-template --profile PROFILE --region us-east-1 --template-body file://template.cfn.json
```

*Update stack*
```
aws cloudformation update-stack --stack-name STACK_NAME --profile PROFILE --template-body file://template.cfn.json --parameters ParameterKey=DomainName,ParameterValue=DOMAIN_NAME ParameterKey=Route53HostedZoneID,ParameterValue=HOSTED_ZONE_ID --region us-east-1 --capabilities CAPABILITY_IAM
```

### Delete stack

To delete all resources created by this stack.

*Note* that all files in the S3 Bucket corresponding your domain will have to be deleted manually before deleting the CloudFormation stack.

```
aws cloudformation delete-stack --stack-name website-pragmatiqsoft --profile calin-dev --region us-east-1
```
