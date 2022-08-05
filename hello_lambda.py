import os


def lambda_handler(event, context):
    return "{} hi all from Lambda!".format(os.environ['greeting'])
