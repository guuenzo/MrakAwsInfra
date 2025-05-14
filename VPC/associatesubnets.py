import boto3

client = boto3.client('ec2')

def GetRouteTableIdByNameAndOwner(name,owner):
    response = client.describe_route_tables(
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
    return response['RouteTables'][0]['RouteTableId']

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

def CreateAssociationInRtb(subnet_id,rtb_id):
    response = client.associate_route_table(
        SubnetId=subnet_id,
        RouteTableId=rtb_id
    )
    return response

print(CreateAssociationInRtb(GetSubnetIdByNameAndOwner('MRAK-PUB-1a','mrak'),GetRouteTableIdByNameAndOwner('MRAK-PUB-RT','mrak')))
print(CreateAssociationInRtb(GetSubnetIdByNameAndOwner('MRAK-PUB-1b','mrak'),GetRouteTableIdByNameAndOwner('MRAK-PUB-RT','mrak')))
print(CreateAssociationInRtb(GetSubnetIdByNameAndOwner('MRAK-PRIV-1a','mrak'),GetRouteTableIdByNameAndOwner('MRAK-PRIV-RT','mrak')))
print(CreateAssociationInRtb(GetSubnetIdByNameAndOwner('MRAK-PRIV-1b','mrak'),GetRouteTableIdByNameAndOwner('MRAK-PRIV-RT','mrak')))