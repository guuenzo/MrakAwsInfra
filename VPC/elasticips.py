import boto3

client = boto3.client('ec2')

def CreateElasticIp(name, owner):
    response = client.allocate_address(
        TagSpecifications=[
            {
                'ResourceType':'elastic-ip',
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
    )
    return response

print(CreateElasticIp('MRAK-EIP', 'mrak'))