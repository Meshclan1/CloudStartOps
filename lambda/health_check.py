import json
import boto3
import datetime

ec2 = boto3.client("ec2")

def lambda_handler(event, context):
    response = ec2.describe_instances(
        Filters=[{"Name": "instance-state-name", "Values": ["running"]}]
    )

    instance_count = sum(len(r["Instances"]) for r in response["Reservations"])

    return {
        "timestamp": datetime.datetime.utcnow().isoformat(),
        "running_instances": instance_count
    }
