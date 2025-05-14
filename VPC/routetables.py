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

def CreateRouteTable(name,owner,vpc_id):
    response = client.create_route_table(
        TagSpecifications=[
            {
                'ResourceType':'route-table',
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
        VpcId=vpc_id
    )
    return response

print(CreateRouteTable('MRAK-PUB-RT','mrak',GetVpcIdByOwner('mrak')))
print(CreateRouteTable('MRAK-PRIV-RT','mrak',GetVpcIdByOwner('mrak')))