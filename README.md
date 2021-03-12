# Static Website backed by HTTPS CloudFront S3 bucket, with deployment pipelin from a CodeCommit (git) repo

CloudFormation template that sets up the DNS, CDN, S3 hosted website, git repository and pipleine to allow serving a static website for teh specified domain. Updating the HTML code is done thrpugh a build pipeline that copies code over to S3 and invalidates the CDN.

## Requirements

TBD

## Commands

### Create stack

*Parameters*

* StackName
* ProfileName
for Cloudformation execution
Region must be us-east-1.

* DomainName
* Route53 hosted zone name


### Update stack


### Delete stack


