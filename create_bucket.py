import boto3,botocore,json,string,random,pprint

session = boto3.Session(profile_name='plasabas-general-admin')
client  = session.client('s3')
buckets = ['plasabas-bucket','plasabas-project-bucket-01']
length_of_suffix = 8
random_suffix = ''.join(random.choices(string.ascii_lowercase + string.digits, k=length_of_suffix))

def main():
    result = create_bucket()
    return result

def create_bucket():
    created_bucket_response=[]
    for bucket in buckets:
        response = client.create_bucket(
            Bucket = f"{bucket}-{random_suffix}"
        )
        created_bucket_response.append(response)
    return created_bucket_response


if __name__ == "__main__":
    result = main()

    for item in result: 
        bucket_name = item["ResponseMetadata"]["HTTPHeaders"]["location"]
        print(f"{'='*100}\nCreated {bucket_name.lstrip('/')} bucket\n{'='*100}")
        print(json.dumps(item, indent=4, default=str))
