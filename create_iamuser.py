import logging
import boto3
from botocore.exceptions import ClientError

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger('iamuser')

#Create iam client
iam = boto3.client('iam')

#Take input from screen
username = input('Please enter a name:\n')

def create_user(username):
    try:
        response = iam.create_user(UserName=username)
        logger.info('Created a user %s.', username)
    except ClientError:
        logger.exception("Couldn't create a user %s.", username)
    else:
        return response
def main():
    response = create_user(username) 
    print(response['User']['UserName'], 'C.R.E.A.M')

if __name__ == '__main__':
    main()