import os


def lambda_handler(event, context):
    return "{} after the changes from Lambda!".format(os.environ['greeting'])
