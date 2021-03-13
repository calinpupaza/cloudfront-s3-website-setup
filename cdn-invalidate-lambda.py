# Lambda invoked by CodePipeline to invalidate the specified Cloudfront distribution
# For the structure of the event sent by CodePipeline, see 
# https://docs.aws.amazon.com/lambda/latest/dg/services-codepipeline.html

# This code in this file for legibility only
# Same code is embedded less readable in the CloudFormation template Lambda Code section

import boto3, time, os, json
def handler(event, context):
  cf_distrib_id = os.environ['CFDISTRIBUTIONID']
  cp_job_id = event['CodePipeline.job']['id']
  cloudfront = boto3.client('cloudfront')
  codepipeline = boto3.client('codepipeline')
  try:
    cloudfront.create_invalidation( DistributionId=cf_distrib_id, InvalidationBatch={ 'Paths': { 'Quantity': 1, 'Items': [ '/*' ] }, 'CallerReference': str(time.time()) })
  except Exception as ex:
    print(ex)
    codepipeline.put_job_failure_result(jobId=cp_job_id, failureDetails={ 'type': 'JobFailed', 'message': str(ex)})
  else:
    codepipeline.put_job_success_result(jobId=cp_job_id)
