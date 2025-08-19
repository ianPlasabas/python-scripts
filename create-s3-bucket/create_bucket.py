import boto3,yaml,string,random,os

def create_bucket(bucket_name, iam_profile):
    session = boto3.Session(profile_name=iam_profile)
    client  = session.client('s3')
    length_of_suffix = 16
    random_suffix = ''.join(random.choices(string.ascii_lowercase + string.digits, k=length_of_suffix))

    client.create_bucket(
        Bucket = f"{bucket_name}-{random_suffix}"
    )

    return print("Success!")

if __name__ == "__main__":
    
    print(f"{'='*75}\nS3 Bucket Provisioning Script\n\nInstruction:\nPlease provide the file name under the same directory\n{'='*75}")

    while True:
        file_name=input("\nFile name: ")
        file_path=os.path.join(os.getcwd(),file_name)

        if os.path.exists(file_path):
            print(f"File '{file_name}' found. Proceeding with the script.\n")

            with open(file_path,"r") as f:
                file_content = yaml.safe_load(f)
                for item in file_content["buckets"]:
                    print(f'-->Creating {item["name"]} bucket')
                    create_bucket(item["name"],item["profile"])
            break
        else:
            print(f"Error: The file '{file_name}' does not exist in the current directory.")