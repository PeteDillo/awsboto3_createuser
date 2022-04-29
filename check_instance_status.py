import logging
import boto3
from botocore.exceptions import ClientError

#set up logger
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger('ecpy_describe')

#create iam client
ec2 = boto3.client('ec2')

#creating starts instance function
def describe_instance_status(instance_id):
    try:
        response = ec2.describe_instance_status(InstanceIds=[instance_id])
        logger.info("Describing instance status %s.", instance_id)
    except ClientError:
        logger.exception("Couldn't describe instance status %s.", instance_id)
        raise
    else:
        return response

response = describe_instance_status('i-083e1c0ec94239626')
print(response)