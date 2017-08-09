#/usr/bin/python

import boto3
client = boto3.client('ecs')
instance_ID = 'ou812'
cluster_Name = 'Tempest-ECS'
port_1 = 80

### Create instance task definition
response = client.register_task_definition(
    containerDefinitions=[
        {
            'name': 'ou812',
            'portMappings': [
                {
                    'containerPort': port_1,
                    'hostPort': port_1,
                    'protocol': 'tcp'
                },
            ],
            'cpu': 128,
            'essential': True,
            'image': 'nginx:latest',
            'memory': 128,
        },
    ],
    family=instance_ID,
    taskRoleArn='',
    volumes=[
    ],
)

## create and start service based on previously created task
response = client.create_service(
    cluster=cluster_Name,
    serviceName=instance_ID,
    taskDefinition=instance_ID,
    loadBalancers=[
        {
            'targetGroupArn': 'arn:aws:elasticloadbalancing:us-east-1:250871914685:targetgroup/tempest1-tg/e04aae038c739a47',
            'containerName': 'ou812',
            'containerPort': 80
        },
    ],
    desiredCount=2,
    role='arn:aws:iam::250871914685:role/ecsServiceRole',
    placementConstraints=[
        {
            'type': 'distinctInstance'
        },
    ],)