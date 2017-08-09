from __future__ import print_function

import boto3

print('Loading function')

def lambda_handler(event, context):

    serviceId = event['serviceId']
    tableName = 'activeServices'

    #### Connect to DynamoDB service
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table(tableName)
    
    data = table.get_item(Key={'serviceId':serviceId})#   data.save()
    
    addr1=data['Item']['addr1']
    addr2=data['Item']['addr2']
    addr3=data['Item']['addr3']
    addr4=data['Item']['addr4']
    addr5=data['Item']['addr5']
    addr6=data['Item']['addr6']
    addr7=data['Item']['addr7']
    addr8=data['Item']['addr8']
    
    port1=int(data['Item']['port1'])
    port2=int(data['Item']['port2'])
    port3=int(data['Item']['port3'])
    port4=int(data['Item']['port4'])
    port5=int(data['Item']['port5'])
    port6=int(data['Item']['port6'])
    port7=int(data['Item']['port7'])
    port8=int(data['Item']['port8'])

    cache1=data['Item']['cache1']
    cache2=data['Item']['cache2']
    cache3=data['Item']['cache3']
    cache4=data['Item']['cache4']
    cache5=data['Item']['cache5']
    cache6=data['Item']['cache6']
    cache7=data['Item']['cache7']
    cache8=data['Item']['cache8']

    comp1=data['Item']['comp1']
    comp2=data['Item']['comp2']
    comp3=data['Item']['comp3']
    comp4=data['Item']['comp4']
    comp5=data['Item']['comp5']
    comp6=data['Item']['comp6']
    comp7=data['Item']['comp7']
    comp8=data['Item']['comp8']
    
    type1=data['Item']['type1']
    type2=data['Item']['type2']
    type3=data['Item']['type3']
    type4=data['Item']['type4']
    type5=data['Item']['type5']
    type6=data['Item']['type6']
    type7=data['Item']['type7']
    type8=data['Item']['type8']


    #### Connect to ECS service
    client = boto3.client('ecs')
    cluster_Name = 'Tempest-ECS'

    ### Create instance task definition
    response = client.register_task_definition(
        containerDefinitions=[
            {
                'name': serviceId,
                'portMappings': [
                    {
                        'containerPort': port1,
                        'protocol': type1
                    },
                ],
                'cpu': 128,
                'essential': True,
                'image': 'nginx:latest',
                'memory': 128,
            },
        ],
        family=serviceId,
        taskRoleArn='',
        volumes=[
        ],
    )

    ## create and start service based on previously created task
    response = client.create_service(
        cluster=cluster_Name,
        serviceName=serviceId,
        taskDefinition=serviceId,
        loadBalancers=[
            {
                'targetGroupArn': 'arn:aws:elasticloadbalancing:us-east-1:250871914685:targetgroup/tempest1-tg/e04aae038c739a47',
                'containerName': serviceId,
                'containerPort': port1
            },
        ],
        desiredCount=2,
        role='arn:aws:iam::250871914685:role/ecsServiceRole',
        placementConstraints=[
            {
                'type': 'distinctInstance'
            },
        ],)