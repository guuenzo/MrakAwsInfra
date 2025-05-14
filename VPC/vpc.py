import boto3

client = boto3.client('ec2')

def CreateVpc(cidr, name, owner):
   return client.create_vpc(
        CidrBlock=cidr,
        TagSpecifications=[
            {
                'ResourceType' : 'vpc',
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


print(CreateVpc('192.168.0.0/16','MRAK-VPC','mrak'))