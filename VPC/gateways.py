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

def GetSubnetIdByNameAndOwner(name, owner):
    response = client.describe_subnets(
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
    return response['Subnets'][0]['SubnetId']

def GetElasticIpByOwner(owner):
    response = client.describe_addresses(
        Filters=[
            {
                'Name':'tag:owner',
                'Values':[owner]
            }
        ]
    )
    return response['Addresses'][0]['AllocationId']

def CreateIgw(name,owner):
    response = client.create_internet_gateway(
        TagSpecifications=[
            {
                'ResourceType':'internet-gateway',
                'Tags':[
                    {
                        'Key':'Name',
                        'Value':name
                    },
                    {
                        'Key':'owner',
                        'Value':owner
                    }
                ]
            }
        ]
    )
    return response

def CreateNgw(name,owner,connectivity,subnet_id,allocation_id):
    response = client.create_nat_gateway(
        TagSpecifications=[
            {
                'ResourceType':'natgateway',
                'Tags':[
                    {
                        'Key':'Name',
                        'Value':name
                    },
                    {
                        'Key':'owner',
                        'Value':owner
                    }
                ]
            }
        ],
        ConnectivityType=connectivity,
        SubnetId=subnet_id,
        AllocationId=allocation_id
    )
    return response

print(CreateIgw('MRAK-IGW','mrak'))

print(CreateNgw('MRAK-NAT', 'mrak', 'public', GetSubnetIdByNameAndOwner('MRAK-PUB-1a','mrak'), GetElasticIpByOwner('mrak')))