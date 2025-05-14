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

def CreateSubnet(name,owner,cidr,az,vpc_id):
    response = client.create_subnet(
        TagSpecifications=[
            {
                'ResourceType':'subnet',
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
        CidrBlock=cidr,
        AvailabilityZone=az,
        VpcId=vpc_id
    )

    return response

print(CreateSubnet('MRAK-PUB-1a', 'mrak', '192.168.0.0/24', 'us-east-1a', GetVpcIdByOwner('mrak')))
print(CreateSubnet('MRAK-PRIV-1a', 'mrak', '192.168.1.0/24', 'us-east-1a', GetVpcIdByOwner('mrak')))
print(CreateSubnet('MRAK-PUB-1b', 'mrak', '192.168.2.0/24', 'us-east-1b', GetVpcIdByOwner('mrak')))
print(CreateSubnet('MRAK-PRIV-1b', 'mrak', '192.168.3.0/24', 'us-east-1b', GetVpcIdByOwner('mrak')))