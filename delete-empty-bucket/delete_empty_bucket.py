import boto3,botocore,json,string,random,pprint

session = boto3.Session(profile_name='plasabas-general-admin')
client  = session.client('s3')
list_of_buckets = client.list_buckets()["Buckets"]

def main():
    list_of_empty_buckets = []

    print(f"{'='*100}\nList of Empty buckets bucket\n{'='*100}")
    for bucket in list_of_buckets:
        check_if_empty = client.list_objects_v2(Bucket=bucket["Name"])
        if check_if_empty["KeyCount"] == 0:
            list_of_empty_buckets.append(bucket["Name"])
            print(f"{bucket["Name"]}")
    print(f"{'='*100}\nEnd of the list\n{'='*100}")

    return list_of_empty_buckets

def delete_empty_buckets(list_of_empty_buckets):

    print(f"{'='*100}\nDeleting Empty Buckets\n{'='*100}")
    for bucket in list_of_empty_buckets:
        print(f"Deleting: {bucket}")
        client.delete_bucket(Bucket=bucket)


if __name__ == "__main__":
    list_of_empty_buckets = main()
    delete_empty_buckets(list_of_empty_buckets)