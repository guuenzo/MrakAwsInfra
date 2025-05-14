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

def GetIgwIdByNameAndOwner(name,owner):
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

def GetNgwByNameAndOwner(name,owner):
    response = client.describe_nat_gateways(
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
    return response['NatGateways'][0]['NatGatewayId']

def GetRtbIdByNameAndOwner(name,owner):
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

def CreateRouteInPubRtb(gateway,rtb_id,destination_cidr):
    response = client.create_route(
        GatewayId=gateway,
        RouteTableId=rtb_id,
        DestinationCidrBlock=destination_cidr
    )
    return response

def CreateRouteInPrivbRtb(nat_gateway,rtb_id,destination_cidr):
    response = client.create_route(
        NatGatewayId=nat_gateway,
        RouteTableId=rtb_id,
        DestinationCidrBlock=destination_cidr
    )
    return response

print(CreateRouteInPubRtb(GetIgwIdByNameAndOwner('MRAK-IGW','mrak'),GetRouteTableIdByNameAndOwner('MRAK-PUB-RT','mrak'),'0.0.0.0/0'))
print(CreateRouteInPrivbRtb(GetNgwByNameAndOwner('MRAK-NAT','mrak'),GetRouteTableIdByNameAndOwner('MRAK-PRIV-RT','mrak'),'0.0.0.0/0'))