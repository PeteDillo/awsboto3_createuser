import logging
import boto3
from botocore.exceptions import ClientError

#set up logger
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger('ecpy_describe')

#create iam client
ec2 = boto3.resource('ec2')

#creating starts instance function
def start_instance(instance_id):
    try:
        response = ec2.Instance(instance_id).start()
        logger.info("Started instance %s.", instance_id)
    except ClientError:
        logger.exception("Couldn't start instance %s.", instance_id)
        raise
    else:
        return response

response = start_instance('i-083e1c0ec94239626')