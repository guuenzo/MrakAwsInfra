import boto3

client = boto3.client('ec2')

def GetVpcIdByOwner(owner):
    response = client.describe_vpcs(
        Filters=[
        {
            'Name':'tag:owner',
            'Values':[owner]
        }
    ]
    )
    return response['Vpcs'][0]['VpcId']

def GetIgwByNameAndOwner(name,owner):
    response = client.describe_internet_gateways(
        Filters=[
            {
                'Name':'tag:Name',
                'Values':[name]
            },
            {
                'Name':'tag:owner',
                'Values':[owner]
            }
        ]
    )
    return response['InternetGateways'][0]['InternetGatewayId']

def AttachIgwToVpc(igw_id,vpc_id):
    response = client.attach_internet_gateway(
        InternetGatewayId=igw_id,
        VpcId=vpc_id
    )
    return response

print(AttachIgwToVpc(GetIgwByNameAndOwner('MRAK-IGW','mrak'), GetVpcIdByOwner('mrak')))